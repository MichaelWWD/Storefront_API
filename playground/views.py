from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from rest_framework.views import APIView
import requests


class HelloView(APIView):
    def get(self,request):
        response = requests.get('https://httpbin.org/delay/2')
        data =  response.json()
        return render(request, 'hello.html', {'name': data})


# caching example for class based view
# class HelloView(APIView):
#     @method_decorator(cache_page(5 * 60))
#     def get(self,request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data =  response.json()
#         return render(request, 'hello.html', {'name': data})


# SENDING EMAILS 
 # try:
    #     send_mail('subject', 'message', 'dimejimike9@gmail.com', ['mayodemichaeloladimeji@gmail.com'])
    # except BadHeaderError:
    #     pass
    # try:
    #     message = EmailMessage('subject', 'message', 'dimejimike9@gmail.com', ['mayodemichaeloladimeji@gmail.com'])
    #     message.attach_file('playground/static/images/IMG_8012 copy.jpg')
    #     message.send()
    # except BadHeaderError:
    #     pass

    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/helo.html',
    #         context={'name':'Mike'},
    #         )
    #     message.send(to=['oladimejimichael@outlook.com'])
    # except BadHeaderError:
    #     pass 