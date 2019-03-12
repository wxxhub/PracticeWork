from django.shortcuts import render


class Article:
    def __init__(self):
        self.title = 'hello'
        self.date = '2019-3-12'
        self.text = '从沪深港通南北资金流向看，截至发稿，南向资金净流入6.69亿元，其中沪港通净流入3.6亿元，当日资金余额为416.4亿元，深港通净流入3.09亿元，当日资金余额为416.91亿元。'


class Person:
    def __init__(self):
        self.name = 'Lucy'
        self.sex = 'girl'


def home(request):
    nav = ['军事', '科技', '汽车', '体育']
    article = Article()
    bob = Person()

    context = {
        'nav': nav,
        'article': article,
        'person': bob
    }
    return render(request, 'article.html', context)
