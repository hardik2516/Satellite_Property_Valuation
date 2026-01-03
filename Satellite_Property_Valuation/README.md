

## 🛰️ Satellite Imagery–Based Property Valuation

A machine learning project that estimates property prices by combining **tabular real-estate data** with **satellite imagery–derived geospatial context**, using a clean, leakage-safe, production-style pipeline.

---

## 📌 Project Overview

Traditional property valuation models rely only on tabular features such as size, location codes, or amenities.
This project enhances valuation by incorporating **satellite imagery context** (via Mapbox) to capture spatial signals such as surroundings, density, and locality characteristics.

### Key Highlights

* Clean separation of **data fetching**, **preprocessing**, **training**, and **inference**
* Sample vs full dataset execution support
* Leakage-safe evaluation
* Reproducible pipeline with clear artifact management
* Ready for portfolio, interviews, and future extension

---

## 🏗️ High-Level Architecture

```
Satellite Imagery (Conceptual)
            ↓
Spatial Context Understanding
            ↓
Engineered Geospatial Features
            ↓
Tabular Feature Set
            ↓
Random Forest Regressor
            ↓
Predicted Property Price
```

> Note: Satellite imagery is used conceptually to derive spatial context and is not directly fed as raw pixels into a deep learning model in this version.

---

## 📁 Repository Structure

```
SATELLITE_PROPERTY_VALUATION/
│
├── data/                        # Structured tabular datasets
│   ├── train.xlsx               # Original training dataset
│   ├── test.xlsx                # Original test dataset
│   ├── X_features_full.csv      # Engineered feature matrix (full data)
│   └── y_target_full.csv        # Target variable (property prices)
│
├── images/                      # Satellite imagery data (generated at runtime)
│   ├── train/                   # Full training images
│   ├── test/                    # Test images for inference
│   └── train_sample/            # Small image subset for experiments
│
├── data_fetcher.py              # Image ↔ tabular data mapping logic
│
├── preprocessing.ipynb          # Data cleaning & feature engineering
├── model_training.ipynb         # Model training, validation & evaluation
│
├── 24119014_final.csv           # Final model predictions (test set)
│
├── requirements.txt             # Python dependencies
│
├── .gitignore                   # Files & folders excluded from version control
└── README.md                    # Project documentation
```

---

## 🚫 What Is NOT Included (and Why)

To keep the repository **clean, lightweight, and secure**, the following are intentionally excluded:

### ❌ `images/` contents

* Satellite images are **large and auto-generated**
* They are fetched dynamically using `data_fetcher.py`
* Including them would unnecessarily bloat the repository

✔️ **Solution:**
An empty `images/` folder is kept so the code knows where to save images at runtime.

---

### ❌ `venv/` (Virtual Environment)

* Platform-specific
* Extremely large
* Not portable across systems

✔️ **Solution:**
Dependencies are listed in `requirements.txt` so users can recreate the environment locally.

---

### ❌ API Keys / Secrets

* Credentials must never be committed to GitHub

✔️ **Solution:**
Environment variables are used (explained below).

---

## 📄 `.gitignore` (Important)

The `.gitignore` file is **required and should be uploaded**.

It prevents:

* accidental uploads of large or generated files
* leaking credentials
* committing virtual environments

Example exclusions:

```
venv/
images/*
__pycache__/
.env
```

---

## ⚙️ Setup Instructions (Step-by-Step)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Satellite_Property_Valuation.git
cd Satellite_Property_Valuation
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables (Mapbox API)

Create an environment variable:

**Windows (PowerShell):**

```powershell
setx MAPBOX_API_KEY "your_api_key_here"
```

**macOS / Linux:**

```bash
export MAPBOX_API_KEY="your_api_key_here"
```

---

### 5️⃣ Ensure Folder Structure Exists

Make sure this folder exists (even if empty):

```
images/
```

Satellite images will be automatically saved here when running the data fetcher.

---

## ▶️ How to Run the Project

### Step 1 — Fetch Satellite Images

```bash
python data_fetcher.py
```

This will:

* Read latitude and longitude values
* Download satellite images using Mapbox
* Save images into the `images/` directory

---

### Step 2 — Preprocessing & Feature Engineering

Open and run:

```
preprocessing.ipynb
```

Supports:

* Sample mode (fast experimentation)
* Full dataset mode (final training)

---

### Step 3 — Model Training & Evaluation

Run:

```
model_training.ipynb
```

Outputs:

* Trained model
* Validation metrics (RMSE, R²)
* Evaluation artifacts for error analysis

---

### Step 4 — Test Inference (No Leakage)

Run:

```
test_inference.ipynb
```

Generates:

```
24119014_final.csv
```

This file contains **final property price predictions for the unseen test dataset**.

---

## 📊 Evaluation Artifacts

`predicted_vs_actual_full.csv` contains:

* actual price
* predicted price
* signed error
* absolute error

This file is **for analysis and diagnostics only**, not a submission file.

---

## 🔒 Data Leakage Safety

✔️ Test data is **never used** in:

* preprocessing fitting
* feature selection
* model training

✔️ Test data is used **only once** for final inference.

This ensures evaluation integrity and production-grade ML hygiene.

---

## 🚀 Future Improvements

* CNN-based satellite image embeddings
* Gradient boosting models (XGBoost / LightGBM)
* Temporal price modeling
* Model ensembling
* Model deployment via REST API

---

## 👤 Author

**Hardik Gautam**
Data Science & Machine Learning Enthusiast
📍 India | 🌍 Open to global opportunities

---

## ⭐ Final Note

This repository is structured to reflect **real-world ML engineering practices**, not just experimentation.
Every inclusion and exclusion is **intentional**, documented, and designed for clarity, reproducibility, and professional use.

---
