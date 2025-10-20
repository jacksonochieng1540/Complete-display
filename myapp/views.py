from django.http import JsonResponse
from django.shortcuts import render
from .models import Visitor
import os

def home(request):
    # Track visitors
    visitor, created = Visitor.objects.get_or_create(
        ip_address=request.META.get('REMOTE_ADDR', 'unknown')
    )
    visitor.visit_count += 1
    visitor.save()
    
    context = {
        'message': 'Welcome to Django Docker App!',
        'total_visitors': Visitor.objects.count(),
        'your_visits': visitor.visit_count,
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'container_id': os.environ.get('HOSTNAME', 'unknown')
    }
    return render(request, 'home.html', context)

def health_check(request):
    return JsonResponse({'status': 'healthy', 'service': 'django-app'})