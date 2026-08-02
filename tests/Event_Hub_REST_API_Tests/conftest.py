
import pytest

from api_clients.eventhub_api_client import EventHubAPIClients

@pytest.fixture(scope="session")
def testuser(apicontext, env):
    eventhub_client = EventHubAPIClients(env)
    response, register_payload = eventhub_client.post_eventhub_register_request(apicontext)
    assert response.status == 201, f"Expected status code 201, but got {response.status}"
    yield register_payload # Yield the register payload for use in tests
    apicontext.dispose()

