# Running a Vertex AI Custom Container Training Pipeline with CustomTrainingJobOp

This repository supports a Medium article that explains how to run a simple two-step Vertex AI Pipeline using a custom container and `CustomTrainingJobOp`.

## What this sample does

The pipeline runs two managed Vertex AI custom training jobs:

1. `preprocess`
2. `training`

Both steps use the same container image, but each step receives a different environment variable. This makes it easy to validate that Vertex AI is running the correct step with the correct runtime configuration.

## Why this matters

In production, ML workflows usually need a repeatable process. A team may need to prepare data, train a model, evaluate the model, register it, and deploy it. Vertex AI Pipelines provide a managed way to orchestrate these steps.

This sample starts with a simple container so the basic pattern is easy to understand.

## Medium link

Paste the published Medium story link here:

`https://medium.com/@babul_b/running-a-vertex-ai-custom-container-training-pipeline-with-customtrainingjobop-1b1cca9c840b`
