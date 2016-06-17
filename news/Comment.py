from datetime import datetime
import copy

class Comment():
    def __init__(self, title=None, text=None, author=None, date = datetime.now()):
        self.title = title
        self.text = text
        self.author = author
        self.date = date

    # Геттер для поля text
    def get_text(self):
        return copy.deepcopy(self.text)

    # Сеттер для поля text
    def set_text(self, text):
        self.text = text

    # Геттер для поля title
    def get_title(self):
        return copy.deepcopy(self.title)

    # Сеттер для поля title
    def set_title(self, title):
        self.title = title

    # Геттер для поля author
    def get_author(self):
        return copy.deepcopy(self.author)

    # Сеттер для поля author
    def set_author(self, author):
        self.author = author

    # Сеттер для поля date
    def set_date(self, date = datetime.now()):
        self.date = date

    # Геттер для поля date
    def get_date(self):
        return copy.deepcopy(self.date)