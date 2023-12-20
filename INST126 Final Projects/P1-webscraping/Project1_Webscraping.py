# 6.1, 6.2, 6.5: This documentation is also in the form of a README
# The program extracts information from a table in Wikipedia. The Wikipedia website I used is about a list of the highest grossing films.
# The program lists the name of these films in ascending order. 
# A Wikipedia link is inserted in the program. It requests all the information in HTML format. In order to make it look more organized, 
# we use a loop that selects specifically the names of the films in ascending order from each row from the Wikipedia table 
# and remove any text that is written in HTML format. 

# 6.7, 6.8: A LICENSE was attached to the github repository. 

from bs4 import BeautifulSoup
import requests

#################################################################
# Scraping an HTML table
movies_page = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")
movies_soup = BeautifulSoup(movies_page.content, "html.parser")
movies_table = movies_soup.find("table")
print(movies_table)

# This loop allows the program to select all the rows from the table. 
# But it only keeps the name of the movies as they are listed in the table. +
for title in movies_table.find_all("tbody"):
    rows = title.find_all("tr")
    for row in rows:
        movie_name = row.find("th").text.strip()
        print(movie_name)


# 10.1, 10.2, 10.3 Webscraping Advanced Topic: This program satifies by scraping a page

