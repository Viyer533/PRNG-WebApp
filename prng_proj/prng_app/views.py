from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import os
from math import log2, ceil
from prng_ecga import PRNS_GENERATOR


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {'result' : []})

    def post(self, request, *args, **kwargs):
        print("Hello")
        if request.method == "POST" and request.FILES["imageUpload"]:
            print("Hello! Upload")

            image_file = request.FILES["imageUpload"]
            print(type(image_file))
            image_path = os.getcwd() + "/assets/" + image_file.name

            with open(image_path, "wb") as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            number1 = int(request.POST.get("number1"))
            number2 = int(request.POST.get("number2"))
            number_of_digits = number2
            number2 = int(log2((10 ** number_of_digits)))
            result = PRNS_GENERATOR.generate({"img": image_path, "n": number1, "m": number2})[:number1] 
            result = PRNS_GENERATOR.optimize(result)
            padded_result = ['0' * (number_of_digits - len(str(number))) +  str(number) for number in result]
            return render(request, "index.html", {"seqLen": number1, "result": padded_result})
        else:
            return render(request, "index.html")
