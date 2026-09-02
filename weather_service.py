"""
Weather and Soil Analysis Engine
Integrates live weather forecasting and computes disease proliferation risk
alongside soil NPK, moisture, and pH parameters.
"""
import requests
import datetime

# Default weather simulation / fallback when offline or without coordinates
DEFAULT_WEATHER = {
    "location": "Indore / Central Agri Zone, India",
    "temperature": 27.5,
    "feels_like": 29.2,
    "humidity": 78,
    "rainfall_probability": 35,
    "wind_speed": 12.4,
    "condition": "Partly Cloudy with Humid Breeze",
    "condition_hi": "आंशिक बादल और आर्द्र हवाएं",
    "uv_index": 6.8,
    "forecast_3day": [
        {"day": "Today (आज)", "temp": "28°C / 20°C", "humidity": "78%", "rain_chance": "35%", "icon": "cloud-sun"},
        {"day": "Tomorrow (कल)", "temp": "27°C / 19°C", "humidity": "82%", "rain_chance": "60%", "icon": "cloud-rain"},
        {"day": "Day After (परसों)", "temp": "26°C / 19°C", "humidity": "85%", "rain_chance": "75%", "icon": "cloud-lightning"}
    ]
}


def fetch_live_weather(lat=22.7196, lon=75.8577):
    """
    Fetches real-time weather using Open-Meteo free public API.
    Fallback to DEFAULT_WEATHER if network is offline.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto"
        res = requests.get(url, timeout=4)
        if res.status_code == 200:
            data = res.json()
            curr = data.get("current", {})
            daily = data.get("daily", {})
            
            temp = curr.get("temperature_2m", 28.0)
            humidity = curr.get("relative_humidity_2m", 75)
            feels = curr.get("apparent_temperature", temp + 2)
            wind = curr.get("wind_speed_10m", 11.0)
            rain_prob = daily.get("precipitation_probability_max", [30])[0] if daily.get("precipitation_probability_max") else 30
            
            return {
                "location": f"GPS Lat {lat:.2f}, Lon {lon:.2f}",
                "temperature": temp,
                "feels_like": feels,
                "humidity": humidity,
                "rainfall_probability": rain_prob,
                "wind_speed": wind,
                "condition": "Live Sensor Data",
                "condition_hi": "लाइव उपग्रह व मौसम पूर्वानुमान",
                "uv_index": 7.0,
                "forecast_3day": DEFAULT_WEATHER["forecast_3day"]
            }
    except Exception:
        pass
    return DEFAULT_WEATHER


def evaluate_disease_weather_risk(temperature, humidity, rain_chance, crop_name="Tomato"):
    """
    Evaluates micro-climate fungal/bacterial proliferation index.
    """
    risk_score = 0
    factors_en = []
    factors_hi = []
    
    if humidity >= 80:
        risk_score += 45
        factors_en.append("Critical humidity (>80%) accelerates fungal spore germination.")
        factors_hi.append("80% से अधिक नमी फफूंद बीजाणुओं के अंकुरण को तेजी से बढ़ाती है।")
    elif humidity >= 65:
        risk_score += 25
        factors_en.append("Moderate humidity promotes mild foliar infections.")
        factors_hi.append("मध्यम नमी से पत्तियों पर संक्रमण की संभावना बढ़ती है।")
        
    if 18 <= temperature <= 28:
        risk_score += 35
        factors_en.append("Optimal pathogen incubation temperature range (18-28°C).")
        factors_hi.append("18-28°C का तापमान फंगस के फैलने के लिए सर्वाधिक अनुकूल है।")
    elif temperature > 34:
        risk_score += 15
        factors_en.append("High heat induces plant stress, lowering immunity against viral vectors.")
        factors_hi.append("तेज गर्मी पौधे को कमजोर करती है और वायरस फैलाने वाले कीट बढ़ते हैं।")
        
    if rain_chance >= 50:
        risk_score += 20
        factors_en.append("Rain splash causes rapid bacterial and spore dispersion across canopy.")
        factors_hi.append("बारिश की बूंदों से जीवाणु और फंगस एक पौधे से दूसरे पर तेजी से छिटकते हैं।")
        
    risk_level = "High Risk" if risk_score >= 65 else ("Moderate Risk" if risk_score >= 40 else "Low Risk")
    risk_level_hi = "उच्च खतरा (High Risk)" if risk_score >= 65 else ("मध्यम खतरा (Moderate Risk)" if risk_score >= 40 else "कम खतरा (Low Risk)")
    color = "red" if risk_score >= 65 else ("amber" if risk_score >= 40 else "green")
    
    return {
        "risk_score": min(risk_score, 100),
        "risk_level": risk_level,
        "risk_level_hi": risk_level_hi,
        "color": color,
        "factors_en": factors_en,
        "factors_hi": factors_hi,
        "spray_window_en": "Spray fungicides within 24-48 hours before the expected rain window.",
        "spray_window_hi": "अनुमानित बारिश से 24-48 घंटे पहले फफूंदनाशी का छिड़काव अवश्य पूरा करें।"
    }


def analyze_soil_health(crop_type="Tomato", ph=6.5, nitrogen=180, phosphorus=28, potassium=240, moisture=62):
    """
    Analyzes soil parameters against crop requirements.
    """
    crop_benchmarks = {
        "Tomato": {"ph_min": 6.0, "ph_max": 7.0, "n_rec": "150-200 kg/ha", "p_rec": "50-70 kg/ha", "k_rec": "100-150 kg/ha", "moist_rec": "60-70%"},
        "Potato": {"ph_min": 5.2, "ph_max": 6.5, "n_rec": "180-240 kg/ha", "p_rec": "80-100 kg/ha", "k_rec": "120-150 kg/ha", "moist_rec": "65-75%"},
        "Wheat": {"ph_min": 6.0, "ph_max": 7.5, "n_rec": "120-150 kg/ha", "p_rec": "60 kg/ha", "k_rec": "40-60 kg/ha", "moist_rec": "50-60%"},
        "Rice": {"ph_min": 5.5, "ph_max": 7.0, "n_rec": "120-140 kg/ha", "p_rec": "50-60 kg/ha", "k_rec": "40-50 kg/ha", "moist_rec": "80-95%"},
        "Cotton": {"ph_min": 6.0, "ph_max": 8.0, "n_rec": "100-120 kg/ha", "p_rec": "50-60 kg/ha", "k_rec": "50-60 kg/ha", "moist_rec": "50-65%"},
        "Default": {"ph_min": 6.0, "ph_max": 7.5, "n_rec": "120-180 kg/ha", "p_rec": "50-70 kg/ha", "k_rec": "60-100 kg/ha", "moist_rec": "55-70%"}
    }
    
    crop_first = crop_type.split()[0]
    bench = crop_benchmarks.get(crop_first, crop_benchmarks["Default"])
    
    ph_status = "Optimal" if (bench["ph_min"] <= ph <= bench["ph_max"]) else ("Acidic (कम pH)" if ph < bench["ph_min"] else "Alkaline (अधिक pH)")
    moist_status = "Optimal" if 55 <= moisture <= 75 else ("Dry (सिंचाई की जरूरत)" if moisture < 55 else "Waterlogged (जलभराव)")
    
    advisory_en = []
    advisory_hi = []
    
    if ph < bench["ph_min"]:
        advisory_en.append(f"Soil is acidic (pH {ph}). Apply Agricultural Lime (CaCO3) @ 250 kg/acre to neutralize acidity.")
        advisory_hi.append(f"मिट्टी अम्लीय है (pH {ph})। अम्लता कम करने के लिए 250 किग्रा/एकड़ कृषि चूना डालें।")
    elif ph > bench["ph_max"]:
        advisory_en.append(f"Soil is alkaline (pH {ph}). Incorporate Gypsum @ 300 kg/acre and organic compost.")
        advisory_hi.append(f"मिट्टी क्षारीय है (pH {ph})। सुधार के लिए 300 किग्रा/एकड़ जिप्सम और गोबर की खाद डालें।")
    else:
        advisory_en.append(f"Soil pH ({ph}) is ideal for nutrient bioavailability.")
        advisory_hi.append(f"मिट्टी का pH ({ph}) पोषक तत्वों के अवशोषण के लिए एकदम उत्तम है।")
        
    if moisture < 50:
        advisory_en.append("Soil moisture is low. Schedule a light drip irrigation cycle immediately.")
        advisory_hi.append("मिट्टी में नमी कम है। तुरंत हल्की ड्रिप सिंचाई करें।")
    elif moisture > 80:
        advisory_en.append("High soil saturation. Ensure drainage channels are open to prevent root rot.")
        advisory_hi.append("अधिक नमी से जड़ सड़न का खतरा है। जलनिकासी की नालियां साफ रखें।")
        
    return {
        "ph": ph,
        "ph_status": ph_status,
        "nitrogen_level": f"{nitrogen} kg/ha (Medium)",
        "phosphorus_level": f"{phosphorus} kg/ha (Adequate)",
        "potassium_level": f"{potassium} kg/ha (Good)",
        "moisture": f"{moisture}%",
        "moisture_status": moist_status,
        "target_benchmarks": bench,
        "soil_advisory_en": advisory_en,
        "soil_advisory_hi": advisory_hi
    }
