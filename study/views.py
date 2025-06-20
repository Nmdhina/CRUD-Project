from django.shortcuts import render, redirect, get_object_or_404
from .models import study1
from .forms import sform  # You’ll create this form next

def main(request):
    studies = study1.objects.all()
    return render(request, 'study/main.html', {'studies': studies})

def add_study(request):
    if request.method == 'POST':
        form = sform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = sform()
    return render(request, 'study/add_study.html', {'form': form})

def edit_study(request, id):
    study = get_object_or_404(study1, id=id)
    if request.method == 'POST':
        form = sform(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = sform(instance=study)
    return render(request, 'study/edit_study.html', {'form': form})

def view_study(request, id):
    studies = get_object_or_404(study1, id=id)
    return render(request, 'study/view_study.html', {'studies': studies})

def delete_study(request, id):
    study = get_object_or_404(study1, id=id)
    
    if request.method == 'POST':
        study_name = study.study_name  
        study.delete()
        return redirect('main')    
    return render(request, 'study/delete_study.html', {'study': study})
