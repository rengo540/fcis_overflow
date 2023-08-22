from django.dispatch import receiver
from django.db.models.signals import post_save ,pre_save
from django.contrib.auth.models import User
from .models import Student
from utils.utils import get_id_from_email
import datetime
from .models import Level
@receiver(post_save,sender=User)
def set_level_for_student(sender ,created ,instance,**kwargs):
    
    if created :
        college_email = instance.email 
        college_id = get_id_from_email(college_email)
        if college_id is not None:
            enter_year = college_id[:4]
            print(enter_year)
            year =int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)

        
            for i in range(0,5):
                if year - i == int(enter_year):
                    if month<8:
                        level = i 
                    else :
                        level= i+1 
                        
                if year - 4 > int(enter_year) :
                    level= 5
                    break
            level = Level.objects.get(pk=level)
            
            student = Student.objects.create(user=instance,
                                             level=level,
                                             college_id=college_id,
                                             is_grad= (level==5))
            student.save()

        
