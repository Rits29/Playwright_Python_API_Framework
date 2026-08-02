from urllib.parse import urljoin

from api_clients.base_api_client import BaseAPIClient
from payloads.generators.soap_generator import SoapPayloadFactory


class SOAPAPIClient(BaseAPIClient):

    def __init__(self, env):
        super().__init__("Soap", env)
        self.soap_endpoint = "/axis2/services/Version.VersionHttpSoap11Endpoint/"

    def post_get_version_request(self, context, tracking_id=None):
        """
        Sends SOAP request to get service version.
        """

        endpoint = urljoin(self.base_url, self.soap_endpoint)

        payload = (SoapPayloadFactory.generate_get_version(tracking_id).serialize())

        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": "urn:getVersion"
        }

        response = self.post_request(
            context=context,
            url=endpoint,
            payload=payload,
            headers=headers,
            api_name="SOAP_Get_Version"
        )

        return response