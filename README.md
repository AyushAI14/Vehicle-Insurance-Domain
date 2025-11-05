---

# Vehicle Data Pipeline Project

A full-stack, end-to-end MLOps project leveraging **MongoDB**, **AWS**, **Docker**, and **CI/CD**. This project showcases modern data engineering, model development, and deployment workflows — all wrapped in a scalable and production-ready pipeline.

---

## Project Setup

### Initial Setup

1. **Generate Project Template**

   ```bash
   python template.py
   ```

2. **Local Package Imports**

   * Add import logic to `setup.py` and `pyproject.toml`.
   * Need help? See `crashcourse.txt`.

3. **Create Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

4. **Verify Installation**

   ```bash
   pip list
   ```

---

## MongoDB Atlas Integration

1. Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

2. Create a new project > Create Cluster (M0 Tier).

3. Set up DB user (username & password).

4. Add IP access: `0.0.0.0/0` for open access.

5. Grab your connection string (Driver: Python 3.6+).

6. Inside `notebook/`, create:

   * `mongoDB_demo.ipynb`
   * Add dataset and push it to MongoDB.

7. Confirm data upload at Atlas > Database > Browse Collections.

---

## Logging, Exceptions, EDA

1. Implement `logger.py` and `exception.py`.
2. Test them via `demo.py`.
3. Add EDA & feature engineering notebooks in `notebook/`.

---

## Data Ingestion Pipeline

1. Add configuration constants in `constants/__init__.py`.
2. Define DB connection in `configuration/mongo_db_connection.py`.
3. Fetch and transform data to DataFrame in `data_access/proj1_data.py`.
4. Define `DataIngestionConfig` and `DataIngestionArtifact` classes.
5. Implement logic in `components/data_ingestion.py` and training pipeline.
6. Run `demo.py` after setting MongoDB URI:

   **Set MongoDB URL:**

   **Linux/Mac (bash):**

   ```bash
   export MONGODB_URL="mongodb+srv://<username>:<password>@..."
   echo $MONGODB_URL
   ```

   **Windows (PowerShell):**

   ```powershell
   $env:MONGODB_URL="mongodb+srv://<username>:<password>@..."
   echo $env:MONGODB_URL
   ```

   Also: Add `artifact/` to `.gitignore`

---

## Data Validation & Transformation

1. Complete `utils/main_utils.py` and `config/schema.yaml`.
2. Build:

   * `data_validation` component.
   * `data_transformation` component (add `estimator.py` to entity).
   * `model_trainer` component (update `estimator.py`).

---

## AWS S3 Integration for Model Registry

1. **IAM User Setup**

   * Name: `firstproj`
   * Policy: `AdministratorAccess`
   * Save access keys and set env vars:

   **Bash:**

   ```bash
   export AWS_ACCESS_KEY_ID="..."
   export AWS_SECRET_ACCESS_KEY="..."
   ```

2. Add config to `constants/__init__.py`:

   ```python
   MODEL_BUCKET_NAME = "mymodel-mlopsproj-1"
   MODEL_PUSHER_S3_KEY = "model-registry"
   MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
   ```

3. Create S3 bucket with above name (region: `us-east-1`).

4. Add code to:

   * `configuration/aws_connection.py`
   * `aws_storage/`
   * `entity/s3_estimator.py`

---

## Model Evaluation & Pusher

* Implement `model_evaluation` and `model_pusher` components.
* Push latest model to S3 if it beats existing score threshold.

---

## Model Prediction Pipeline

1. Setup `app.py` with prediction logic.
2. Add `static/` and `template/` for web interface.

---

## CI/CD & Deployment (EC2 + Docker)

### Docker & Github Actions

1. Add `Dockerfile`, `.dockerignore`, and `.github/workflows/aws.yaml`.

2. Create IAM user (`usvisa-user`) and add secrets:

   * `AWS_ACCESS_KEY_ID`
   * `AWS_SECRET_ACCESS_KEY`
   * `AWS_DEFAULT_REGION`
   * `ECR_REPO`

3. Create ECR repo: `vehicleproj`.

### EC2 Setup (Ubuntu)

1. Launch EC2 (t2.medium), 30GB storage, allow HTTP/HTTPS.
2. Install Docker:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

### Self-Hosted Github Runner

1. Go to Github > Settings > Actions > Runner > Add Linux runner.
2. Run provided commands inside EC2.
3. Verify runner is “idle”.

---

## Final Deployment

1. Open port `5080` on EC2 (Security Groups).
2. Visit `http://<EC2_IP>:5080` to view the app.
3. Use `/training` route to retrain your model.

---

## Tech Stack

* **Languages**: Python 3.12
* **Data**: MongoDB Atlas, Pandas
* **Model**: Sklearn, Custom Estimators
* **Cloud**: AWS (S3, EC2, IAM, ECR)
* **DevOps**: Docker, GitHub Actions (CI/CD)
* **Web**: FastApi, HTML/CSS

---


