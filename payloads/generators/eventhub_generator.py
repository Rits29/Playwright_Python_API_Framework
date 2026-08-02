from payloads.models.eventhub_model import Register, NewEvent

class EventHubModelFactory:
    """Responsible for generating test data for EventHub API Testing."""

    @staticmethod
    def generate_register():
        """Return a new register user payload as dictionary"""
        return Register.generate()
    
    
    @staticmethod
    def generate_new_event():
        """Return new event payload"""
        return NewEvent.generate()