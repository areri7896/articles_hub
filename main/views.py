from django.shortcuts import render, get_object_or_404
from .models import Article
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView) 
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import Http404

from django_daraja.mpesa.core import MpesaClient
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# from .query import query_stk_status
from .models import MPesaTransaction
from decouple import config

from rest_framework.views import APIView
from .models import MPesaTransaction

from decouple import config
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from datetime import datetime


from . import forms
# Create your views here.
def home(request):
    art_list = Article.objects.all()
    paginator = Paginator(art_list, 6)
    page_number = request.GET.get('page', 1)
    # arts = paginator.page(page_number)
    try:
        arts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, deliver the first page
        arts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range, deliver the last page of results
        arts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'arts': arts})

def post(request, id):
    # posts = article.objects.get(id=id)
    try:
        post = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404("No Article found.")
    return render (request, 'about.html', {'post': post})

def login(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('home')

class BlogUpdateView(UpdateView):
    model = Article
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'status']
    # success_url = reverse_lazy('h') 



class BlogDeleteView(DeleteView): # new
    model = Article
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    message = 'deleted successfully'

class BlogCreateView(CreateView):
    model = Article
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body', 'document', ]

@login_required
def mpay(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')  # Get the phone number from the POST request
        amount = request.POST.get('amount')  # Get the amount from the POST request

        cl = MpesaClient()
        account_reference = 'lasio'
        transaction_desc = 'Pay'
        callback_url = 'https://api.darajambili.com/express-payment'

            # Call the Mpesa API for payment (STK Push)
        response = cl.stk_push(phone_number,int(amount), account_reference, transaction_desc, callback_url)

            # Display a success message to the user
        messages.success(request, f"Payment of {amount} has been initiated. Please check your phone!")
        return render(request, 'payment_successful.html', {'amount': amount, 'desc': account_reference})
        # return HttpResponse(f"Payment of {amount} has been initiated. Please check your phone!")

    else:
        # If it's a GET request, simply display the payment form
        return render(request, 'payment.html')
    

def receipt(request):

    return render (request, 'receipt.html', {})



class HandleCallBackView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Assuming request.data contains the M-Pesa callback data
        mpesa_post_data = request.data
      
        
        try:
            # Extract necessary fields
            result_code = mpesa_post_data['Body']['stkCallback']['ResultCode']
        
            if result_code == 0:

                checkout_request_id = mpesa_post_data['Body']['stkCallback']['CheckoutRequestID']
                callback_metadata = mpesa_post_data['Body']['stkCallback']['CallbackMetadata']['Item']

                # Extract individual items from CallbackMetadata
                mpesa_receipt_number = next((item['Value'] for item in callback_metadata if item['Name'] == 'MpesaReceiptNumber'), None)
                transaction_date = next((item['Value'] for item in callback_metadata if item['Name'] == 'TransactionDate'), None)


                transaction = MPesaTransaction.objects.filter(transaction_id=checkout_request_id).first()

                if transaction:
                    transaction.transaction_date  = datetime.strptime(str(transaction_date), "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
                    transaction.status = 'Success'
                    transaction.mpesa_receipt_number  = mpesa_receipt_number 
                    transaction.save()

                    return Response({"message": "Callback processed successfully"}, status=status.HTTP_200_OK)
            
            if result_code != 0:
                checkout_request_id = mpesa_post_data['Body']['stkCallback']['CheckoutRequestID']
                transaction = MPesaTransaction.objects.filter(transaction_id=checkout_request_id).first()
                if transaction:
                    transaction.status = 'Failed'
                    transaction.save()
                
            return Response({"message": "Callback process failed!"}, status=status.HTTP_400_BAD_REQUEST)
        
        except KeyError as e:
            return Response({"error": "Invalid callback data"}, status=status.HTTP_400_BAD_REQUEST)
        



class PaymentStatusView(APIView):

    def get(self, request, transaction_id):
        transaction = MPesaTransaction.objects.filter(transaction_id=transaction_id).first()
        
        if not transaction:
            return Response({"status": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Return the current status of the transaction
        return Response({"status": transaction.status}, status=status.HTTP_200_OK)