from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error
from datetime import datetime


class Connector:
    ## -------------------- Конструктор класса Connector --------------------------##
    def __init__(self, filename='config.ini', section='mysql'):
        parser = ConfigParser()
        parser.read(filename)

        self.db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                self.db[item[0]] = item[1]
        else:
            raise Exception('{0} not found in the {1}'.format(section, filename))

    ## -------------------- Метод внесения информции в базу -----------------------##
    def add_information(self, title, text, author, date, bunch_of_comments=None):
        query_to_article = "INSERT INTO article(title, text, author, date) VALUES(%s, %s, %s, %s)"
        id_article = 0
        args = (title, text, author, date)
        try:
            conn = MySQLConnection(**self.db)
            cursor = conn.cursor()
            cursor.execute(query_to_article, args)

            id_article = cursor.lastrowid
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

        # for comments
        if bunch_of_comments is not None:
            try:
                conn = MySQLConnection(**self.db)

                for comment in bunch_of_comments.get_comments():
                    query_to_comments = "INSERT INTO comment(title, text, author, date, article_id) VALUES(%s, %s, %s, %s, %s)"
                    args = (
                    comment.get_title(), comment.get_text(), comment.get_author(), comment.get_date(), id_article)
                    cursor = conn.cursor()
                    cursor.execute(query_to_comments, args)

                    conn.commit()

            except Error as error:
                print(error)
            finally:
                cursor.close()
                conn.close()
        return id_article

    ## -------------------- Метод удаления информции из базы -----------------------##
    def delete_information(self, article_id):
        # At first I wnat to do it for comments
        delete_query_for_comments = "DELETE FROM comment where article_id = %s"
        delete_query_for_article  = "DELETE FROM article where id = %s"

        try:
            conn = MySQLConnection(**self.db)

            cursor = conn.cursor()
            cursor.execute(delete_query_for_comments, (article_id,))
            cursor.execute(delete_query_for_article, (article_id,))
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def get_comments(self, article_id):
        try:
            conn = MySQLConnection(**self.db)

            query = "SELECT * FROM comment WHERE article_id=%s"

            cursor = conn.cursor()
            cursor.execute(query, (article_id,))

            list_of_comments = list()

            row_comment = cursor.fetchone()
            if row_comment is None:
                return None

            while row_comment is not None:
                list_of_comments.append(row_comment)
                row_comment = cursor.fetchone()
            return list_of_comments

        except Error as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

    ## -------------------- Метод получения информции из базы -----------------------##
    def get_information(self, title):
        article_dict = dict()
        try:
            conn = MySQLConnection(**self.db)

            query = "SELECT * FROM article WHERE title=%s"

            cursor = conn.cursor()
            cursor.execute(query, (title,))

            article_row = cursor.fetchone()
            if article_row is not None:
                article_dict['article'] = article_row
                article_dict['comment'] = self.get_comments(article_row[0])
            return article_dict
        except Error as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

    ## --------------------- Метод обновления информции в базе ------------------------##
    def update_information(self, article_id, title, text, author, date, bunch_of_comments=None):
        self.delete_information(article_id);
        new_id = self.add_information(title=title, text=text, author=author,
                                      date=date, bunch_of_comments=bunch_of_comments)
        return new_id


