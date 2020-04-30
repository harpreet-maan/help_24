from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):


    def authenticate(self,request,username,password):
        try:
            user=User.objects.get(email=username)
            success=user.check_password(password)
            if success:
                if user.check_password(password):
                    return user
        except:
            pass
        return None