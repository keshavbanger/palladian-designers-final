import os
import django
import sys

# Add project root to path
sys.path.append(r"D:\newcleint palldf\palladian_designers")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'palladiun.settings')
django.setup()

from core.models import Project, ProjectImage, AboutUs

def fix():
    mappings = [
        ('Bar Designs', 'project_images/bar_04.webp'), 
        ('Clinic Designs', 'project_images/CLINIC_04.webp'), 
        ('Modular Kitchen', 'project_images/KITCHEN_06.webp'), 
        ('Living Room Designs', 'project_images/LIVING_01.webp'), 
        ('Living Room Designs', 'project_images/SITTING_AREA_01.webp'), 
        ('Bedroom', 'project_images/BEDROOM_01_7KXZXil.webp'), 
        ('Modern Living Room', 'project_images/LIVING_01.webp'), 
        ('Modern Living Room', 'project_images/SITTING_AREA_01.webp'), 
        ('Exterior Designs', 'project_images/ADINATH_VIHAR_RIGHT.webp'), 
        ('Exterior Designs', 'project_images/FRONT_VIEW_1.webp'), 
        ('Colony Design', 'project_images/Seven_City_Exterior-e1526460260781.webp'), 
        ('Vila Scan-to-BIM', 'project_images/mfh.webp'), 
        ('Vila Scan-to-BIM', 'project_images/right_corner_view.webp'), 
        ('BIM | SCAN| 3D CONVERSION | LOD:- 300', 'project_images/TOWER_1_.webp'), 
        ('BIM | SCAN| 3D CONVERSION | LOD:- 300', 'project_images/BRIDGE_13.webp'), 
        ('Restaurant', 'project_images/bar_04.webp')
    ]
    for p_title, p_image in mappings:
        p = Project.objects.filter(title=p_title).first()
        if p and not ProjectImage.objects.filter(project=p, project_image=p_image).exists():
            ProjectImage.objects.create(project=p, project_image=p_image)
    a = AboutUs.objects.first()
    if a:
        a.year = 2021
        a.save()

if __name__ == "__main__":
    fix()
