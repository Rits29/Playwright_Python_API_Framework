from api_clients.base_api_client import BaseAPIClient
from utilities.read_properties import ReadConfig
from payloads.generators.library_generator import LibraryModelFactory
from urllib.parse import urljoin
from payloads.models.library_model import AddBookResponse, DeleteBookResponse


class LibraryAPIClients(BaseAPIClient):
    """A class to manage API clients for different services."""
    

    def __init__(self, env):
        super().__init__("Library", env)
        self.post_endpoint = "Library/Addbook.php"
        self.get_authorName_endpoint = "Library/GetBook.php"
        self.post_delete_endpoint = "Library/DeleteBook.php"
        

    def post_library_request(self, context):
        # This method sends the POST request to add a book using the library API.
        library_post_url = urljoin(self.base_url, self.post_endpoint)
        response = self.post_request(context, library_post_url, LibraryModelFactory.generate_book().serialize(), "Add Book")
        return response
    
    def delete_library_request(self, context, book_id):
        if not book_id:
            raise ValueError("book_id must be provided to delete a book")
        delete_url = urljoin(self.base_url, self.post_delete_endpoint)
        library_delete_url = f"{delete_url}?ID={book_id}"
        delete_payload = LibraryModelFactory.generate_delete_book(book_id).serialize()
        response = self.post_request(context, library_delete_url, delete_payload, "Delete Book")
        return response