from django.shortcuts import render, redirect
from django.http import JsonResponse
from .tasks import run_scrapy_task
from django.views.decorators.csrf import csrf_exempt
from .models import ScrapedProducts
from django.core.paginator import Paginator

# Create your views here.


@csrf_exempt
def scrape_view(request):
    task = run_scrapy_task.delay()
    return render(request, 'processing.html')

def home_view(request):
    return render(request, 'scrap.html')

@csrf_exempt
def products_view(request):
    products = ScrapedProducts.objects.all()
    paginator = Paginator(products, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product_list.html', {'page_obj': page_obj})

def clear_db(request):
    if request.method == 'POST' and 'clear_db' in request.POST:
        ScrapedProducts.objects.all().delete()
        return redirect(products_view)
    


