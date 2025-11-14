# lib/classes/many_to_many/magazine.py

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
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        value = value.strip()
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be 2–16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string.")
        value = value.strip()
        if len(value) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                authors.append(author)
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        from .article import Article
        if not Article.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles()))
