from datetime import datetime
import copy

class Bunch_of_comments():
    def __init__(self, *list_of_comments):
        self.list_of_comments = []
        for comm in list_of_comments:
            self.list_of_comments.append(comm)

    # Добавить комментарии
    def add_comments(self, *list_of_comments):
        for comm in list_of_comments:
            self.list_of_comments.append(comm)

    # Получение количества коментариев
    def get_comments_count(self):
        return len(self.list_of_comments)

    # Получение списка комментарив
    def get_comments(self):
        return copy.deepcopy(self.list_of_comments)

    # Удаление комментария по объекту
    def delete(self, comment):
        if self.list_of_comments.__contains__(comment):
            self.list_of_comments.remove(comment)

    # Удаление комментария по заголовку
    def delete(self, title):
        for comment in self.list_of_comments:
            if title == comment.get_title():
                self.list_of_comments.remove(comment)
                return
        print('there is no such comment to delete')

    # Получение комментария по заголовку
    def get_comment(self, title):
        for comment in self.list_of_comments:
            if title == comment.get_title():
                return copy.deepcopy(comment)
        print('there is no such comment to get')
