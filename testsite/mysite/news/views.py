from django.shortcuts import render

#new imports
############################1
from django.http import HttpResponse
############################
###############################21
from .models import News


#new code
############################2
# def index(requests):
#     print(requests)
#     return HttpResponse('Hello World')

# ############################5
# def index(requests):
#     print(dir(requests))
#     return HttpResponse('Hello World')


############################6
# def index(request):
#     return HttpResponse('Hello World')
#
# def test(requests):
#     return HttpResponse('<h1>Тестовая страница</h1>')

############################22 Не работает
# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
#     return HttpResponse(res)
#
# def test(request):
#     return HttpResponse('<h1>Тестовая страница</h1>')

#############################23
# def index(request):
#     news = News.objects.all()
#     return render(request, 'news/index.html', {'news' : news, 'title' : 'Список новостей'})

# #############################25
# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, template_name='news/index.html', context=context)


# #############################26
# def index(request):
#     news = News.objects.order_by('-created_at')
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, template_name='news/index.html', context=context)


#############################30
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)

