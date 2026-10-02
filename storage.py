import json
import os

from book import Book


DATA_FOLDER = "data"
DATA_FILE = "books.json"


class JsonStorage:
    def __init__(self, folder: str = DATA_FOLDER, filename: str = DATA_FILE):
        self.folder = folder
        self.path = os.path.join(folder, filename)
        self._ensure_folder()


    def _ensure_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)


    def load(self) -> list:
        if not os.path.exists(self.path):
            return []

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                raw_data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Invalid json format in storage file.")
        except OSError:
            raise ValueError("Could not read storage file.")

        if not isinstance(raw_data, list):
            raise ValueError("Json data must be a list.")

        books = []
        for item in raw_data:
            books.append(Book.from_dict(item))
        return books


    def save(self, books: list):
        self._ensure_folder()

        data= []
        for book in books:
            data.append(book.to_dict())

        try:
          with open(self.path, "w", encoding="utf-8") as file:
              json.dump(data, file, indent = 4, ensure_ascii = False ) 
        except OSError:
          raise ValueError("Could not save storage file.")