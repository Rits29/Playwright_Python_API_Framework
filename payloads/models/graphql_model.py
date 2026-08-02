from typing import Any, Dict, Optional
from pydantic import Field
from payloads.models.base_payload_model import BasePayloadModel
from payloads.randomdatagenerator import RandomDataGenerator


class GraphQLRequest(BasePayloadModel):
    """
    GraphQL payload for Create Location mutation.
    """

    query: str = Field(..., min_length=1)
    variables: Dict[str, Any]
    operationName: Optional[str] = None

    @classmethod
    def generate(cls):

        mutation = """
        mutation CreateLocation(
            $name: String!,
            $type: String!,
            $dimension: String!
        ) {
            createLocation(
                location: {
                    name: $name
                    type: $type
                    dimension: $dimension
                }
            ) {
                id
            }
        }
        """

        return cls(
            operationName="CreateLocation",
            query=mutation,
            variables={
                "name": RandomDataGenerator.generate_random_string(10),
                "type": RandomDataGenerator.generate_random_string(10),
                "dimension": RandomDataGenerator.generate_random_string(10)
            }
        )