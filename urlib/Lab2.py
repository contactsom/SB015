import urllib.request

# https://www.google.com/search?q=best+restaurants+in+bangalore
# https://www.google.com/search?q=best+mall+in+bangalore
# https://www.google.com/search?q=best+place+in+bangalore
# https://www.google.com/search?q=best+hill+in+bangalore


# best restaurants in bangalore
# best mall in bangalore
# best place in bangalore
# best hill in bangalore

googlesearch = [
    'best restaurants in bangalore',
    'best mall in bangalore',
    'best place in bangalore',
    'best hill in bangalore',
    'best place in Delhi'
]

baseurl="https://www.google.com/search?q="
urls = [baseurl + t.replace(" ","+") for t in googlesearch]
#print(urls)

for url in urls:
    print(url)