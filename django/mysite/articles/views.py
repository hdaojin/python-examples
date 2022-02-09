from django.shortcuts import render, get_object_or_404

import markdown
from .models import ArticlePost

# Create your views here.


def article_detail(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    with open(article.content.path, 'r', encoding='utf-8') as f:
        text = f.read()
    article_md = markdown.Markdown(output_format='html5', extensions=[
                            'extra',
                            'toc',
                            'codehilite',
                            'nl2br',
                            'meta'
                            ])
    article_content = article_md.convert(text)    
    context = {'article_content': article_content, 'article': article, 'toc': article_md.toc}    
    return render(request, 'articles/detail.html', context)