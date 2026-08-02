from pydantic import BaseModel


class BasePayloadModel(BaseModel):
    """
    Base model for all request payloads.
    """

    def serialize(self):
        """
        Default serialization for REST/GraphQL payloads.
        """
        return self.model_dump()
    
    