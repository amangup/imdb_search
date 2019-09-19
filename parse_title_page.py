import re
import requests

from bs4 import BeautifulSoup


def parse_title_page(html):
    soup = BeautifulSoup(html, 'html.parser')

    title = _get_title_(soup)
    year = _get_year_(soup)
    genres = _get_genres_(soup)
    summary = _get_summary_(soup)
    director = _get_director_(soup)
    cast_names = _get_cast_(soup)

    movie_details = {
        'title': title,
        'year': year,
        'genres': ' '.join(genres),
        'summary': summary,
        'director': director,
        'cast': ' '.join(cast_names)
    }

    return movie_details


def _get_title_(soup):
    title_tag = soup.find("div", class_="title_wrapper")
    title = title_tag.find_all('h1')[0].contents[0].strip()
    return title


def _get_year_(soup):
    year_tag = soup.find("span", id="titleYear")
    year = year_tag.a.contents[0]
    return year


def _get_genres_(soup):
    subtext_tag = soup.find("div", class_="subtext")
    subtext_a = subtext_tag.find_all('a')
    genres = []
    for a_tag in subtext_a:
        if a_tag.has_attr('title'):
            continue
        genres.append(a_tag.contents[0])
    return genres


def _get_summary_(soup):
    summary_tag = soup.find("div", class_="summary_text")
    summary = ''.join([tag.string for tag in summary_tag.contents]).strip()
    return summary


def _get_director_(soup):
    director_tag = soup.find("h4", class_="inline", string=re.compile("Director"))
    for tag in director_tag.next_siblings:
        if tag.name == 'a':
            director = tag.string
    return director


def _get_cast_(soup):
    cast_list_tag = soup.find("table", class_="cast_list")
    cast_names = []
    for tag in cast_list_tag.find_all('a', href=re.compile("name")):
        if tag.string:
            cast_names.append(tag.string.strip())
    return cast_names


if __name__ == "__main__":
    http_response = requests.get("https://www.imdb.com/title/tt0120815")
    details = parse_title_page(http_response.text)
    print(details)