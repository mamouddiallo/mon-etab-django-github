# Create your views here.
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from teacher.models import Teachermodels
from teacher.forms import TeacherForm
from personn.models.address import AddressModels
from django.contrib.auth.decorators import login_required
from user.models.user import UserModels
from user.models.role import RoleUserModels
from django.contrib.auth.hashers import make_password
from user.models.school import SchoolModels
# Create your views here.

##################  add  ##################

@login_required(login_url='user:login')
def add(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        url = request.POST.get('url')
        date_naissance = request.POST.get('date')
        genre = request.POST.get('genre')
        vacant = request.POST.get('vacant') == "oui"
        matiere = request.POST.get('matiere')
        telephone = request.POST.get('telephone')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        rue = request.POST.get('rue')
        pseudo = request.POST.get('pseudo')
        password = request.POST.get('password')

        # Validation du formulaire (si nécessaire)
        form = TeacherForm({
            'first_name': nom,
            'last_name': prenom,
            'birthday': date_naissance,  
            'gender': genre,
            'phone_number': telephone,
            'available': vacant,
            'specially': matiere,
            'url_picture': url,
            'ville': ville,
            'pays': pays,
            'rue': rue,
            'pseudo': pseudo,
            'password': password
        })

        if form.is_valid():
            # Création DIRECTE de l'adresse (sans vérification)
            adresse = AddressModels.objects.create(
                city=ville,
                country=pays,
                street=rue
            )
            school=SchoolModels.objects.first()
            user = UserModels(
                    pseudo=form.cleaned_data['pseudo'],
                    password=make_password(form.cleaned_data['password'])  ,
                    school=school
                )
            user.save()

            # Création du professeur
            teacher = Teachermodels.objects.create(
                first_name=nom,
                last_name=prenom,
                birthday=date_naissance if date_naissance else None,  
                phone_number=telephone,
                available=vacant,
                specially=matiere,
                url_picture=url,
                address=adresse , # Liaison avec la nouvelle adresse
                user=user
            )

            return redirect('teacher:list')

    return render(request, 'teacher/add.html')
    
######################  list  ######################    
@login_required(login_url='user:login')
def list(request):
    prof= Teachermodels.objects.all()
    return render(request, 'teacher/list.html',{'profs':prof})


################## update  ##################
@login_required(login_url='user:login')
def update(request, id):
    teacher = get_object_or_404(Teachermodels, id=id)

    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        url = request.POST.get('url')
        date_naissance = request.POST.get('date')
        genre = request.POST.get('genre')
        vacant = request.POST.get('vacant') == "oui"
        matiere = request.POST.get('matiere')
        telephone = request.POST.get('telephone')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        rue = request.POST.get('rue')

        # Validation du formulaire (si nécessaire)
        form = TeacherForm({
            'first_name': nom,
            'last_name': prenom,
            'birthday': date_naissance,  
            'gender': genre,
            'phone_number': telephone,
            'available': vacant,
            'specially': matiere,
            'url_picture': url,
            'ville': ville,
            'pays': pays,
            'rue': rue
        })

        if form.is_valid():
            teacher.first_name = nom
            teacher.last_name = prenom
            teacher.birthday = date_naissance
            teacher.gender = genre
            teacher.phone_number = telephone
            teacher.available = vacant
            teacher.specially = matiere
            teacher.url_picture = url
            teacher.address.city = ville
            teacher.address.country = pays
            teacher.address.street = rue
            teacher.save()
            return redirect ('teacher:list')
        else:
            return HttpResponse("Tous les champs sont obligatoires.", status=400)
    else:
        return render(request, 'teacher/update.html', {'teacher': teacher})

    return render(request, 'update.html')

################## delete  ################## 
@login_required(login_url='user:login') 
def delete(request, id):
    prof = get_object_or_404(Teachermodels, id=id)
    prof.delete()
    return redirect('teacher:list')


################# Recherche ##################
@login_required(login_url='user:login')
def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')  
        if query:  
            teachers = Teachermodels.objects.filter(first_name__icontains=query)  
            return render(request, 'teacher/recherche.html', {'teachers': teachers})  
        else:
            return render(request, 'teacher/recherche.html', {'teachers': []})
    return render(request, 'teacher/list.html')