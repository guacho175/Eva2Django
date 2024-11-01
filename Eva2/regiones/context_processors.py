# context_processors.py
from django.utils import timezone

def incluir_hora(request):
    current_year = timezone.now().year
    current_time = timezone.now().strftime('%H:%M:%S')
    return {
        'current_year': current_year,
        'current_time': current_time,
    }
    
