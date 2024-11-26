from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Study
from.forms import StudyForm

def index(request):
    if request.method == "POST":
        selected_studies = request.POST.getlist('selected_studies')
        if selected_studies:
            Study.objects.filter(id__in=selected_studies).delete()
            return redirect('index')
        else:
            return HttpResponse("No records selected for deletion.", status=400)

    return render(request, 'study/index.html', {
        'study': Study.objects.all()
    })

def view_study(request, id):
     study=Study.objects.get(pk=id)
     return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            new_study_name = form.cleaned_data['study_name']
            new_study_phase = form.cleaned_data['study_phase']
            new_sponsor_name = form.cleaned_data['sponsor_name']
            new_study_description = form.cleaned_data['study_description']

            # Save the new study record
            new_study = Study(
                study_name=new_study_name,
                study_phase=new_study_phase,
                sponsor_name=new_sponsor_name,
                study_description=new_study_description
            )
            new_study.save()

            # Render the form with a success message
            return render(request, 'study/add.html', {
                'form': StudyForm(),
                'success': True
            })
    else:
        form = StudyForm()
    
    # Render the form for a GET request
    return render(request, 'study/add.html', {
        'form': form,
        'success': False  # Explicitly pass success as False
    })

def edit(request, id):
    if request.method =='POST':
        study= Study.objects.get(pk=id)
        form =StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return render(request, 'study/edit.html',{
                'form':form,
                'success':True
            })
    else:
        study =Study.objects.get(pk=id)
        form= StudyForm(instance=study)
    return render(request, 'study/edit.html',{
        'form':form
    })





