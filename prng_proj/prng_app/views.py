from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import os
from prng_ecga import PRNS_GENERATOR

class HomePage(View) :

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


    def post(self, request, *args, **kwargs):

        print('Hello')
        if request.method == 'POST' and request.FILES['imageUpload']:
            print("Hello! Upload")

            image_file = request.FILES['imageUpload']
            print(type(image_file))
            image_path = os.getcwd() + "/assets/"+image_file.name
            
            with open(image_path, 'wb') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            number1 = request.POST.get('number1')
            number2 = request.POST.get('number2')
            number3 = request.POST.get('number3')
            number4 = request.POST.get('number4')

            print(PRNS_GENERATOR.generate({'img' : image_path}))

            # Process the form data (e.g., save the image, perform calculations with numbers, etc.)
            
            return HttpResponse("Form submitted successfully.")
        else:
            return render(request, 'index.html')