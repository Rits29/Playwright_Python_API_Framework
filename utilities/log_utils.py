import copy
import json
import xml.etree.ElementTree as ET


class LogUtils:
    """
    Utility class for formatting and masking request/response
    payloads before logging.
    """

    SENSITIVE_KEYS = {
        "token",
        "access_token",
        "refresh_token",
        "authorization",
        "password",
        "client_secret",
        "api_key"
    }

    @classmethod
    def mask_sensitive_data(cls, data):
        """
        Recursively mask sensitive values in JSON payloads.
        """

        if isinstance(data, dict):

            masked = copy.deepcopy(data)

            for key, value in masked.items():

                if key.lower() in cls.SENSITIVE_KEYS:
                    masked[key] = "********"
                else:
                    masked[key] = cls.mask_sensitive_data(value)

            return masked

        elif isinstance(data, list):

            return [
                cls.mask_sensitive_data(item)
                for item in data
            ]

        return data

    @classmethod
    def mask_xml(cls, xml_string):
        """
        Mask sensitive XML elements.
        """

        try:

            root = ET.fromstring(xml_string)

            for element in root.iter():

                tag = element.tag.split("}")[-1].lower()

                if tag in cls.SENSITIVE_KEYS:
                    element.text = "********"

            return ET.tostring(
                root,
                encoding="unicode"
            )

        except Exception:
            return xml_string

    @staticmethod
    def pretty_json(data):

        return json.dumps(
            data,
            indent=30
        )

    @classmethod
    def format_payload(cls, payload):
        """
        Formats JSON or XML payload for logging.
        """

        if isinstance(payload, dict):

            payload = cls.mask_sensitive_data(payload)

            return cls.pretty_json(payload)

        elif isinstance(payload, str):

            payload = payload.strip()

            if payload.startswith("<"):
                return cls.mask_xml(payload)

            return payload

        return str(payload)

    @classmethod
    def format_response(cls, response):
        """
        Automatically formats REST/GraphQL/SOAP responses.
        """

        try:

            response_json = response.json()

            response_json = cls.mask_sensitive_data(
                response_json
            )

            return cls.pretty_json(response_json)

        except Exception:

            return cls.mask_xml(
                response.text()
            )