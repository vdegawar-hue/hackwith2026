"""
AgriShield AI (कृषि रक्षक) - Flask Web Application Backend
Serves modern web UI and comprehensive agricultural diagnostic APIs.
"""
import os
import json
import base64
from flask import Flask, request, jsonify, send_from_directory
from disease_kb import get_all_diseases, get_disease_by_id, DISEASE_DATABASE
from market_data import get_market_data_for_crop, calculate_economic_impact, MARKET_RATES
from weather_service import fetch_live_weather, evaluate_disease_weather_risk, analyze_soil_health
from image_processor import process_and_analyze_image
from sample_images import generate_sample_leaf_image

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

@app.route("/api/sample-image/<disease_id>", methods=["GET"])
def get_sample_image(disease_id):
    """Returns a generated authentic diseased leaf base64 data URI."""
    try:
        data_uri = generate_sample_leaf_image(disease_id)
        return jsonify({"success": True, "disease_id": disease_id, "image_data_uri": data_uri})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/crops-list", methods=["GET"])
def get_crops_list():
    """Returns supported crops and disease catalog for quick selection."""
    crops = [
        {"id": "tomato", "name_en": "Tomato", "name_hi": "टमाटर", "icon": "🍅", "default_disease": "tomato_early_blight"},
        {"id": "potato", "name_en": "Potato", "name_hi": "आलू", "icon": "🥔", "default_disease": "potato_late_blight"},
        {"id": "wheat", "name_en": "Wheat", "name_hi": "गेहूं", "icon": "🌾", "default_disease": "wheat_yellow_rust"},
        {"id": "rice", "name_en": "Rice / Paddy", "name_hi": "धान", "icon": "🌾", "default_disease": "rice_blast"},
        {"id": "cotton", "name_en": "Cotton", "name_hi": "कपास", "icon": "☁️", "default_disease": "cotton_bacterial_blight"},
        {"id": "maize", "name_en": "Corn / Maize", "name_hi": "मक्का", "icon": "🌽", "default_disease": "corn_common_rust"},
        {"id": "apple", "name_en": "Apple", "name_hi": "सेब", "icon": "🍎", "default_disease": "apple_scab"},
        {"id": "chilli", "name_en": "Chilli / Pepper", "name_hi": "मिर्च", "icon": "🌶️", "default_disease": "chilli_leaf_curl"},
        {"id": "groundnut", "name_en": "Groundnut", "name_hi": "मूंगफली", "icon": "🥜", "default_disease": "groundnut_tikka"},
        {"id": "mustard", "name_en": "Mustard", "name_hi": "सरसों", "icon": "🌼", "default_disease": "mustard_white_rust"},
        {"id": "healthy", "name_en": "Healthy Crop", "name_hi": "स्वस्थ फसल", "icon": "🌱", "default_disease": "healthy_crop"}
    ]
    return jsonify({"success": True, "crops": crops})

@app.route("/api/encyclopedia", methods=["GET"])
def get_encyclopedia():
    """Returns all disease database entries for the disease library page."""
    search = request.args.get("q", "").lower()
    crop_filter = request.args.get("crop", "").lower()
    
    results = []
    for d_id, item in DISEASE_DATABASE.items():
        if crop_filter and crop_filter not in item["crop"].lower():
            continue
        if search:
            match_txt = f"{item['name_en']} {item['name_hi']} {item['crop']} {item['pathogen_type']}".lower()
            if search not in match_txt:
                continue
        results.append(item)
        
    return jsonify({"success": True, "count": len(results), "diseases": results})

@app.route("/api/ask-agronomist", methods=["POST"])
def ask_agronomist():
    """AI Agronomist Q&A advisory for farmer queries."""
    try:
        data = request.get_json() or {}
        query = data.get("query", "").strip().lower()
        crop = data.get("crop", "general")
        lang = data.get("lang", "en")
        
        # Rule-based / NLP matching for agronomy answers
        answer_en = "Apply balanced N-P-K fertilizer and ensure good field drainage. For severe foliar symptoms, spray Mancozeb 75% WP @ 2.5g/L."
        answer_hi = "संतुलित NPK खाद दें और जल निकासी का ध्यान रखें। फफूंद के लक्षण दिखने पर मैनकोज़ेब 75% WP का 2.5 ग्राम/लीटर छिड़काव करें।"
        
        if "yellow" in query or "पीला" in query:
            answer_en = "Yellowing of leaves can indicate Nitrogen deficiency or Fungal Rust. Apply urea top-dressing (30kg/acre) and spray Propiconazole 25% EC @ 1ml/L if yellow powdery stripes appear."
            answer_hi = "पत्तियों का पीलापन नाइट्रोजन की कमी या रतुआ रोग हो सकता है। 30 किग्रा/एकड़ यूरिया दें और पीला पाउडर दिखने पर प्रोपिकोनाज़ोल 1 मिली/लीटर स्प्रे करें।"
        elif "spot" in query or "धब्बा" in query or "blight" in query or "झुलसा" in query:
            answer_en = "Leaf spots/blights are typically caused by Alternaria or Phytophthora. Spray Copper Oxychloride 50% WP @ 3g/L or Ridomil Gold @ 2g/L. Avoid overhead sprinkler watering."
            answer_hi = "पत्ती धब्बे व झुलसा फफूंद से होते हैं। कॉपर ऑक्सीक्लोराइड 3 ग्राम/लीटर या रिडोमिल 2 ग्राम/लीटर का छिड़काव करें और पत्तियों को गीला रखने से बचें।"
        elif "neem" in query or "organic" in query or "जैविक" in query or "नीम" in query:
            answer_en = "For organic pest and fungal protection, use Cold-Pressed 10,000 ppm Neem Oil @ 5ml/L + 2ml liquid soap. Spray in evening hours every 10-12 days."
            answer_hi = "जैविक रोकथाम के लिए 10,000 ppm नीम का तेल 5 मिली/लीटर साबुन के साथ मिलाकर शाम को हर 10-12 दिन में छिड़कें।"
        elif "price" in query or "mandi" in query or "भाव" in query or "मंडी" in query:
            answer_en = "Current APMC Mandi trends show strong upward demand for quality graded produce. Refer to the Market Price Prediction tab for 15-day forecast."
            answer_hi = "वर्तमान मंडी भाव में अच्छी ग्रेडिंग वाली फसल को ऊंचा भाव मिल रहा है। 15 दिन के भाव अनुमान के लिए मंडी टैब देखें।"

        return jsonify({
            "success": True,
            "query": query,
            "answer_en": answer_en,
            "answer_hi": answer_hi,
            "helpline": "Kisan Call Center: 1800-180-1551"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/diagnose", methods=["POST"])
def diagnose_crop():
    """
    Core AI diagnosis endpoint.
    Accepts JSON with image (base64) or multipart file, along with crop and disease hints.
    """
    try:
        data = request.get_json(silent=True) or {}
        image_data = data.get("image")
        crop_hint = data.get("crop", "tomato")
        manual_disease_id = data.get("disease_id")
        acres = float(data.get("acres", 2.0))
        
        # Handle form-data if sent via multipart
        if not image_data and "image_file" in request.files:
            file = request.files["image_file"]
            image_data = file.read()
            
        if not image_data:
            image_data = b""
            
        # Run computer vision and diagnosis
        analysis = process_and_analyze_image(image_data, crop_hint=crop_hint, manual_disease_id=manual_disease_id)
        
        disease_info = analysis["disease_data"]
        crop_name = disease_info["crop"]
        severity = disease_info["severity"]
        
        # Calculate economic impact & market data
        market_info = get_market_data_for_crop(crop_name)
        economic_impact = calculate_economic_impact(crop_name, acres=acres, disease_severity=severity)
        
        # Weather risk assessment
        weather_risk = evaluate_disease_weather_risk(
            temperature=27.0,
            humidity=78.0,
            rain_chance=35,
            crop_name=crop_name
        )
        
        return jsonify({
            "success": True,
            "analysis": analysis,
            "disease": disease_info,
            "market_info": market_info,
            "economic_impact": economic_impact,
            "weather_risk": weather_risk
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/weather", methods=["GET"])
def get_weather():
    """Returns live weather and disease risk scores for current GPS coordinates."""
    try:
        lat = float(request.args.get("lat", 22.7196))
        lon = float(request.args.get("lon", 75.8577))
        crop = request.args.get("crop", "Tomato")
        
        weather = fetch_live_weather(lat, lon)
        risk = evaluate_disease_weather_risk(
            temperature=weather["temperature"],
            humidity=weather["humidity"],
            rain_chance=weather["rainfall_probability"],
            crop_name=crop
        )
        
        return jsonify({
            "success": True,
            "weather": weather,
            "disease_spread_risk": risk
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/soil-analysis", methods=["POST"])
def soil_analysis():
    """Evaluates soil N-P-K, pH and moisture against optimal crop ranges."""
    try:
        data = request.get_json() or {}
        crop = data.get("crop", "Tomato")
        ph = float(data.get("ph", 6.5))
        n = float(data.get("nitrogen", 180))
        p = float(data.get("phosphorus", 28))
        k = float(data.get("potassium", 240))
        moist = float(data.get("moisture", 62))
        
        result = analyze_soil_health(crop_type=crop, ph=ph, nitrogen=n, phosphorus=p, potassium=k, moisture=moist)
        return jsonify({"success": True, "soil_health": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/market-prices", methods=["GET"])
def get_market_prices():
    """Returns mandi prices and forecast trends for a crop."""
    try:
        crop = request.args.get("crop", "Tomato")
        data = get_market_data_for_crop(crop)
        return jsonify({"success": True, "market_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/calculate-dosage", methods=["POST"])
def calculate_dosage():
    """
    Calculates precise pesticide/fertilizer tank mixing measurements for Knapsack, Drone, or Tractor.
    """
    try:
        data = request.get_json() or {}
        acres = float(data.get("acres", 1.0))
        tank_liters = float(data.get("tank_capacity_liters", 15.0))
        dose_per_liter = float(data.get("dose_per_liter_g_or_ml", 2.0))
        spray_type = data.get("spray_type", "knapsack") # knapsack, drone, tractor
        product_name = data.get("product_name", "Mancozeb 75% WP")
        
        # Spray type water requirements per acre
        water_per_acre = {
            "knapsack": 180,
            "tractor": 250,
            "drone": 10 # Ultra low volume drone spray
        }.get(spray_type, 180)
        
        water_needed_liters = int(acres * water_per_acre)
        
        if spray_type == "drone":
            # Drone spray uses high-concentration ultra low volume
            total_product_amount = round(acres * 500, 1) # ~500g per acre standard
            product_per_tank = round((total_product_amount / max(1, water_needed_liters)) * tank_liters, 1)
        else:
            total_product_amount = round(water_needed_liters * dose_per_liter, 1)
            product_per_tank = round(tank_liters * dose_per_liter, 1)
            
        tank_count = round(water_needed_liters / max(1, tank_liters), 1)
        unit = "grams" if "WP" in product_name or "g" in data.get("unit", "") else "ml"
        
        return jsonify({
            "success": True,
            "product_name": product_name,
            "spray_type": spray_type,
            "acres": acres,
            "total_water_liters": f"{water_needed_liters} Litres (लीटर पानी)",
            "total_product_needed": f"{total_product_amount} {unit}",
            "sprayer_tanks_count": f"~{tank_count} Tanks ({tank_liters}L capacity)",
            "product_per_tank": f"{product_per_tank} {unit} per {tank_liters}L Tank",
            "safety_instructions_en": [
                "Wear protective gloves, goggles and face mask during tank mixing.",
                "Spray in early morning (7-10 AM) or late afternoon (4-6 PM) to prevent rapid evaporation.",
                "Do not spray against the prevailing wind direction.",
                "Maintain 7-10 days waiting period before harvesting post-spray."
            ],
            "safety_instructions_hi": [
                "दवा घोलते व छिड़कते समय दस्ताने, चश्मा और मास्क अवश्य पहनें।",
                "छिड़काव सुबह 7-10 बजे या शाम 4-6 बजे करें ताकि तेज धूप में दवा उड़े नहीं।",
                "हवा की विपरीत दिशा में छिड़काव कभी न करें।",
                "छिड़काव के बाद फसल तुड़ाई से पहले 7-10 दिन का सुरक्षित अंतराल (Waiting Period) रखें।"
            ]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"[AgriShield AI] Server starting on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
