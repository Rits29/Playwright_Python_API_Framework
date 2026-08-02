from api_clients.soap_api_client import SOAPAPIClient
from utilities.api_validation import APIValidation

validate = APIValidation()


class TestSOAPVersionService:

    def test_get_version(self, apicontext, env):

        test_name = "SOAP Test Case: Get Version"

        validate.testname_log(test_name)

        soap_client = SOAPAPIClient(env)

        response = soap_client.post_get_version_request(apicontext)

        validate.validate_status_code(response, 200, test_name)

        validate.log_request_response(response, test_name=test_name)

        namespaces = {
            "soap": "http://schemas.xmlsoap.org/soap/envelope/",
            "ns": "http://axisversion.sample"
        }

        validate.validate_xml_tag(response.text(), ".//ns:getVersionResponse/ns:return", namespaces, test_name)

       