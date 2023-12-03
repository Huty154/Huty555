from django.shortcuts import render
from .models import Property, Category
from django.http import Http404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'homepage.html', {'categories': categories})

def rental(request, category=None):
    try:
        category_object = Category.objects.get(name=category)
        properties = Property.objects.filter(category=category_object)

        context = {
            'category': category_object,
            'properties': properties,
        }

        template_name = f'{category}.html'
        return render(request, template_name, context)

    except Category.DoesNotExist:
        raise Http404("Category does not exist")

def reservation(request):
    return render(request, 'reservation.html')

def checkout(request):
    # Add your logic for handling the checkout page
    return render(request, 'checkout.html')

def end(request):
    # Add your logic for handling the checkout page
    return render(request, 'end.html')
@csrf_exempt
def handle_reservation(request):
    if request.method == 'POST':
        # Zde přidáte kód pro zpracování rezervačního požadavku
        # Například získání dat z POST požadavku a uložení do databáze

        # Po zpracování požadavku můžete vrátit JSON odpověď
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
