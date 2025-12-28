"""
Objective:
- Programmatically download satellite images for properties using geographic
  coordinates (latitude and longitude).

- Integrate the Mapbox Static Images API to acquire high-resolution satellite imagery.

- Securely load API credentials using environment variables (.env file).

- Support runtime-controlled execution modes (sample vs full dataset) to enable
  fast testing and scalable data ingestion.

- Provide progress logging at fixed intervals to monitor long-running download tasks.

- Avoid redundant API calls by skipping images that have already been downloaded.

- Store images in a structured directory aligned with property identifiers for
  consistent downstream usage.

"""

import os
import requests
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

# LOAD ENV

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
if not MAPBOX_TOKEN:
    raise RuntimeError("MAPBOX_TOKEN not found in .env file")


# RUNTIME SWITCH 

USE_SAMPLE = False          # True = sample data, False = full data
SAMPLE_SIZE = 500          
PROGRESS_INTERVAL = 50     

RUN_MODE = "sample" if USE_SAMPLE else "full"


# PATHS

DATA_PATH = "data/train.xlsx"
IMAGE_DIR = Path("images/train")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)


# LOAD DATA

df = pd.read_excel(DATA_PATH)

if USE_SAMPLE:
    df = df.sample(n=min(SAMPLE_SIZE, len(df)), random_state=42)

total_images = len(df)

print(f"Starting image download...")
print(f"Total images to download: {total_images}")


# MAPBOX URL BUILDER

def mapbox_url(lat, lon, zoom=17, size=256):
    return (
        f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
        f"{lon},{lat},{zoom}/{size}x{size}"
        f"?access_token={MAPBOX_TOKEN}"
    )


downloaded = 0
skipped = 0

for idx, row in df.iterrows():
    pid = row["id"]
    lat = row["lat"]
    lon = row["long"]

    out_path = IMAGE_DIR / f"{pid}.jpg"

    if out_path.exists():
        skipped += 1
        continue

    url = mapbox_url(lat, lon)

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(out_path, "wb") as f:
                f.write(response.content)
            downloaded += 1
        else:
            print(f"⚠️ Failed ID {pid} | HTTP {response.status_code}")

    except Exception as e:
        print(f"❌ Error for ID {pid}: {e}")

  
    if downloaded % PROGRESS_INTERVAL == 0:
        print(f"Downloaded {downloaded}/{total_images} images")


print("\n========== DOWNLOAD SUMMARY ==========")
print(f"Total requested : {total_images}")
print(f"Downloaded      : {downloaded}")
print(f"Already existed : {skipped}")
print("=====================================")


'''
Observations/outputs:
- Satellite images are reliably fetched for all valid latitude–longitude pairs.

- Progress-based logging improves visibility during large-scale image downloads.

- Skipping existing files significantly reduces execution time and API usage.

- Sample-mode execution enables rapid validation of the image ingestion pipeline.

- Image filenames mapped to property IDs ensure seamless alignment with tabular data.

- The fetching pipeline is reproducible, modular, and independent of preprocessing
  and model training stages.

- Downloaded imagery provides environmental context suitable for future CNN-based
  feature extraction and multimodal modeling.
  
'''