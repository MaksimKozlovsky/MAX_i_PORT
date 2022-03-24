from dotenv import load_dotenv
load_dotenv()
from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
from django.http import HttpResponse
import os
import requests
from .models import Pages, Comment
from .forms import CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django import views
from django.core.paginator import Paginator
User = get_user_model()


def news(request):
    if request.method == 'GET':
        page_id = request.GET.get('id')
        if page_id:
            page = Pages.objects.get(pk=request.GET.get('id'))
            context = {'page': page}
        else:
            pages = Pages.objects.all().order_by('-created')
            paginator = Paginator(pages, 2)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {'pages': pages,
                       'page_obj': page_obj}
    else:
        pages = Pages.objects.all().order_by('-created')
        context = {'pages': pages}
    return render(request, 'news.html', context=context)


def comment_page(request, page):
    comments = page.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
#        if not request.user.is_authenticated():
#            return HttpResponse('Зарегистрируйтесь')
#            comments = Comment.objects.filter(active=True)
            comment = comment_form.cleaned_data.get(commit=False)
            comment.page = page
            comment.save()
            context = {'comment': comment,
                       'comments': comments,
                       'comment_form': comment_form,
                       'page': page}

    else:
        comment_form = CommentForm()
        context = {'comment_form': comment_form}
    return render(request, 'news.html', context=context)


