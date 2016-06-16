from datetime import datetime
from configuration import Connector
from news import Article, Comment, Bunch_of_comments






if __name__ == '__main__':

    # # # Test 1
    # article = Article.Article()
    # article.register_connector(Connector.Connector())
    #
    # article.get_article_from_base('I love dogs')
    #
    # bunch_of_comments = article.get_bunch_of_comments()
    #
    # print(bunch_of_comments.get_comment('Perfect article').get_date())
    #
    # connector = Connector.Connector()
    # print(connector.get_information('I love dogs'))


    # Test 2
    # Trying to add information about article in datebase
    connector = Connector.Connector()

    comment1 = Comment.Comment(title='Comment 1', text='Comment for testing 1',
                              author='me', date=datetime.now())
    comment2 = Comment.Comment(title='Comment 2', text='Comment for testing 2',
                               author='you', date=datetime.now())
    comment3 = Comment.Comment(title='Comment 3', text='Comment for testing 3',
                               author='we', date=datetime.now())

    bunch_of_comments = Bunch_of_comments.Bunch_of_comments(comment1, comment2, comment3)

    article = Article.Article(title='Article', text='For article testing', author='Article Author',
            date = datetime.now(), bunch_of_comments = bunch_of_comments, connector=connector)

    article.save_in_base()

    # Trying to read that information
    article = Article.Article(connector=Connector.Connector()) # Коннектор нужен обязательно
    article.get_article_from_base(title='Article')

    print('Title: ' + article.get_title())
    print('Text: ' + article.get_text())
    print('Author: ' + article.get_author())
    print('Date: ' + str(article.get_date()))
    print()
    print('Number of comments: ' + str(article.get_bunch_of_comments().get_comments_count()), end='\n\n')

    # Example of reading the first comment
    print('Comment number 1')

    bunch_of_comments = article.get_bunch_of_comments()
    comment1 = bunch_of_comments.get_comment('Comment 1')

    print('Comment title: ' + comment1.get_title())
    print('Comment text: ' + comment1.get_text())
    print('Comment author: ' + comment1.get_author())
    print('Comment date: ' + str(comment1.get_date()), end='\n\n')

    print('Comment number 2')

    print('Comment title: ' + article.get_bunch_of_comments().get_comment('Comment 2').get_title())
    print('Comment text: ' + article.get_bunch_of_comments().get_comment('Comment 2').get_text())
    print('Comment author: ' + article.get_bunch_of_comments().get_comment('Comment 2').get_author())
    print('Comment date: ' + str(article.get_bunch_of_comments().get_comment('Comment 2').get_date()))




