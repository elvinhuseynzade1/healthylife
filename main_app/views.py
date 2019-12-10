from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from .models import Clinic, Comment, Doctor
from .forms import CommentForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from apiclient.discovery import build
import geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def home(request):
    api = 'AIzaSyDcAg6W03iEMa2tZkKTYrn5McTIzDIk59A'
    resource = build('customsearch', 'v1', developerKey=api).cse()
    result = resource.list(
        q='həkim səhlənkarlığı', cx='002994718784441088409:6lklv3uftgn').execute()
    result['items']
    print( result['items'][0])
    # print( result['items'][0])
    context = {
        'result': result['items'] 
        #'result':'salam'
    }
    return render(request, 'home.html', context)
# class ClinicView(ListView):


class MainView(ListView):
    context_object_name = "clinics"
    template_name = "index.html"

    def get_queryset(self, **kwargs):
         query = self.request.GET.get('q')
         print(query)
         if query:
             print(Clinic.objects.filter(name__icontains=query))
             return Clinic.objects.filter(name__icontains=query)
         else:
             return Clinic.objects.all()
    # clinics=Clinic.objects.all()
    # context={
    #     'clinics':clinics
    # }
    # return render(request, "index.html",context)


class MainViewDoctor(ListView):
    context_object_name = "doctors"
    template_name = "doctors.html"

    def get_queryset(self, **kwargs):
         query = self.request.GET.get('q')
         print(query)
         if query:
             print(Clinic.objects.filter(name__icontains=query))
             return Clinic.objects.filter(name__icontains=query)
         else:
             return Clinic.objects.all()


class ClinicView(ListView):
    model = Clinic
    context_object_name = "clinics"
    template_name = "clinic_list.html"

    # def get_queryset(self,**kwargs):
    #      query=self.request.GET.get('q')
    #      print(query)
    #      if query:
    #          print(Clinic.objects.filter(name__icontains=query))
    #          return Clinic.objects.filter(name__icontains=query)
    #      else:
    #          return Clinic.objects.all()

class DoctorView(ListView):
    model               = Doctor
    context_object_name = "doctors"
    template_name       = "doctors.html"


def description(request, id):
    clinic = Clinic.objects.get(id=id)
    print(clinic.name)
    nom=Nominatim()
   
    
    # print(n.latitude,n.longitude)
    comments = Comment.objects.filter(post=id)
    if request.method == "POST":
        post = get_object_or_404(Clinic, id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('description', id=post.id)
    else:
        form = CommentForm()
    doctors = Doctor.objects.filter(clinic=id)
    print(doctors)

    n=nom.geocode(clinic.name)
  
    try:
       print(n.latitude, n.longitude)
       context = {
        'clinic': clinic,
        'comments': comments,
        'form': form,
        'hekimler': doctors,
        'lat':n.latitude,
        'lng':n.longitude,
    }
    except GeocoderTimedOut as e:
          context = {
        'clinic': clinic,
        'comments': comments,
        'form': form,
        'hekimler': doctors,
        'lat':40.4093,
        'lng':49.8671,
    }
        
    return render(request, 'description.html', context)


def description_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
   
    
    # comments = Comment.objects.filter(post=id)
    # if request.method == "POST":
    #     post = get_object_or_404(Clinic, id=id)
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = request.user
    #         comment.post = post
    #         comment.save()
    #         return redirect('description', id=post.id)
    # else:
    #     form = CommentForm()
    # doctors = Doctor.objects.filter(clinic=id)
    context = {
        'doctor': doctor,
        # 'comments': comments,
        # 'form': form,
        # 'hekimler': doctors,
        # 'lat':40.4093,
        # 'lng':49.8671,
    }
        
    return render(request, 'desc_doctor.html', context)


def ajaxify_rating(request):

    if request.is_ajax():
        ID = request.POST.get('id')
        count = request.POST.get('count')
        print('id', id)
        print('count=', count)
        user = request.user
        clinic = Clinic.objects.get(id=ID)
        last = int((int(clinic.rating)+int(count)))/2
        clinic.rating = last
        clinic.save()
        return JsonResponse({
            'message': "successfully",
        }, status=201)

def ajaxify_rating_doctor(request):

    if request.is_ajax():
        ID = request.POST.get('id')
        count = request.POST.get('count')
        print('id', ID)
        print('count=', count)
        user = request.user
        clinic = Doctor.objects.get(id=ID)
        print(clinic)
        last = int((int(clinic.rating)+int(count)))/2
        clinic.rating = last
        clinic.save()
        return JsonResponse({
            'message': "successfully",
        }, status=201)        
