import ipdb

class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
       

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_parameter):
        if(isinstance(title_parameter, str) and (5 <= len(title_parameter) <= 50) and not hasattr(self, 'title')):
            self._title = title_parameter
        else:
            print('Invalid title')

class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str) and (len(name_parameter) > 0) and not hasattr(self, 'name')):
            self._name = name_parameter
        else:
            print('No')

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str) and (len(name_parameter) > 0)):
            self._name = name_parameter
        else:
            print('No')

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_parameter):
        if(isinstance(category_parameter, str) and (2 <= len(category_parameter) <= 16)):
            self._category = category_parameter
        else:
            print('No')
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in Article.all]
        return list(set(authors))
        
    def article_titles(self):
        titles = self.titles
        if not titles:
            return None
        return [article.title for article in self.titles]

    def contributing_authors(self):
        authors = [article['author'] for article in self._articles]
        unique_authors = set(authors)
        return [author for author in unique_authors if authors.count(author) > 2]
