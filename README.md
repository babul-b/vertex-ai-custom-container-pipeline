# Vertex AI CustomTrainingJobOp - Custom Container Pipeline

This repository contains a simple, generic example of running a two-step Vertex AI Pipeline using `CustomTrainingJobOp` from Google Cloud Pipeline Components.

The pipeline demonstrates:

- Building a custom Python container
- Pushing the image to Artifact Registry
- Running a preprocessing step on Vertex AI
- Running a training step after preprocessing completes
- Passing environment variables into the custom container
- Executing the pipeline with a runtime service account

> Medium article: `https://medium.com/@babul_b/running-a-vertex-ai-custom-container-training-pipeline-with-customtrainingjobop-1b1cca9c840b`

---

## Architecture

```text
Developer code
   |
   v
CI/CD pipeline builds container image
   |
   v
Artifact Registry
   |
   v
Vertex AI Pipeline
   |
   +--> CustomTrainingJobOp: preprocess
   |
   +--> CustomTrainingJobOp: training
   |
   v
Cloud Storage pipeline root and Vertex AI metadata
```

---

## Repository structure

```text
.
├── Dockerfile
├── README.md
├── requirements.txt
├── .gitignore
├── .gitlab-ci.yml
├── src/
│   └── deploy.py
├── pipeline/
│   ├── compile_pipeline.py
│   └── run_pipeline.py
└── docs/
    └── medium-story.md
```

---

## Prerequisites

You need:

- A Google Cloud project
- Vertex AI API enabled
- Artifact Registry repository created
- Cloud Storage bucket for pipeline root
- A service account for Vertex AI pipeline execution
- Permission to act as the runtime service account
- Docker, GitLab CI, GitHub Actions, Cloud Build, or another tool to build and push the image

---

## Configure environment variables

Set these values before compiling or running the pipeline:

```bash
export PROJECT_ID="your-gcp-project-id"
export REGION="northamerica-northeast1"
export BUCKET_URI="gs://your-gcp-project-bucket"
export PIPELINE_ROOT="${BUCKET_URI}/pipeline_root"
export SERVICE_ACCOUNT="your-service-account@your-gcp-project-id.iam.gserviceaccount.com"
export TRAINING_IMAGE_URI="northamerica-northeast1-docker.pkg.dev/your-gcp-project-id/your-repo/vertex-ai-traincontainer:latest"
```

---

## Build the container locally

```bash
docker build -t vertex-ai-traincontainer:latest .
```

Run it locally:

```bash
docker run --rm -e MY_CUSTOM_VAR="LOCAL TEST" vertex-ai-traincontainer:latest deploy.py
```

Expected output:

```text
hello_world
LOCAL TEST
```

---

## Push the image to Artifact Registry

```bash
gcloud auth configure-docker northamerica-northeast1-docker.pkg.dev

docker tag vertex-ai-traincontainer:latest \
  northamerica-northeast1-docker.pkg.dev/your-gcp-project-id/your-repo/vertex-ai-traincontainer:latest

docker push \
  northamerica-northeast1-docker.pkg.dev/your-gcp-project-id/your-repo/vertex-ai-traincontainer:latest
```

---

## Install Python dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Compile the pipeline

```bash
python pipeline/compile_pipeline.py
```

This creates:

```text
custom_train_pipeline.json
```

---

## Run the pipeline

```bash
python pipeline/run_pipeline.py
```

The pipeline will run two steps:

1. `preprocess`
2. `training`

The `training` step runs after the `preprocess` step completes.

---

## Important security note

Do not commit real project IDs, service account keys, secrets, tokens, internal IPs, customer names, or company-specific information into a public repository.

Use placeholders in sample code and use environment variables or a secret manager for real values.

---

## License

This sample is provided for learning purposes. Add your preferred license before publishing publicly.
