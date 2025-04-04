from user.models.user import UserModels

def create_default_user(sender, **kwargs):
    if not UserModels.objects.filter(pseudo="admin").exists():
        UserModels.objects.create_superuser(pseudo="admin", password="admin123")
