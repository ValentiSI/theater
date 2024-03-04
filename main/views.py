from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# def home_view(request: HttpResponse):
#     return HttpResponse(f'''
#         <h1 style='color: blue;'>Hello, {request.user.email}!</h1>
#     ''')

def index_view(request: HttpResponse):
    return HttpResponse(render(request, 'products.html', {}))

   
def time_view(request: HttpResponse):
    return HttpResponse(f'<h3>{datetime.now().strftime("%A")}  {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</h3>')

def script_view(request: HttpResponse):
    return HttpResponse(f'''
        <script>
            alert('Hello, {request.user.email}!');
        </script> <a href="http://127.0.0.1:8000/time/">Time now</a>
    ''')
