from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required




def index(request):
   return HttpResponse("ALL GOOD")
