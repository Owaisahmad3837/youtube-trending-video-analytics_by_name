
# 🚀 YouTube Channel ETL Pipeline

## 📌 Overview

This project is a **Python-based ETL pipeline** that extracts data from the YouTube Data API, processes multiple videos from a channel using playlist chaining, and stores structured analytics in a JSON file.

It demonstrates **real-world data engineering concepts** like API chaining, batching, and ETL workflow design.

---

## 🎯 What This Project Does

Given a **YouTube Channel ID**, the pipeline:

* 📥 Extracts channel information (title, subscribers, views)
* 📂 Retrieves uploads playlist from the channel
* 🎬 Collects multiple video IDs (batch extraction)
* 📊 Fetches video details (title, views, likes)
* 🧹 Transforms raw data into structured format
* 💾 Saves output as JSON file

---

## 🏗️ Architecture (ETL Flow)

```
Channel ID
    ↓
[Extract Channel Info]
    ↓
Uploads Playlist ID
    ↓
[Extract Video IDs (Playlist API)]
    ↓
[List of Video IDs]
    ↓
[Extract Video Details]
    ↓
Transform (Clean & Structure Data)
    ↓
Load → raw_data.json
```

---

## 📁 Project Structure

```
youtube-channel-etl-pipeline/
│
├── main.py
│
├── config/
│   └── config.py
│
├── extract/
│   ├── channel.py
│   ├── playlist.py
│   └── videos.py
│
├── transform/
│   └── clean.py
│
├── load/
│   └── json_loader.py
│
├── output/
│   └── raw_data.json
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python 🐍
* YouTube Data API v3
* Google API Client
* JSON (for storage)
* dotenv (for environment variables)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/youtube-channel-etl-pipeline.git
cd youtube-channel-etl-pipeline
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```env
YOUTUBE_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📤 Output Example

```json
{
  "channel": {
    "title": "Google Developers",
    "subscribers": "2000000",
    "views": "500000000"
  },
  "videos": [
    {
      "title": "Intro to Python",
      "views": "120000",
      "likes": "5000"
    },
    {
      "title": "API Basics",
      "views": "90000",
      "likes": "3200"
    }
  ]
}
```

---

## 🧠 Key Learning Concepts

* API chaining (Channel → Playlist → Videos)
* Batch data extraction
* ETL pipeline design
* Handling nested JSON data
* YouTube Data API integration
* Modular Python project structure

---

## 📈 Future Improvements

* Add pagination (fetch 100+ videos)
* Store data in PostgreSQL / MongoDB
* Add scheduling (Airflow / Cron jobs)
* Build dashboard (Streamlit / Power BI)
* Add logging system
* Add error handling + retries

---

## 👨‍💻 Author

Built as a **Data Engineering learning project** to understand real-world ETL systems using YouTube Data API.

