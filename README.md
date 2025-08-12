# 🚀 ML CI/CD Pipeline on Google Cloud Platform

This project demonstrates a robust and automated CI/CD pipeline for machine learning models using **Google Cloud Platform (GCP)**.  
The pipeline is designed to automatically train, package, and deploy a new **scikit-learn** model whenever a new dataset is uploaded to a **GitHub repository**.  
This ensures that the deployed model is always up-to-date with the latest data, showcasing a **continuous deployment** cycle.

---

## 🏗️ Project Architecture

The CI/CD pipeline is triggered by a simple yet powerful event: **a new `data.csv` file being pushed to the main branch** of this GitHub repository.  
The process then flows through the following stages:

### **Continuous Integration (CI)**
1. A build is triggered by a **GitHub Action**.
2. The `train.py` script is executed:
   - Loads the new `data.csv`
   - Trains a scikit-learn model
   - Saves the trained model artifact
3. The trained model artifact is uploaded to a designated **Google Cloud Storage (GCS)** bucket.

### **Continuous Deployment (CD)**
1. The build pipeline triggers the `deploy.py` script.
2. This script retrieves the newly trained model from the GCS bucket.
3. The model is deployed to a **GCP endpoint**, making it available for serving predictions.

This step demonstrates **true continuous deployment**, as a new model is automatically made live without any manual intervention.

---

## 📁 Key Components

- **`train.py`**  
  Core of the training process: loads data, trains the model, and uploads the serialized model to GCS.

- **`deploy.py`**  
  Handles deployment: fetches the latest model from GCS and deploys it to a managed GCP endpoint for predictions.

- **`data.csv`**  
  Training dataset. Updating and pushing this file triggers the entire CI/CD pipeline.

- **Google Cloud Storage (GCS) Bucket**  
  Central storage for trained model artifacts.

- **GCP Endpoint**  
  Hosted service where the model is deployed and ready to serve predictions.

---

## ⚙️ Getting Started

To get this pipeline running, you'll need to set up the following:

1. **GCP Project**  
   Ensure you have an active GCP project with billing enabled.

2. **Service Account**  
   Create a service account with the following permissions:
   - `Storage Object Creator`
   - `Storage Object Viewer`
   - `Cloud AI Platform Deployer`  
   Generate a JSON key for this account.

3. **GCS Bucket**  
   Create a GCS bucket to store your model artifacts.

4. **GitHub Secrets**  
   Store your GCP service account key as a secret in your GitHub repository to allow GitHub Actions to authenticate with your GCP project.

---

Once these prerequisites are met, configure your **GitHub Actions** workflow file:  
`.github/workflows/main.yml` to trigger the build and deployment scripts.
