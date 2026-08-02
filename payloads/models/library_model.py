from pydantic import Field
from payloads.models.base_payload_model import BasePayloadModel
from payloads.randomdatagenerator import RandomDataGenerator

generator = RandomDataGenerator()


class AddBook(BasePayloadModel):
    """Pydantic model for creating a new book"""
    name: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., min_length=1, max_length=20)
    aisle: int = Field(..., gt=0)
    author: str = Field(..., min_length=1, max_length=100)

    @classmethod
    def generate(cls):
        """Generate random valid book data"""
        return cls(
            name=generator.generate_random_string(),
            isbn=generator.generate_random_alphanumeric(),
            aisle=generator.generate_random_integer(100, 999),
            author=generator.generate_random_string()
        )

class DeleteBook(BasePayloadModel):
    """Model for book deletion"""
    ID: str = Field(..., min_length=1)

"""Response JSON into Pydantic model. """

class AddBookResponse(BasePayloadModel):
    Msg: str
    ID: str

class DeleteBookResponse(BasePayloadModel):
    msg: str

