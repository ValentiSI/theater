from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Ticket

# def home_view(request: HttpResponse):
#     return HttpResponse(f'''
#         <h1 style='color: blue;'>Hello, {request.user.email}!</h1>
#     ''')

def index_view(request: HttpRequest):
    tickets = Ticket.objects.all()
    
    return HttpResponse(render(request, 'index.html', {
        'tickets': tickets
    }))
