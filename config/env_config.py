import os
from dotenv import load_dotenv


load_dotenv()


''' gcp '''
# cm360
GCP_CM360_CREDENTIAL_JSON = os.getenv('LOCAL') + os.getenv('GCP_CM360_CREDENTIAL_JSON')
GCP_CM360_CREDENTIAL_DAT = os.getenv('LOCAL') + os.getenv('GCP_CM360_CREDENTIAL_DAT')
