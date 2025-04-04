from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
from io import BytesIO
from student.models import StudentModels 
from teacher.models import Teachermodels
from user.models.user import UserModels   
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='user:login')
def rapport(request):
    if request.method == 'POST':
        format_rapport = request.POST.get('format')
        selected_list = request.POST.get('generer')

        if not selected_list:
            return HttpResponse("Veuillez sélectionner une liste.", status=400)
        
        if not format_rapport:
            return HttpResponse("Veuillez sélectionner un format.", status=400)

        # Définir les données et les champs spécifiques pour chaque modèle
        if selected_list == 'liste_des_eleves':
            data = StudentModels.objects.all()
            title = "Liste des élèves"
            fields = [
                ('first_name', 'Prénom'),
                ('last_name', 'Nom'),
                ('birthday', 'Date de naissance'),
                ('classe', 'Classe'),
                ('phone_number', 'Numéro de téléphone'),
                ('gender', 'Genre'),
                # Ajoutez d'autres champs spécifiques aux élèves
            ]
        elif selected_list == 'liste_des_profs':
            data = Teachermodels.objects.all()
            title = "Liste des professeurs"
            fields = [
                ('first_name', 'Prénom'),
                ('last_name', 'Nom'),
                ('birthday', 'Date de naissance'),
                ('specially', 'Matière enseignée'),
                ('phone_number', 'Numéro de tеlефone'),
                ('available', 'Disponible'),
                ('url_picture', 'URL de l\'image'),

                
            ]
        elif selected_list == 'liste_des_users':
            data = UserModels.objects.all()
            title = "Liste des utilisateurs"
            fields = [
                ('pseudo', 'Nom d\'utilisateur'),
                ('creation_date', 'Date d \'inscription'),
            ]
        else:
            return HttpResponse("Option invalide.", status=400)

        if format_rapport == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{selected_list}.pdf"'

            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            p.drawString(100, 750, title)
           
            y_position = 730
            for item in data:
                info_lines = []
                for field, label in fields:
                    if hasattr(item, field):
                        value = getattr(item, field)
                        # Formater les dates
                        if isinstance(value, datetime):
                            value = value.strftime('%d/%m/%Y')
                        info_lines.append(f"{label}: {value}")
                    else:
                        info_lines.append(f"{label}: N/A")
                
                full_info = " - ".join(info_lines)
                p.drawString(100, y_position, full_info)
                y_position -= 20
                if y_position < 50:  
                    p.showPage()
                    y_position = 750
                    p.drawString(100, 750, title)
                    y_position = 730
            
            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response

        elif format_rapport == 'excel':
            data_dict = []
            for item in data:
                item_data = {}
                for field, label in fields:
                    if hasattr(item, field):
                        value = getattr(item, field)
                        # Formater les dates
                        if isinstance(value, datetime):
                            value = value.strftime('%d/%m/%Y')
                        item_data[label] = value
                    else:
                        item_data[label] = 'N/A'
                data_dict.append(item_data)
            
            df = pd.DataFrame(data_dict)
            
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{selected_list}.xlsx"'

            with BytesIO() as bio:
                with pd.ExcelWriter(bio, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Rapport', index=False)
                response.write(bio.getvalue())
            
            return response

    return render(request, 'rapport.html')