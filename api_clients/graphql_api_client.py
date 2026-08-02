from urllib.parse import urljoin
from api_clients.base_api_client import BaseAPIClient
from payloads.generators.graphql_generator import GraphQLPayloadFactory


class GraphQLAPIClient(BaseAPIClient):

    def __init__(self, env):
        super().__init__("Graphql", env)
        self.graphql_endpoint = "/gq/graphql"

    def post_create_new_location_request(self, context):
        """
        Creates a new location using GraphQL mutation.
        """

        endpoint = urljoin(self.base_url, self.graphql_endpoint)

        payload = (GraphQLPayloadFactory.generate_create_location().serialize())
 
        response = self.post_request(
            context=context,
            url=endpoint,
            payload=payload,
            api_name="GraphQL_Create_New_Location"
        )

        return response