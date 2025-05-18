# 🔍 Self-Healing Real-Time Anomaly Detection System

An end-to-end ML system that performs **real-time anomaly detection** and automatically retrains itself when **data or concept drift** is detected—ideal for domains like fraud detection, cybersecurity, or IoT monitoring.

---

## 🚀 Features

- ✅ Real-time data ingestion via **Kafka**
- 🧠 Anomaly detection using **Isolation Forest / Autoencoder**
- 📉 Drift detection via **Evidently AI** & **Kolmogorov–Smirnov tests**
- 🔁 Auto-triggered model **retraining using Apache Airflow**
- 📊 Visual dashboard with **Streamlit** for monitoring
- 🐳 Fully **Dockerized**, deployable in any environment

---

## 📦 Architecture

    +---------+        +------------------+
    | Kafka   | -----> | Anomaly Detector |
    +---------+        +------------------+
                           |         |
                           v         v
                +-------------+   +----------------+
                | Drift Check |   | Dashboard/API  |
                +-------------+   +----------------+
                           |
                  Drift Detected?
                           |
                  +--------+--------+
                  | Trigger Airflow |
                  | DAG to Retrain  |
                  +-----------------+
