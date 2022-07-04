from django.shortcuts import render
from newsapi import NewsApiClient



def index(request):
    
    NewsApi=NewsApiClient(api_key='63bd5808cfce4606bce27c2f5af5cf36')
    top=NewsApi.get_top_headlines(sources='the-verge')
    
    latest_news=top['articles']
    desc=[]
    news=[]
    img=[] 
    
    for i in range(len(latest_news)):
        temp_news=latest_news[i]
        news.append(temp_news['title'])
        desc.append(temp_news['description'])
        img.append(temp_news['urlToImage'])
    
    myNews=zip(news, desc,img)
    
    return render(request, 'index.html',context={"mylist":myNews})    

    
    