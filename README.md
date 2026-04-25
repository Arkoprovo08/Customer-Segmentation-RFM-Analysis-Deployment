# Customer Segmentation Platform with RFM Analysis, Machine Learning, and Cloud Deployment

## Overview

This project implements an end-to-end customer segmentation platform using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering. It identifies and categorizes customers based on purchasing behavior to support data-driven business decisions.

The system generates actionable segments such as High Value, Regular, At Risk, Potential High Value, and Lost High Value. These insights can be used for targeted marketing, customer retention, and revenue optimization.

The solution is productionized by exposing the segmentation logic through a FastAPI-based REST API, containerized using Docker, and deployed on AWS EC2 for real-time predictions.

---

## Problem Statement

Businesses often face challenges in:

* Identifying high-value customers
* Detecting customers at risk of churn
* Recognizing potential loyal customers

This project addresses these challenges through behavioral segmentation using transactional data.

---

## Architecture

The system follows a modular, production-oriented architecture:

Client Request (User / API Consumer)→ FastAPI Application Layer (app.py)→ Model Layer (model.py)→ Preprocessing Pipeline

* Log Transformation
* Feature Scaling (StandardScaler)→ Clustering Model (K-Means)→  Business Rules Engine
* Quantile-based refinement
* Segment reassignment logic→ Response (Customer Segment Output)→ Docker Container Runtime→ AWS EC2 Instance (Cloud Hosting)

---

## System Description

* The FastAPI layer handles incoming requests and input validation.
* The model layer processes data using pre-trained artifacts (scaler, clustering model, quantiles).
* The K-Means model assigns initial clusters based on RFM features.
* A business rules engine refines clusters using quantile thresholds to improve interpretability.
* The final customer segment is returned as a JSON response.
* Docker ensures consistent execution across environments.
* AWS EC2 hosts the application for public access.

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

## Tech Stack

* Python
* Pandas, NumPy, Scikit-learn
* FastAPI
* Docker
* AWS EC2

---

## Project Structure

```
Customer-Segmentation-RFM-Analysis-Deployment/
│
├── app.py
├── model.py
├── config.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
│
├── artifacts/
│   ├── scaler.pkl
│   ├── kmeans.pkl
│   ├── quantiles.pkl
```

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
