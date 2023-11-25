from django.shortcuts import render
from .models import Property, Category
def homepage (request):
    categories = Category.objects.all()


    return render(request, 'homepage.html',{'categories': categories})

from django.http import Http404

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


