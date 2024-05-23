from django.shortcuts import render , redirect
from.models import *
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.utils.translation import gettext as _


# Create your views here.

def contact(request):
    if request.method == "POST":
        nameLaboratorTirane_ = request.POST["nameKontactTirana_contact"]
        telTLaboratorirane_ = request.POST["telKontactTirana_contact"]
        emailLaboratorTirane_ = request.POST["emailKontactTirana_contact"]
        messageLaboratorTirane_ = request.POST["messageKontactTirana_contact"]
        
        # Save the form data into the model
        Kontact_Salus_Tirana.objects.create(
            name=nameLaboratorTirane_,
            phone=telLaboratorTirane_,
            email=emailLaboratorTirane_,
            message=messageLaboratorTirane_
        )
        if request.method == "POST":
            nameLaboratorTirane_ = request.POST["nameLaboratoriSalus"]
            telLaboratorTirane_ = request.POST["telLaboratoriSalus"]
            emailLaboratorTirane_ = request.POST["emailLaboratoriSalus"]
            messageLaboratorTirane_ = request.POST["messageLaboratoriSalus"]
        
        # Save the form data into the model
        Kontact_Salus_Laborator(
            name=nameLaboratorTirane_,
            phone=telLaboratorTirane_,
            email=emailLaboratorTirane_,
            message=messageLaboratorTirane_
        ).save()
    
    context = {}
    return render(request, 'contact.html', context)
def home(request):
    if request.method == "POST":
        nameTirane_ = request.POST["nameKontactTirana"]
        telTirane_ = request.POST["telKontactTirana"]
        emailTirane_ = request.POST["emailKontactTirana"]
        messageTirane_ = request.POST["messageKontactTirana"]
        
        # Save the form data into the model
        Kontact_Salus_Tirana.objects.create(
            name=nameTirane_,
            phone=telTirane_,
            email=emailTirane_,
            message=messageTirane_
        )
    prof_mjeket = Mjeket.objects.filter(translations__name__istartswith='Prof.').distinct()

    context = {'prof_mjeket': prof_mjeket}

    
    return render(request, "home.html", context)

def mjeket(request):
    q = request.GET.get('q', '')

    # Filter Mjeket objects based on the translated 'name' field
    mjeket = Mjeket.objects.filter(
        Q(departamenti__translations__name__icontains=q) |  
        Q(translations__name__icontains=q)
    ).distinct()
    
    departamenti = Departamenti.objects.all()
    
    context={"mjeket":mjeket,
             'departamenti':departamenti}
    return render(request,"mjeket.html",context)


def mjeket_detail(request,pk):
    mjeket_detail = Mjeket.objects.get(id=pk)
    context = {"mjeket_detail":mjeket_detail}
    return render(request,"mjeket_detail.html",context)

def specialitet(request):
    specialitet = Specialitet.objects.all()
    
    
    context = {'specialitet': specialitet ,}
    return render(request,"specialitet.html",context)

def specialitet_detail(request,pk):
    specialitet_detail = Specialitet.objects.get(id=pk)
    
    if request.method=="POST":
        fullname_ = request.POST["fullname"]
        tel_ = request.POST["tel"]
        message_ = request.POST["message"]

        # Ruajtja ne Admin Django Administration
        Kontakt_Salus(
          fullname =  fullname_ ,
          number = tel_,
          message = message_ 
        ).save()
    
    context = {"specialitet_detail":specialitet_detail}
    return render(request,"specialitet_detail.html",context)

def checkup(request):
    checkup = CheckUp.objects.all()
    context = {"checkup":checkup}
    return render(request,"checkup.html",context)

def about (request):
    about = About.objects.all()
    foto = Foto.objects.all()
    context = {"about":about,"foto":foto}
    return render (request,"about.html",context)

def klinikaefertilizimit (request):
    klinikaferti = KlinikaFerti.objects.all()
    artikujt_informues_DonnaSalus = artikujtinformuesDonnaSalus.objects.all()
    context = {"klinikaferti":klinikaferti,"artikujt_informues_DonnaSalus":artikujt_informues_DonnaSalus}
    return render (request,"klinikaefertilizimit.html",context)


 
def klinikaferte_detail(request,pk):
    klinikaferte_detail = KlinikaFerti.objects.get(id=pk)
    context = {"klinikaferte_detail":klinikaferte_detail}
    return render (request,"klinikaferte_detail.html",context)


def aemc(request):
    aemc = AeMC.objects.all()
    artikujt_informues_AeMC = artikujtinformuesAeMC.objects.all()
    context = {"aemc":aemc,"artikujt_informues_AeMC":artikujt_informues_AeMC}
    return render (request,'AeMC.html',context)



def kartaeshendetit(request):
    artikuj_informues_KartaInSalus = artikujtinformuesKartaInSalus.objects.all()
    context = {"artikuj_informues_KartaInSalus":artikuj_informues_KartaInSalus}
    return render (request,"kartaeshendetit.html",context)



def artikuj_informues(request):
    q = request.GET.get('q', '')
    artikuj_informues = artikujtinformues.objects.filter(
        
        Q(departamenti__translations__name__icontains=q) |  
        Q(translations__name__icontains=q)
    ).distinct()
    departamenti = Departamenti.objects.all()
    
    context = {"artikuj_informues":artikuj_informues,"departamenti":departamenti}
    return render (request,"artikujtinformues.html",context)

# Artikujt informues detail AeMC
def artikujt_informuesAeMC(request,pk):
    artikujt_informuesAeMC = artikujtinformuesAeMC.objects.get(id=pk)
    context={"artikujt_informuesAeMC":artikujt_informuesAeMC}
    return render (request,"artinfodetail_Aemc.html",context)

# Artikujt informues detail InSalus
def artikujt_informuesInSalus(request,pk):
    artikujt_informuesInSalus = artikujtinformuesKartaInSalus.objects.get(id=pk)
    context = {"artikujt_informuesInSalus":artikujt_informuesInSalus} 
    return render (request,"artinfodetail_InSalus.html",context)

# Artikujt informues detail DonnaSalus
def artikujt_informuesDonnaSalus(request,pk):
    artikujt_informuesDonnaSalus = artikujtinformuesDonnaSalus.objects.get(id=pk)
    context = {"artikujt_informuesDonnaSalus":artikujt_informuesDonnaSalus}
    return render (request,"artinfodetail_DonnaSalus.html",context)






def artinfodetail(request,pk):
    artinfodetail= artikujtinformues.objects.get(id=pk)
    context = {"artinfodetail":artinfodetail}
    return render (request,"artinfodetail.html",context)



def politikaeprivatesise(request):
    context = {}
    return render (request,'politikateprivatesise.html',context)



def navbar(request):
    
    if request.method == "POST":
        name_ = request.POST["name"]
        email_ = request.POST["email"]
        phone_ = request.POST["phone"]
        date_ = request.POST["date"]
        age_ = request.POST["age"]
        sms_ = request.POST["sms"]
    
        # Save the form data to the database
        LiniTakim_salus(
            name=name_,
            email=email_,
            phone=phone_,
            specialiteti=date_,
            mjeku=age_,
            sms=sms_
        ).save()
        return redirect('home')
    return render(request, "base/navbar.html")



def translate(request):
    trans = _('hello')
    return render(request,'translate.html', {'trans':trans})





def search(request):
    query = request.GET.get('q', '')

    # Search in Mjeket
    mjeket_results = Mjeket.objects.translated().filter(
        Q(translations__name__icontains=query) |
        Q(departamenti__translations__name__icontains=query)
    ).distinct()

    # Search in Specialitet
    specialitet_results = Specialitet.objects.translated().filter(
        Q(translations__name__icontains=query) |
        Q(translations__specialitet_pershkrimi__icontains=query)
    ).distinct()

    # Search in Artikujtinformues
    artikujtinformues_results = artikujtinformues.objects.translated().filter(
        Q(translations__name__icontains=query) |
        Q(translations__art_description__icontains=query) |
        Q(departamenti__translations__name__icontains=query)
    ).distinct()

    context = {
        'mjeket_results': mjeket_results,
        'specialitet_results': specialitet_results,
        'artikujtinformues_results': artikujtinformues_results,
        'query': query,
    }

    return render(request, 'search_results.html', context)




def albanostra(request):
    videos = Video_AlbaNostra.objects.all()
    artikujt_informuesAlbaNostra = artikujtinformuesAlbaNostra.objects.all()
    context ={'videos': videos,'artikujt_informuesAlbaNostra': artikujt_informuesAlbaNostra}

    return render (request,'albanostra.html',context)