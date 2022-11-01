from lib.gcp.cm360 import property


def tracking(service, cm_profile, cm_account, cm_advertiser, creative_list):
    for creative_name in creative_list:
        body = property.creative

        body['accountId'] = cm_account
        body['advertiserId'] = cm_advertiser
        body['type'] = 'TRACKING_TEXT'
        body['name'] = creative_name

        service.creatives().insert(profileId=cm_profile, body=body).execute()


if __name__ == '__main__':
    from app.gcp.connect import service
    from config.env_config import GCP_CM360_CREDENTIAL_DAT, GCP_CM360_CREDENTIAL_JSON
    from auth.gcp import platform_info

    service = service(credential_json=GCP_CM360_CREDENTIAL_JSON, credential_dat=GCP_CM360_CREDENTIAL_DAT,
                      api_name='dfareporting', api_version='v3.5',
                      api_scope='https://www.googleapis.com/auth/dfatrafficking')

    tracking(service=service,
             cm_profile=platform_info.CM360_ARTIENCE_PROFILE_ID,
             cm_account=platform_info.CM360_ARTIENCE_ACCOUNT_ID,
             cm_advertiser=platform_info.CM360_ARTIENCE_ADVERTISER_ID,
             creative_list=['gsmin_api_test1', 'gsmin_api_test2'])
