from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render (request,'home.html',{'shag':'this is me' })

def  count(request):
    fulltext=request.GET['fulltext']
    wordlength=fulltext.split()
    wordlist={}
    for char in wordlength:
        if char in wordlist:
            wordlist[char]+=1
        else:
            wordlist[char]=1
    sortedlist=sorted(wordlist.items(), key=operator.itemgetter(1),reverse=True)
    return render (request,'count.html',{'wordlength':len(wordlength),'fulltext':fulltext,'wordlist':sortedlist})
def about(request):
    return render (request,'about.html')
