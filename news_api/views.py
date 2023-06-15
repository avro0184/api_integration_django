from django.shortcuts import render
import requests
API_KEY = '6982ba64f6784ab89184e051c03b62c0'


# Create your views here.
def home(request):
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2023-05-10&sortBy=publishedAt&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {"articles":articles}
    return render(request,"home.html", context)