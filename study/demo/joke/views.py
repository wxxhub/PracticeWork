from django.shortcuts import render

from joke.models import Article, Person

def home(request):
    nav = ['军事', '科技', '汽车', '体育']
    article = Article.objects.get(id=1)
    person = Person.objects.get(id=1)

    context = {
        'nav': nav,
        'article': article,
        'person': person
    }
    return render(request, 'article.html', context)
