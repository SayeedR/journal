from django.shortcuts import render,redirect

from .models import Paper
from django.contrib import messages



     

def Submitted_Papers(request):
    if request.method == "POST":
        
        
    
        
        file1=request.FILES["file"]
        document = Paper.objects.create(files=file1)
        
        

        document.save()
       
        messages.info(request,'Paper Submitted succesfully')
       

    return render(request, 'upload.html')   

    
    