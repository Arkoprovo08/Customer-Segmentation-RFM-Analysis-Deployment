# Customer Segmentation Engine (RFM + Machine Learning + Deployment)

## Overview

This project builds an end-to-end customer segmentation system using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering.

The solution is deployed as a REST API using FastAPI, containerized with Docker, and hosted on AWS EC2 for real-time predictions.

---

## Problem Statement

Businesses often struggle to identify:

* High-value customers
* At-risk customers
* Potential loyal customers

This project addresses the problem by segmenting customers based on purchasing behavior.

---

## Approach

### 1. RFM Feature Engineering

* Recency: Days since last purchase
* Frequency: Number of transactions
* Monetary: Total spend

### 2. Data Transformation

* Log transformation applied to reduce skewness
* Standard scaling applied for clustering

### 3. Clustering

* K-Means clustering with K = 3
* Segments identified:

  * High Value
  * Regular
  * At Risk

### 4. Business Rules Layer

Segmentation refined using quantile-based rules:

* Potential High Value
* Lost High Value

---

## Architecture

User → FastAPI → Model → Segmentation Logic → Response
↓
Docker
↓
AWS EC2

---

## Tech Stack

* Python
* Pandas, NumPy, Scikit-learn
* FastAPI
* Docker
* AWS EC2

---

## How to Run Locally

### 1. Clone repository

```
git clone https://github.com/Arkoprovo08/Customer-Segmentation-RFM-Analysis-Deployment.git
cd Customer-Segmentation-RFM-Analysis-Deployment
```

### 2. Build Docker image

```
docker build -t rfm-app .
```

### 3. Run container

```
docker run -p 8000:8000 rfm-app
```

### 4. Access API

```
http://localhost:8000/docs
```

---

## Live Deployment

```
http://13.60.9.212:8000/docs/
```

---

## API Usage

### Endpoint

```
POST /predict
```

### Sample Input

```json
{
  "recency": 30,
  "frequency": 5,
  "monetary": 2000
}
```

### Sample Output

```json
{
  "segment": "High Value"
}
```

---

## Key Insights

* High frequency and low recency indicate high-value customers
* High recency and low frequency indicate at-risk customers
* High monetary but inactive customers are classified as lost high value

---

## Features

* End-to-end machine learning pipeline
* Real-time prediction API
* Dockerized deployment
* Cloud hosting on AWS EC2
* Business-driven segmentation logic

---

## Author

Arkoprovo Ghosh

---

## License

This project is for educational and demonstration purposes.
