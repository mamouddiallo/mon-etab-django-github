from django.shortcuts import render , redirect ,get_object_or_404
from student.forms import StudentForm
from student.models.student import StudentModels
from personn.models.address import AddressModels
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from student.models.absence import AbsenceModels
from student.absenceform import AbsenceForm
from user.models.user import UserModels
from django.contrib.auth.hashers import make_password
from user.models.role import RoleUserModels
from user.models.school import SchoolModels
from user.models.appsetting import AppSettingmodels
from student.models.cards import StudentCardsModels
from datetime import datetime, timedelta
import secrets
import string
from django.db.models import Q

# Create your views here.
from django.contrib import messages
######################################
def generate_secure_reference(length=7):
    """Génère une référence aléatoire sécurisée"""
    alphabet = string.ascii_uppercase + string.digits
    return 'REF#' + ''.join(secrets.choice(alphabet) for _ in range(length))
#####################################
@login_required(login_url='user:login')
def add(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        url = request.POST.get('url')
        date_naissance_str = request.POST.get('date')
        genre = request.POST.get('genre')
        telephone = request.POST.get('telephone')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        rue = request.POST.get('rue')
        mailticket = request.POST.get('mailticket')
        phone_number_label = request.POST.get('phone_father')
        classe = request.POST.get('classe')
        pseudo = request.POST.get('pseudo')
        password = request.POST.get('password')


        form_data = {
            'first_name': nom,
            'last_name': prenom,
            'birthday': date_naissance_str,
            'gender': genre,
            'phone_number': telephone,
            'url_picture': url,
            'mailticket': mailticket,
            'phone_number_label': phone_number_label,
            'classe': classe,
            'ville': ville,
            'pays': pays,
            'rue': rue,
            'pseudo': pseudo,
            'password': password,
        }
        form = StudentForm(form_data)
        if form.is_valid():
            try:
                adress = AddressModels(
                    city=form.cleaned_data['ville'],
                    country=form.cleaned_data['pays'],
                    street=form.cleaned_data['rue']
                )
                adress.save()  

                school=SchoolModels.objects.first()
                user = UserModels(
                    pseudo=form.cleaned_data['pseudo'],
                    password=make_password(form.cleaned_data['password'])  ,
                    school=school
                )
                user.save()


                eleve = StudentModels(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    birthday=form.cleaned_data['birthday'],
                    gender=form.cleaned_data['gender'],
                    phone_number=form.cleaned_data['phone_number'],
                    url_picture=form.cleaned_data['url_picture'],
                    mailticket=form.cleaned_data['mailticket'],
                    phone_number_label=form.cleaned_data['phone_number_label'],
                    classe=form.cleaned_data['classe'],
                    address=adress  ,
                    user = user
                )
                eleve.save()

                expiration_date = datetime.now() + timedelta(days=365)
                StudentCardsModels.objects.create(
                    student=eleve,
                    reference="REF #" + generate_secure_reference(7),
                    issue_date=datetime.now(),
                    expiration_date=expiration_date,
            )
                messages.success(request, "L'étudiant a été ajouté avec succès!")
                return redirect('student:list')  

            except ValidationError as e:
                messages.error(request, f"Erreur de validation: {str(e)}")
                form.add_error(None, str(e))
            except Exception as e:
                messages.error(request, f"Une erreur s'est produite lors de l'ajout de l'étudiant: {str(e)}")
                form.add_error(None, f"Une erreur s'est produite : {str(e)}")
        else:
            messages.error(request, "Le formulaire contient des erreurs. Veuillez corriger les champs indiqués.")
        
        return render(request, 'student/add.html', {'form': form})
    
    return render(request, 'student/add.html', {'form': StudentForm()})


##################### list #####################
@login_required(login_url='user:login')
def list(request):
    eleves = StudentModels.objects.all()
    return render(request,'student/list.html',{'students':eleves})   


##################### delete #####################
@login_required(login_url='user:login')
def delete(request, id):
    eleve = get_object_or_404(StudentModels, id=id)
    eleve.delete()
    return redirect('student:list')

################### update #####################

@login_required(login_url='user:login')
def update(request, id):
    eleve = get_object_or_404(StudentModels, id=id)

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        url = request.POST.get('url')
        date_naissance = request.POST.get('date')
        genre = request.POST.get('genre')
        telephone = request.POST.get('telephone')
        mailticket = request.POST.get('mailticket')
        phone_number_label = request.POST.get('phone_father')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        rue = request.POST.get('rue')
        classe = request.POST.get('classe')
        pseudo = request.POST.get('pseudo')
        password = request.POST.get('password')
        role= request.POST.get('role')

        form_data = {
            'first_name': nom,
            'last_name': prenom,
            'birthday': date_naissance,
            'gender': genre,
            'phone_number': telephone,
            'url_picture': url,
            'mailticket': mailticket,
            'phone_number_label': phone_number_label,
            'ville': ville,
            'pays': pays,
            'rue': rue,
            'classe': classe,
            'pseudo': pseudo,
            'password': password,
            'role': role
        }

        
        form = StudentForm(form_data)
        if form.is_valid():
            try:
                eleve.first_name = form.cleaned_data['first_name']
                eleve.last_name = form.cleaned_data['last_name']
                eleve.birthday = form.cleaned_data['birthday']
                eleve.gender = form.cleaned_data['gender']
                eleve.phone_number = form.cleaned_data['phone_number']
                eleve.url_picture = form.cleaned_data['url_picture']
                eleve.mailticket = form.cleaned_data['mailticket']
                eleve.phone_number_label = form.cleaned_data['phone_number_label']
                eleve.classe = form.cleaned_data['classe']
                eleve.address.city = form.cleaned_data['ville']
                eleve.address.country = form.cleaned_data['pays']
                eleve.address.street = form.cleaned_data['rue']
                eleve.user.pseudo = form.cleaned_data['pseudo']
                eleve.user.password = make_password(form.cleaned_data['password'])
                eleve.user.roles.clear()
                role = get_object_or_404(RoleUserModels, role=form.cleaned_data['role'])
                eleve.user.roles.set([role])

                eleve.address.save()  
                eleve.save()
                return redirect('student:list')

            except ValidationError as e:
                form.add_error(None, str(e))
            except Exception as e:
                
                form.add_error(None, f"Une erreur s'est produite : {str(e)}")
        return render(request, 'student/update.html')
    return render(request, 'student/update.html', {'student': eleve})


############################################
@login_required(login_url='user:login')
def absence(request , id):
    eleve = get_object_or_404(StudentModels, id=id)
    if request.method == 'POST':
        absence_date = request.POST.get('absence_date')
        absence_number = request.POST.get('absence_number')
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence=AbsenceModels(absence_date=form.cleaned_data['absence_date'],absence_number=form.cleaned_data['absence_number'],student=eleve)
            absence.save()
            return redirect('student:list_absence')
    return render(request,'absence/absence.html',{'student':eleve})    
@login_required(login_url='user:login')
def delete_absence(request , id):
    absence = get_object_or_404(AbsenceModels, id=id)
    absence.delete()
    return redirect('student:list_absence')

@login_required(login_url='user:login')
def absence_list(request):

    absences = AbsenceModels.objects.select_related('student').all()
    
    print("Données envoyées au template:", {
        'count': absences.count(),
        'first': absences.first() if absences.exists() else None
    })
    
    return render(request, 'absence/list_absence.html', {
        'Absences': absences
    })




########################################
@login_required(login_url='user:login')
def cards(request , id):
    eleve = get_object_or_404(StudentModels, id=id)
    return render(request,'cards/cards.html',{'student':eleve})

######################################
@login_required(login_url='user:login')
def search(request):
    search_query = request.GET.get('search', '').strip()  
    
    if search_query:
        students = StudentModels.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) 
        ).distinct()
        
        context = {
            'students': students,
            'query': search_query,
            'has_results': students.exists()  
        }
        return render(request,'student/search.html',context)
    return render(request, 'student/list.html', context)
