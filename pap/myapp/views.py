from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Cashflow, Product, AffordabilityPrediction
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cashflow_list(request):
    cashflows = Cashflow.objects.all()
    paginator = Paginator(cashflows, 10) 
    page = request.GET.get('page')

    try:
        cashflows_page = paginator.page(page)
    except PageNotAnInteger:
        cashflows_page = paginator.page(1)
    except EmptyPage:
        cashflows_page = paginator.page(paginator.num_pages)

    if not cashflows:
        logger.warning("No cashflow records found.")
    
    return render(request, 'cashflow_list.html', {'cashflows': cashflows_page})

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  
    page = request.GET.get('page')

    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    if not products:
        logger.warning("No product records found.")
    
    return render(request, 'product_list.html', {'products': products_page})

def affordability_predictions(request):
    predictions = AffordabilityPrediction.objects.all()
    paginator = Paginator(predictions, 10)  
    page = request.GET.get('page')

    try:
        predictions_page = paginator.page(page)
    except PageNotAnInteger:
        predictions_page = paginator.page(1)
    except EmptyPage:
        predictions_page = paginator.page(paginator.num_pages)

    if not predictions:
        logger.warning("No affordability predictions found.")
    
    return render(request, 'affordability_predictions.html', {'predictions': predictions_page})
