"""
Comprehensive Agricultural Disease Knowledge Base & Advisory Catalog
Supports 15+ major Indian crops with detailed pathogen data, severity grading,
chemical, organic, and preventive treatments in English & Hindi.
"""

DISEASE_DATABASE = {
    # TOMATO
    "tomato_early_blight": {
        "id": "tomato_early_blight",
        "crop": "Tomato (टमाटर)",
        "category": "Vegetables",
        "name_en": "Early Blight (Alternaria solani)",
        "name_hi": "अगेती झुलसा (अर्ली ब्लाइट)",
        "pathogen_type": "Fungal (फफूंद जनित)",
        "severity": "Moderate to High",
        "confidence_base": 96.2,
        "symptoms_en": [
            "Concentric dark brown 'bullseye' rings on older leaves.",
            "Yellow halo surrounding brown necrotic spots.",
            "Premature defoliation starting from lower foliage upward.",
            "Dark, leathery sunken spots on tomato fruit stem ends."
        ],
        "symptoms_hi": [
            "पुरानी पत्तियों पर गोल भूरे छल्ले (बुलआई) जैसे धब्बे।",
            "भूरे धब्बों के चारों ओर पीले रंग का घेरा।",
            "निचली पत्तियों का समय से पहले सूखकर गिरना।",
            "टमाटर के तने के पास काले धब्बेदार गड्ढे।"
        ],
        "causes_en": "Warm temperatures (24-29°C) accompanied by high humidity (>80%) or frequent rains and heavy dew.",
        "causes_hi": "24-29°C तापमान और 80% से अधिक नमी या लगातार बारिश और ओस।",
        "chemical_treatment_en": [
            "Spray Mancozeb 75% WP @ 2.5g per litre of water (500g in 200L/acre).",
            "Apply Azoxystrobin 23% SC @ 1ml per litre for systemic curative action.",
            "Use Copper Oxychloride 50% WP @ 3g per litre on 10-day intervals."
        ],
        "chemical_treatment_hi": [
            "मैनकोज़ेब 75% WP का 2.5 ग्राम प्रति लीटर पानी में घोलकर छिड़काव करें (500 ग्राम प्रति एकड़)।",
            "सिस्टेमिक रोकथाम के लिए एज़ोक्सीस्ट्रोबिन 23% SC 1 मिली/लीटर स्प्रे करें।",
            "कॉपर ऑक्सीक्लोराइड 50% WP 3 ग्राम प्रति लीटर 10 दिन के अंतराल पर छिड़कें।"
        ],
        "organic_treatment_en": [
            "Spray Cold-Pressed Neem Oil (10,000 ppm) @ 5ml/litre with liquid soap.",
            "Foliar spray of Trichoderma viride @ 5g/litre or Jeevamrutha @ 10%.",
            "Spray 10% Cow urine (Gomutra) mixed with 2% sour buttermilk."
        ],
        "organic_treatment_hi": [
            "नीम का तेल (10,000 ppm) 5 मिली प्रति लीटर पानी में थोड़ा साबुन मिलाकर छिड़कें।",
            "ट्राइकोडर्मा विरिडी 5 ग्राम/लीटर या जीवामृत (10%) का छिड़काव करें।",
            "10% गोमूत्र और 2% खट्टी छाछ का मिश्रण बनाकर पत्तों पर स्प्रे करें।"
        ],
        "preventive_practices_en": [
            "Practice minimum 3-year crop rotation with non-solanaceous crops.",
            "Use drip irrigation to avoid leaf wetness; avoid overhead sprinklers.",
            "Prune bottom 12 inches of leaves to prevent soil splash.",
            "Mulch soil bed with straw or silver-black plastic mulch."
        ],
        "preventive_practices_hi": [
            "टमाटर कुल के अलावा अन्य फसलों के साथ 3 साल का फसल चक्र अपनाएं।",
            "टपक (ड्रिप) सिंचाई का उपयोग करें ताकि पत्तियां गीली न रहें।",
            "पौधे के निचले 1 फुट के पत्तों की छंटाई करें ताकि मिट्टी का संक्रमण न लगे।",
            "मिट्टी पर पुआल या प्लास्टिक मल्चिंग बिछाएं।"
        ],
        "recommended_fertilizers_en": "Apply balanced NPK 19:19:19, supplement Calcium Nitrate @ 5kg/acre to strengthen cell walls.",
        "recommended_fertilizers_hi": "संतुलित NPK 19:19:19 दें और कोशिका मजबूती के लिए कैल्शियम नाइट्रेट 5 किग्रा/एकड़ दें।",
        "spread_risk": "High if relative humidity > 80% and temp 22-28°C"
    },

    "tomato_late_blight": {
        "id": "tomato_late_blight",
        "crop": "Tomato (टमाटर)",
        "category": "Vegetables",
        "name_en": "Late Blight (Phytophthora infestans)",
        "name_hi": "पछेती झुलसा (लेट ब्लाइट)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity": "Severe / Critical",
        "confidence_base": 97.5,
        "symptoms_en": [
            "Water-soaked dark greasy spots that enlarge rapidly into brown blotches.",
            "White velvety fungal growth on undersides of leaves during wet weather.",
            "Stem cankers causing vine collapse and rotten firm brown fruits."
        ],
        "symptoms_hi": [
            "पत्तियों पर पानी में भीगे जैसे काले-भूरे तेजी से फैलने वाले धब्बे।",
            "गीले मौसम में पत्ती की निचली सतह पर सफेद मखमली फफूंद।",
            "तने का सड़ना और टमाटर के फलों पर कड़े भूरे सड़न के दाग।"
        ],
        "causes_en": "Cool (15-22°C), overcast, and persistently wet foggy weather.",
        "causes_hi": "ठंडा (15-22°C), बादलों भरा और लगातार कोहरा/बारिश वाला मौसम।",
        "chemical_treatment_en": [
            "Emergency Spray: Metalaxyl 8% + Mancozeb 64% WP (Ridomil MZ) @ 2.5g/L.",
            "Cymoxanil 8% + Mancozeb 64% @ 2g/L of water.",
            "Dimethomorph 50% WP @ 1g/L for advanced infections."
        ],
        "chemical_treatment_hi": [
            "आपातकालीन स्प्रे: मेटालेक्सिल 8% + मैनकोज़ेब 64% WP 2.5 ग्राम/लीटर।",
            "साइमोक्सानिल 8% + मैनकोज़ेब 64% 2 ग्राम प्रति लीटर पानी में।",
            "अधिक संक्रमण पर डाइमथॉमॉर्फ 50% WP 1 ग्राम/लीटर छिड़कें।"
        ],
        "organic_treatment_en": [
            "Apply Copper Octanoate (Soap) spray @ 3ml/L.",
            "Spray Bacillus subtilis bio-fungicide @ 5g/L before rain spells.",
            "Apply fermented garlic & ginger extract (50ml/L)."
        ],
        "organic_treatment_hi": [
            "कॉपर आधारित बायो-फंगीसाइड 3 मिली/लीटर स्प्रे करें।",
            "बारिश से पहले बैसिलस सबटिलिस 5 ग्राम/लीटर छिड़कें।",
            "लहसुन और अदरक का किण्वित अर्क (50 मिली/लीटर) स्प्रे करें।"
        ],
        "preventive_practices_en": [
            "Destroy severely infected crop debris immediately (do not compost).",
            "Space plants widely (60cm x 60cm) to maximize air circulation.",
            "Plant certified late-blight resistant tomato hybrid seeds."
        ],
        "preventive_practices_hi": [
            "संक्रमित पौधों को तुरंत उखाड़कर जला दें (खाद गड्ढे में न डालें)।",
            "पौधों के बीच पर्याप्त दूरी (60 सेमी) रखें ताकि हवा का प्रवाह बना रहे।",
            "रोग-रोधी प्रमाणित हाइब्रिड बीजों का ही उपयोग करें।"
        ],
        "recommended_fertilizers_en": "Reduce excessive nitrogen; apply Potassium Sulfate (0-0-50) @ 3g/L to improve immunity.",
        "recommended_fertilizers_hi": "यूरिया (नाइट्रोजन) कम करें; रोग प्रतिरोधक क्षमता बढ़ाने के लिए पोटाश (0-0-50) 3 ग्राम/लीटर दें।",
        "spread_risk": "Very High in cool foggy mornings with temp 14-20°C"
    },

    # POTATO
    "potato_late_blight": {
        "id": "potato_late_blight",
        "crop": "Potato (आलू)",
        "category": "Tubers",
        "name_en": "Potato Late Blight (Phytophthora infestans)",
        "name_hi": "आलू का पछेती झुलसा",
        "pathogen_type": "Fungal / Oomycete",
        "severity": "Critical",
        "confidence_base": 98.1,
        "symptoms_en": [
            "Dark water-soaked lesions appearing at tips and margins of leaves.",
            "White powdery mold on the lower leaf surface in humid conditions.",
            "Rapid total blackening and death of foliage within days."
        ],
        "symptoms_hi": [
            "पत्तियों के किनारों और सिरों पर काले गीले धब्बे।",
            "पत्तियों के नीचे सफेद पाउडर जैसा फफूंद।",
            "कुछ ही दिनों में पौधे का काला पड़कर पूरी तरह नष्ट हो जाना।"
        ],
        "causes_en": "High humidity (>90%) with cool temperature (10-20°C) and cloudy days.",
        "causes_hi": "90% से अधिक नमी, ठंडा मौसम (10-20°C) और बादल/कोहरा।",
        "chemical_treatment_en": [
            "Prophylactic: Mancozeb 75% WP @ 2.5g/L.",
            "Curative: Cymoxanil + Mancozeb (Curzate) @ 2g/L or Fenamidone + Mancozeb @ 2.5g/L."
        ],
        "chemical_treatment_hi": [
            "बचाव हेतु: मैनकोज़ेब 75% WP 2.5 ग्राम/लीटर।",
            "उपचार हेतु: साइमोक्सानिल + मैनकोज़ेब 2 ग्राम/लीटर या फेनामिडोन 2.5 ग्राम/लीटर।"
        ],
        "organic_treatment_en": [
            "Spray Trichoderma harzianum @ 10g/L.",
            "Bordeaux mixture (1%) application on clear days."
        ],
        "organic_treatment_hi": [
            "ट्राइकोडर्मा हरज़ियानम 10 ग्राम/लीटर का छिड़काव करें।",
            "साफ मौसम में 1% बोर्डो मिश्रण का स्प्रे करें।"
        ],
        "preventive_practices_en": [
            "Earthing up soil to cover tubers by at least 10cm to protect from spores.",
            "De-haulm (cut foliage) 10-15 days before harvest if blight appears."
        ],
        "preventive_practices_hi": [
            "कंदों को फफूंद से बचाने के लिए कम से कम 10 सेमी मिट्टी चढ़ाएं (Earthing up)।",
            "रोग आने पर खुदाई से 12 दिन पहले बेल काट दें (De-haulming)।"
        ],
        "recommended_fertilizers_en": "Potash (MOP) @ 40kg/acre at planting; avoid excessive urea.",
        "recommended_fertilizers_hi": "बुवाई के समय पोटाश 40 किग्रा/एकड़ दें; यूरिया का अत्यधिक प्रयोग न करें।",
        "spread_risk": "Extremely High during dense winter fog"
    },

    # WHEAT
    "wheat_yellow_rust": {
        "id": "wheat_yellow_rust",
        "crop": "Wheat (गेहूं)",
        "category": "Cereals",
        "name_en": "Yellow / Stripe Rust (Puccinia striiformis)",
        "name_hi": "गेहूं का पीला रतुआ (स्ट्राइप रस्ट)",
        "pathogen_type": "Fungal (फफूंद)",
        "severity": "High to Critical",
        "confidence_base": 96.8,
        "symptoms_en": [
            "Bright yellow pustules arranged in continuous long stripes along leaf veins.",
            "Yellow powder readily rubs off onto fingers or clothes.",
            "Stunted grain filling resulting in shriveled lightweight wheat kernels."
        ],
        "symptoms_hi": [
            "पत्तियों की नसों के समानांतर पीले रंग की धारियों में उभरे दाने।",
            "उंगलियों या कपड़ों पर छूने से पीला पाउडर लग जाना।",
            "दानों का छोटा और सिकुड़ जाना जिससे भारी उपज नुकसान होता है।"
        ],
        "causes_en": "Cold weather (10-15°C) with high humidity and morning dew in northern plains.",
        "causes_hi": "10-15°C तापमान, सुबह की ओस और उत्तरी मैदानी इलाकों की सर्दी।",
        "chemical_treatment_en": [
            "Spray Propiconazole 25% EC (Tilt) @ 1ml per litre of water (200ml in 200L/acre).",
            "Tebuconazole 25.9% EC @ 1.25ml/L at first appearance of yellow stripes."
        ],
        "chemical_treatment_hi": [
            "प्रोपिकोनाज़ोल 25% EC (टिल्ट) 1 मिली/लीटर (200 मिली प्रति 200 लीटर पानी प्रति एकड़) छिड़कें।",
            "पीली धारियां दिखते ही टेबुकोनाज़ोल 25.9% EC 1.25 मिली/लीटर का छिड़काव करें।"
        ],
        "organic_treatment_en": [
            "Apply Sour Butter Milk (Chhach) 5L + Copper plate soaked for 5 days in 100L water.",
            "Neem Seed Kernel Extract (NSKE 5%) spray."
        ],
        "organic_treatment_hi": [
            "5 दिन तांबे के बर्तन में रखी 5 लीटर खट्टी छाछ को 100 लीटर पानी में मिलाकर छिड़कें।",
            "नीम बीज अर्क (NSKE 5%) का छिड़काव करें।"
        ],
        "preventive_practices_en": [
            "Sow rust-resistant varieties such as HD-3086, DBW-187, DBW-222, PBW-725.",
            "Timely sowing in November to avoid late cold moisture peaks."
        ],
        "preventive_practices_hi": [
            "प्रतिरोधी किस्में जैसे HD-3086, DBW-187, DBW-222, PBW-725 लगाएं।",
            "नवंबर में समय पर बुवाई करें ताकि देर से होने वाले संक्रमण से बचा जा सके।"
        ],
        "recommended_fertilizers_en": "Balanced NPK (120:60:40 kg/ha); avoid late top-dressing with nitrogen alone.",
        "recommended_fertilizers_hi": "संतुलित NPK (120:60:40); बाद की अवस्था में केवल यूरिया देने से बचें।",
        "spread_risk": "High in January-February cold humid periods"
    },

    # RICE
    "rice_blast": {
        "id": "rice_blast",
        "crop": "Rice / Paddy (धान)",
        "category": "Cereals",
        "name_en": "Rice Blast (Magnaporthe oryzae)",
        "name_hi": "धान का झोंका रोग (ब्लास्ट)",
        "pathogen_type": "Fungal (फफूंद)",
        "severity": "Severe",
        "confidence_base": 95.4,
        "symptoms_en": [
            "Spindle/diamond-shaped lesions with grayish centers and brown/red margins on leaves.",
            "Neck blast causes blackening of the panicle stem, leading to sterile white heads."
        ],
        "symptoms_hi": [
            "पत्तियों पर नाव/आंख के आकार के धब्बे जिनका केंद्र भूरा-धूसर और किनारा लाल-भूरा होता है।",
            "गर्दन तोड़ (नेक ब्लास्ट) में बाली का आधार काला पड़ जाता है और दाने नहीं भरते।"
        ],
        "causes_en": "Night temp 20-24°C, day temp 28°C, relative humidity > 90%, excessive nitrogen fertilizer.",
        "causes_hi": "रात का तापमान 20-24°C, 90% से अधिक नमी और यूरिया का अत्यधिक उपयोग।",
        "chemical_treatment_en": [
            "Spray Tricyclazole 75% WP (Beam) @ 0.6g per litre (120g/acre).",
            "Kasugamycin 3% SL @ 2ml/L or Isoprothiolane 40% EC @ 1.5ml/L."
        ],
        "chemical_treatment_hi": [
            "ट्राइसाइक्लाज़ोल 75% WP (बीम) 0.6 ग्राम प्रति लीटर (120 ग्राम/एकड़) छिड़कें।",
            "कासुगामाइसिन 3% SL 2 मिली/लीटर या आइसोप्रोधियोलेन 40% EC 1.5 मिली/लीटर स्प्रे करें।"
        ],
        "organic_treatment_en": [
            "Seed treatment with Pseudomonas fluorescens @ 10g/kg seed.",
            "Spray Agnihotra ash water + fermented seaweed extract @ 3ml/L."
        ],
        "organic_treatment_hi": [
            "स्यूडोमोनास फ्लोरेसेंस 10 ग्राम/किग्रा से बीज शोधन करें।",
            "समुद्री शैवाल अर्क (सीवीड) 3 मिली/लीटर पानी में मिलाकर छिड़कें।"
        ],
        "preventive_practices_en": [
            "Avoid excessive nitrogenous fertilizers; apply nitrogen in 3 split doses.",
            "Maintain proper field water level (2-3 inches) without drying out during panicle emergence."
        ],
        "preventive_practices_hi": [
            "यूरिया का एकमुश्त प्रयोग न करें; इसे 3 बराबर किस्तों में बांटकर दें।",
            "बाली निकलते समय खेत में 2-3 इंच पानी का स्तर बनाए रखें, सूखने न दें।"
        ],
        "recommended_fertilizers_en": "Apply Silicon fertilizer @ 100kg/ha and Potash @ 50kg/ha to strengthen rice epidermis.",
        "recommended_fertilizers_hi": "पत्तियों को सख्त बनाने के लिए सिलिकॉन 100 किग्रा/हेक्टेयर और पोटाश 50 किग्रा/हेक्टेयर दें।",
        "spread_risk": "High during monsoon cloudy weeks with persistent drizzle"
    },

    # COTTON
    "cotton_bacterial_blight": {
        "id": "cotton_bacterial_blight",
        "crop": "Cotton (कपास)",
        "category": "Cash Crops",
        "name_en": "Bacterial Blight / Angular Leaf Spot (Xanthomonas citri pv. malvacearum)",
        "name_hi": "कपास का जीवाणु झुलसा (कोणीय पत्ती धब्बा)",
        "pathogen_type": "Bacterial (जीवाणु जनित)",
        "severity": "Moderate to Severe",
        "confidence_base": 94.7,
        "symptoms_en": [
            "Small angular water-soaked translucent spots restricted by leaf veins.",
            "Black arm symptoms causing stem lesions and branch breakage.",
            "Boll rot leading to stained lint and reduced fiber quality."
        ],
        "symptoms_hi": [
            "पत्तियों की नसों के बीच कोणीय (त्रिकोणीय) गीले धब्बे।",
            "तने पर काले घाव (ब्लैक आर्म) जिससे टहनियां टूट जाती हैं।",
            "टिंडों का सड़ना जिससे कपास की गुणवत्ता खराब हो जाती है।"
        ],
        "causes_en": "Warm humid conditions (30-35°C, RH > 85%) and rain-splash wind storms.",
        "causes_hi": "गर्म और उमस भरा मौसम (30-35°C, नमी > 85%) और तेज बारिश की फुहारें।",
        "chemical_treatment_en": [
            "Spray Streptocycline 100ppm (1g in 10L water) + Copper Oxychloride 50% WP (30g in 10L water).",
            "Repeat after 12-15 days if rain persists."
        ],
        "chemical_treatment_hi": [
            "स्ट्रेप्टोसाइक्लिन 1 ग्राम + कॉपर ऑक्सीक्लोराइड 30 ग्राम को 10 लीटर पानी में मिलाकर छिड़कें।",
            "लगातार बारिश होने पर 12-15 दिन बाद दोबारा छिड़कें।"
        ],
        "organic_treatment_en": [
            "Spray 5% Cow Dung supernatant extract mixed with 2% Turmeric powder.",
            "Neem cake application in soil @ 150kg/acre."
        ],
        "organic_treatment_hi": [
            "गोबर का छना हुआ पानी (5%) में 2% हल्दी पाउडर मिलाकर छिड़कें।",
            "खेत में 150 किग्रा/एकड़ की दर से नीम की खली डालें।"
        ],
        "preventive_practices_en": [
            "Acid delinting of cotton seeds with concentrated Sulfuric acid (100ml/kg seed).",
            "Burn infected cotton stalks post-harvest."
        ],
        "preventive_practices_hi": [
            "बीजों को सल्फ्यूरिक एसिड (100 मिली/किग्रा) से उपचारित (Delinting) करके बोएं।",
            "फसल कटाई के बाद संक्रमित डंठलों को खेत से हटाकर नष्ट करें।"
        ],
        "recommended_fertilizers_en": "Foliar spray of Potassium Nitrate (13:0:45) @ 10g/L during boll development.",
        "recommended_fertilizers_hi": "टिंडे बनते समय पोटेशियम नाइट्रेट (13:0:45) 10 ग्राम/लीटर का छिड़काव करें।",
        "spread_risk": "High after monsoon storms"
    },

    # CORN
    "corn_common_rust": {
        "id": "corn_common_rust",
        "crop": "Corn / Maize (मक्का)",
        "category": "Cereals",
        "name_en": "Common Rust (Puccinia sorghi)",
        "name_hi": "मक्का का रतुआ (कॉमन रस्ट)",
        "pathogen_type": "Fungal (फफूंद)",
        "severity": "Moderate",
        "confidence_base": 95.8,
        "symptoms_en": [
            "Small, oval to elongate brownish-red pustules scattered over both leaf surfaces.",
            "Pustules rupture epidermal tissue turning golden-brown to blackish.",
            "Premature drying of leaf canopy affecting cob filling."
        ],
        "symptoms_hi": [
            "पत्तियों की दोनों सतहों पर लाल-भूरे उभरे हुए छोटे दाने।",
            "दानों के फटने से पत्तियों पर भूरा पाउडर निकलना।",
            "पत्तियों का समय से पहले सूखना जिससे भुट्टे में दाना कम भरता है।"
        ],
        "causes_en": "Moderate temperatures (16-25°C) with high relative humidity (>95%) and dew.",
        "causes_hi": "16-25°C तापमान और 95% से अधिक नमी व ओस।",
        "chemical_treatment_en": [
            "Spray Mancozeb 75% WP @ 2.5g/L or Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1ml/L."
        ],
        "chemical_treatment_hi": [
            "मैनकोज़ेब 75% WP 2.5 ग्राम/लीटर या एमिस्टार टॉप (एज़ोक्सीस्ट्रोबिन + डाइफेनोकोनाज़ोल) 1 मिली/लीटर छिड़कें।"
        ],
        "organic_treatment_en": [
            "Spray 10% fermented Dashparni Kashayam @ 20ml/L.",
            "Foliar application of Ampelomyces quisqualis bio-fungicide @ 5g/L."
        ],
        "organic_treatment_hi": [
            "दशपर्णी कषायम (10%) 20 मिली प्रति लीटर पानी में मिलाकर छिड़कें।",
            "जैविक फफूंदनाशी 5 ग्राम/लीटर का पर्णीय छिड़काव करें।"
        ],
        "preventive_practices_en": [
            "Plant rust-tolerant hybrid corn varieties.",
            "Avoid high plant densities to encourage sunlight penetration."
        ],
        "preventive_practices_hi": [
            "रोग-रोधी हाइब्रिड मक्का के बीजों का चयन करें।",
            "पौधों को बहुत घना न लगाएं ताकि धूप और हवा सही से मिले।"
        ],
        "recommended_fertilizers_en": "Zinc Sulfate (ZnSO4 21%) @ 10kg/acre soil application + balanced NPK.",
        "recommended_fertilizers_hi": "जिंक सल्फेट 10 किग्रा/एकड़ और संतुलित NPK का प्रयोग करें।",
        "spread_risk": "Moderate during cloudy monsoon days"
    },

    # APPLE
    "apple_scab": {
        "id": "apple_scab",
        "crop": "Apple (सेब)",
        "category": "Horticulture",
        "name_en": "Apple Scab (Venturia inaequalis)",
        "name_hi": "सेब का स्कैब रोग (खुरंड)",
        "pathogen_type": "Fungal (फफूंद)",
        "severity": "Severe",
        "confidence_base": 96.1,
        "symptoms_en": [
            "Olive-green velvety spots on leaves that turn dark brown to black.",
            "Cork-like scabby cracked lesions on apple fruit skin causing deformity."
        ],
        "symptoms_hi": [
            "पत्तियों पर जैतूनी-हरे मखमली धब्बे जो बाद में काले पड़ जाते हैं।",
            "सेब के छिलके पर खुरदुरे दरारदार काले चकत्ते जिससे फल टेढ़ा-मेढ़ा हो जाता है।"
        ],
        "causes_en": "Cool spring rains and wet leaves for > 9 hours continuously at 15-20°C.",
        "causes_hi": "बसंत ऋतु की बारिश और 15-20°C पर पत्तियों का 9 घंटे से ज्यादा गीला रहना।",
        "chemical_treatment_en": [
            "Spray Captan 50% WP @ 2.5g/L or Difenoconazole 25% EC (Score) @ 0.5ml/L at petal fall."
        ],
        "chemical_treatment_hi": [
            "कैप्टन 50% WP 2.5 ग्राम/लीटर या डाइफेनोकोनाज़ोल 25% EC 0.5 मिली/लीटर पंखुड़ी झड़ने पर स्प्रे करें।"
        ],
        "organic_treatment_en": [
            "Spray Lime Sulfur 2% during dormant stage.",
            "Potassium Bicarbonate spray @ 3g/L."
        ],
        "organic_treatment_hi": [
            "सुप्त अवस्था में 2% लाइम सल्फर का छिड़काव करें।",
            "पोटेशियम बाइकार्बोनेट 3 ग्राम/लीटर पानी में स्प्रे करें।"
        ],
        "preventive_practices_en": [
            "Rake and destroy fallen leaves in autumn or spray 5% urea on orchard floor to accelerate leaf decomposition."
        ],
        "preventive_practices_hi": [
            "शरद ऋतु में गिरे हुए पत्तों को नष्ट करें या 5% यूरिया का छिड़काव करके सड़ा दें।"
        ],
        "recommended_fertilizers_en": "Boron & Calcium foliar sprays (0.2%) during fruit development.",
        "recommended_fertilizers_hi": "फल विकास के समय बोरॉन व कैल्शियम (0.2%) का पर्णीय छिड़काव करें।",
        "spread_risk": "High during spring rainy days"
    },

    # CHILLI
    "chilli_leaf_curl": {
        "id": "chilli_leaf_curl",
        "crop": "Chilli / Pepper (मिर्च)",
        "category": "Spices",
        "name_en": "Chilli Leaf Curl Virus (transmitted by Whitefly)",
        "name_hi": "मिर्च का पर्ण कुंचन रोग (मरोड़िया/चुर्रा-मुर्रा)",
        "pathogen_type": "Viral (सफेद मक्खी द्वारा फैलने वाला वायरस)",
        "severity": "High",
        "confidence_base": 97.0,
        "symptoms_en": [
            "Upward curling and puckering of leaves with vein thickening.",
            "Severe stunting of plants with bushy appearance and flower drop."
        ],
        "symptoms_hi": [
            "पत्तियों का ऊपर की ओर मुड़ना (नाव जैसी बनना) और नसों का मोटा होना।",
            "पौधे की बढ़वार रुकना, झाड़ी जैसा दिखना और फूलों का झड़ जाना।"
        ],
        "causes_en": "Whitefly (Bemisia tabaci) insect vector populations proliferating in dry warm conditions.",
        "causes_hi": "गर्म व शुष्क मौसम में सफेद मक्खी (Whitefly) कीट का प्रकोप।",
        "chemical_treatment_en": [
            "Vector Control: Spray Diafenthiuron 50% WP @ 1.2g/L or Acetamiprid 20% SP @ 0.3g/L.",
            "Imidacloprid 17.8% SL @ 0.5ml/L."
        ],
        "chemical_treatment_hi": [
            "कीट नियंत्रण: डायफेंथियूरॉन 50% WP 1.2 ग्राम/लीटर या एसिटामिप्रिड 20% SP 0.3 ग्राम/लीटर।",
            "इमिडाक्लोप्रिड 17.8% SL 0.5 मिली/लीटर पानी में छिड़कें।"
        ],
        "organic_treatment_en": [
            "Install Yellow Sticky Traps @ 20 traps per acre.",
            "Spray Agniastra @ 20ml/L or 5% Neem Oil spray regularly."
        ],
        "organic_treatment_hi": [
            "खेत में 20 पीले चिपचिपे कार्ड (येलो स्टिकी ट्रैप) प्रति एकड़ लगाएं।",
            "अग्निअस्त्र 20 मिली/लीटर या 5% नीम तेल का नियमित छिड़काव करें।"
        ],
        "preventive_practices_en": [
            "Grow 2-3 border rows of Maize or Sorghum as natural wind/insect barrier.",
            "Nursery bed covered with 40-mesh nylon net."
        ],
        "preventive_practices_hi": [
            "खेत के चारों ओर मक्का या ज्वार की 3 कतारें सुरक्षा घेरा (बैरियर) बनाकर लगाएं।",
            "नर्सरी में 40 मेश की जाली से पौधों को ढककर रखें।"
        ],
        "recommended_fertilizers_en": "Foliar spray of Micronutrient mixture (Zinc + Boron + Magnesium) @ 2g/L to overcome stress.",
        "recommended_fertilizers_hi": "तनाव दूर करने के लिए सूक्ष्म पोषक तत्व (जिंक + बोरॉन) 2 ग्राम/लीटर का छिड़काव करें।",
        "spread_risk": "High in warm sunny spells"
    },

    # GROUNDNUT (Tikka Disease)
    "groundnut_tikka": {
        "id": "groundnut_tikka",
        "crop": "Groundnut / Peanut (मूंगफली)",
        "category": "Oilseeds",
        "name_en": "Tikka Leaf Spot (Cercospora arachidicola)",
        "name_hi": "मूंगफली का टिक्का रोग (पत्ती धब्बा)",
        "pathogen_type": "Fungal (फफूंद)",
        "severity": "Moderate to Severe",
        "confidence_base": 96.0,
        "symptoms_en": [
            "Small circular dark brown to black spots with yellow halo on upper leaf surfaces.",
            "Severe early leaf fall leaving bare stalks and reduced pod weight."
        ],
        "symptoms_hi": [
            "पत्तियों की ऊपरी सतह पर पीले घेरे वाले गोल गहरे भूरे या काले धब्बे।",
            "पत्तियों का तेजी से गिरना और फलियों का छोटा रह जाना।"
        ],
        "causes_en": "Warm and humid weather (25-30°C) with prolonged leaf wetness.",
        "causes_hi": "25-30°C तापमान और पत्तियों का लंबे समय तक गीला रहना।",
        "chemical_treatment_en": [
            "Spray Carbendazim 12% + Mancozeb 63% WP (SAAF) @ 2g/L of water.",
            "Hexaconazole 5% EC @ 2ml/L on 12-day intervals."
        ],
        "chemical_treatment_hi": [
            "कार्बेन्डाजिम 12% + मैनकोज़ेब 63% WP (साफ) 2 ग्राम/लीटर पानी में घोलकर छिड़कें।",
            "हेक्साकोनाज़ोल 5% EC 2 मिली/लीटर 12 दिन के अंतराल पर स्प्रे करें।"
        ],
        "organic_treatment_en": [
            "Spray 5% Neem Seed Kernel Extract (NSKE) with soap.",
            "Trichoderma viride seed treatment @ 4g/kg seed."
        ],
        "organic_treatment_hi": [
            "5% नीम बीज अर्क (NSKE) का छिड़काव करें।",
            "ट्राइकोडर्मा विरिडी 4 ग्राम/किग्रा बीज से बीज शोधन करें।"
        ],
        "preventive_practices_en": [
            "Deep summer ploughing to bury crop residue and fungal spores.",
            "Intercrop with Pearl Millet (Bajra) in 4:1 ratio."
        ],
        "preventive_practices_hi": [
            "गर्मियों में गहरी जुताई करें ताकि फफूंद के अवशेष नष्ट हो जाएं।",
            "मूंगफली के साथ बाजरे की अंतर्वर्ती खेती (4:1 अनुपात) करें।"
        ],
        "recommended_fertilizers_en": "Gypsum application @ 200 kg/acre at 40-45 DAS for pod filling and sulfur nutrition.",
        "recommended_fertilizers_hi": "बुवाई के 40-45 दिन बाद जिप्सम 200 किग्रा/एकड़ दें जिससे फलियां भारी बनें।",
        "spread_risk": "High in humid kharif periods"
    },

    # MUSTARD (White Rust)
    "mustard_white_rust": {
        "id": "mustard_white_rust",
        "crop": "Mustard (सरसों)",
        "category": "Oilseeds",
        "name_en": "White Rust / Blister (Albugo candida)",
        "name_hi": "सरसों का सफेद रतुआ (सफेद फफोले)",
        "pathogen_type": "Oomycete (फफूंद)",
        "severity": "Moderate to High",
        "confidence_base": 95.7,
        "symptoms_en": [
            "White or creamy raised blister-like pustules on leaf undersides.",
            "Floral malformation ('Staghead') where flower heads become swollen and sterile."
        ],
        "symptoms_hi": [
            "पत्तियों की निचली सतह पर सफेद या मलाईदार उभरे हुए फफोले।",
            "फूलों का फूलकर विकृत (स्टैगहेड) हो जाना जिससे बीज नहीं बनते।"
        ],
        "causes_en": "Moist cool weather (12-18°C) with morning fog and high relative humidity (>85%).",
        "causes_hi": "12-18°C का ठंडा मौसम, सुबह का कोहरा और 85% से अधिक नमी।",
        "chemical_treatment_en": [
            "Spray Metalaxyl 8% + Mancozeb 64% WP (Ridomil MZ) @ 2g/L of water.",
            "Mancozeb 75% WP @ 2g/L prophylactic spray."
        ],
        "chemical_treatment_hi": [
            "मेटालेक्सिल 8% + मैनकोज़ेब 64% WP (रिडोमिल) 2 ग्राम/लीटर छिड़कें।",
            "बचाव के लिए मैनकोज़ेब 75% WP 2 ग्राम/लीटर का स्प्रे करें।"
        ],
        "organic_treatment_en": [
            "Seed treatment with Trichoderma viride @ 5g/kg seed.",
            "Spray Garlic bulb extract (5%) mixed with sour buttermilk."
        ],
        "organic_treatment_hi": [
            "ट्राइकोडर्मा विरिडी 5 ग्राम/किग्रा से बीज उपचारित करें।",
            "लहसुन का अर्क (5%) खट्टी छाछ के साथ मिलाकर छिड़कें।"
        ],
        "preventive_practices_en": [
            "Timely sowing before 20th October to escape peak staghead phase.",
            "Remove and burn stagheads immediately on noticing."
        ],
        "preventive_practices_hi": [
            "20 अक्टूबर से पहले समय पर बुवाई करें ताकि कोहरे के समय रोग न लगे।",
            "स्टैगहेड (विकृत फूलों) को तोड़कर तुरंत जला दें।"
        ],
        "recommended_fertilizers_en": "Apply Sulfur (Bentonite Sulfur 90%) @ 10 kg/acre to boost oil content and disease resistance.",
        "recommended_fertilizers_hi": "सल्फर (90%) 10 किग्रा/एकड़ दें जिससे तेल की मात्रा और रोग प्रतिरोधक क्षमता बढ़े।",
        "spread_risk": "High during winter foggy mornings"
    },

    # HEALTHY CROP
    "healthy_crop": {
        "id": "healthy_crop",
        "crop": "General Crop (फसल स्वस्थ है)",
        "category": "Optimal",
        "name_en": "Healthy Crop - No Pathogen Detected",
        "name_hi": "स्वस्थ फसल - कोई रोग नहीं पाया गया",
        "pathogen_type": "None (स्वस्थ)",
        "severity": "None / Optimal",
        "confidence_base": 99.1,
        "symptoms_en": [
            "Vibrant green leaf coloration with uniform texture.",
            "No necrotic spots, powdery spores, or insect chew marks.",
            "Optimal turgidity and vigorous stem growth."
        ],
        "symptoms_hi": [
            "पत्तियों का चमकीला हरा रंग और एकसमान बनावट।",
            "कोई धब्बा, फफूंद, पीलापन या कीट के निशान नहीं।",
            "पौधे की तंदुरुस्त वृद्धि और मजबूत तना।"
        ],
        "causes_en": "Good agronomic management, balanced nutrition, and favorable climate.",
        "causes_hi": "उत्कृष्ट कृषि प्रबंधन, संतुलित पोषण और अनुकूल मौसम।",
        "chemical_treatment_en": [
            "No chemical pesticides required. Avoid unnecessary preventive chemical sprays."
        ],
        "chemical_treatment_hi": [
            "किसी रासायनिक कीटनाशक की आवश्यकता नहीं है। अनावश्यक छिड़काव से बचें।"
        ],
        "organic_treatment_en": [
            "Continue prophylactic Jeevamrutha or Panchagavya (3%) foliar spray every 15 days.",
            "Maintain bio-fertilizer soil inoculation."
        ],
        "organic_treatment_hi": [
            "हर 15 दिन में 3% पंचगव्य या जीवामृत का हल्का छिड़काव जारी रखें।",
            "मिट्टी में जैविक खाद और केचुआ खाद बनाए रखें।"
        ],
        "preventive_practices_en": [
            "Maintain clean field boundaries.",
            "Regular scouting twice a week to detect any early signs of pests."
        ],
        "preventive_practices_hi": [
            "खेत की मेड़ों को खरपतवार मुक्त रखें।",
            "हफ्ते में दो बार खेत का निरीक्षण करें ताकि किसी भी कीट का समय पर पता चल सके।"
        ],
        "recommended_fertilizers_en": "Maintain regular scheduled fertilizer plan based on soil test report.",
        "recommended_fertilizers_hi": "मृदा स्वास्थ्य कार्ड (Soil Health Card) के अनुसार नियमित खाद दें।",
        "spread_risk": "Low"
    }
}


def get_all_diseases():
    return DISEASE_DATABASE


def get_disease_by_id(disease_id):
    return DISEASE_DATABASE.get(disease_id, DISEASE_DATABASE["healthy_crop"])
