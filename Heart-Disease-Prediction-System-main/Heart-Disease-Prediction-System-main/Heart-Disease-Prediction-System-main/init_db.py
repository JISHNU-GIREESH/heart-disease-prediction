import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_desease.settings')
django.setup()

from django.contrib.auth.models import User
from health.models import Admin_Helath_CSV
from django.core.files import File

def initialize():
    # Create superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created with password 'admin123'")
    else:
        print("Superuser 'admin' already exists")

    # Add Heart CSV if not exists
    if not Admin_Helath_CSV.objects.filter(id=1).exists():
        csv_path = 'media/heart.csv'
        if os.path.exists(csv_path):
            with open(csv_path, 'rb') as f:
                obj = Admin_Helath_CSV.objects.create(name='Heart Data', id=1)
                obj.csv_file.save('heart.csv', File(f))
                obj.save()
            print("Heart CSV initialized in database.")
        else:
            print("Warning: media/heart.csv not found. Prediction might not work.")
    else:
        print("Heart CSV already initialized.")

if __name__ == '__main__':
    initialize()
