import os
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django import views
#import requests
import json
import urllib.request
import datetime
from .forms import City_Form
import math
from django.template import RequestContext
#from dotenv import load_dotenv
#load_dotenv()


def index(request):
    return render(request, 'index.html')
