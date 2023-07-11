from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    newsApi = NewsApiClient(api_key="46edf4898dcd4960891324c8f1d0bd99")
    headLines = newsApi.get_top_headlines(sources='cbs-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(desc, img, news)
    return render(request, 'index.html', context={"mylist": mylist})




# Create your views here.
