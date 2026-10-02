from dataclasses import dataclass

MAX_TITLE_LENGTH = 200
MAX_AUTHOR_NAME = 100

@dataclass
class Book:
    id: int = 0
    title: str = ""
    author: str = ""
    read: bool = False

    def __post_init__(self):
        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")
        
        if not isinstance(self.author, str):
            raise ValueError("Author must be a string")
        
        self.title = self.title.strip()
        self.author = self.author.strip()

        if not self.title :
            raise ValueError("Title can not be Empty")
        if not self.author : 
            raise ValueError("Author can not be Empty")

        if len(self.title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title must be at most {MAX_TITLE_LENGTH} characters")
        
        if len(self.author) > MAX_AUTHOR_NAME:
            raise ValueError(f"Author must be at most {MAX_AUTHOR_NAME} characters")

    def mark_read(self):
        self.read = True

    def mark_unread(self):
        self.read = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "read": self.read,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        for key in ["id", "title", "author", "read"]:
            if key not in data:
                raise ValueError(f"Missing key: {key}")
        return cls(
            id = data["id"],
            title = data["title"],
            author = data["author"],
            read = bool(data.get("read", False)),
        )
        

  