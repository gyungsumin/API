import argparse

from googleapiclient import discovery
import httplib2
from oauth2client import client
from oauth2client import file as oauthFile
from oauth2client import tools


def service(credential_json, credential_dat,
            api_name='dfareporting', api_version='v3.5', api_scope='https://www.googleapis.com/auth/dfatrafficking'):

    """
            alert 인증 후 discovery 객체 제공
                                               """

    print('API Name: {}\nAPI Scope: {}\nAPI Version: {}'.format(api_name, api_scope, api_version))

    return _get_auth(api_name=api_name, api_version=api_version, api_scope=api_scope,
                     client_path=credential_json, credential_path=credential_dat)


def _get_auth(api_name: str, api_version: str, api_scope: str, client_path, credential_path):
    """
            google api auth 함수
                                   """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, parents=[tools.argparser])
    flow = client.flow_from_clientsecrets(client_path, scope=[api_scope],
                                          message=tools.message_if_missing(client_path))

    storage = oauthFile.Storage(credential_path)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, parser.parse_args([]))
    http = credentials.authorize(http=httplib2.Http())

    return discovery.build(api_name, api_version, http=http)
