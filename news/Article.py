from datetime import datetime
from configuration import Connector
from news import Comment, Bunch_of_comments
import copy

class Article():
    def __init__(self, title=None, author=None, text=None, connector=None,
                 date=datetime.now(), bunch_of_comments=None):
        self.title = title
        self.author = author
        self.text = text
        self.date = date
        self.bunch_of_comments = bunch_of_comments
        self.__id_number = 0
        self.connector = connector

    # Геттер работы с полем text
    def get_text(self):
        return copy.deepcopy(self.text)

    # Сеттер для работы с полем text
    def set_text(self, text):
        self.text = text

    # Геттер для работы с полем title
    def get_title(self):
        return copy.deepcopy(self.title)

    # Сеттер для работы с полем title
    def set_title(self, title):
        self.title = title

    # Геттер для работы с полем author
    def get_author(self):
        return copy.deepcopy(self.author)

    # Сеттер для работы с полем author
    def set_author(self):
        return copy.deepcopy(self.author)

    # Сеттер для работы с полем date
    def set_date(self, date=datetime.now()):
        self.date = date

    # Геттер для работы с полем date
    def get_date(self):
        return copy.deepcopy(self.date)

    def get_bunch_of_comments(self):
        return copy.deepcopy(self.bunch_of_comments)

    def register_connector(self, connector):
        self.connector = connector

    def register_bunch_of_comments(self, bunch_of_comments):
        self.bunch_of_comments = bunch_of_comments

    def save_in_base(self):
        if self.connector is None:
            raise SyntaxError("bunch_of_comments or connector is empty")
        self.__id_number = self.connector.add_information(title=self.title, author=self.author, text=self.text,
                                                        date=self.date, bunch_of_comments=self.bunch_of_comments)

    def delete_from_base(self):
        if self.__id_number == 0:
            raise SyntaxError("You can't delete the article which hasn't been added")
        self.connector.delete_information(self.__id_number)

    def get_article_from_base(self, title):
        article_dict = self.connector.get_information(title)
        if len(article_dict) == 0:
            print('There is no such article')
        else:
            self.__id_number = article_dict['article'][0]
            self.title = article_dict['article'][1]
            self.text  = article_dict['article'][2]
            self.author = article_dict['article'][3]
            self.date = article_dict['article'][4]
            if article_dict['comment'] is not None:
                bunch_of_comments = Bunch_of_comments.Bunch_of_comments()
                for comment_list in article_dict['comment']:
                    comment = Comment.Comment(title=comment_list[1],
                                              text=comment_list[2],
                                              author=comment_list[3],
                                              date=comment_list[4])
                    bunch_of_comments.add_comments(comment)
                self.bunch_of_comments = bunch_of_comments
            else:
                self.bunch_of_comments = None



    def update_base(self):
        if self.__id_number == 0:
            raise SyntaxError("You can't update the article which hasn't been added")
        connector.update_information(article_id=self.__id_number, title=self.tite, text=self.text,
                                     author=self.author, bunch_of_comments=self.bunch_of_comments)


if __name__ == '__main__':
    connector = Connector.Connector() # "TypeError: 'module' object is not callable" error... why ?
    article = Article(title='Hello Hello',
                      text='This is text of hello hello',
                      author='mememe',
                      connector=connector)
    article.save_in_base()
