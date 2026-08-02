from utilities.custom_logger import LogGen
from pydantic import BaseModel, ValidationError
from typing import Type
import xml.etree.ElementTree as ET
logger = LogGen.loggen()

class APIValidation:
   
    @staticmethod
    def testname_log(test_name: str =""):
        logger.info(f"Test Case Name is: {test_name}\n")
        

    @staticmethod
    def validate_status_code(response, expected_code: int, test_name: str= ""):
        status_code = response.status
        logger.info(f"""{test_name}: Validating status code. || Expected: {expected_code} | Actual: {status_code}\n""")
        assert status_code == expected_code, \
            f"""{test_name}: Status code mismatch. || Expected {expected_code} | Actual: {status_code}."""

    @staticmethod
    def validate_response_schema(response_json, model: Type[BaseModel], test_name: str=""):
        try:
            model.model_validate(response_json)
            logger.info(f"[{test_name}] Schema validation passed using model: {model.__name__}")
        except ValidationError as e:
            logger.error(f"[{test_name}] Schema validation failed:\n{e}")
            raise AssertionError(f"Response schema validation failed:\n{e}")
                                 
                            
    @staticmethod
    def validate_keys_present(response_json, keys: list, test_name: str=""):
        try:
            json_data = response_json
            for key in keys:
                assert key in json_data, f"{test_name}: Missing key: {key}"
                logger.info(f" {test_name}: Key '{key}' found in response")
        except Exception as e:
            raise AssertionError(f"{test_name}: Missing keys in response.")

    @staticmethod
    def validate_success_message(response, expected_msg, test_name: str=""):
        try:
            json_data = response
            actual_msg = json_data.get("message") or json_data.get("Msg") or json_data.get("msg")
            logger.info(f"""{test_name}: Validating message. || Expected: {expected_msg} | Actual: {actual_msg}""")
            assert actual_msg == expected_msg, f"""{test_name}: Message mismatch. || Expected {expected_msg} | Received: {actual_msg}"""
        except Exception as e:
            raise AssertionError(f"{test_name}: Message mismatch: {str(e)}")

    @staticmethod
    def log_request_response(response, payload=None, test_name: str=""):
        #logger.info(f"{test_name}: Request Payload: {payload}")
        #logger.info(f"{test_name}: Response Status: {response.status}")
        try:
            logger.info(f"{test_name}: Response Body: {response.json()}")
        except:
            logger.info(f"{test_name}: Response Body: {response.text()}")

    @staticmethod
    def validate_compare_value(val1, val2, test_name: str=""):
        try:
            val1 = val1
            val2 = val2
            logger.info(f"{test_name}: Compare values for {val1} & {val2}.")
            assert val1 == val2, f"""{test_name}: Available seats in response do not match the expected total seats value.
                                        Expected: Available seats == Total seats
                                        Got: Value Mismatched. """
        except Exception as e:
            raise AssertionError(f"{test_name}: Value mismatched: {str(e)}")
        
    #Soap Validation
    @staticmethod
    def validate_xml_value(xml_response: str, xpath: str, namespaces: dict, expected_value=None, test_name=""):
        root = ET.fromstring(xml_response)
        element = root.find(xpath, namespaces)
        assert element is not None, f"{test_name}: XML element '{xpath}' not found."
        assert element.text is not None, f"{test_name}: XML value is empty."
        if expected_value is not None:
            assert element.text == expected_value, f"{test_name}: Expected '{expected_value}', Got '{element.text}'."
        logger.info(f"{test_name}: XML value = {element.text}")
        
    
    @staticmethod
    def validate_xml_tag(xml_response: str, xpath: str, namespaces: dict, test_name: str = ""):
        root = ET.fromstring(xml_response)
        element = root.find(xpath, namespaces)
        assert element is not None, f"{test_name}: XML element '{xpath}' not found."
        logger.info(f"{test_name}: XML tag '{xpath}' found.")
        
