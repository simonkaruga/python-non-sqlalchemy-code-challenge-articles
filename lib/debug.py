# lib/debug.py
#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Author, Magazine, Article

if __name__ == '__main__':
    print("Debugging Magazine Domain")

    # Example objects
    author1 = Author("Simon")
    author2 = Author("Alice")

    magazine1 = Magazine("TechNow", "Technology")
    magazine2 = Magazine("Vogue", "Fashion")

    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author2, magazine2, "Fashion Trends 2025")
    article3 = author1.add_article(magazine2, "AI in Fashion")

    ipdb.set_trace()
