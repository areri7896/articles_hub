from django.shortcuts import render

# Create your views here.
def payment(request):
    # posts = article.objects.get(id=id)
    # try:
    #     post = Article.objects.get(id=id)
    # except Article.DoesNotExist:
    #     raise Http404("No Article found.")
    return render (request, 'payment.html', {})