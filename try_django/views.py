"""
to render HTML web pages
"""
from django.http import HttpResponse

HTML_STRING="""
<h1>Hello World</h1>
"""

def home(request):
    """
    take in a request:
    returns HTML as response
    """
    return HttpResponse(HTML_STRING)
