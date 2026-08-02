from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
import json
import time
from utilities.log_utils import LogUtils

class BaseAPIClient:

    def __init__(self, app_name, env):
        self.base_url = ReadConfig.get_base_url(app_name, env)
        self.logger = LogGen.loggen()  # Initialize the logger for the BaseAPIClient class

    def post_request(self, context, url, payload, api_name, headers=None):
        """Generic POST request method supporting REST, GraphQL and SOAP."""

        start = time.perf_counter()

        response = context.post(url, data=payload, headers=headers)

        duration = (time.perf_counter() - start) * 1000

        payload_log = LogUtils.format_payload(payload)

        response_log = LogUtils.format_response(response)
            # ---------------- Logging ---------------- #

        self.logger.info(
            f"""
=========================================================================================
            API Name      :  {api_name}
            HTTP Method   :  POST
            URL           :  {url}
            Payload       :  {payload_log}
            Status Code   :  {response.status}
            Response      :  {response_log}
            Response Time :  {duration:.2f} ms
            """
        )
        return response
    
    def get_request(self, context, url):
        """Send a GET request to the specified URL."""
        self.logger.info(f"Sending GET request to {url}")
        response = context.get(url)
        return response
    
    def delete_request(self, context, url, payload, api_name):
        """Send a DELETE request to the specified URL with the given payload."""
        self.logger.info("Sending DELETE request to %s\n using payload: \n%s", url,json.dumps(payload, indent =4))
        response = context.delete(url, data=payload)
        return response
    
    def patch_request(self, context, url, payload):
        """Send a PATCH request to the specified URL with the given payload."""
        self.logger.info("Sending PATCH request to %s\n using payload: \n%s", url,json.dumps(payload, indent =4))
        response = context.patch(url, data=payload)
        return response