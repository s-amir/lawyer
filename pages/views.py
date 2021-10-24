from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'base.html')


def consultation(request):
    context = "شما میتوانید برای دریافت وقت مشاوره با شماره 09122844127 تماس حاصل فرمایید"
    messages.add_message(request, messages.SUCCESS, context)
    return redirect('index')



def cost(request):
    return render(request, 'cost.html')


def about(request):
    return render(request, 'about.html')


def abroad(request):
    return render(request,'abroad.html')