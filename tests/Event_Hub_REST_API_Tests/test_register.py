from api_clients.eventhub_api_client import EventHubAPIClients
from utilities.api_validation import APIValidation
from payloads.models.eventhub_model import RegisterResponse
validate = APIValidation()

class TestRegisterNewUser:
    test_name = "Test case to register a new user using the EventHub API."
    
    def test_register_new_user(self, apicontext, env):
        validate.testname_log(self.test_name)
        # Create an instance of the EventHubAPIClients
        eventhub_client = EventHubAPIClients(env)
        # Send a POST request to register a new user
        #response, register_payload = eventhub_client.post_eventhub_register_request(apicontext)
        reg_response, reg_payload = eventhub_client.post_eventhub_register_request(apicontext)

        # Validations
        validate.validate_status_code(reg_response, 201, "Register New User")
        response_json = reg_response.json()
        validate.validate_response_schema(response_json, RegisterResponse, "Register New User")
        validate.validate_keys_present(response_json, ['success', "token", 'user'])
        validate.validate_keys_present(response_json['user'], ['id', 'email'])
        #token = response_json.get("token")
        #logger.info(f"Token received: {token}")

    
        
       