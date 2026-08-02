from payloads.models.soap_model import GetVersionRequest


class SoapPayloadFactory:

    @staticmethod
    def generate_get_version(tracking_id=None):

        return GetVersionRequest.generate(tracking_id)