"""
Market Price Prediction and APMC Mandi Trends Engine
Provides realistic APMC market benchmark rates, historical price curves,
future 30-day forecast predictions, and economic loss calculations.
"""
import random
import datetime

MARKET_RATES = {
    "Tomato (टमाटर)": {
        "crop_key": "tomato",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 2450,
        "msp": 1900,
        "price_range": "₹2,200 - ₹2,800",
        "trend": "Bullish (+12% this month)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Azadpur Mandi (Delhi)", "state": "Delhi", "price": 2600, "arrival": "420 tonnes"},
            {"mandi": "Kolar Mandi", "state": "Karnataka", "price": 2400, "arrival": "850 tonnes"},
            {"mandi": "Nashik Mandi", "state": "Maharashtra", "price": 2350, "arrival": "610 tonnes"},
            {"mandi": "Madanapalle Mandi", "state": "Andhra Pradesh", "price": 2500, "arrival": "730 tonnes"}
        ],
        "advisory_en": "High seasonal demand in northern consumer hubs. Stagger harvest to capitalize on predicted price peak over the next 14 days.",
        "advisory_hi": "उत्तरी राज्यों में मांग बढ़ने से दाम तेज रहने की संभावना है। अगले 14 दिनों में मिलने वाले ऊंचे भाव का लाभ लेने के लिए तुड़ाई योजना बनाएं।",
        "historical_days": 30,
        "base_pattern": [2100, 2150, 2200, 2180, 2240, 2300, 2280, 2350, 2400, 2450],
        "forecast_days": 15,
        "forecast_pattern": [2480, 2520, 2580, 2640, 2700, 2750, 2720, 2690, 2650, 2600]
    },

    "Potato (आलू)": {
        "crop_key": "potato",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 1680,
        "msp": 1400,
        "price_range": "₹1,500 - ₹1,850",
        "trend": "Stable (+3%)",
        "trend_direction": "stable",
        "top_mandis": [
            {"mandi": "Agra APMC", "state": "Uttar Pradesh", "price": 1720, "arrival": "1200 tonnes"},
            {"mandi": "Jalandhar Mandi", "state": "Punjab", "price": 1650, "arrival": "950 tonnes"},
            {"mandi": "Indore Mandi", "state": "Madhya Pradesh", "price": 1690, "arrival": "540 tonnes"},
            {"mandi": "Hooghly Mandi", "state": "West Bengal", "price": 1620, "arrival": "1100 tonnes"}
        ],
        "advisory_en": "Cold storage dispatch is steady. Good quality disease-free tubers command a ₹200/quintal premium.",
        "advisory_hi": "कोल्ड स्टोरेज से निकासी सामान्य है। रोगमुक्त और साफ ग्रेडिंग वाले आलू पर ₹200/क्विंटल तक का प्रीमियम मिल रहा है।",
        "historical_days": 30,
        "base_pattern": [1550, 1580, 1600, 1590, 1620, 1640, 1630, 1660, 1670, 1680],
        "forecast_days": 15,
        "forecast_pattern": [1690, 1710, 1730, 1750, 1760, 1780, 1790, 1800, 1820, 1850]
    },

    "Wheat (गेहूं)": {
        "crop_key": "wheat",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 2580,
        "msp": 2425,
        "price_range": "₹2,450 - ₹2,750",
        "trend": "Strong Bullish (+8%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Khanna Mandi", "state": "Punjab", "price": 2620, "arrival": "1800 tonnes"},
            {"mandi": "Karnal Mandi", "state": "Haryana", "price": 2600, "arrival": "1400 tonnes"},
            {"mandi": "Sehore Mandi", "state": "Madhya Pradesh", "price": 2570, "arrival": "900 tonnes"},
            {"mandi": "Kota APMC", "state": "Rajasthan", "price": 2550, "arrival": "850 tonnes"}
        ],
        "advisory_en": "Flour mills active buying at open market rates higher than MSP. Yield loss protection is crucial.",
        "advisory_hi": "रोलर फ्लोर मिलों की सक्रिय लिवाली से बाजार भाव एमएसपी से ऊपर चल रहा है। पीला रतुआ नियंत्रण करके उपज बचाना सर्वाधिक लाभ देगा।",
        "historical_days": 30,
        "base_pattern": [2380, 2400, 2420, 2450, 2480, 2500, 2520, 2540, 2560, 2580],
        "forecast_days": 15,
        "forecast_pattern": [2600, 2620, 2650, 2680, 2700, 2720, 2740, 2750, 2760, 2780]
    },

    "Rice / Paddy (धान)": {
        "crop_key": "rice",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 3200,
        "msp": 2300,
        "price_range": "₹2,900 - ₹3,600",
        "trend": "Bullish (+6%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Karnal Basmati Mandi", "state": "Haryana", "price": 3650, "arrival": "1500 tonnes"},
            {"mandi": "Gondal Mandi", "state": "Gujarat", "price": 3150, "arrival": "600 tonnes"},
            {"mandi": "Burdwan APMC", "state": "West Bengal", "price": 2980, "arrival": "2100 tonnes"},
            {"mandi": "Warangal Mandi", "state": "Telangana", "price": 3100, "arrival": "1300 tonnes"}
        ],
        "advisory_en": "Export demand for long grain and premium varieties remains robust.",
        "advisory_hi": "बासमती और उत्तम गुणवत्ता वाले धान की निर्यात मांग मजबूत बनी हुई है।",
        "historical_days": 30,
        "base_pattern": [2950, 3000, 3020, 3050, 3080, 3100, 3140, 3160, 3180, 3200],
        "forecast_days": 15,
        "forecast_pattern": [3220, 3250, 3280, 3320, 3350, 3390, 3420, 3450, 3480, 3500]
    },

    "Cotton (कपास)": {
        "crop_key": "cotton",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 7450,
        "msp": 7122,
        "price_range": "₹7,200 - ₹7,900",
        "trend": "Firm (+4%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Rajkot APMC", "state": "Gujarat", "price": 7600, "arrival": "900 tonnes"},
            {"mandi": "Adilabad Mandi", "state": "Telangana", "price": 7400, "arrival": "650 tonnes"},
            {"mandi": "Abohar Mandi", "state": "Punjab", "price": 7500, "arrival": "400 tonnes"},
            {"mandi": "Amravati Mandi", "state": "Maharashtra", "price": 7380, "arrival": "750 tonnes"}
        ],
        "advisory_en": "Textile spinning mills are purchasing spot lots. Maintain fiber grade to avoid discount.",
        "advisory_hi": "कपास मिलों की मांग सामान्य है। दाग-धब्बों रहित साफ कपास पर उच्चतम भाव मिल रहा है।",
        "historical_days": 30,
        "base_pattern": [7150, 7200, 7220, 7280, 7300, 7350, 7380, 7400, 7420, 7450],
        "forecast_days": 15,
        "forecast_pattern": [7480, 7520, 7560, 7600, 7650, 7700, 7740, 7780, 7820, 7850]
    },

    "Corn / Maize (मक्का)": {
        "crop_key": "maize",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 2220,
        "msp": 2090,
        "price_range": "₹2,100 - ₹2,350",
        "trend": "Steady (+2%)",
        "trend_direction": "stable",
        "top_mandis": [
            {"mandi": "Gulabbagh Mandi (Purnea)", "state": "Bihar", "price": 2280, "arrival": "3200 tonnes"},
            {"mandi": "Davangere Mandi", "state": "Karnataka", "price": 2200, "arrival": "1400 tonnes"},
            {"mandi": "Chhindwara Mandi", "state": "Madhya Pradesh", "price": 2240, "arrival": "800 tonnes"}
        ],
        "advisory_en": "Poultry feed and starch industrial demand providing solid price floor.",
        "advisory_hi": "पोल्ट्री फीड और स्टार्च कंपनियों की खरीद के कारण मक्का के भाव स्थिर व मजबूत बने रहेंगे।",
        "historical_days": 30,
        "base_pattern": [2120, 2140, 2150, 2170, 2180, 2190, 2200, 2210, 2215, 2220],
        "forecast_days": 15,
        "forecast_pattern": [2230, 2240, 2260, 2275, 2290, 2300, 2315, 2330, 2340, 2350]
    },

    "Apple (सेब)": {
        "crop_key": "apple",
        "unit": "₹/Box (20kg) (₹/पेटी)",
        "current_price": 1850,
        "msp": 1200,
        "price_range": "₹1,600 - ₹2,400",
        "trend": "High Demand (+15%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Azadpur Fruit Mandi", "state": "Delhi", "price": 2100, "arrival": "1500 boxes"},
            {"mandi": "Dhalli Mandi (Shimla)", "state": "Himachal Pradesh", "price": 1800, "arrival": "2800 boxes"},
            {"mandi": "Parimpora Fruit Mandi", "state": "Jammu & Kashmir", "price": 1850, "arrival": "3500 boxes"}
        ],
        "advisory_en": "Scab-free, graded Delicious apples fetching premium prices in terminal markets.",
        "advisory_hi": "स्कैब मुक्त, साफ छिलके वाले ए-ग्रेड सेबों को दिल्ली व महानगरों में रिकॉर्ड दाम मिल रहे हैं।",
        "historical_days": 30,
        "base_pattern": [1550, 1600, 1620, 1680, 1700, 1750, 1780, 1800, 1820, 1850],
        "forecast_days": 15,
        "forecast_pattern": [1890, 1940, 1980, 2040, 2100, 2150, 2200, 2250, 2300, 2350]
    },

    "Chilli / Pepper (मिर्च)": {
        "crop_key": "chilli",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 14500,
        "msp": 9500,
        "price_range": "₹13,000 - ₹17,500",
        "trend": "Strong Bullish (+18%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Guntur APMC", "state": "Andhra Pradesh", "price": 15200, "arrival": "1800 tonnes"},
            {"mandi": "Khammam Mandi", "state": "Telangana", "price": 14600, "arrival": "950 tonnes"},
            {"mandi": "Byadagi Mandi", "state": "Karnataka", "price": 16400, "arrival": "1200 tonnes"}
        ],
        "advisory_en": "High spice export orders from Southeast Asia and Europe. Controlling leaf curl protects up to 40% marketable yield.",
        "advisory_hi": "मसाला निर्यातकों की जोरदार मांग। वायरस और थ्रिप्स नियंत्रित करके किसान 40% तक अतिरिक्त उत्पादन बेच सकते हैं।",
        "historical_days": 30,
        "base_pattern": [12800, 13100, 13400, 13600, 13900, 14000, 14200, 14350, 14400, 14500],
        "forecast_days": 15,
        "forecast_pattern": [14650, 14800, 15100, 15400, 15800, 16200, 16500, 16800, 17100, 17400]
    },

    "Groundnut / Peanut (मूंगफली)": {
        "crop_key": "groundnut",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 6350,
        "msp": 6783,
        "price_range": "₹6,100 - ₹6,800",
        "trend": "Bullish (+5%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Rajkot APMC", "state": "Gujarat", "price": 6500, "arrival": "2100 tonnes"},
            {"mandi": "Bikaner Mandi", "state": "Rajasthan", "price": 6420, "arrival": "1400 tonnes"},
            {"mandi": "Kurnool Mandi", "state": "Andhra Pradesh", "price": 6300, "arrival": "980 tonnes"}
        ],
        "advisory_en": "Oil mill demand strong. Grade bold pods for best market value.",
        "advisory_hi": "तेल मिलों की मजबूत मांग। बोल्ड दाने वाली मूंगफली को बाजार में अधिकतम भाव मिल रहा है।",
        "historical_days": 30,
        "base_pattern": [6050, 6100, 6150, 6200, 6220, 6280, 6300, 6320, 6340, 6350],
        "forecast_days": 15,
        "forecast_pattern": [6380, 6420, 6470, 6520, 6580, 6630, 6680, 6720, 6760, 6800]
    },

    "Mustard (सरसों)": {
        "crop_key": "mustard",
        "unit": "₹/Quintal (₹/क्विंटल)",
        "current_price": 5650,
        "msp": 5950,
        "price_range": "₹5,400 - ₹6,100",
        "trend": "Upward (+7%)",
        "trend_direction": "up",
        "top_mandis": [
            {"mandi": "Jaipur Mandi", "state": "Rajasthan", "price": 5780, "arrival": "2800 tonnes"},
            {"mandi": "Agra Mandi", "state": "Uttar Pradesh", "price": 5690, "arrival": "1600 tonnes"},
            {"mandi": "Morena APMC", "state": "Madhya Pradesh", "price": 5620, "arrival": "1100 tonnes"}
        ],
        "advisory_en": "High oil extraction percentage fetches ₹150/qtl bonus. Protect crop from white rust to preserve oil content.",
        "advisory_hi": "42% से अधिक तेल वाली सरसों को ₹150/क्विंटल तक का बोनस मिल रहा है। सफेद रतुआ से बचाएं ताकि तेल की मात्रा कम न हो।",
        "historical_days": 30,
        "base_pattern": [5300, 5350, 5400, 5440, 5500, 5530, 5580, 5600, 5620, 5650],
        "forecast_days": 15,
        "forecast_pattern": [5680, 5720, 5760, 5820, 5880, 5940, 6000, 6050, 6090, 6150]
    }
}


def get_market_data_for_crop(crop_name):
    # Match against keys
    for key, data in MARKET_RATES.items():
        if crop_name.lower().split()[0] in key.lower():
            return data
    # Fallback to Tomato
    return MARKET_RATES["Tomato (टमाटर)"]


def calculate_economic_impact(crop_name, acres=2, disease_severity="Moderate"):
    """
    Calculates the financial protection gained by diagnosing and treating in time.
    """
    data = get_market_data_for_crop(crop_name)
    price = data["current_price"]
    
    # Average yield in quintals per acre
    yield_map = {
        "Tomato": 120,
        "Potato": 100,
        "Wheat": 22,
        "Rice": 25,
        "Cotton": 12,
        "Corn": 30,
        "Apple": 40,
        "Chilli": 15,
        "Groundnut": 14,
        "Mustard": 9
    }
    
    crop_first_word = crop_name.split()[0]
    avg_yield = yield_map.get(crop_first_word, 25)
    
    severity_loss_pct = {
        "Low": 0.10,
        "Moderate": 0.28,
        "Moderate to High": 0.38,
        "Severe": 0.55,
        "Critical": 0.75,
        "None / Optimal": 0.0
    }.get(disease_severity, 0.30)
    
    total_yield = avg_yield * acres
    potential_crop_value = total_yield * price
    potential_loss = int(potential_crop_value * severity_loss_pct)
    saved_value = int(potential_loss * 0.85)  # 85% recovered through timely treatment
    treatment_cost = int(acres * 1400)
    net_gain = saved_value - treatment_cost
    
    return {
        "acres": acres,
        "estimated_total_yield": f"{total_yield} Quintals",
        "potential_crop_value": f"₹{potential_crop_value:,}",
        "potential_loss_without_action": f"₹{potential_loss:,}",
        "estimated_yield_saved": f"₹{saved_value:,}",
        "treatment_cost": f"₹{treatment_cost:,}",
        "net_farmer_benefit": f"₹{net_gain:,}"
    }
