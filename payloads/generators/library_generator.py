from payloads.models.library_model import AddBook, DeleteBook

class LibraryModelFactory:
    """Responsible for generating test data for Library API"""

    @staticmethod
    def generate_book():
        """Return a new book payload as dictionary"""
        return AddBook.generate()

    @staticmethod
    def generate_delete_book(book_id: str):
        """Return delete payload"""
        return DeleteBook(ID=book_id)