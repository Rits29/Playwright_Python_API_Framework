from payloads.models.base_payload_model import BasePayloadModel
from pydantic import BaseModel, Field
from payloads.randomdatagenerator import RandomDataGenerator

generator = RandomDataGenerator()

class Register(BasePayloadModel):
    email: str = Field(..., min_length=1, max_length=100)
    password: str = Field(..., min_length=1, max_length=20)

    @classmethod
    def generate(cls):
        """Generating Email & Password for login."""
        str_ran = generator.generate_random_string(10)
        return cls(
            email = f"{str_ran}@abcmail.com",
            password = f"{str_ran}123#" 
        )
    
class NewEvent(BasePayloadModel):
        """Generating Event details to create a new event."""
        title: str = Field(..., min_length=1, max_length=100)
        description: str = Field(..., min_length=1, max_length=200)
        category: str = Field(..., min_length=1, max_length=100)
        venue: str = Field(..., min_length=1, max_length=100)
        city: str = Field(..., min_length=1, max_length=100)
        eventDate: str = Field(..., min_length=1, max_length=100)
        price: int = Field(..., gt=0)
        totalSeats: int = Field(..., gt=0)
        imageUrl: str = Field(..., min_length=1, max_length=100)
        
        @classmethod
        def generate(cls):
            return cls(
                title = generator.generate_random_alphanumeric(),
                description = generator.generate_random_string(),
                category = generator.generate_random_event(),
                venue = generator.generate_random_venue(),
                city = generator.generate_random_city(),
                eventDate = generator.generate_random_date(),
                price = generator.generate_random_integer(),
                totalSeats = generator.generate_random_integer(),
                imageUrl = generator.generate_random_url()
            )     

class UserInfo(BasePayloadModel):
    id: int
    email: str

class RegisterResponse(BasePayloadModel):
    success: bool
    user: UserInfo
     
class LoginResponse(BasePayloadModel):
    success: bool
    token: str
    user: UserInfo

class CreateNewEventResponse(BasePayloadModel):
    success: bool
    data: NewEvent
    message: str
