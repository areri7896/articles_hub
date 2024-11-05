import json
from django.http import JsonResponse
from .models import Trans 

def process_stk_callback(request):
    stk_callback_response = json.loads(request.body)
    log_file = "Mpesastkresponse.json"
    with open(log_file, "a") as log:
        json.dump(stk_callback_response, log)
    
    merchant_request_id = stk_callback_response['Body']['stkCallback']['MerchantRequestID']
    checkout_request_id = stk_callback_response['Body']['stkCallback']['CheckoutRequestID']
    result_code = stk_callback_response['Body']['stkCallback']['ResultCode']
    result_desc = stk_callback_response['Body']['stkCallback']['ResultDesc']
    amount = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
    transaction_id = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
    user_pone_number = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

    if result_code == 0:
        data = Trans(merchant_request_id, checkout_request_id, result_code, result_desc, amount, transaction_id, user_pone_number)
        data.save

        response = daraja.send_stk_push(url=stk_push_url)
        response_code = response.get('ResponseCode')
       
        # Success
        if response_code == '0':
            # Update transaction with the CheckoutRequestID if present
            transaction_id = response.get("CheckoutRequestID")
            transaction.transaction_id = transaction_id
            transaction.save()

            return Response(response, status=status.HTTP_200_OK)
        
    return Response(response, status=status.HTTP_400_BAD_REQUEST)