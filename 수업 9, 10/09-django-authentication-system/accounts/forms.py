from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import User

class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # 여기를 User로 써서 받아버려서 User모델에 변경사항이 생기면 여기도 다 바꿔야 되서 get_user_model()을 쓰는게 편리함 얘는 다 바꿔줌

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')