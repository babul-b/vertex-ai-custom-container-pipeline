"""Compile a Vertex AI Pipeline using CustomTrainingJobOp.

Before running this script, export:

PROJECT_ID
REGION
BUCKET_URI
PIPELINE_ROOT
TRAINING_IMAGE_URI
"""

import os
from kfp import compiler, dsl
from google_cloud_pipeline_components.v1.custom_job import CustomTrainingJobOp

PROJECT_ID = os.environ.get("PROJECT_ID", "your-gcp-project-id")
REGION = os.environ.get("REGION", "northamerica-northeast1")
BUCKET_URI = os.environ.get("BUCKET_URI", "gs://your-gcp-project-bucket")
PIPELINE_ROOT = os.environ.get("PIPELINE_ROOT", f"{BUCKET_URI}/pipeline_root")
TRAINING_IMAGE_URI = os.environ.get(
    "TRAINING_IMAGE_URI",
    "northamerica-northeast1-docker.pkg.dev/your-gcp-project-id/your-repo/vertex-ai-traincontainer:latest",
)


@dsl.pipeline(name="custom-container-training-pipeline", pipeline_root=PIPELINE_ROOT)
def custom_training_pipeline(
    project: str = PROJECT_ID,
    gcp_region: str = REGION,
    training_image_uri: str = TRAINING_IMAGE_URI,
):
    """Two-step custom container training pipeline."""

    preprocess = CustomTrainingJobOp(
        display_name="preprocess",
        project=project,
        location=gcp_region,
        worker_pool_specs=[
            {
                "containerSpec": {
                    "imageUri": training_image_uri,
                    "args": ["deploy.py"],
                    "env": [
                        {
                            "name": "MY_CUSTOM_VAR",
                            "value": "PREPROCESSING THE DATA",
                        }
                    ],
                },
                "replicaCount": "1",
                "machineSpec": {
                    "machineType": "n1-standard-4",
                },
            }
        ],
    )

    CustomTrainingJobOp(
        display_name="training",
        project=project,
        location=gcp_region,
        worker_pool_specs=[
            {
                "containerSpec": {
                    "imageUri": training_image_uri,
                    "args": ["deploy.py"],
                    "env": [
                        {
                            "name": "MY_CUSTOM_VAR",
                            "value": "TRAINING THE MODEL",
                        }
                    ],
                },
                "replicaCount": "1",
                "machineSpec": {
                    "machineType": "n1-standard-4",
                },
            }
        ],
    ).after(preprocess)


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=custom_training_pipeline,
        package_path="custom_train_pipeline.json",
    )
    print("Pipeline compiled to custom_train_pipeline.json")
