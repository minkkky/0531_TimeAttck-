from django.shortcuts import render


# Create your views here.
def new_view(request):
    return render(request, 'new.html')


def article_view(request):
    return render(request, 'article.html')

def category_view(request):
    return render(request, 'category.html')

def datail_view(request):
    return render(request, 'datail.html')