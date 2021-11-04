from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=8a2536a41045b294e84f1ea31afc4d2f&countries=in')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description,image, url)
    return render(request, 'index.html',{'news':news} )