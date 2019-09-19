import re

from crawl_top_movies import get_movie_details
from create_index import create_index


def search(terms, index):
    term_words = re.split('\W', terms)
    results = []
    for word in term_words:
        if word:
            results.append(index.get(word.lower(), set()))

    return set.intersection(*results)


if __name__ == '__main__':
    print("Crawling...")
    movie_details = get_movie_details(100)

    print("Creating index...")
    index = create_index(movie_details)

    print(search('tarantino samuel', index))