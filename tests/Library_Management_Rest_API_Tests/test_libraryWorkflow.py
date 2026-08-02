from api_clients.library_api_client import LibraryAPIClients
from tests.conftest import env
from utilities.api_validation import APIValidation
from payloads.models.library_model import AddBookResponse, DeleteBookResponse

validate = APIValidation()

class Test_Library_Workflow():
  
    test_name = "Library_Book_Management_Workflow_Add and Delete"


    def test_libraryworkflow(self, apicontext, env): 
        validate.testname_log(self.test_name)
        ''' Send a POST request to add the book & parse the response.'''
        lab = LibraryAPIClients(env)
        response = lab.post_library_request(apicontext)
        validate.validate_status_code(response, 200, "Add a Book")
        post_response = response.json()
        validate.validate_response_schema(post_response, AddBookResponse, "Add a Book")
        validate.validate_success_message(post_response, "successfully added", "Add a Book")
        validate.validate_keys_present(post_response, ["Msg", "ID"], "Add a Book")
        
        '''Send a DELETE request to delete the book, please note the website is sending the post for delete request,
        so we are using post method here. '''
        # Delete the same book using the returned ID.
        Book_id =post_response["ID"]
        response = lab.delete_library_request(apicontext, Book_id)
        validate.validate_status_code(response, 200, "Delete a Book")
        del_response = response.json()
        validate.validate_response_schema(del_response, DeleteBookResponse, "Delete a Book")
        validate.validate_success_message(del_response, "book is successfully deleted", "Delete a Book")
        