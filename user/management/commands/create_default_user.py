from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Crée un utilisateur par défaut"

    def handle(self, *args, **kwargs):
        pseudo = "admin"
        email = "admin@example.com"
        password = "admin123"

        try:
            if not User.objects.filter(pseudo=pseudo).exists():
                user = User.objects.create_user(pseudo=pseudo)
                user.set_password(password)  # Hachage du mot de passe
                user.is_superuser = True
                user.is_staff = False
                user.save()
                self.stdout.write(self.style.SUCCESS(f"✅ Utilisateur '{pseudo}' créé avec succès !"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ L'utilisateur '{pseudo}' existe déjà."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Erreur : {str(e)}"))
