from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse("Hello")
    #return render(request, 'home.html', {'hi':'This is me'})

    return render(request, 'home.html')

# def eggs(reqeust):
#     return HttpResponse("<h1>Eggs are great!</h1>")

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    #make empty dictionary
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    # return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':worddictionary.items()})
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    # name = 'Garam'
    # nationality = 'South Korea'
    # age = 27

    myinfo = {'name':'Garam', 'age':27, 'nationality':'S Korea'}
    return render(request, 'about.html', {'myinfo':myinfo})
