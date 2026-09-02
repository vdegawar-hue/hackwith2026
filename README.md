# 🌾 AgriShield AI (कृषि रक्षक)

> **Theme 3: Agriculture — Problem 1: AI Crop Disease Detection & Precision Farming Platform**

An intelligent, full-stack agricultural decision support system designed to diagnose crop leaf infections from photos, run computer vision enhancement & thermal NDVI heatmaps, calculate micro-climate disease risks, compute precision fertilizer/pesticide dosage, project APMC mandi prices, and provide bilingual farmer advisory with voice narration (Kisan Vani) and printable Kisan Health Cards.

---

## 🚀 Core Features (7 Modules Implemented)

1. **Farmer Upload & Camera Stream**
   - Drag-and-drop & file picker for JPG/PNG/WEBP.
   - Real-time webcam / smartphone camera capture with instant shutter.
   - Built-in 1-click test samples (Tomato Early Blight, Potato Late Blight, Wheat Yellow Rust, Rice Blast, Healthy Leaf).

2. **Image Processing & Interactive Visualizer**
   - HTML5 Canvas filter pipeline: Original, NDVI False-Color Thermal Vegetation, Grayscale, Edge Detection, Contrast boost.
   - Bounding box and infection hotspots with severity % calculation.

3. **AI Disease Detection Engine**
   - Diagnosis across Solanaceae, Cereals, Cash Crops, and Orchards (Tomato, Potato, Wheat, Rice, Cotton, Maize, Apple, Chilli).
   - High confidence grading, pathogen classification (Fungal, Bacterial, Viral, None).

4. **Weather & Soil Health Analysis**
   - Live GPS weather integration (Temperature, Humidity, Rain Probability, Wind Speed).
   - Micro-climate fungal spore propagation risk calculator.
   - Soil pH and N-P-K nutrient status evaluation.

5. **Fertilizers & Treatment Advisory + Dosage Calculator**
   - Triple-Tier Solutions: Chemical synthetic pesticides, Organic/Bio remedies (Neem oil, Jeevamrutha, Trichoderma), Preventive cultural practices.
   - Acreage and Knapsack sprayer tank dilution dosage calculator.

6. **Market Price Prediction & Mandi Forecast**
   - Real-time modal prices from top state APMC mandis.
   - 30-day historical price curve & 15-day AI forecast trend chart (powered by Chart.js).
   - Economic yield protection calculator (Potential financial loss vs. saved harvest value).

7. **Farmer-Centric Accessibility**
   - **Bilingual Interface**: Full toggle between English and Hindi (हिंदी).
   - **Kisan Vani Voice Synthesizer**: Text-to-Speech audio narration in Hindi/English.
   - **Printable Kisan Crop Health Card**: 1-click printable prescription slip with QR stamp.
   - **Kisan Call Center Integration**: Toll-Free 1800-180-1551 quick dial.

---

## 💻 How to Run the Application

### Option 1: Double click `run.bat`
Simply double click `run.bat` in Windows Explorer.

### Option 2: Run via Terminal
```bash
cd C:\Users\Hp\.gemini\antigravity\scratch\agrishield-ai
python app.py
```
Open your browser at: **`http://localhost:5000`**
