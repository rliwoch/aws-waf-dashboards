import os

from requests_aws4auth import AWS4Auth


class ServiceSettings:
    def __init__(self,
                 credentials,
                 account_id=os.environ['ACCOUNT_ID'],
                 region=os.environ['REGION'],
                 host=os.environ['ES_ENDPOINT'],
                 aws_auth=None,
                 service='es'):
        self.dashboards_port = os.environ.get("DASHBOARDS_PORT", "443")
        self.account_id = account_id
        self.region = region
        self.host = host
        self.credentials = credentials
        self.aws_auth = aws_auth
        self.service = service
        self.headers = {
            "Content-Type": "application/json",
            'osd-xsrf': 'true'}
        self.aws_auth = AWS4Auth(
            self.credentials.access_key,
            self.credentials.secret_key,
            self.region,
            self.service,
            session_token=self.credentials.token)
        self.dashboards_api_resource_types = {
            "dashboards": "dashboard",
            "templates": "template",
            "index_patterns": "index-pattern",
            "visualizations": "visualization"
        }

    def source_settings_from_event(self, event):
        self.region = event['ResourceProperties']['Region']
        self.host = event['ResourceProperties']['Host']
        self.account_id = event['ResourceProperties']['AccountID']
        self.aws_auth = AWS4Auth(
            self.credentials.access_key,
            self.credentials.secret_key,
            self.region,
            self.service,
            session_token=self.credentials.token)
