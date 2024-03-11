from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# def home_view(request: HttpResponse):
#     return HttpResponse(f'''
#         <h1 style='color: blue;'>Hello, {request.user.email}!</h1>
#     ''')

def index_view(request: HttpResponse):
    return HttpResponse(render(request, 'index.html', {}))
