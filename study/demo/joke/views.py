from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    aaa = ['动漫', '欧美大片', '电视剧', 'NBA', '体育', '时尚']
    data = {
        'title': '今日要闻',
        'text': '电动自行车新国标确实自2019年4月15日起实施，但在用超标车辆能否上路行驶，以及能行驶多久，要看当地对于过渡期间管理的具体规定，并没有一刀切的皆不准上路。至于具体过渡期有多久、需要办什么手续、怎么办，还请车主咨询当地交管部门。所以，网传的“4月15日起，违规电动车都不准上路”等消息并不确切，而是多有不实。',
        'nav': aaa,
    }
    return render(request, 'base.html', data)


def talk(request):
    return HttpResponse('Miao Miao ~')
