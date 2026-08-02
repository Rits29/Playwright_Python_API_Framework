from api_clients.eventhub_api_client import EventHubAPIClients
from utilities.api_validation import APIValidation
from payloads.models.eventhub_model import LoginResponse, CreateNewEventResponse 

"""Test case to perform event management flow using the EventHub API."""

validate = APIValidation()

class TestEventManagementFlow:
    def test_event_management_flow(self, apicontext, env, testuser):
        validate.testname_log("Login & Create a new event.")

        # Create an instance of the EventHubAPIClients
        eventhub_client = EventHubAPIClients(env)
       
        # Step 1: Login with the registered user
        login_response = eventhub_client.post_eventhub_login_request(apicontext, testuser)
        validate.validate_status_code(login_response, 200, "Login Test")
        response_json = login_response.json()
        validate.validate_response_schema(response_json, LoginResponse, "Login_Test")
        validate.validate_keys_present(response_json, ["success", "token", "user"]) 
        token = response_json["token"]

        # Step 2: Create a new event using the token
        create_event_response = eventhub_client.post_eventhub_create_event_request(apicontext, token)
        validate.validate_status_code(create_event_response, 201, "Create a new event.")
        response_json = create_event_response.json()
        validate.validate_response_schema(response_json, CreateNewEventResponse, "Create a new event.")
        validate.validate_keys_present(response_json, ["success", "data", "message"], "Create a new event.")
        validate.validate_success_message(response_json, "Event created successfully", "Create a new event.") #"Unexpected message in Create Event response"
        val1 = response_json['data']['totalSeats']
        val2 = response_json['data']['availableSeats']
        validate.validate_compare_value(val1, val2)
        
       