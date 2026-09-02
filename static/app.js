/**
 * AgriShield AI (कृषि रक्षक) - Frontend Application Logic
 * Integrates 7 modules: Upload/Camera, Image Processing Canvas, AI Disease Detection,
 * Weather/Soil, Treatments/Dosage, Market Forecast, and Bilingual Farmer UI.
 */

// Application State
const state = {
  currentLang: 'en', // 'en' or 'hi'
  currentPage: 'page-doctor',
  selectedCrop: 'tomato',
  selectedDiseaseId: 'tomato_early_blight',
  loadedImage: null, // HTMLImageElement
  currentFilter: 'original',
  showHeatmap: true,
  diagnosisData: null,
  marketChartInstance: null,
  isSpeaking: false,
  webcamStream: null,
  dosage: {
    sprayType: 'knapsack', // 'knapsack', 'tractor', 'drone', 'drip'
    waterPerAcre: 180,
    areaUnit: 'acres',
    acres: 2.0,
    tankLiters: 15.0,
    dosePerL: 2.5,
    productName: 'Mancozeb 75% WP',
    productUnit: 'g',
    unitCost: 550,
    rounds: 1,
    calculationResult: null
  }
};

// Bilingual Translation Dictionary
const I18N = {
  en: {
    headerTagline: "AI Crop Disease Detection & Smart Agronomy (कृषि रक्षक)",
    heroTitle: "🌾 Smart AI Crop Doctor & Precision Agronomy Hub",
    heroSubtitle: "Upload leaf photo ➔ Real-time Image Processing & Thermal NDVI ➔ AI Disease Classification ➔ Weather & Soil Risk ➔ Dosage Calculator ➔ Mandi Price Forecast.",
    step1Title: "1. Upload Crop Image / Camera",
    cropSelectLabel: "Select Crop Type",
    lblCropType: "Target Crop / फसल का प्रकार:",
    dropzoneText: "Drag & Drop Leaf Photo or Click to Browse",
    btnCamText: "Use Live Camera",
    btnBrowseText: "Choose File",
    samplePrompt: "Instant Test Samples (1-क्लिक टेस्ट नमूने):",
    step2Title: "2. Image Processing & Heatmap",
    lblHeatmap: "Heatmap Overlay",
    lblFilters: "Visual Diagnostic Filters / दृश्य फ़िल्टर:",
    lblInfectedArea: "Infected Area",
    lblLesionsCount: "Lesions Detected",
    lblPlantHealth: "Plant Health",
    lblAiDiagnosticTitle: "3. AI Diagnostic Result (रोग निदान)",
    lblSymptoms: "Observed Diagnostic Symptoms (लक्षण):",
    tabTitleTreatments: "5. Fertilizers & Treatments",
    tabTitleWeatherSoil: "4. Weather & Soil Analysis",
    tabTitleMarket: "6. Market Price Prediction",
    lblChemical: "Chemical Pesticides",
    lblOrganic: "Organic / Bio Remedies",
    lblPreventive: "Preventive Farm Practices",
    lblDosageCalcTitle: "Smart Spray Tank & Fertilizer Dosage Calculator",
    lblCalcFormula: "180L Water / Acre Standard",
    lblAcres: "Land Area (Acres):",
    lblTankCap: "Tank Capacity (L):",
    lblDoseL: "Dose (g or ml / L):",
    lblResWater: "Total Water",
    lblResChemical: "Total Chemical",
    lblResTanks: "Tanks Needed",
    lblResPerTank: "Per Tank Dose",
    lblRiskMeterTitle: "Micro-Climate Disease Propagation Risk (रोग विस्तार खतरा)",
    lblSprayWindow: "Recommended Spray Window (छिड़काव समय):",
    lblTemp: "Temperature",
    lblHumidity: "Humidity",
    lblRainChance: "Rain Chance",
    lblWind: "Wind Speed",
    lblSoilTitle: "Soil Health & NPK Nutrients Status (मृदा स्वास्थ्य)",
    lblSoilAdvisoryHeading: "Soil Management Recommendation:",
    lblCurrPrice: "Current Benchmark Rate",
    lblMspPrice: "Govt MSP / Floor Benchmark",
    lblYieldSaved: "Yield Value Saved by Early Action",
    lblChartHeading: "30-Day Historical Trend & 15-Day AI Price Forecast (मंडी भाव पूर्वानुमान)",
    lblTopMandis: "Top Mandi Spot Rates (प्रमुख मंडियां):",
    btnVoiceText: "Kisan Vani (Voice)",
    btnPrintText: "Health Card",
    navDoc: "Crop Doctor",
    navMandi: "Mandi Intelligence",
    navWeather: "Weather & Soil",
    navDosage: "Dosage Calculator",
    navLibrary: "Disease Library",
    navAdvisory: "Ask Agronomist",
    footerCopyright: "© 2026 AgriShield AI. Built for Smart Agriculture & Crop Protection.",
    advDosageHeaderTitle: "Precision Multi-Sprayer & Fertilizer Calculator",
    advDosageHeaderSubtitle: "Compute exact water volumes, chemical gram/ml dosages, tank refill cycles, application time, and total cost across Knapsack, Tractor Boom, Agri-Drone ULV, and Fertigation systems.",
    btnAdvSyncText: "Sync with Active Diagnosis",
    btnAdvResetText: "Reset",
    advLblSprayerType: "Select Spraying Equipment / स्प्रे उपकरण:",
    advLblFarmConfig: "Farm Area & Tank Configuration:",
    advLblArea: "Land Area / क्षेत्रफल:",
    advLblTankCapacity: "Tank Capacity / टंकी क्षमता (L):",
    advLblProductConfig: "Chemical / Fertilizer Prescription:",
    advLblSelectProduct: "Select Product Preset / दवा या खाद चुनें:",
    advLblProdName: "Product Name / उत्पाद का नाम:",
    advLblDoseRate: "Dose per Litre (मात्रा प्रति लीटर):",
    advLblSprayRounds: "Spray Applications / छिड़काव चक्र:",
    advLblUnitCost: "Estimated Rate (₹ / Kg or L):",
    btnAdvCalculateText: "Calculate Precise Tank Dosage (सटीक गणना करें)",
    advLblResWater: "Total Water Required",
    advLblResProduct: "Total Product Needed",
    advLblResTanks: "Tank Fills Required",
    advLblResPerTank: "Dose per Tank",
    advLblEconomicsTitle: "Economic Investment & Application Time Forecast",
    advLblTotalCost: "Total Chemical Investment",
    advLblTimeEst: "Estimated Spray Duration",
    advLblSticker: "Recommended Spreader Sticker",
    advLblMixingTitle: "Standard 5-Step Tank Mixing Order (घोल तैयार करने का सही क्रम)",
    advLblSafetyTitle: "CIBRC & ICAR Certified Spray Safety Protocols (सुरक्षा नियम)",
    btnAdvWhatsAppText: "Share Prescription on WhatsApp",
    btnAdvPrintText: "Print Dosage Sheet"
  },
  hi: {
    headerTagline: "एआई फसल रोग पहचान एवं सटीक कृषि सलाहकार (कृषि रक्षक)",
    heroTitle: "🌾 स्मार्ट एआई फसल डॉक्टर एवं सटीक कृषि सलाहकार",
    heroSubtitle: "पत्ती का फोटो अपलोड करें ➔ इमेज प्रोसेसिंग एवं NDVI ➔ एआई रोग पहचान ➔ मौसम एवं मिट्टी विश्लेषण ➔ सटीक दवा मात्रा ➔ मंडी भाव पूर्वानुमान।",
    step1Title: "1. फसल का फोटो अपलोड / कैमरा",
    cropSelectLabel: "फसल चुनें",
    lblCropType: "फसल का प्रकार:",
    dropzoneText: "पत्ती की फोटो यहां खींचे या चुनने के लिए क्लिक करें",
    btnCamText: "लाइव कैमरा शुरू करें",
    btnBrowseText: "फ़ाइल चुनें",
    samplePrompt: "तुरंत जांचने के लिए नमूने चुनें:",
    step2Title: "2. इमेज प्रोसेसिंग व हीटमैप",
    lblHeatmap: "संक्रमण हीटमैप",
    lblFilters: "दृश्य फ़िल्टर (Visual Filters):",
    lblInfectedArea: "संक्रमित क्षेत्र",
    lblLesionsCount: "पाए गए रोग धब्बे",
    lblPlantHealth: "पौधे का स्वास्थ्य",
    lblAiDiagnosticTitle: "3. एआई रोग निदान परिणाम",
    lblSymptoms: "रोग के मुख्य लक्षण:",
    tabTitleTreatments: "5. खाद एवं दवा उपचार",
    tabTitleWeatherSoil: "4. मौसम व मिट्टी विश्लेषण",
    tabTitleMarket: "6. मंडी भाव पूर्वानुमान",
    lblChemical: "रासायनिक कीटनाशक व फफूंदनाशी",
    lblOrganic: "जैविक / देसी उपचार",
    lblPreventive: "बचाव के कृषि उपाय",
    lblDosageCalcTitle: "स्मार्ट स्प्रे पंप व दवा मात्रा कैलकुलेटर",
    lblCalcFormula: "180 लीटर पानी प्रति एकड़ मानक",
    lblAcres: "खेत का क्षेत्रफल (एकड़):",
    lblTankCap: "स्प्रे पंप क्षमता (लीटर):",
    lblDoseL: "मात्रा (ग्राम या मिली / ली):",
    lblResWater: "कुल पानी",
    lblResChemical: "कुल दवा/खाद",
    lblResTanks: "स्प्रे टंकी संख्या",
    lblResPerTank: "प्रति टंकी खुराक",
    lblRiskMeterTitle: "मौसम अनुसार बीमारी फैलने का खतरा:",
    lblSprayWindow: "दवा छिड़काव का सबसे उत्तम समय:",
    lblTemp: "तापमान",
    lblHumidity: "हवा में नमी",
    lblRainChance: "बारिश की संभावना",
    lblWind: "हवा की गति",
    lblSoilTitle: "मृदा स्वास्थ्य एवं पोषक तत्व (NPK):",
    lblSoilAdvisoryHeading: "मिट्टी सुधार हेतु कृषि सलाह:",
    lblCurrPrice: "वर्तमान औसत मंडी भाव",
    lblMspPrice: "सरकारी समर्थन मूल्य (MSP)",
    lblYieldSaved: "समय पर उपचार से सुरक्षित फसल मूल्य",
    lblChartHeading: "30 दिन का पुराना भाव एवं 15 दिन का एआई पूर्वानुमान",
    lblTopMandis: "प्रमुख मंडियों के दैनिक भाव:",
    btnVoiceText: "किसान वाणी (बोलकर सुनें)",
    btnPrintText: "स्वास्थ्य पर्ची",
    navDoc: "रोग डॉक्टर",
    navMandi: "मंडी भाव",
    navWeather: "मौसम व मिट्टी",
    navDosage: "दवा कैलकुलेटर",
    navLibrary: "रोग ज्ञानकोष",
    navAdvisory: "किसान सलाह",
    footerCopyright: "© 2026 AgriShield AI. भारतीय किसानों के लिए समर्पित।",
    advDosageHeaderTitle: "सटीक स्प्रेयर व खाद मात्रा कैलकुलेटर (Precision Calculator)",
    advDosageHeaderSubtitle: "नैपसैक, ट्रैक्टर बूम, एग्री-ड्रोन और ड्रिप सिस्टम हेतु सटीक पानी, दवा की मात्रा, टंकी संख्या व खर्च का तुरंत हिसाब लगाएं।",
    btnAdvSyncText: "सक्रिय रोग निदान से जोड़ें",
    btnAdvResetText: "रीसेट करें",
    advLblSprayerType: "छिड़काव उपकरण चुनें (Sprayer Equipment):",
    advLblFarmConfig: "खेत क्षेत्रफल एवं टंकी क्षमता:",
    advLblArea: "खेत का क्षेत्रफल:",
    advLblTankCapacity: "टंकी क्षमता (लीटर):",
    advLblProductConfig: "दवा / खाद का विवरण व खुराक:",
    advLblSelectProduct: "दवा/खाद सूची से चुनें:",
    advLblProdName: "दवा/उत्पाद का नाम:",
    advLblDoseRate: "मात्रा प्रति लीटर पानी:",
    advLblSprayRounds: "छिड़काव चक्र (Applications):",
    advLblUnitCost: "अनुमानित दर (₹ प्रति किग्रा/लीटर):",
    btnAdvCalculateText: "सटीक स्प्रे मात्रा की गणना करें",
    advLblResWater: "कुल आवश्यक पानी",
    advLblResProduct: "कुल आवश्यक दवा/खाद",
    advLblResTanks: "कुल स्प्रे टंकियां",
    advLblResPerTank: "प्रति टंकी खुराक",
    advLblEconomicsTitle: "लागत खर्च एवं समय का पूर्वानुमान",
    advLblTotalCost: "कुल दवा खर्च",
    advLblTimeEst: "छिड़काव में लगने वाला समय",
    advLblSticker: "सिलिकॉन स्टीकर / गोंद मात्रा",
    advLblMixingTitle: "टंकी में घोल तैयार करने का सही 5-चरणीय क्रम",
    advLblSafetyTitle: "ICAR एवं CIBRC प्रमाणित सुरक्षा नियम व सावधानियां",
    btnAdvWhatsAppText: "व्हाट्सएप पर दवा पर्ची भेजें",
    btnAdvPrintText: "दवा पर्ची प्रिंट करें"
  }
};

// DOM Content Loaded Initializer
document.addEventListener('DOMContentLoaded', () => {
  if (window.lucide) {
    lucide.createIcons();
  }
  
  setupEventListeners();
  setupLanguageSwitcher();
  setupTabs();
  setupFilterButtons();
  setupDosageCalculator();
  setupAdvancedDosageCalculator();
  setupPageNavigation();
  setupAgronomist();
  loadEncyclopedia();
  
  // Load default initial sample (Tomato Early Blight)
  loadSampleImage('tomato_early_blight', 'tomato');
});

// Setup Page Navigation
function setupPageNavigation() {
  document.querySelectorAll('.nav-page-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const pageId = btn.getAttribute('data-page');
      switchMainPage(pageId);
    });
  });
}

function switchMainPage(pageId) {
  state.currentPage = pageId;

  document.querySelectorAll('.nav-page-btn').forEach(b => {
    if (b.getAttribute('data-page') === pageId) {
      b.className = 'nav-page-btn active px-3 py-1.5 rounded-lg bg-brand-600/20 text-brand-400 border border-brand-500/30 font-semibold';
    } else {
      b.className = 'nav-page-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition font-semibold';
    }
  });

  document.querySelectorAll('.page-view').forEach(p => {
    if (p.id === pageId) {
      p.classList.remove('hidden');
    } else {
      p.classList.add('hidden');
    }
  });

  if (pageId === 'page-mandi' && state.diagnosisData) {
    setTimeout(renderMarketChart, 100);
  }
  if (pageId === 'page-dosage') {
    calculateAdvancedDosage();
  }
  if (window.lucide) {
    lucide.createIcons();
  }
}

// Setup All Core Event Listeners
function setupEventListeners() {
  const fileInput = document.getElementById('fileInput');
  const dropZone = document.getElementById('dropZone');
  const btnBrowseFile = document.getElementById('btnBrowseFile');

  btnBrowseFile.addEventListener('click', () => fileInput.click());
  dropZone.addEventListener('click', () => fileInput.click());

  fileInput.addEventListener('change', (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFileSelected(e.target.files[0]);
    }
  });

  ['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropZone.classList.add('border-brand-500', 'bg-brand-950/20');
    });
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropZone.classList.remove('border-brand-500', 'bg-brand-950/20');
    });
  });

  dropZone.addEventListener('drop', (e) => {
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileSelected(e.dataTransfer.files[0]);
    }
  });

  // Crop Selector Buttons
  document.querySelectorAll('.crop-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.crop-btn').forEach(b => {
        b.classList.remove('active', 'bg-slate-800', 'border-brand-500/50', 'text-white');
        b.classList.add('bg-slate-800/60', 'border-slate-700', 'text-slate-300');
      });
      btn.classList.add('active', 'bg-slate-800', 'border-brand-500/50', 'text-white');
      btn.classList.remove('bg-slate-800/60', 'border-slate-700', 'text-slate-300');

      state.selectedCrop = btn.getAttribute('data-crop');
      const diseaseId = btn.getAttribute('data-disease');
      loadSampleImage(diseaseId, state.selectedCrop);
    });
  });

  // Sample Chips
  document.querySelectorAll('.sample-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const crop = chip.getAttribute('data-crop');
      const diseaseId = chip.getAttribute('data-disease');
      loadSampleImage(diseaseId, crop);
    });
  });

  // Heatmap Toggle
  const toggleHeatmap = document.getElementById('toggleHeatmap');
  toggleHeatmap.addEventListener('change', (e) => {
    state.showHeatmap = e.target.checked;
    renderCanvasAndOverlays();
  });

  // Voice Readout Button (Kisan Vani)
  const btnVoiceReadout = document.getElementById('btnVoiceReadout');
  btnVoiceReadout.addEventListener('click', toggleVoiceReadout);

  // Print Health Card Button
  const btnPrintHealthCard = document.getElementById('btnPrintHealthCard');
  btnPrintHealthCard.addEventListener('click', () => {
    preparePrintableCard();
    window.print();
  });

  // WhatsApp Share Button
  const btnShareWhatsApp = document.getElementById('btnShareWhatsApp');
  if (btnShareWhatsApp) {
    btnShareWhatsApp.addEventListener('click', sharePrescriptionWhatsApp);
  }

  // Geo Weather Button
  const btnGeoWeather = document.getElementById('btnGeoWeather');
  btnGeoWeather.addEventListener('click', fetchLiveGeolocationWeather);

  // Camera Modal triggers
  const btnOpenCam = document.getElementById('btnOpenCam');
  const btnCloseCam = document.getElementById('btnCloseCam');
  const btnSnapPhoto = document.getElementById('btnSnapPhoto');
  const btnSwitchCam = document.getElementById('btnSwitchCam');

  btnOpenCam.addEventListener('click', openLiveCamera);
  btnCloseCam.addEventListener('click', closeLiveCamera);
  btnSnapPhoto.addEventListener('click', captureLiveSnapshot);
  btnSwitchCam.addEventListener('click', switchCameraSource);
}

// Share on WhatsApp
function sharePrescriptionWhatsApp() {
  if (!state.diagnosisData) return;
  const disease = state.diagnosisData.disease;
  const analysis = state.diagnosisData.analysis;
  const isHi = state.currentLang === 'hi';

  const text = isHi ?
    `🌾 *कृषि रक्षक AI फसल स्वास्थ्य पर्ची* 🌾%0A%0A` +
    `📌 *फसल:* ${disease.crop}%0A` +
    `🔬 *रोग निदान:* ${disease.name_hi} (${disease.name_en})%0A` +
    `📊 *गंभीरता:* ${disease.severity} | विश्वसनीयता: ${analysis.confidence_score}%%0A%0A` +
    `💊 *दवा उपचार:*%0A• ${disease.chemical_treatment_hi[0]}%0A%0A` +
    `🌱 *जैविक उपचार:*%0A• ${disease.organic_treatment_hi[0]}%0A%0A` +
    `📞 *किसान हेल्पलाइन:* 1800-180-1551` :
    `🌾 *AgriShield AI Crop Health Card* 🌾%0A%0A` +
    `📌 *Crop:* ${disease.crop}%0A` +
    `🔬 *Diagnosis:* ${disease.name_en}%0A` +
    `📊 *Severity:* ${disease.severity} | Confidence: ${analysis.confidence_score}%%0A%0A` +
    `💊 *Prescription:*%0A• ${disease.chemical_treatment_en[0]}%0A%0A` +
    `🌱 *Organic Remedy:*%0A• ${disease.organic_treatment_en[0]}%0A%0A` +
    `📞 *Kisan Helpline:* 1800-180-1551`;

  window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
}

// Setup Language Switcher
function setupLanguageSwitcher() {
  const btnEn = document.getElementById('btnLangEn');
  const btnHi = document.getElementById('btnLangHi');

  btnEn.addEventListener('click', () => setLanguage('en'));
  btnHi.addEventListener('click', () => setLanguage('hi'));
}

function setLanguage(lang) {
  state.currentLang = lang;
  const btnEn = document.getElementById('btnLangEn');
  const btnHi = document.getElementById('btnLangHi');

  if (lang === 'hi') {
    btnHi.classList.add('bg-brand-600', 'text-white');
    btnHi.classList.remove('text-slate-300');
    btnEn.classList.remove('bg-brand-600', 'text-white');
    btnEn.classList.add('text-slate-300');
  } else {
    btnEn.classList.add('bg-brand-600', 'text-white');
    btnEn.classList.remove('text-slate-300');
    btnHi.classList.remove('bg-brand-600', 'text-white');
    btnHi.classList.add('text-slate-300');
  }

  const dict = I18N[lang];
  for (const [id, text] of Object.entries(dict)) {
    const el = document.getElementById(id);
    if (el) {
      el.textContent = text;
    }
  }

  if (state.diagnosisData) {
    renderDiagnosisResults(state.diagnosisData);
  }
  calculateAdvancedDosage();
  if (window.lucide) {
    lucide.createIcons();
  }
}

// Tab Switching Logic
function setupTabs() {
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      tabButtons.forEach(b => {
        b.classList.remove('active', 'border-brand-500', 'text-brand-400', 'bg-slate-800/50');
        b.classList.add('border-transparent', 'text-slate-400');
      });
      btn.classList.add('active', 'border-brand-500', 'text-brand-400', 'bg-slate-800/50');
      btn.classList.remove('border-transparent', 'text-slate-400');

      const targetId = btn.getAttribute('data-tab');
      tabPanels.forEach(panel => {
        if (panel.id === targetId) {
          panel.classList.remove('hidden');
        } else {
          panel.classList.add('hidden');
        }
      });

      if (targetId === 'tab-market' && state.diagnosisData) {
        setTimeout(renderMarketChart, 100);
      }
    });
  });
}

// Visual Filter Buttons
function setupFilterButtons() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('active', 'bg-brand-600', 'text-white', 'border-brand-500');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('active', 'bg-brand-600', 'text-white', 'border-brand-500');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      state.currentFilter = btn.getAttribute('data-filter');
      renderCanvasAndOverlays();
    });
  });
}

// Load Sample Image
async function loadSampleImage(diseaseId, crop) {
  state.selectedDiseaseId = diseaseId;
  state.selectedCrop = crop;

  startScanningAnimation();

  try {
    const res = await fetch(`/api/sample-image/${diseaseId}`);
    const data = await res.json();
    if (data.success && data.image_data_uri) {
      const img = new Image();
      img.onload = () => {
        state.loadedImage = img;
        triggerAiDiagnosis(data.image_data_uri, crop, diseaseId);
      };
      img.src = data.image_data_uri;
    }
  } catch (err) {
    console.error("Failed to load sample image:", err);
    stopScanningAnimation();
  }
}

// Handle User Uploaded File
function handleFileSelected(file) {
  if (!file || !file.type.startsWith('image/')) {
    alert("Please select a valid image file (JPG, PNG, WEBP).");
    return;
  }

  const reader = new FileReader();
  reader.onload = (e) => {
    const dataUri = e.target.result;
    const img = new Image();
    img.onload = () => {
      state.loadedImage = img;
      startScanningAnimation();
      triggerAiDiagnosis(dataUri, state.selectedCrop);
    };
    img.src = dataUri;
  };
  reader.readAsDataURL(file);
}

// Trigger AI Diagnosis Server Endpoint
async function triggerAiDiagnosis(imageBase64, crop, diseaseId = null) {
  startScanningAnimation();

  try {
    const payload = {
      image: imageBase64,
      crop: crop,
      disease_id: diseaseId,
      acres: parseFloat(document.getElementById('calcAcres').value) || 2.0
    };

    const res = await fetch('/api/diagnose', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (data.success) {
      state.diagnosisData = data;
      renderCanvasAndOverlays();
      renderDiagnosisResults(data);
      renderWeatherRisk(data.weather_risk);
      renderMarketInfo(data.market_info, data.economic_impact);
      recalculateDosage();
    }
  } catch (err) {
    console.error("Diagnosis error:", err);
  } finally {
    stopScanningAnimation();
  }
}

// Laser Scanner Controls
function startScanningAnimation() {
  const laser = document.getElementById('scanLaser');
  if (laser) laser.classList.remove('hidden');
}

function stopScanningAnimation() {
  const laser = document.getElementById('scanLaser');
  if (laser) laser.classList.add('hidden');
}

// Canvas & Visual Filter Renderer
function renderCanvasAndOverlays() {
  const canvas = document.getElementById('imageCanvas');
  const ctx = canvas.getContext('2d');
  const placeholder = document.getElementById('canvasPlaceholder');
  const hotspotLayer = document.getElementById('hotspotLayer');

  if (!state.loadedImage) {
    if (placeholder) placeholder.classList.remove('hidden');
    return;
  }

  if (placeholder) placeholder.classList.add('hidden');

  const img = state.loadedImage;
  canvas.width = img.naturalWidth || 500;
  canvas.height = img.naturalHeight || 500;

  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

  const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imgData.data;

  if (state.currentFilter === 'grayscale') {
    for (let i = 0; i < data.length; i += 4) {
      const avg = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
      data[i] = avg;
      data[i + 1] = avg;
      data[i + 2] = avg;
    }
    ctx.putImageData(imgData, 0, 0);
  } else if (state.currentFilter === 'ndvi') {
    for (let i = 0; i < data.length; i += 4) {
      const r = data[i];
      const g = data[i + 1];
      const b = data[i + 2];
      const ndvi = (g - r) / (g + r + 1);

      if (ndvi > 0.15) {
        data[i] = 20;
        data[i + 1] = Math.min(255, g * 1.3);
        data[i + 2] = 80;
      } else if (ndvi < -0.05) {
        data[i] = 240;
        data[i + 1] = 40;
        data[i + 2] = 50;
      } else {
        data[i] = 230;
        data[i + 1] = 180;
        data[i + 2] = 30;
      }
    }
    ctx.putImageData(imgData, 0, 0);
  } else if (state.currentFilter === 'edge') {
    for (let i = 0; i < data.length; i += 4) {
      const r = data[i];
      const g = data[i + 1];
      const b = data[i + 2];
      const brightness = (r + g + b) / 3;
      const val = (r > 120 && b < 90) || brightness < 60 ? 255 : 30;
      data[i] = val;
      data[i + 1] = val;
      data[i + 2] = val;
    }
    ctx.putImageData(imgData, 0, 0);
  }

  hotspotLayer.innerHTML = '';
  if (state.showHeatmap && state.diagnosisData && state.diagnosisData.analysis) {
    const spots = state.diagnosisData.analysis.hotspots || [];
    spots.forEach(spot => {
      const box = document.createElement('div');
      box.className = 'bounding-box';
      box.style.left = `${spot.x}%`;
      box.style.top = `${spot.y}%`;
      box.style.width = `${spot.width}%`;
      box.style.height = `${spot.height}%`;
      box.title = `${spot.severity} (${spot.confidence}%)`;

      const tag = document.createElement('span');
      tag.className = 'absolute -top-4 left-0 bg-red-600 text-white text-[9px] font-bold px-1 rounded';
      tag.textContent = `${spot.confidence}%`;
      box.appendChild(tag);

      hotspotLayer.appendChild(box);
    });
  }
}

// Render AI Diagnosis Summary Card
function renderDiagnosisResults(data) {
  const isHi = state.currentLang === 'hi';
  const disease = data.disease;
  const analysis = data.analysis;

  document.getElementById('diagDiseaseName').textContent = disease.name_en;
  document.getElementById('diagDiseaseHindi').textContent = disease.name_hi;
  document.getElementById('diagPathogenType').textContent = `Pathogen: ${disease.pathogen_type} • Target Crop: ${disease.crop}`;

  const badgeSev = document.getElementById('badgeSeverity');
  badgeSev.textContent = `${disease.severity} Severity`;
  if (disease.severity.includes('Critical') || disease.severity.includes('Severe')) {
    badgeSev.className = 'px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-500/20 text-red-300 border border-red-500/40 pulse-glow-danger';
  } else if (disease.severity.includes('None')) {
    badgeSev.className = 'px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40';
  } else {
    badgeSev.className = 'px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40';
  }

  document.getElementById('badgeConfidence').textContent = `${analysis.confidence_score}% Confidence`;

  document.getElementById('metricInfectedPct').textContent = `${analysis.damage_percentage}%`;
  document.getElementById('metricHotspots').textContent = `${(analysis.hotspots || []).length} Hotspots`;
  document.getElementById('metricHealthStatus').textContent = analysis.infection_grade;

  const symptomsList = document.getElementById('diagSymptomsList');
  symptomsList.innerHTML = '';
  const symptoms = isHi ? disease.symptoms_hi : disease.symptoms_en;
  (symptoms || []).forEach(sym => {
    const li = document.createElement('li');
    li.textContent = sym;
    symptomsList.appendChild(li);
  });

  const chemUl = document.getElementById('treatmentChemical');
  chemUl.innerHTML = '';
  const chemTreatments = isHi ? disease.chemical_treatment_hi : disease.chemical_treatment_en;
  (chemTreatments || []).forEach(item => {
    const li = document.createElement('li');
    li.className = 'flex items-start gap-1.5';
    li.innerHTML = `<span class="text-red-400 font-bold">•</span> <span>${item}</span>`;
    chemUl.appendChild(li);
  });

  const orgUl = document.getElementById('treatmentOrganic');
  orgUl.innerHTML = '';
  const orgTreatments = isHi ? disease.organic_treatment_hi : disease.organic_treatment_en;
  (orgTreatments || []).forEach(item => {
    const li = document.createElement('li');
    li.className = 'flex items-start gap-1.5';
    li.innerHTML = `<span class="text-emerald-400 font-bold">•</span> <span>${item}</span>`;
    orgUl.appendChild(li);
  });

  const prevUl = document.getElementById('treatmentPreventive');
  prevUl.innerHTML = '';
  const prevTreatments = isHi ? disease.preventive_practices_hi : disease.preventive_practices_en;
  (prevTreatments || []).forEach(item => {
    const li = document.createElement('li');
    li.className = 'flex items-start gap-1.5';
    li.innerHTML = `<span class="text-blue-400 font-bold">•</span> <span>${item}</span>`;
    prevUl.appendChild(li);
  });
}

// Setup Smart Dosage Calculator
function setupDosageCalculator() {
  const btnRecalc = document.getElementById('btnRecalculateDosage');
  if (btnRecalc) btnRecalc.addEventListener('click', recalculateDosage);

  ['calcAcres', 'calcTankLiters', 'calcDosePerL'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', recalculateDosage);
  });
}

async function recalculateDosage() {
  const acresEl = document.getElementById('calcAcres');
  const tankEl = document.getElementById('calcTankLiters');
  const doseEl = document.getElementById('calcDosePerL');

  const acres = acresEl ? parseFloat(acresEl.value) || 2.0 : 2.0;
  const tankLiters = tankEl ? parseFloat(tankEl.value) || 15.0 : 15.0;
  const dosePerL = doseEl ? parseFloat(doseEl.value) || 2.5 : 2.5;

  try {
    const res = await fetch('/api/calculate-dosage', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        acres: acres,
        tank_capacity_liters: tankLiters,
        dose_per_liter_g_or_ml: dosePerL,
        product_name: "Mancozeb 75% WP"
      })
    });
    const data = await res.json();
    if (data.success) {
      document.getElementById('resTotalWater').textContent = data.total_water_liters;
      document.getElementById('resTotalChemical').textContent = data.total_product_needed;
      document.getElementById('resTanksCount').textContent = data.sprayer_tanks_count;
      document.getElementById('resPerTank').textContent = data.product_per_tank;
    }
  } catch (err) {
    console.error("Dosage calc error:", err);
  }
}

// Setup Advanced Precision Multi-Sprayer & Fertilizer Calculator
function setupAdvancedDosageCalculator() {
  // Sprayer type buttons
  document.querySelectorAll('.adv-sprayer-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.adv-sprayer-btn').forEach(b => {
        b.classList.remove('active', 'bg-slate-800', 'border-brand-500/50');
        b.classList.add('bg-slate-900/80', 'border-slate-700');
        const p = b.querySelector('p.text-xs');
        if (p) {
          p.classList.remove('text-white');
          p.classList.add('text-slate-300');
        }
      });
      btn.classList.add('active', 'bg-slate-800', 'border-brand-500/50');
      btn.classList.remove('bg-slate-900/80', 'border-slate-700');
      const p = btn.querySelector('p.text-xs');
      if (p) {
        p.classList.remove('text-slate-300');
        p.classList.add('text-white');
      }

      state.dosage.sprayType = btn.getAttribute('data-spray');
      state.dosage.waterPerAcre = parseFloat(btn.getAttribute('data-water-per-acre')) || 180;
      const defaultTank = parseFloat(btn.getAttribute('data-tank')) || 15;
      const tankInput = document.getElementById('advCalcTankLiters');
      if (tankInput) {
        tankInput.value = defaultTank;
      }
      calculateAdvancedDosage();
    });
  });

  // Tank preset chips
  document.querySelectorAll('.adv-tank-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const liters = chip.getAttribute('data-liters');
      const tankInput = document.getElementById('advCalcTankLiters');
      if (tankInput && liters) {
        tankInput.value = liters;
        calculateAdvancedDosage();
      }
    });
  });

  // Product select dropdown
  const prodSelect = document.getElementById('advProductSelect');
  if (prodSelect) {
    prodSelect.addEventListener('change', (e) => {
      const opt = e.target.selectedOptions[0];
      if (opt && opt.value !== 'custom') {
        const name = opt.getAttribute('data-name');
        const dose = opt.getAttribute('data-dose');
        const unit = opt.getAttribute('data-unit');
        const cost = opt.getAttribute('data-cost');

        if (name && document.getElementById('advProductName')) document.getElementById('advProductName').value = name;
        if (dose && document.getElementById('advCalcDosePerL')) document.getElementById('advCalcDosePerL').value = dose;
        if (unit && document.getElementById('advProductUnit')) document.getElementById('advProductUnit').value = unit;
        if (cost && document.getElementById('advUnitCost')) document.getElementById('advUnitCost').value = cost;
      }
      calculateAdvancedDosage();
    });
  }

  // Real-time input change listeners
  ['advCalcAcres', 'advAreaUnit', 'advCalcTankLiters', 'advCalcDosePerL', 'advProductUnit', 'advSprayRounds', 'advUnitCost', 'advProductName'].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener('input', () => calculateAdvancedDosage(false));
      el.addEventListener('change', () => calculateAdvancedDosage(false));
    }
  });

  // Calculate Action Button
  const btnCalc = document.getElementById('btnAdvCalculateDosage');
  if (btnCalc) {
    btnCalc.addEventListener('click', () => calculateAdvancedDosage(true));
  }

  // Sync with Crop Doctor Button
  const btnSync = document.getElementById('btnAdvSyncDoctor');
  if (btnSync) {
    btnSync.addEventListener('click', syncDosageWithActiveDoctor);
  }

  // Reset Button
  const btnReset = document.getElementById('btnAdvReset');
  if (btnReset) {
    btnReset.addEventListener('click', resetAdvancedDosageForm);
  }

  // WhatsApp Share Button
  const btnWhatsApp = document.getElementById('btnAdvWhatsApp');
  if (btnWhatsApp) {
    btnWhatsApp.addEventListener('click', shareAdvancedDosageWhatsApp);
  }

  // Print Button
  const btnPrint = document.getElementById('btnAdvPrint');
  if (btnPrint) {
    btnPrint.addEventListener('click', printAdvancedDosagePrescription);
  }

  // Perform initial calculation
  calculateAdvancedDosage(false);
}

// Calculate Advanced Dosage Function
async function calculateAdvancedDosage(triggerServer = false) {
  const acresInput = document.getElementById('advCalcAcres');
  const unitSelect = document.getElementById('advAreaUnit');
  const tankInput = document.getElementById('advCalcTankLiters');
  const doseInput = document.getElementById('advCalcDosePerL');
  const prodUnitSelect = document.getElementById('advProductUnit');
  const prodNameInput = document.getElementById('advProductName');
  const roundsSelect = document.getElementById('advSprayRounds');
  const costInput = document.getElementById('advUnitCost');

  if (!acresInput || !tankInput || !doseInput) return;

  const rawArea = parseFloat(acresInput.value) || 2.0;
  const areaUnit = unitSelect ? unitSelect.value : 'acres';

  // Normalize area to acres
  let acres = rawArea;
  if (areaUnit === 'hectares') acres = rawArea * 2.471;
  else if (areaUnit === 'bigha') acres = rawArea * 0.62;

  const tankLiters = parseFloat(tankInput.value) || 15.0;
  const dosePerL = parseFloat(doseInput.value) || 2.5;
  const productUnit = prodUnitSelect ? prodUnitSelect.value : 'g';
  const productName = prodNameInput ? prodNameInput.value : 'Mancozeb 75% WP';
  const rounds = roundsSelect ? parseInt(roundsSelect.value) || 1 : 1;
  const unitCost = costInput ? parseFloat(costInput.value) || 550 : 550;
  const sprayType = state.dosage.sprayType || 'knapsack';

  // Water per acre standard
  let waterPerAcre = state.dosage.waterPerAcre || 180;
  if (sprayType === 'drone') waterPerAcre = 10;
  else if (sprayType === 'tractor') waterPerAcre = 250;
  else if (sprayType === 'drip') waterPerAcre = 500;
  else waterPerAcre = 180;

  const totalWaterLiters = Math.round(acres * waterPerAcre * rounds);
  
  let totalProduct = 0;
  let productPerTank = 0;

  if (sprayType === 'drone') {
    totalProduct = Math.round(acres * 500 * rounds * 10) / 10;
    productPerTank = Math.round(((totalProduct / Math.max(1, totalWaterLiters)) * tankLiters) * 10) / 10;
  } else {
    totalProduct = Math.round(totalWaterLiters * dosePerL * 10) / 10;
    productPerTank = Math.round(tankLiters * dosePerL * 10) / 10;
  }

  const tanksCount = Math.round((totalWaterLiters / Math.max(1, tankLiters)) * 10) / 10;
  const totalCost = Math.round(((totalProduct / 1000) * unitCost) * 100) / 100;
  const costPerAcre = Math.round((totalCost / Math.max(0.1, acres)) * 100) / 100;

  // Spray duration forecast
  let timeEst = "";
  let timeSubtext = "";
  if (sprayType === 'drone') {
    const mins = Math.round(acres * 9 * rounds);
    timeEst = `~${mins} Minutes`;
    timeSubtext = `~9 mins / acre aerial ULV`;
  } else if (sprayType === 'tractor') {
    const mins = Math.round(acres * 20 * rounds);
    timeEst = `~${mins} Minutes`;
    timeSubtext = `~20 mins / acre boom spray`;
  } else if (sprayType === 'drip') {
    const hrs = (acres * 1.5 * rounds).toFixed(1);
    timeEst = `~${hrs} Hours`;
    timeSubtext = `Direct fertigation cycle`;
  } else {
    const hrs = (acres * 2.4 * rounds).toFixed(1);
    timeEst = `~${hrs} Hours`;
    timeSubtext = `~2.4 hrs / acre knapsack`;
  }

  const stickerDose = `${Math.round(totalWaterLiters * 0.5)} ml Silicon Sticker`;

  // Update UI Elements
  const elWater = document.getElementById('advResTotalWater');
  if (elWater) elWater.textContent = `${totalWaterLiters} Liters`;

  const elWaterFormula = document.getElementById('advResWaterFormula');
  if (elWaterFormula) elWaterFormula.textContent = `${waterPerAcre} L / Acre Standard`;

  const unitLabel = productUnit === 'g' ? 'grams' : 'ml';
  const elChem = document.getElementById('advResTotalChemical');
  if (elChem) elChem.textContent = `${totalProduct.toLocaleString()} ${unitLabel}`;

  const kgLabel = productUnit === 'g' ? 'kg' : 'Liters';
  const elKg = document.getElementById('advResProductKg');
  if (elKg) elKg.textContent = `${(totalProduct / 1000).toFixed(3)} ${kgLabel}`;

  const elTanks = document.getElementById('advResTanksCount');
  if (elTanks) elTanks.textContent = `~${tanksCount} Tanks`;

  const elTankSub = document.getElementById('advResTankSubtext');
  if (elTankSub) elTankSub.textContent = `${tankLiters}L Capacity / Tank`;

  const elPerTank = document.getElementById('advResPerTank');
  if (elPerTank) elPerTank.textContent = `${productPerTank} ${unitLabel}`;

  const caps = (productPerTank / 15).toFixed(1);
  const elPerTankCap = document.getElementById('advResPerTankCap');
  if (elPerTankCap) elPerTankCap.textContent = `~${caps} standard caps (15ml)`;

  const elCost = document.getElementById('advResTotalCost');
  if (elCost) elCost.textContent = `₹${totalCost.toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;

  const elCostAcre = document.getElementById('advResCostPerAcre');
  if (elCostAcre) elCostAcre.textContent = `₹${costPerAcre.toLocaleString('en-IN', { minimumFractionDigits: 2 })} / Acre`;

  const elTime = document.getElementById('advResTimeEst');
  if (elTime) elTime.textContent = timeEst;

  const elTimeSub = document.getElementById('advResTimeSubtext');
  if (elTimeSub) elTimeSub.textContent = timeSubtext;

  const elSticker = document.getElementById('advResStickerDose');
  if (elSticker) elSticker.textContent = stickerDose;

  // Save in State
  state.dosage.calculationResult = {
    acres,
    rawArea,
    areaUnit,
    tankLiters,
    dosePerL,
    productName,
    productUnit,
    totalWaterLiters,
    totalProduct,
    tanksCount,
    productPerTank,
    totalCost,
    costPerAcre,
    timeEst,
    sprayType,
    rounds
  };

  // Trigger server sync if requested
  if (triggerServer) {
    try {
      const res = await fetch('/api/calculate-dosage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          acres: acres,
          tank_capacity_liters: tankLiters,
          dose_per_liter_g_or_ml: dosePerL,
          spray_type: sprayType,
          product_name: productName,
          unit: productUnit
        })
      });
      const data = await res.json();
      if (data.success) {
        if (state.currentLang === 'hi' && data.safety_instructions_hi) {
          renderSafetyList(data.safety_instructions_hi);
        } else if (data.safety_instructions_en) {
          renderSafetyList(data.safety_instructions_en);
        }
      }
    } catch (err) {
      console.warn("Server dosage calculation fallback to local:", err);
    }
  }
}

// Render Safety Instructions List
function renderSafetyList(list) {
  const ul = document.getElementById('advSafetyList');
  if (!ul || !list) return;
  ul.innerHTML = '';
  list.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    ul.appendChild(li);
  });
}

// Sync Dosage with Active Crop Doctor Diagnosis
function syncDosageWithActiveDoctor() {
  if (!state.diagnosisData) {
    alert("Please run a crop diagnosis first in the Crop Doctor tab.");
    return;
  }
  const disease = state.diagnosisData.disease;
  const isHi = state.currentLang === 'hi';

  const bannerText = document.getElementById('advSyncBannerText');
  if (bannerText) {
    bannerText.innerHTML = `Active Target Crop: <strong>${disease.crop}</strong> • Target Problem: <strong>${isHi ? disease.name_hi : disease.name_en}</strong> • Severity: <strong>${disease.severity}</strong>`;
  }

  // Parse chemical prescription from disease
  const chemList = disease.chemical_treatment_en || [];
  if (chemList.length > 0) {
    const chemStr = chemList[0].toLowerCase();
    if (chemStr.includes('mancozeb')) {
      document.getElementById('advProductSelect').value = 'mancozeb';
      document.getElementById('advProductName').value = 'Mancozeb 75% WP';
      document.getElementById('advCalcDosePerL').value = 2.5;
      document.getElementById('advProductUnit').value = 'g';
      document.getElementById('advUnitCost').value = 550;
    } else if (chemStr.includes('azoxystrobin')) {
      document.getElementById('advProductSelect').value = 'azoxystrobin';
      document.getElementById('advProductName').value = 'Azoxystrobin 23% SC';
      document.getElementById('advCalcDosePerL').value = 1.0;
      document.getElementById('advProductUnit').value = 'ml';
      document.getElementById('advUnitCost').value = 2400;
    } else if (chemStr.includes('propiconazole')) {
      document.getElementById('advProductSelect').value = 'propiconazole';
      document.getElementById('advProductName').value = 'Propiconazole 25% EC';
      document.getElementById('advCalcDosePerL').value = 1.0;
      document.getElementById('advProductUnit').value = 'ml';
      document.getElementById('advUnitCost').value = 1600;
    } else if (chemStr.includes('copper')) {
      document.getElementById('advProductSelect').value = 'copper_oxychloride';
      document.getElementById('advProductName').value = 'Copper Oxychloride 50% WP';
      document.getElementById('advCalcDosePerL').value = 3.0;
      document.getElementById('advProductUnit').value = 'g';
      document.getElementById('advUnitCost').value = 680;
    } else if (chemStr.includes('metalaxyl')) {
      document.getElementById('advProductSelect').value = 'metalaxyl';
      document.getElementById('advProductName').value = 'Metalaxyl 8% + Mancozeb 64% WP';
      document.getElementById('advCalcDosePerL').value = 2.5;
      document.getElementById('advProductUnit').value = 'g';
      document.getElementById('advUnitCost').value = 1400;
    } else if (chemStr.includes('tricyclazole')) {
      document.getElementById('advProductSelect').value = 'tricyclazole';
      document.getElementById('advProductName').value = 'Tricyclazole 75% WP';
      document.getElementById('advCalcDosePerL').value = 0.6;
      document.getElementById('advProductUnit').value = 'g';
      document.getElementById('advUnitCost').value = 1900;
    } else {
      document.getElementById('advProductSelect').value = 'custom';
      document.getElementById('advProductName').value = disease.chemical_treatment_en[0].split('@')[0].replace('Spray', '').replace('Apply', '').trim();
      document.getElementById('advCalcDosePerL').value = 2.0;
    }
  }

  calculateAdvancedDosage(true);
}

// Reset Dosage Form
function resetAdvancedDosageForm() {
  document.getElementById('advCalcAcres').value = '2.0';
  document.getElementById('advAreaUnit').value = 'acres';
  document.getElementById('advCalcTankLiters').value = '15';
  document.getElementById('advProductSelect').value = 'mancozeb';
  document.getElementById('advProductName').value = 'Mancozeb 75% WP';
  document.getElementById('advCalcDosePerL').value = '2.5';
  document.getElementById('advProductUnit').value = 'g';
  document.getElementById('advSprayRounds').value = '1';
  document.getElementById('advUnitCost').value = '550';

  document.querySelectorAll('.adv-sprayer-btn').forEach((b, idx) => {
    if (idx === 0) {
      b.classList.add('active', 'bg-slate-800', 'border-brand-500/50');
      b.classList.remove('bg-slate-900/80', 'border-slate-700');
    } else {
      b.classList.remove('active', 'bg-slate-800', 'border-brand-500/50');
      b.classList.add('bg-slate-900/80', 'border-slate-700');
    }
  });
  state.dosage.sprayType = 'knapsack';
  state.dosage.waterPerAcre = 180;
  calculateAdvancedDosage(false);
}

// Share Advanced Dosage on WhatsApp
function shareAdvancedDosageWhatsApp() {
  const res = state.dosage.calculationResult;
  if (!res) return;
  const isHi = state.currentLang === 'hi';

  const text = isHi ?
    `🌾 *कृषि रक्षक AI सटीक स्प्रे व खाद पर्ची* 🌾%0A%0A` +
    `🚜 *स्प्रे उपकरण:* ${res.sprayType.toUpperCase()} (${res.tankLiters}L Tank)%0A` +
    `📍 *क्षेत्रफल:* ${res.rawArea} ${res.areaUnit} (${res.acres.toFixed(1)} Acres)%0A` +
    `💊 *दवा/खाद:* ${res.productName}%0A` +
    `⚖️ *मात्रा दर:* ${res.dosePerL} ${res.productUnit}/लीटर%0A%0A` +
    `💧 *कुल पानी:* ${res.totalWaterLiters} लीटर%0A` +
    `🧪 *कुल आवश्यक दवा:* ${res.totalProduct} ${res.productUnit === 'g' ? 'ग्राम' : 'मिली'}%0A` +
    `🛢️ *स्प्रे टंकी संख्या:* ~${res.tanksCount} टंकियां%0A` +
    `🥄 *प्रति टंकी खुराक:* ${res.productPerTank} ${res.productUnit === 'g' ? 'ग्राम' : 'मिली'}%0A` +
    `💰 *अनुमानित खर्च:* ₹${res.totalCost} (₹${res.costPerAcre}/एकड़)%0A%0A` +
    `📞 *किसान हेल्पलाइन:* 1800-180-1551` :
    `🌾 *AgriShield AI Precision Dosage Prescription* 🌾%0A%0A` +
    `🚜 *Sprayer Type:* ${res.sprayType.toUpperCase()} (${res.tankLiters}L Tank)%0A` +
    `📍 *Land Area:* ${res.rawArea} ${res.areaUnit} (${res.acres.toFixed(1)} Acres)%0A` +
    `💊 *Product:* ${res.productName}%0A` +
    `⚖️ *Dose Rate:* ${res.dosePerL} ${res.productUnit}/Litre%0A%0A` +
    `💧 *Total Water:* ${res.totalWaterLiters} Litres%0A` +
    `🧪 *Total Product Needed:* ${res.totalProduct} ${res.productUnit === 'g' ? 'grams' : 'ml'}%0A` +
    `🛢️ *Tank Refills:* ~${res.tanksCount} Tanks%0A` +
    `🥄 *Dose per Tank:* ${res.productPerTank} ${res.productUnit === 'g' ? 'grams' : 'ml'}%0A` +
    `💰 *Estimated Cost:* ₹${res.totalCost} (₹${res.costPerAcre}/Acre)%0A%0A` +
    `📞 *Kisan Helpline:* 1800-180-1551`;

  window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
}

// Print Advanced Dosage Prescription
function printAdvancedDosagePrescription() {
  const res = state.dosage.calculationResult;
  if (!res) return;

  const slipId = document.getElementById('printDosageSlipId');
  if (slipId) slipId.textContent = `DOSAGE-${Math.floor(1000 + Math.random() * 9000)}-${new Date().getFullYear()}`;
  
  const dateEl = document.getElementById('printDosageDate');
  if (dateEl) dateEl.textContent = new Date().toLocaleString();
  
  const sprayEl = document.getElementById('printDosageSprayer');
  if (sprayEl) sprayEl.textContent = `${res.sprayType.toUpperCase()} (${res.tankLiters}L Tank)`;
  
  const areaEl = document.getElementById('printDosageArea');
  if (areaEl) areaEl.textContent = `${res.rawArea} ${res.areaUnit} (${res.acres.toFixed(1)} Acres)`;
  
  const prodEl = document.getElementById('printDosageProduct');
  if (prodEl) prodEl.textContent = res.productName;
  
  const doseEl = document.getElementById('printDosageDoseRate');
  if (doseEl) doseEl.textContent = `${res.dosePerL} ${res.productUnit} / Litre`;
  
  const tankEl = document.getElementById('printDosageTankCap');
  if (tankEl) tankEl.textContent = `${res.tankLiters} Liters`;
  
  const cycEl = document.getElementById('printDosageCycles');
  if (cycEl) cycEl.textContent = `${res.rounds} Application Cycle(s)`;

  const waterEl = document.getElementById('printDosageTotalWater');
  if (waterEl) waterEl.textContent = `${res.totalWaterLiters} Liters`;
  
  const unitLabel = res.productUnit === 'g' ? 'grams' : 'ml';
  const kgLabel = res.productUnit === 'g' ? 'kg' : 'L';
  const chemEl = document.getElementById('printDosageTotalChem');
  if (chemEl) chemEl.textContent = `${res.totalProduct} ${unitLabel} (${(res.totalProduct / 1000).toFixed(2)} ${kgLabel})`;
  
  const fillsEl = document.getElementById('printDosageTankFills');
  if (fillsEl) fillsEl.textContent = `~${res.tanksCount} Tanks (${res.tankLiters}L Capacity)`;
  
  const doseTankEl = document.getElementById('printDosagePerTankDose');
  if (doseTankEl) doseTankEl.textContent = `${res.productPerTank} ${unitLabel} per ${res.tankLiters}L Tank`;

  window.print();
}

// Render Weather & Micro-climate Risk
function renderWeatherRisk(weatherRisk) {
  if (!weatherRisk) return;
  const isHi = state.currentLang === 'hi';

  const riskBadge = document.getElementById('riskScoreBadge');
  const riskBar = document.getElementById('riskScoreBar');
  riskBadge.textContent = `${isHi ? weatherRisk.risk_level_hi : weatherRisk.risk_level} (${weatherRisk.risk_score}%)`;
  riskBar.style.width = `${weatherRisk.risk_score}%`;

  const factorsDiv = document.getElementById('weatherRiskFactors');
  factorsDiv.innerHTML = '';
  const factors = isHi ? weatherRisk.factors_hi : weatherRisk.factors_en;
  (factors || []).forEach(f => {
    const p = document.createElement('p');
    p.className = 'flex items-center gap-1.5';
    p.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span> <span>${f}</span>`;
    factorsDiv.appendChild(p);
  });

  document.getElementById('weatherSprayWindow').textContent = isHi ? weatherRisk.spray_window_hi : weatherRisk.spray_window_en;
}

// Fetch Live Geolocation Weather
async function fetchLiveGeolocationWeather() {
  if (!navigator.geolocation) {
    alert("Geolocation is not supported by your browser.");
    return;
  }

  const navText = document.getElementById('navWeatherText');
  navText.textContent = "Fetching GPS Weather...";

  navigator.geolocation.getCurrentPosition(async (pos) => {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;
    try {
      const res = await fetch(`/api/weather?lat=${lat}&lon=${lon}&crop=${state.selectedCrop}`);
      const data = await res.json();
      if (data.success) {
        const w = data.weather;
        navText.textContent = `${w.temperature}°C • ${w.humidity}% Humidity`;
        document.getElementById('cardTemp').textContent = `${w.temperature}°C`;
        document.getElementById('cardHumidity').textContent = `${w.humidity}%`;
        document.getElementById('cardRainChance').textContent = `${w.rainfall_probability}%`;
        document.getElementById('cardWind').textContent = `${w.wind_speed} km/h`;
        renderWeatherRisk(data.disease_spread_risk);
      }
    } catch (err) {
      navText.textContent = "27.5°C • Humid (78%)";
    }
  }, () => {
    navText.textContent = "27.5°C • Humid (78%)";
  });
}

// Render Market Rates & Mandi Chart
function renderMarketInfo(marketData, economicImpact) {
  if (!marketData) return;

  document.getElementById('marketCurrPrice').textContent = `₹${marketData.current_price.toLocaleString()} / Quintal`;
  document.getElementById('marketMspPrice').textContent = `₹${marketData.msp.toLocaleString()} / Quintal`;
  document.getElementById('marketTrendPct').textContent = `▲ ${marketData.trend}`;

  if (economicImpact) {
    document.getElementById('marketYieldSaved').textContent = `${economicImpact.estimated_yield_saved} / ${economicImpact.acres} Acres`;
  }

  const tbody = document.getElementById('topMandisTableBody');
  tbody.innerHTML = '';
  (marketData.top_mandis || []).forEach(mandi => {
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-slate-900/40 transition';
    tr.innerHTML = `
      <td class="py-2.5 px-3 font-semibold text-white">${mandi.mandi}</td>
      <td class="py-2.5 px-3 text-slate-400">${mandi.state}</td>
      <td class="py-2.5 px-3 text-emerald-400 font-bold">₹${mandi.price.toLocaleString()}</td>
      <td class="py-2.5 px-3 text-slate-400">${mandi.arrival}</td>
    `;
    tbody.appendChild(tr);
  });

  renderMarketChart();
}

// Chart.js Price Forecast Graph
function renderMarketChart() {
  const ctx = document.getElementById('marketChart');
  if (!ctx || !state.diagnosisData || !state.diagnosisData.market_info) return;

  const mData = state.diagnosisData.market_info;
  const hist = mData.base_pattern || [2100, 2200, 2300, 2450];
  const fore = mData.forecast_pattern || [2480, 2550, 2620, 2700];

  const labels = [
    '30d ago', '25d ago', '20d ago', '15d ago', '10d ago', '7d ago', '5d ago', '3d ago', 'Yesterday', 'Today',
    '+2d', '+4d', '+6d', '+8d', '+10d', '+12d', '+14d', '+15d'
  ];

  const historicalSeries = [...hist, ...Array(fore.length).fill(null)];
  const forecastSeries = [...Array(hist.length - 1).fill(null), hist[hist.length - 1], ...fore];

  if (state.marketChartInstance) {
    state.marketChartInstance.destroy();
  }

  state.marketChartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Historical APMC Mandi Rate (₹/Qtl)',
          data: historicalSeries,
          borderColor: '#10b981',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          borderWidth: 3,
          tension: 0.3,
          fill: true
        },
        {
          label: 'AI 15-Day Projected Price Forecast (₹/Qtl)',
          data: forecastSeries,
          borderColor: '#f59e0b',
          borderDash: [6, 4],
          borderWidth: 3,
          tension: 0.3,
          pointBackgroundColor: '#f59e0b'
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { labels: { color: '#cbd5e1', font: { size: 11 } } },
        tooltip: {
          backgroundColor: '#0f172a',
          titleColor: '#f8fafc',
          bodyColor: '#34d399',
          borderColor: '#334155',
          borderWidth: 1
        }
      },
      scales: {
        x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8', font: { size: 10 } } },
        y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8', font: { size: 10 } } }
      }
    }
  });
}

// Kisan Vani Text-to-Speech
function toggleVoiceReadout() {
  if (!('speechSynthesis' in window)) {
    alert("Text-to-Speech is not supported in this browser.");
    return;
  }

  const btn = document.getElementById('btnVoiceReadout');

  if (state.isSpeaking) {
    window.speechSynthesis.cancel();
    state.isSpeaking = false;
    btn.innerHTML = `<i data-lucide="volume-2" class="w-4 h-4"></i> <span>${state.currentLang === 'hi' ? 'किसान वाणी (बोलकर सुनें)' : 'Kisan Vani (Voice)'}</span>`;
    lucide.createIcons();
    return;
  }

  if (!state.diagnosisData) return;

  const isHi = state.currentLang === 'hi';
  const disease = state.diagnosisData.disease;
  const analysis = state.diagnosisData.analysis;

  let textToSpeak = "";
  if (isHi) {
    textToSpeak = `नमस्ते किसान भाई। आपकी फसल ${disease.crop} में ${disease.name_hi} का संक्रमण पाया गया है। 
    एआई विश्वसनीयता ${analysis.confidence_score} प्रतिशत है। 
    उपचार हेतु: ${disease.chemical_treatment_hi[0]} 
    जैविक उपाय: ${disease.organic_treatment_hi[0]}। अधिक जानकारी के लिए किसान कॉल सेंटर 1800-180-1551 पर संपर्क करें।`;
  } else {
    textToSpeak = `Hello Farmer. Diagnosis for your ${disease.crop} crop is ${disease.name_en}. 
    Detection confidence is ${analysis.confidence_score} percent with ${disease.severity} severity. 
    Recommended Chemical spray: ${disease.chemical_treatment_en[0]}. 
    Organic remedy: ${disease.organic_treatment_en[0]}. For toll free advisory, dial 1800-180-1551.`;
  }

  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  utterance.lang = isHi ? 'hi-IN' : 'en-US';
  utterance.rate = 0.95;

  utterance.onstart = () => {
    state.isSpeaking = true;
    btn.innerHTML = `<i data-lucide="square" class="w-4 h-4 text-red-300"></i> <span>Stop Voice (रोकें)</span>`;
    lucide.createIcons();
  };

  utterance.onend = () => {
    state.isSpeaking = false;
    btn.innerHTML = `<i data-lucide="volume-2" class="w-4 h-4"></i> <span>${state.currentLang === 'hi' ? 'किसान वाणी (बोलकर सुनें)' : 'Kisan Vani (Voice)'}</span>`;
    lucide.createIcons();
  };

  window.speechSynthesis.speak(utterance);
}

// Live Camera Implementation
async function openLiveCamera() {
  const modal = document.getElementById('cameraModal');
  const video = document.getElementById('webcamVideo');

  modal.classList.remove('hidden');

  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: 'environment', width: { ideal: 1280 }, height: { ideal: 720 } }
    });
    state.webcamStream = stream;
    video.srcObject = stream;
  } catch (err) {
    alert("Camera permission denied or camera device not found: " + err.message);
    closeLiveCamera();
  }
}

function closeLiveCamera() {
  const modal = document.getElementById('cameraModal');
  modal.classList.add('hidden');
  if (state.webcamStream) {
    state.webcamStream.getTracks().forEach(track => track.stop());
    state.webcamStream = null;
  }
}

function switchCameraSource() {
  closeLiveCamera();
  openLiveCamera();
}

function captureLiveSnapshot() {
  const video = document.getElementById('webcamVideo');
  const snapCanvas = document.getElementById('snapshotCanvas');
  const ctx = snapCanvas.getContext('2d');

  snapCanvas.width = video.videoWidth || 640;
  snapCanvas.height = video.videoHeight || 480;
  ctx.drawImage(video, 0, 0, snapCanvas.width, snapCanvas.height);

  const dataUri = snapCanvas.toDataURL('image/jpeg', 0.9);
  closeLiveCamera();

  const img = new Image();
  img.onload = () => {
    state.loadedImage = img;
    startScanningAnimation();
    triggerAiDiagnosis(dataUri, state.selectedCrop);
  };
  img.src = dataUri;
}

// Printable Health Card Setup
function preparePrintableCard() {
  if (!state.diagnosisData) return;
  const disease = state.diagnosisData.disease;
  const analysis = state.diagnosisData.analysis;

  document.getElementById('printRxId').textContent = `AGRI-${Math.floor(1000 + Math.random() * 9000)}-${new Date().getFullYear()}`;
  document.getElementById('printDate').textContent = new Date().toLocaleString();
  document.getElementById('printCrop').textContent = disease.crop;
  document.getElementById('printDisease').textContent = `${disease.name_en} / ${disease.name_hi}`;
  document.getElementById('printPathogen').textContent = disease.pathogen_type;
  document.getElementById('printSeverity').textContent = disease.severity;
  document.getElementById('printConfidence').textContent = `${analysis.confidence_score}%`;
  document.getElementById('printArea').textContent = `${analysis.damage_percentage}%`;

  const chemDiv = document.getElementById('printChemTreatments');
  chemDiv.innerHTML = disease.chemical_treatment_en.map(c => `<p>• ${c}</p>`).join('');

  const orgDiv = document.getElementById('printOrgTreatments');
  orgDiv.innerHTML = disease.organic_treatment_en.map(o => `<p>• ${o}</p>`).join('');
}

// Ask Agronomist Chat
function setupAgronomist() {
  const btnAsk = document.getElementById('btnAskAgronomist');
  const input = document.getElementById('agronomistInput');

  if (btnAsk && input) {
    btnAsk.addEventListener('click', () => sendAgronomistQuery());
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') sendAgronomistQuery();
    });
  }
}

async function sendAgronomistQuery() {
  const input = document.getElementById('agronomistInput');
  const query = input.value.trim();
  if (!query) return;

  const resBox = document.getElementById('agronomistResponseBox');
  resBox.classList.remove('hidden');

  document.getElementById('agronomistAnswerEn').textContent = "Consulting ICAR & Agronomy Knowledge Engine...";
  document.getElementById('agronomistAnswerHi').textContent = "";

  try {
    const res = await fetch('/api/ask-agronomist', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: query, crop: state.selectedCrop })
    });
    const data = await res.json();
    if (data.success) {
      document.getElementById('agronomistAnswerEn').textContent = data.answer_en;
      document.getElementById('agronomistAnswerHi').textContent = `(हिंदी सलाह): ${data.answer_hi}`;
    }
  } catch (err) {
    document.getElementById('agronomistAnswerEn').textContent = "Unable to fetch response. Dial 1800-180-1551 for instant voice assistance.";
  }
}

// Load Disease Encyclopedia
async function loadEncyclopedia() {
  const grid = document.getElementById('encyclopediaGrid');
  const searchInput = document.getElementById('encyclopediaSearch');
  if (!grid) return;

  try {
    const res = await fetch('/api/encyclopedia');
    const data = await res.json();
    if (data.success) {
      const renderCards = (list) => {
        grid.innerHTML = '';
        list.forEach(d => {
          const card = document.createElement('div');
          card.className = 'bg-slate-900/90 border border-slate-800 rounded-xl p-4 space-y-3 hover:border-brand-500/50 transition cursor-pointer';
          card.innerHTML = `
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-brand-400">${d.crop}</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold">${d.pathogen_type}</span>
            </div>
            <div>
              <h4 class="font-bold text-white text-sm">${d.name_en}</h4>
              <p class="text-xs text-brand-300 font-medium">${d.name_hi}</p>
            </div>
            <p class="text-[11px] text-slate-400 line-clamp-2">${d.symptoms_en[0]}</p>
            <button class="w-full py-1.5 rounded-lg bg-slate-800 hover:bg-brand-600 text-[11px] font-semibold text-white transition">
              Test This Disease (जांचें)
            </button>
          `;
          card.querySelector('button').addEventListener('click', () => {
            switchMainPage('page-doctor');
            loadSampleImage(d.id, d.crop.split(' ')[0].toLowerCase());
          });
          grid.appendChild(card);
        });
      };

      renderCards(data.diseases);

      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          const q = e.target.value.toLowerCase();
          const filtered = data.diseases.filter(d =>
            d.name_en.toLowerCase().includes(q) ||
            d.name_hi.toLowerCase().includes(q) ||
            d.crop.toLowerCase().includes(q)
          );
          renderCards(filtered);
        });
      }
    }
  } catch (err) {
    console.error("Encyclopedia load error:", err);
  }
}
