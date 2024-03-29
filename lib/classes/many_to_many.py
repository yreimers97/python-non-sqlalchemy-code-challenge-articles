import ipdb

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        pass

    # @property
    # def title(self):
    #     return self._title
    
    # @title.setter
    # def title(self, title_parameter):
    #     print(title_parameter)

class Author:
    def __init__(self, name):
        self.name = name
        pass

    # @property
    # def author_name(self):
    #     return self._name
    
    # @author_name.setter
    # def author(self, author_name_parameter):
    #     if(type(author_name_parameter, str) and len(author_name_parameter) > 0):
    #         self._name = author_name_parameter
    #     else:
    #         print("Author's name must be a string")


    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        pass

    # @property
    # def magazine_name(self):
        
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

ipdb.set_trace()