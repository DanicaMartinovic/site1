import os
from django.shortcuts import render
from .models import Proizvod

# Create your views here.
def index(request):
    return render(request, 'prodaja/index.html')


def home(request):
    return render(request, 'prodaja/home.html')

#def shop(request):
   # return render(request, "prodaja/shop.html",{
       # 'proizvodi':Proizvod.objects.all().order_by('id').values()
#})
    
def o_nama(request):
    return render(request, 'prodaja/o_nama.html')  

def kontakt(request):
    return render(request, 'prodaja/kontakt.html')


def search(request):
    q = request.GET['q']
    data = Proizvod.objects.filter(naziv=q).order_by('naziv')
    return render(request, 'prodaja/search.html', {'data':data})




def voce(request):
    return render(request, "prodaja/voce.html",{
        'proizvodi':Proizvod.objects.all().order_by('id')[0:5]
    
})
def povrce(request):
        return render(request, "prodaja/povrce.html",{
       'proizvodi':Proizvod.objects.all().order_by('id')[5:10]
})
        
def shop(request):
    folder_path = 'image/product/'  
    image_filenames = os.listdir(folder_path)
    proizvodi = Proizvod.objects.all()
    list = zip(image_filenames, proizvodi)
    
    context = {
        'list':list
    }
    
    return render(request, 'prodaja/shop.html', context)        

