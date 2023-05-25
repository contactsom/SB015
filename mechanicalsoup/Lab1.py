import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://steemit.com/")


articiles=list(browser.get_current_page().find('ul',class_="PostsList__summaries"))[:10]
#print(articiles)

for child in articiles:
    userName=child.find('span',class_="author").text
    #print(userName)

    title=child.h2.text
    #print(title)

    print("USER NAME : ",userName," TITLE OF COMMENT: ",title)