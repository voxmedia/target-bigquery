import logging
import os

from scalesec_gcp_workload_identity.main import TokenService
import boto3
import time

logger = logging.getLogger(__name__)

def getToken(gcp_project_number, gcp_workload_id, gcp_workload_provider, gcp_service_account_email,
             aws_account_id, aws_role_name, aws_region, gcp_token_lifetime, gcp_token_scopes):
    logger.info("Started Getting Token, params are:\n"
                "gcp_project_number: " + gcp_project_number +", gcp_workload_id: " + gcp_workload_id + ", gcp_workload_provider: "
                + gcp_workload_provider + ", gcp_service_account_email: " + gcp_service_account_email + ", aws_account_id: "
                + aws_account_id + ", aws_role_name: " + aws_role_name + ", aws_region: " + aws_region + ", gcp_token_lifetime: "
                + gcp_token_lifetime + ", gcp_token_scopes: " + gcp_token_scopes)
    attempts = 6
    while True:
      try:
        client = boto3.client('sts')
        identity = client.get_caller_identity()
        logger.info(f"Using caller identity: {identity}\n")
        break
      except:
        attempts = attempts - 1
        if attempts <= 0:
          raise
        else:
          logger.info("AWS Credentials are not yet available. Trying again in a few seconds...")
          time.sleep(10)

    token_service = TokenService(
        gcp_project_number=gcp_project_number,
        gcp_workload_id=gcp_workload_id,
        gcp_workload_provider=gcp_workload_provider,
        gcp_service_account_email=gcp_service_account_email,
        aws_account_id=aws_account_id,
        aws_role_name=aws_role_name,
        aws_region=aws_region,
        gcp_token_lifetime=gcp_token_lifetime,
        gcp_token_scopes=gcp_token_scopes,
    )

    sa_token, expiry_date = token_service.get_token()
    os.environ['GCP_AUTH_TOKEN'] = sa_token
    os.environ['GCP_AUTH_TOKEN_EXPIRY_DATE'] = expiry_date
