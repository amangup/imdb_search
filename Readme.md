# IMDB Crawl and search

## To run
See `search.py`'s main function. 

## Code components

### parse_title_page

Uses the html string and returns a `dict` containing movie details


### crawl_top_movies

Given a number `N` of movies, it will return a `list` containing movie details for the top `N` movies. `N <= 1000`

### create_index

Given a `list` containing movie details it creates a `dict` which maps search keyword to the set of movies which match that keyword.

### search

This uses the index to search and allows for multiple keywords in the search term. The final results are an intersection of the results for each keyword.

## Assumptions
- The parsing of page can be done in many ways, where some can be more robust to HTML changes. Currently implemented parsing is strongly tied to current HTML structure, and hence easy to break.

- Crawling typically needs to be more aware of rules that it needs to follow and the frequency with which it can hit the servers. The current crawler doesn't do those.
  - It also assumes that pattern in which movie lists are displayed at IMDB, i.e., 50 movies per page.

- Word vocabulary and number of movies in index is small - keeps index design straightforward. 

## Improvements

- A better search algorithm will take union over results over multiple keywords and use intelligent scoring (like prioritizing title match over description match).

- One use case for movie search is to search for an exact movie that one has forgotten the details about. For this, past search history can be used to created a dataset that is usable for supervised learning.

- Parsing the page can be made more robust - for e.g., if we can find what text is in the biggest fontsize, we can assume that is the title. It may require a more browser-rendering like approach.

- We would want all movies to be part of that list, and we may a want a different trade-off between memory usage and search speed.

- Language based optimization - like english words can have many forms and making sure words like `historical` and `history` match each other.