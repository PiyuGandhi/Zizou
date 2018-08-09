'''
This file contains all the search functions:-
1. Google Search    Done
2. Wikipedia Search    Done
3. YouTube Video Search

V2- 

1. Twitter hashtag search
2.

'''


def searchGoogle(data):
    data = data[len("google"):]
    speak("Searching google for:- "+ data)
    import webbrowser
    url = "https://www.google.com/search?q={}".format(data) 
    webbrowser.open(url)



def searchWikipedia(data):
    data = data[len("wikipedia"):]
    speak("Searching Wikipedia for:- " + data)
    import wikipedia
    searches = wikipedia.search(data)
    speak("Please say  stop at the article")
    for x in searches:
        speak(x)
        if recordAudio() == "stop":
            speak("Stopping")
            data = x
            break
    speak("Do you want to open the article on the web browser?")
    if recordAudio() == "yes":
        import webbrowser
        article = wikipedia.page(data)
        url = article.url
        print(url)
        webbrowser.open(url)
    else:
        data = wikipedia.summary(data)
        speak("Summary of the article is " + data)
