import wikipedia

# print(wikipedia.search("Barack"))
# print(wikipedia.summary("Github"))

search_title = input("Enter a search phrase or title of  the wikipedia page you want a summary for: ")
while search_title != "":
    try:
        details = wikipedia.page(search_title)
        print("Title: {}\nURL: {}\nSummary: {}".format(details.title,details.url,details.summary))
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)
    search_title = input("Enter a search phrase or title of  the wikipedia page you want a summary for: ")