"""Run the compiled Vertex AI Pipeline.

Before running this script, export:

PROJECT_ID
REGION
BUCKET_URI
PIPELINE_ROOT
SERVICE_ACCOUNT
"""

import os
from datetime import datetime
from google.cloud import aiplatform

PROJECT_ID = os.environ.get("PROJECT_ID", "your-gcp-project-id")
REGION = os.environ.get("REGION", "northamerica-northeast1")
BUCKET_URI = os.environ.get("BUCKET_URI", "gs://your-gcp-project-bucket")
PIPELINE_ROOT = os.environ.get("PIPELINE_ROOT", f"{BUCKET_URI}/pipeline_root")
SERVICE_ACCOUNT = os.environ.get(
    "SERVICE_ACCOUNT",
    "your-service-account@your-gcp-project-id.iam.gserviceaccount.com",
)


def main() -> None:
    """Submit the pipeline job to Vertex AI."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    aiplatform.init(
        project=PROJECT_ID,
        location=REGION,
        staging_bucket=BUCKET_URI,
    )

    pipeline_job = aiplatform.PipelineJob(
        display_name="custom-train-pipeline",
        template_path="custom_train_pipeline.json",
        job_id=f"custom-train-pipeline-{timestamp}",
        enable_caching=False,
        pipeline_root=PIPELINE_ROOT,
    )

    pipeline_job.run(
        service_account=SERVICE_ACCOUNT,
        sync=True,
    )


if __name__ == "__main__":
    main()
