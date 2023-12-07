from django.shortcuts import render, redirect
from .models import Property, Category
from django.http import Http404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from datetime import datetime, timedelta
from django.contrib import messages
from .forms import OrderForm


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


def reservation(request, property_id):
    property = Property.objects.get(id=property_id)
    event_data = []
    all_reservations = Order.objects.filter(property_object=property)

    for reservation in all_reservations:
        current_date = reservation.date_from
        end_date = reservation.date_to + timedelta(days=1)

        while current_date < end_date:
            event = {
                'start': current_date.strftime('%Y-%m-%d'),
                'end': current_date.strftime('%Y-%m-%d'),
                'classNames': 'in-between'  # Default class for days in between
            }
            if current_date == reservation.date_from:
                event['classNames'] = 'starting-day'
            if current_date == end_date - timedelta(days=1):
                event['classNames'] = 'finishing-day'

            event_data.append(event)
            current_date += timedelta(days=1)

    # Combine events for the same day
    combined_event_data = {}
    for event in event_data:
        date = event['start']
        if date in combined_event_data:
            combined_event_data[date]['classNames'] = 'in-between'
        else:
            combined_event_data[date] = event

    context = {
        'event_data': list(combined_event_data.values()),
        'property': property,
    }

    return render(request, 'reservation.html', context)


def checkout(request, property_id):
    property = Property.objects.get(id=property_id)
    current_date = datetime.now()
    dates = request.GET.get('dates')
    print(property_id)

    if not dates:
        messages.error(request, 'Vyberte si termín.')
        return redirect('reservation', property_id=property_id)

    dates = dates.split(',')
    selected_dates_by_user = []
    reserved_dates = []

    if len(dates) == 1:
        start_date = datetime.strptime(dates[0], '%Y-%m-%d')
        end_date = datetime.strptime(dates[0], '%Y-%m-%d')
    else:
        start_date = datetime.strptime(dates[0], '%Y-%m-%d')
        end_date = datetime.strptime(dates[-1], '%Y-%m-%d')
        if end_date < start_date:
            start_date = datetime.strptime(dates[1], '%Y-%m-%d')
            end_date = datetime.strptime(dates[0], '%Y-%m-%d')

    while start_date <= end_date:
        selected_dates_by_user.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)

    if len(selected_dates_by_user) <3:
        messages.error(request, 'Vyberte si minimálne 2 noci.')
        return redirect('reservation', property_id=property_id)

    # Retrieve all reservations from the database
    reservations = Order.objects.all()

    # Iterate through reservations to extract reserved dates
    # last day of reservation can be reserved again
    for reservation in reservations:
        start_date = reservation.date_from + timedelta(days=1)
        end_date = reservation.date_to - timedelta(days=1)

        # Generate a list of dates within the reservation range
        while start_date <= end_date:
            reserved_dates.append(start_date.strftime('%Y-%m-%d'))
            start_date += timedelta(days=1)

    for date in selected_dates_by_user:
        if date in reserved_dates:
            messages.error(request, 'Váš termín je už obsadený.')
            return redirect('reservation', property_id=property_id)

    nights_count = len(selected_dates_by_user) - 1
    night_text = 'noci' if nights_count < 5 else 'nocí'

    if request.method == 'POST':
        order = Order.objects.create(
            property_object=property,
            name_surname=request.POST.get('name_surname'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date_from=datetime.strptime(selected_dates_by_user[0], '%Y-%m-%d'),
            date_to=datetime.strptime(selected_dates_by_user[-1], '%Y-%m-%d'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            postal=request.POST.get('postal'),
            price=nights_count * property.price
        )
        order_id = order.id
        return redirect('order', order_id=order_id)

    form = OrderForm()

    context = {
        'first_date': datetime.strptime(selected_dates_by_user[0], '%Y-%m-%d').strftime('%d.%m.%Y'),
        'last_date': datetime.strptime(selected_dates_by_user[-1], '%Y-%m-%d').strftime('%d.%m.%Y'),
        'nights': nights_count,
        'night_text': night_text,
        'form': form,
        'property': property,
    }

    return render(request, 'checkout.html', context)


def order(request, order_id):
    order_details = Order.objects.get(id=order_id)

    context = {
        'order': order_details,
    }

    return render(request, 'order.html', context)


def end(request):
    # Add your logic for handling the checkout page
    return render(request, 'end.html')
