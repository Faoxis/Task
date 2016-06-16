from datetime import datetime
import copy

class Comment():
    def __init__(self, title=None, text=None, author=None, date = datetime.now()):
        self.title = title
        self.text = text
        self.author = author
        self.date = date

    def get_text(self):
        return copy.deepcopy(self.text)

    def set_text(self, text):
        self.text = text

    def get_title(self):
        return copy.deepcopy(self.title)

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return copy.deepcopy(self.author)

    def set_author(self, author):
        self.author = author

    def set_date(self, date = datetime.now()):
        self.date = date

    def get_date(self):
        return copy.deepcopy(self.date)