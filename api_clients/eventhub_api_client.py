from api_clients.base_api_client import BaseAPIClient
from payloads.generators.eventhub_generator import EventHubModelFactory
from urllib.parse import urljoin


class EventHubAPIClients(BaseAPIClient):
    def __init__(self, env):
        super().__init__("EventHub", env)
        self.reg_newuser_endpoint = "auth/register"
        self.login_endpoint = "auth/login"
        self.create_event_endpoint = "events"

    def post_eventhub_register_request(self, context):
        """Send a POST request to the EventHub registration endpoint."""
        register_url = urljoin(self.base_url, self.reg_newuser_endpoint)
        register_payload = EventHubModelFactory.generate_register().serialize()
        response = self.post_request(context, register_url, register_payload, "Register_User")
        return response, register_payload

    def post_eventhub_login_request(self, context, login_payload):
        """Send a POST request to the EventHub login endpoint."""
        login_url = urljoin(self.base_url, self.login_endpoint)
        response = self.post_request(context, login_url, login_payload, "Login_User")
        return response

    def post_eventhub_create_event_request(self, context, token):
        """Send a POST request to the EventHub create event endpoint."""
        create_event_url = urljoin(self.base_url, self.create_event_endpoint)
        headers = {"Authorization": f"Bearer {token}"}
        event_payload = EventHubModelFactory.generate_new_event().serialize()
        response = self.post_request(context, create_event_url, event_payload, "Create_Event", headers=headers)
        return response