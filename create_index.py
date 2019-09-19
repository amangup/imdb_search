import re

from crawl_top_movies import get_movie_details


def create_index(movie_details):
    index = {}
    for movie in movie_details:
        for value in movie.values():
            words = re.split('\W', value)
            for word in words:
                if word:
                    lowercase_word = word.lower()
                    mapped_movies = index.get(lowercase_word, set())
                    mapped_movies.add(movie['title'])
                    if len(mapped_movies) == 1:
                        index[lowercase_word] = mapped_movies

    return index


if __name__ == '__main__':
    print("Crawling...")
    movie_details = get_movie_details(1)

    print("Creating index...")
    index = create_index(movie_details)

    print(index['hanks'])