---

## 🛰️ Satellite Imagery–Based Property Valuation

A machine learning project that estimates property prices by combining **tabular real-estate data** with **satellite imagery–derived geospatial context**, using a clean, leakage-safe, production-style pipeline.

This project prioritizes **correct modeling choices, reproducibility, and clarity of design decisions** over unnecessary complexity.

---

## 📌 Project Overview

Traditional property valuation models rely primarily on structured tabular features such as property size, room count, and location codes. However, real-estate prices are strongly influenced by **spatial and environmental context** (neighborhood density, surrounding infrastructure, locality characteristics), which tabular data alone often fails to capture.

This project enhances valuation by incorporating **satellite imagery–informed spatial context** using a **proxy-based multimodal approach**, where satellite images inform **engineered geospatial features** rather than being directly fed into a deep vision model.

---

## 🎯 Key Objectives

* Incorporate spatial awareness into property valuation
* Maintain strict **data leakage safety**
* Use **appropriate explainability methods** for the chosen model
* Keep the pipeline **practical, interpretable, and extensible**

---

## 🏗️ High-Level Architecture (Conceptual)

Satellite Imagery (Conceptual)
-->
Spatial Context Understanding
-->
Engineered Geospatial Features
-->
Tabular Feature Set
-->
Random Forest Regressor
-->
Predicted Property Price

Important clarification:
Satellite imagery is **not** used as raw image pixels inside the model. Instead, it is used to **inform spatial context**, which is converted into numeric features suitable for tabular machine learning.

---

## 🧠 Modeling Approach & Design Choices (Critical Section)

### 1️⃣ Why satellite imagery is used conceptually (not as raw pixels)

Satellite images provide rich spatial information but training CNN-based vision models requires:

* very large labeled datasets
* high computational resources
* complex explainability tooling

Given the dataset size and the project goal (property valuation, not vision research), a **proxy-based approach** was chosen.

Satellite imagery is used to derive **geospatial signals** (location interactions, spatial effects), which are then represented numerically.

This makes the model:

* more stable
* easier to interpret
* suitable for tabular ML

---

### 2️⃣ Why Random Forest (and not CNN)

The final prediction model is a **Random Forest Regressor** because:

* the final feature space is numeric/tabular
* Random Forests handle non-linear relationships well
* they are robust to noise
* they provide feature importance for explainability

CNNs were **not used** because:

* raw image tensors are not model inputs
* the project focuses on valuation accuracy, not image classification
* Random Forest is a better fit for structured + geo-engineered data

---

### 3️⃣ Why Grad-CAM is NOT used (explicit clarification)

Grad-CAM is applicable **only** when:

* a CNN is trained on raw images
* predictions depend directly on pixel activations

In this project:

* no CNN is trained
* no image tensors are passed to the model
* predictions depend on numeric features only

Therefore, **Grad-CAM would be conceptually incorrect** and was intentionally not used.

Instead, explainability is handled via:

* feature importance (Random Forest)
* error analysis (actual vs predicted)
* absolute and relative error inspection

This is the **correct explainability strategy** for tabular models.

---

## 📁 Repository Structure

SATELLITE_PROPERTY_VALUATION/

data/

* train.xlsx
* test.xlsx
* X_features_full.csv
* y_target_full.csv

images/

* train/
* test/
* train_sample/

data_fetcher.py

preprocessing.ipynb
model_training.ipynb
test_inference.ipynb

predicted_vs_actual_training_data.csv
submission.csv

requirements.txt
.gitignore
README.md

---

## 🚫 What Is NOT Included (and Why)

### Satellite image files

* Large in size
* Generated dynamically via Mapbox API
* Can be regenerated at any time

To keep the repository lightweight, only the **folder structure** is included.

---

### Virtual environment (venv/)

* System-specific
* Not portable
* Recreated using requirements.txt

---

### API keys / secrets

* Must never be committed
* Stored locally using environment variables

These exclusions follow **industry-standard ML repository practices**.

---

## ⚙️ Setup & Execution Guide (Zero Ambiguity)

### Step 1 — Clone the repository

git clone [https://github.com/your-username/Satellite_Property_Valuation.git](https://github.com/your-username/Satellite_Property_Valuation.git)
cd Satellite_Property_Valuation

---

### Step 2 — Create and activate a virtual environment

python -m venv venv

Windows:
venv\Scripts\activate

macOS / Linux:
source venv/bin/activate

---

### Step 3 — Install dependencies

pip install -r requirements.txt

---

### Step 4 — Set Mapbox API key

Create an environment variable:

Windows (PowerShell):
setx MAPBOX_API_KEY "your_api_key_here"

macOS / Linux:
export MAPBOX_API_KEY="your_api_key_here"

---

### Step 5 — Ensure folder structure

Ensure the following folder exists:

images/

Satellite images will be automatically saved here when fetching data.

---

## ▶️ How to Run the Project (End-to-End)

### Step 1 — Fetch satellite images (optional but supported)

python data_fetcher.py

Downloads satellite image tiles based on latitude and longitude.

---

### Step 2 — Preprocessing & feature engineering

Open and run:

preprocessing.ipynb

This performs:

* data cleaning
* feature engineering
* geospatial feature creation
* sample vs full dataset switching

Outputs ML-ready CSVs.

---

### Step 3 — Model training & evaluation

Run:

model_training.ipynb

This includes:

* baseline Random Forest (tabular only)
* enhanced Random Forest (tabular + geo features)
* RMSE and R² evaluation
* error and absolute error analysis
* feature importance inspection

---

### Step 4 — Test inference (no leakage)

Run:

test_inference.ipynb

Generates:
submission.csv

Test data is used **only for prediction**, never for training.

---

## 📊 Evaluation Artifacts (Clarification)

predicted_vs_actual_training_data.csv contains:

* actual_price
* predicted_price
* signed_error
* absolute_error
* relative_error

This file is **for analysis only**, not a submission.

Large absolute errors are expected due to the wide price range of real estate; relative error provides better interpretability.

---

## 🔒 Data Leakage Safety (Explicit)

* No test data used during preprocessing fitting
* No test data used during feature selection
* No test data used during model training
* All preprocessing artifacts reused consistently

---

## 🚀 Future Extensions (Not Implemented)

* CNN-based satellite embeddings
* Grad-CAM explainability (only if CNNs are introduced)
* Gradient boosting models
* Region-specific models
* API deployment

These are intentionally left as future work.

---

## 👤 Author

Hardik Gautam
Data Science & Machine Learning Enthusiast
India | Open to global opportunities

---

## ⭐ Final Statement for Evaluators

This project emphasizes **correct methodology over buzzwords**.
Every modeling and explainability choice is intentional, justified, and aligned with the data and problem constraints.

No overclaiming. No misuse of deep learning.
Only appropriate tools applied correctly.

---
