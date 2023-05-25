import readline
from bs4 import BeautifulSoup
import requests

try:
    source=requests.get("https://www.imdb.com/chart/top/")
    status=source.raise_for_status()
    #print(status)

    soup=BeautifulSoup(source.text,'html.parser')
    #print(soup)

    movies=soup.find('tbody',class_="lister-list").findAll('tr')
    #print(movies)

    f=open("IMDB.txt",'a')

    for movie in movies:
        movierank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        #print(movierank)

        movieName = movie.find('td', class_="titleColumn").a.text
        #print(movieName)

        movieYear = movie.find('td', class_="titleColumn").span.text.strip('()')
        #print(movieYear)

        movieRating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        #print(movieRating)

        print("RANK : ",movierank," MOVIE NAME : ",movieName," MOVIE YEAR : ",movieYear," MOVIE RATING",movieRating)

        f.write(movierank)
        f.write(" ")

        f.write(movieName)
        f.write(" ")

        f.write(movieYear)
        f.write(" ")

        f.write(movieRating)
        f.write(" ")
        f.write("\n")

    f.flush()
    f.close()

except Exception as e :
    print(e)