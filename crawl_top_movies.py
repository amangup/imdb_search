import math
import re
import requests

from bs4 import BeautifulSoup

from parse_title_page import parse_title_page


def get_movie_details(num_movies):
    title_ids = _get_title_ids_(num_movies)
    movie_details = _fetch_and_parse_title_pages_(title_ids)

    return movie_details


def _fetch_and_parse_title_pages_(title_ids):
    movie_details = []
    for title in title_ids:
        url = "https://www.imdb.com/title/" + title

        http_response = requests.get(url)
        if http_response.ok:
            movie_details.append(parse_title_page(http_response.text))
    return movie_details


def _get_title_ids_(num_movies):
    movies_per_page = 50
    title_ids = set()
    num_pages = math.ceil(num_movies / movies_per_page)
    for i in range(num_pages):
        start_id = i * movies_per_page + 1
        url = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating&view=simple&start=" + str(start_id)

        http_response = requests.get(url)
        if http_response.ok:
            soup = BeautifulSoup(http_response.text, 'html.parser')

            for tag in soup.find_all('a', href=re.compile("title")):
                href_parts = re.split('\W', tag["href"])
                if href_parts[1] == 'title':
                    title_ids.add(href_parts[2])
    return title_ids


if __name__ == '__main__':
    movies = get_movie_details(50)
    print([movie['title'] for movie in movies])
