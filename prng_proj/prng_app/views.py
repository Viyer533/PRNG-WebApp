from django.shortcuts import render
from django.http import HttpResponse
import os
from prng_ecga import PRNS_GENERATOR
# Create your views here.
def home_view(request):
    print(PRNS_GENERATOR.generate())
    return render(request, 'index.html')


def process_form(request):
    if request.method == 'POST' and request.FILES['imageUpload']:
        print("Hello! Upload")

        #intialize the save path for uploaded and segmented files
        init_save_path = "Images"
        
        # Save the uploaded file
        image_file = request.FILES['imageUpload']
        print(type(image_file))
        # image_path = init_save_path+"/assets/"+image_file.name
        
        # print("Uploaded Image file: ",image_file)
        # print("Uploaded Image path: ",image_path)
        
        # # Perform segmentation using main.py
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        number3 = request.POST.get('number3')
        number4 = request.POST.get('number4')
        

        # Process the form data (e.g., save the image, perform calculations with numbers, etc.)
        
        return HttpResponse("Form submitted successfully.")
    else:
        return render(request, 'index.html')