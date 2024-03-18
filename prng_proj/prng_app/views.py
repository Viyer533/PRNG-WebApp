from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import os
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
            
            result = PRNS_GENERATOR.generate({"img": image_path, "n": number1, "m": number2})[:number1] 
            result = PRNS_GENERATOR.optimize(result)
            return render(request, "index.html", {"img": image_path, "seqLen": number1, "mVal":2**number2 - 1, "result": result})
        else:
            return render(request, "index.html")
