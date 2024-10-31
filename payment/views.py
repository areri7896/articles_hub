from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
# def payment(request):
#     # posts = article.objects.get(id=id)
#     # try:
#     #     post = Article.objects.get(id=id)
#     # except Article.DoesNotExist:
#     #     raise Http404("No Article found.")
#     return render (request, 'payment.html', {})

def receipt(request):

    return render (request, 'receipt.html', {})

# def mpay(request):
#     cl = MpesaClient()
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
#     phone_number = '0797795884'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://api.darajambili.com/express-payment'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)



def mpay(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')  # Get the phone number from the POST request
        amount = request.POST.get('amount')  # Get the amount from the POST request

        if not phone_number or not amount:
            messages.error(request, 'Phone number and amount are required.')
            return render(request, 'payment.html')  # Ensure this template exists

        try:
            # Initialize MpesaClient and initiate the STK Push
            cl = MpesaClient()
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'

            # Call the Mpesa API for payment (STK Push)
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

            # Display a success message to the user
            messages.success(request, f"Payment of {amount} has been initiated. Please check your phone!")
            return HttpResponse(f"Payment Response: {response}")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'payment.html')  # Return to the form in case of error
    else:
        # If it's a GET request, simply display the payment form
        return render(request, 'payment.html')


@login_required

# def payment(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             phone_number = request.POST.get('phone')  # Get phone number from POST data
#             amount = request.POST.get('amount')  # Get amount from POST data
            
#             if phone_number and amount:  # Check if both phone and amount are provided
#                 try:
#                     # Initiate the payment via MpesaClient
#                     payment = MpesaClient()
#                     account_reference = 'reference'
#                     transaction_desc = 'Description'
#                     callback_url = 'https://api.darajambili.com/express-payment'

#                     # Call Mpesa API for payment (STK Push)
#                     response = payment.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

#                     # Save the transaction in the database
#                     data = Transaction(phone=phone_number, amount=int(amount))  # Convert amount to integer
#                     data.save()

#                     # Show success message to the user
#                     messages.success(request, f"Congratulations! Your payment of {amount} has been successfully made!")
#                     return HttpResponse(f"Payment Response: {response}")  # Return response from Mpesa

#                 except Exception as e:
#                     # Handle any exceptions (like payment failure)
#                     messages.error(request, f"An error occurred during payment: {str(e)}")
#                     return render(request, 'payment.html')  # No form, returning template with error message

#             else:
#                 # Handle missing data error
#                 messages.error(request, 'Please provide both phone number and amount.')
#                 return render(request, 'payment.html')  # Re-render the template with error message

#         return render(request, 'payment.html')  # For GET requests, simply render the template

#     else:
#         # If user is not authenticated, show error message
#         messages.error(request, 'You must be logged in to complete the action!')
#         return redirect('login')  # Redirect to the login page or wherever you handle authentication

# def pay(request):
#     if request.method == 'POST':
#         paymt = MpesaClient()
#         account_reference = 'reference'
#         phone_number = request.POST.get('phone')
#         amount_str = request.POST.get('amount')

#         try:
#             amount = int(amount_str)
#         except ValueError:
#             messages.error(request, "Invalid amount. Please enter a valid integer.")
#             return render(request, 'payment.html')

#         transaction_desc = 'Description'
#         callback_url = 'https://api.darajambili.com/express-payment'

#         response = paymt.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#         HttpResponse(response, 'index.html')
#         data = Transaction(phone=phone_number, amount=amount)
#         data.save()
#         messages.success(request, f"Congratulations! Your payment of {{ amount }} has been successfully made!")
#         return redirect("index.html")
#     return render(request, 'payment.html')