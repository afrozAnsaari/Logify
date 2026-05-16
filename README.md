# Logify — Intelligent Log Classification & Error Analysis System

## Overview

Logify is a hybrid machine learning and LLM-powered log analysis system designed to automatically classify, organize, and analyze server logs and system errors.

The project combines:

* Rule-based classification using Regex
* Semantic understanding using BERT embeddings
* Density-based clustering using DBSCAN
* LLM-powered fallback classification using Llama models via Groq API
* REST API integration using FastAPI

The system is capable of processing large volumes of logs, identifying recurring patterns, detecting unclassified logs, and intelligently routing ambiguous cases to an LLM for contextual classification.

---

# Motivation

Modern applications generate thousands of logs every day.

Manually inspecting these logs is:

* Time-consuming
* Error-prone
* Difficult to scale
* Inefficient for real-time systems

Traditional rule-based systems fail when:

* New log formats appear
* Unstructured logs are generated
* Patterns become semantically complex

Logify solves this by combining:

* Traditional regex-based detection
* Machine learning clustering
* Transformer-based semantic embeddings
* LLM contextual reasoning

into a single intelligent pipeline.

---

# Features

## Regex-based Classification

Fast and lightweight rule-based classification for known recurring log patterns.

Examples:

* User login/logout events
* Backup notifications
* System updates
* File upload logs

---

## DBSCAN Clustering

Uses DBSCAN to group semantically similar logs without requiring labeled data.

Advantages:

* Detects naturally occurring log clusters
* Handles noisy/unstructured logs
* Identifies outliers automatically

---

## BERT Semantic Encoding

Unclassified logs are encoded using transformer embeddings.

This enables:

* Semantic understanding
* Similarity comparison
* Context-aware grouping
* Better generalization for unseen logs

---

## LLM-Powered Fallback Classification

For ambiguous or low-confidence cases, the system routes logs to:

* Llama models hosted on Groq API

The LLM performs:

* Contextual understanding
* Semantic reasoning
* Sentiment-aware categorization
* Dynamic label generation

---

## FastAPI Integration

Provides REST APIs for:

* Uploading CSV logs
* Real-time log classification
* Batch processing
* JSON responses

---

## CSV-based Pipeline

Supports structured log ingestion through CSV files.

Expected columns:

| Column      | Description            |
| ----------- | ---------------------- |
| source      | Log source/application |
| log_message | Actual log text        |

---

# Tech Stack

| Category               | Technologies                     |
| ---------------------- | -------------------------------- |
| Backend                | Python, FastAPI                  |
| ML/NLP                 | Scikit-learn, Transformers, BERT |
| Clustering             | DBSCAN                           |
| LLM                    | Groq API, Llama                  |
| Data Processing        | Pandas, NumPy                    |
| API Server             | Uvicorn                          |
| Environment Management | python-dotenv, venv              |

---

# System Architecture

```text
Incoming Logs
      |
      v
Regex Classification
      |
      v
If Unclassified
      |
      v
DBSCAN + BERT Embeddings
      |
      v
Confidence Check
      |
      v
LLM Fallback (Groq + Llama)
      |
      v
Final Classification
      |
      v
FastAPI Response / CSV Export
```

---

# Project Structure

```text
logify/
│
├── models/
│   └── log_classifier.joblib
│
├── resources/
│   ├── output.csv
│   └── test.csv
│
├── scripts/
│   ├── classify.py
│   ├── processor_bert.py
│   ├── processor_llm.py
│   └── processor_regex.py
│
├── server/
│   └── server.py
│
├── training/
│   ├── dataset/
│   │   ├── raw_synthetic_logs.csv
│   │   └── synthetic_logs.csv
│   │
│   ├── raw_synthetic_logs.csv
│   ├── requirements.txt
│   └── training.ipynb
│
├── pyproject.toml
├── requirements.txt
├── README.md
└── .env
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
cd logify
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Get API key from:

[https://console.groq.com](https://console.groq.com)

---

# Running the Project

## Run Classification Script

```bash
python classify.py
```

---

## Run FastAPI Server

```bash
python -m uvicorn server:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

# API Endpoints

## Upload CSV Logs

### Endpoint

```text
POST /classify-csv
```

### Input

CSV file containing:

```csv
source,log_message
CRM,User User123 logged in
ERP,Backup completed successfully
```

### Output

```json
{
  "status": "success",
  "output_file": "classified_logs.csv"
}
```

---

# Example Workflow

## Input Log

```text
System reboot initiated by user Admin123
```

## Regex Match

```text
System Notification
```

---

## Unknown Log Example

```text
Service timeout observed during distributed cache synchronization
```

Pipeline:

1. Regex fails
2. DBSCAN similarity analysis
3. BERT semantic embedding
4. Low confidence detected
5. LLM fallback triggered
6. Final classification generated

---

# Machine Learning Workflow

## Step 1 — Regex Filtering

Known patterns are classified instantly.

Benefits:

* Fast execution
* Low compute usage
* Deterministic behavior

---

## Step 2 — Semantic Encoding

Transformer embeddings generated using BERT.

Used for:

* Semantic similarity
* Clustering
* Intelligent grouping

---

## Step 3 — DBSCAN Clustering

Clusters logs based on semantic proximity.

Benefits:

* No labeled data required
* Noise handling
* Dynamic cluster discovery

---

## Step 4 — LLM Inference

Low-confidence or unseen logs are forwarded to:

* Llama 3.3 models through Groq API

The LLM performs contextual classification.

---

# Future Improvements

## Planned Features

* Real-time streaming pipelines
* Kafka integration
* Elasticsearch support
* Vector databases (FAISS/Pinecone)
* Anomaly detection models
* Grafana dashboards
* Confidence-based routing
* Incremental retraining pipeline
* Docker deployment
* Async batch inference
* Multi-label classification

---

# Challenges Faced

* Handling inconsistent log formats
* Managing multiple Python environments
* Path resolution after project restructuring
* Integrating FastAPI with ML pipelines
* Balancing regex and semantic approaches
* Handling low-confidence predictions

---

# Learning Outcomes

This project helped in understanding:

* NLP pipelines
* Transformer embeddings
* Clustering algorithms
* FastAPI backend development
* Environment management
* Hybrid AI architectures
* LLM API integration
* Production-style ML workflows

---

# Sample Output

| Source      | Log Message                   | Predicted Label     |
| ----------- | ----------------------------- | ------------------- |
| CRM         | User User123 logged out       | User Action         |
| ERP         | Backup completed successfully | System Notification |
| AuthService | Invalid token detected        | Security Alert      |

---

# Requirements

Example dependencies:

```text
fastapi
uvicorn
pandas
numpy
scikit-learn
transformers
groq
python-dotenv
joblib
```

---

# Author

Developed as a hybrid ML + NLP + FastAPI project focused on intelligent log analysis, semantic classification, and scalable backend integration.

---

# License

This project is intended for educational and research purposes.
