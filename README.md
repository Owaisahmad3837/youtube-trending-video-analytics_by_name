
# 🎥 YouTube Trending Video Analytics Platform

An end-to-end Data Engineering project that extracts YouTube video data, processes analytics, stores data in PostgreSQL, and displays insights through a Streamlit dashboard.

## 📌 Project Overview

This system allows users to search YouTube data by:

- Channel name
- Video name

It extracts video information and analyzes engagement metrics.

## 🔄 ETL Flow

```

YouTube API
↓
Extract Video Data
↓
Transform Analytics Data
↓
Load PostgreSQL Database
↓
Streamlit Dashboard

```

## 🛠️ Tech Stack

- Python
- YouTube Data API
- Pandas
- PostgreSQL
- Streamlit
- ETL Pipeline

## 📁 Project Structure

```

youtube-trending-video-analytics/

├── extract/        # Data extraction
├── transform/      # Data processing
├── load/           # Database loading
├── dashboard/      # Streamlit dashboard
├── config/         # Configuration
└── main.py         # ETL pipeline

````

## ✨ Features

✅ Search videos by name  
✅ Search channels by name  
✅ Extract YouTube statistics  
✅ Analyze views, likes, comments  
✅ Store data in PostgreSQL  
✅ Interactive dashboard  

## 🚀 Run Project

```bash
python main.py
````

Run dashboard:

```bash
streamlit run dashboard/app.py
```

## 🎯 Skills

* Data Engineering
* API Data Extraction
* ETL Pipeline
* Data Transformation
* SQL Database
* Data Visualization

## Author

**Owais Ahmad**

```
```
