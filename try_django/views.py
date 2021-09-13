"""
to render HTML web pages
"""
from django.http import HttpResponse
from article.models import Article
import random



def home(request):
    """
    take in a request:
    returns HTML as response
    """
    random_id = random.randint(1,3)
    data_Article = Article.objects.get(id=random_id)
    title =f"""
    <h1>{data_Article.title}</h1>
    """
    content = f"""
    <p>{data_Article.content}</p>
    """
    HTML_STRING = title + content

    return HttpResponse(HTML_STRING)
