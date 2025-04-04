from django.shortcuts import render, redirect, get_object_or_404
from .forms import  CustomAuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from student.models.student import StudentModels
from teacher.models import Teachermodels
from user.models.user import UserModels
from user.smtpForm import SmtpForm
from user.models.appsetting import AppSettingmodels
from user.schoolform import SchoolForm
from user.models.school import SchoolModels
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from user.userform import UserForm





#####################################################
def login_view (request):
    if request.user.is_authenticated:
        return redirect('user:home')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user:home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authen/connexion.html', {'form': form}) 
#####################################################
@login_required(login_url='user:login')
def home(request):
    students = StudentModels.objects.all()
    teacher=Teachermodels.objects.all()
    user=UserModels.objects.all()
    filles = StudentModels.objects.filter(gender='female') 
    garcons = StudentModels.objects.filter(gender='male')
    context = {
        'students': students,
        'teacher':teacher,
        'user':user,
        'filles': filles,
        'garcons': garcons
    }
    return render(request, 'authen/Home.html',context)

@login_required(login_url='user:login')
def list (request):
    listes=UserModels.objects.all()
    return render(request, 'list.html' , {'listes':listes})

###############################################################

def appsetting(request):
    appsetting = AppSettingmodels.objects.first()
    
    
    if appsetting:
        return redirect('user:login')  # Ajout du 'return' manquant
    
    if request.method == "POST":
        form = SmtpForm(request.POST)
        if form.is_valid():
            # Utiliser les données nettoyées du formulaire
            config = AppSettingmodels(
                smtp_server=form.cleaned_data['smtp_server'],
                smtp_port=form.cleaned_data['smtp_port'],
                smtp_username=form.cleaned_data['smtp_username'],
                smtp_password=form.cleaned_data['smtp_password']
            )
            config.save()
            messages.success(request, 'Paramètres SMTP enregistrés avec succès!')
            return redirect('user:school')
        else:
            # Afficher les erreurs de validation du formulaire
            messages.error(request, 'Le formulaire n\'est pas valide. Veuillez corriger les erreurs.')
    else:
        form = SmtpForm()  # Créer un formulaire vide pour les requêtes GET

    return render(request, 'school/appsetting.html', {'form': form})


#####################################################
def school(request):
    if request.method=="POST":
        name=request.POST.get('name')
        url_logo=request.POST.get('url_logo')

        form=SchoolForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            url_logo = form.cleaned_data['url_logo']
            school=SchoolModels(name=name,url_logo=url_logo,app_setting=AppSettingmodels.objects.first())
            school.save()
            return redirect('user:home')
        return messages.error(request, 'le formulaire n\' est pas valide.')
    return render(request, 'school/school.html')

######################################################
@login_required(login_url='user:login')
def update_appsetting(request):
    appsetting = AppSettingmodels.objects.first()
    if request.method == 'POST':
        # If the form is submitted, we update the existing AppSettingmodels object
        form = SmtpForm(request.POST)
        if form.is_valid():
            # Manually update the AppSettingmodels instance with the form data
            appsetting.smtp_server = form.cleaned_data['smtp_server']
            appsetting.smtp_port = form.cleaned_data['smtp_port']
            appsetting.smtp_username = form.cleaned_data['smtp_username']
            appsetting.smtp_password = form.cleaned_data['smtp_password']
            appsetting.save()  # Save the updated settings to the database
            return render(request, 'school/afficher_appsetting.html', {'form': form, 'appsetting': appsetting})
        else:
            messages.error(request, "Le formulaire contient des erreurs.")
    else:
        # Initialize the form with the current settings data (GET request)
        form = SmtpForm(initial={
            'smtp_server': appsetting.smtp_server,
            'smtp_port': appsetting.smtp_port,
            'smtp_username': appsetting.smtp_username,
            'smtp_password': appsetting.smtp_password
        })

    return render(request, 'school/afficher_appsetting.html', {'form': form, 'appsetting': appsetting})
#################################################################

def update_user(request, id):
    user = get_object_or_404(UserModels, id=id)

    
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')  
        form = UserForm(request.POST) 
        
        if form.is_valid():

            if password and password != confirm_password:
                messages.error(request, "Les mots de passe ne correspondent pas!")
                return render(request, 'update_user.html', {'user': user, 'form': form})

            user.pseudo = pseudo
            if password:  
                user.set_password(password)
            
            user.save()
            messages.success(request, "Profil mis à jour avec succès!")
            return redirect('user:list')  
            
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = UserForm()  
    
    return render(request, 'update_user.html', {
        'user': user,
        'form': form
    })
#################################################################
@login_required(login_url='user:login')
def update_school(request):
    school = SchoolModels.objects.first()
    if request.method == "POST":
        name = request.POST.get('name')
        url_logo = request.POST.get('url_logo')

        form = SchoolForm(request.POST)
        if form.is_valid():
            school.name = name
            school.url_logo = url_logo
            school.save()
            return redirect('user:afficher_school')
        return messages.error(request, 'le formulaire n\' est pas valide.')
    return render(request, 'school/afficher_school.html', {'schools': school})

#######################################################

@login_required(login_url='user:login')
def logout(request):
    auth_logout(request)
    return redirect('user:login')


######################################################
@login_required(login_url='user:login')
def desactivate_user(request, user_id):
    user = get_object_or_404(UserModels, id=user_id)
    user.is_active = False
    user.save()
    return redirect('user:list')

def activate_user(request, id):
    user = get_object_or_404(UserModels, id=id)
    user.is_active = True
    user.save()
    return redirect('user:list')
