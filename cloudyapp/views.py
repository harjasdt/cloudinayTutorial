from django.shortcuts import render,redirect
from cloudyapp.models import Photos
import cloudinary 
from cloudinary import uploader
from django.contrib import messages
import os
# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        ima = request.FILES['pic']
        data = Photos.objects.create(
        title = title,
        image = ima,
        cc=ima)
        data.save()
        custommodel= Photos.objects.get(title=title)
        x=str(custommodel.image)
        public_id ='media/'+ x
        cloudinary.uploader.upload(public_id)
        os.remove(public_id)
        messages.info(request, 'Image Uploaded !!')
        
    return render(request,"home.html")

def dekho(request):
    photo = Photos.objects.all
    # adding context 
    ctx = {'photo':photo}
    return render(request,"dekho.html",ctx)

def remove(request,pk):
    custommodel= Photos.objects.get(pk=pk)
    x=str(custommodel.image)
    public_id = x
    uploader.destroy(public_id)

    custommodel.delete()
    
    return redirect('dekho')