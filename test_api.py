"""
Comprehensive API Test Suite for AgriShield AI Backend
"""
import unittest
from app import app
import json

class TestAgriShieldApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_crops_list(self):
        res = self.client.get('/api/crops-list')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertGreaterEqual(len(data['crops']), 8)

    def test_encyclopedia(self):
        res = self.client.get('/api/encyclopedia')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertGreaterEqual(data['count'], 10)

    def test_ask_agronomist(self):
        res = self.client.post('/api/ask-agronomist', json={
            "query": "How to treat yellow leaves in wheat?",
            "crop": "wheat"
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('answer_en', data)

    def test_sample_image(self):
        res = self.client.get('/api/sample-image/wheat_yellow_rust')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertTrue(data['image_data_uri'].startswith('data:image/png;base64,'))

    def test_diagnose(self):
        res = self.client.post('/api/diagnose', json={
            "crop": "tomato",
            "disease_id": "tomato_early_blight",
            "acres": 2.5
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('Early Blight', data['disease']['name_en'])
        self.assertIn('economic_impact', data)
        self.assertIn('weather_risk', data)

    def test_weather_api(self):
        res = self.client.get('/api/weather?lat=28.6139&lon=77.2090&crop=Wheat')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('disease_spread_risk', data)

    def test_dosage_calculator_knapsack(self):
        res = self.client.post('/api/calculate-dosage', json={
            "acres": 3.0,
            "tank_capacity_liters": 15.0,
            "dose_per_liter_g_or_ml": 2.5,
            "spray_type": "knapsack",
            "product_name": "Mancozeb 75% WP"
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['total_product_needed'], '1350.0 grams')

    def test_dosage_calculator_drone(self):
        res = self.client.post('/api/calculate-dosage', json={
            "acres": 5.0,
            "tank_capacity_liters": 10.0,
            "spray_type": "drone",
            "product_name": "Azoxystrobin 23% SC"
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('ml', data['total_product_needed'])

    def test_market_prices(self):
        res = self.client.get('/api/market-prices?crop=Tomato')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('top_mandis', data['market_data'])

if __name__ == '__main__':
    unittest.main()
