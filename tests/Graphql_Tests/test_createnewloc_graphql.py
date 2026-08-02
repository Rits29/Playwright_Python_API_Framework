from api_clients.graphql_api_client import GraphQLAPIClient
from utilities.api_validation import APIValidation

"""Test case to create a new location using the Graphql API."""
validate = APIValidation()

class TestCreateNewLocation:
    def test_create_new_location(self, apicontext, env):   
        test_name = "Graphql Test case: test_create_new_location"
        validate.testname_log(test_name)
    # Create an instance of the GraphqlAPIClients
        graphql_client = GraphQLAPIClient(env)
    # Send a POST request to create a new location
        response = graphql_client.post_create_new_location_request(apicontext)
        response_json = response.json()
        validate.validate_status_code(response, 200, "Create a new location")
        assert "errors" not in response_json, f"Response JSON contains errors: {response_json['errors']}"
        # Assert that the response contains the expected ID.
        location_id = response_json["data"]["createLocation"]
        validate.validate_keys_present(response_json, ['data'], "Create new location")
        validate.validate_keys_present(location_id, ['id'], 'Create new location')
        assert location_id is not None
       