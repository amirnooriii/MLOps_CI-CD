import logging
import os
import sys
from google.cloud import aiplatform

# Configure logging to output to both console and a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Output to console
        logging.FileHandler('deploy.log')   # Output to a file
    ]
)
logger = logging.getLogger(__name__)


REGION = "us-central1"

try:
    logger.info("Initializing Vertex AI client...")
    aiplatform.init(project={PROJECT_ID}, location=REGION, staging_bucket=f"gs://{BUCKET_NAME}")

    logger.info("Uploading model...")
    model = aiplatform.Model.upload(
        display_name="trained-model",
        artifact_uri=f"gs://{BUCKET_NAME}/model/",
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-5:latest"
    )
    logger.info(f"Model uploaded successfully: {model.resource_name}")

    logger.info("Creating endpoint...")
    endpoint = aiplatform.Endpoint.create(display_name="endpoint")
    logger.info(f"Endpoint created: {endpoint.resource_name}")

    logger.info("Deploying model to endpoint...")
    model.deploy(endpoint=endpoint, machine_type="n1-standard-4")
    logger.info("Model deployed successfully")

except Exception as e:
    logger.error(f"Deployment failed: {str(e)}", exc_info=True)
    sys.exit(1)