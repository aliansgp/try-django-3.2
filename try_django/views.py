"""
to render HTML web pages
"""
from django.http import HttpResponse
from article.models import Article
import random
from django.template.loader import render_to_string


def home(request):
    """
    take in a request:
    returns HTML as response
    """

    random_id = random.randint(1,3)
    data_Article = Article.objects.get(id=random_id)

    #working with html variables and merge them
    Description= """
    <h3>working with template as variables and merge them:</h3>
    """
    title =f"""
    <h1>{data_Article.title} (id : {data_Article.id})</h1>
    """
    content = f"""
    <p>{data_Article.content}</p>
    """
    HTML_STRING =  Description + title + content

    #working with template as dictionary
    contex = {
        "title" : data_Article.title,
        "id": data_Article.id,
        "content": data_Article.content
    }
    HTML_DIC = """
    <h3>working with template as dictionary:</h3>
    <h1>{title} (id : {id})</h1>
    <p>{content}</p>
    """.format(**contex)

    #working with templates as HTML file:
    HTML_FILE = render_to_string("home-view.html",context=contex)
    
    HTML_RES = HTML_STRING + HTML_DIC + HTML_FILE
    return HttpResponse(HTML_RES)
