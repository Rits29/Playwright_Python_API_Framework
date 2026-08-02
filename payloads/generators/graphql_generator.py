from payloads.models.graphql_model import GraphQLRequest


class GraphQLPayloadFactory:

    @staticmethod
    def generate_create_location():
        return GraphQLRequest.generate()