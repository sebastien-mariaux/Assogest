from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        user.save()
        # self.send_email(user)
        return user

    # @staticmethod
    # def send_email(user):
    #     user.generate_validation_token()
    #     user.send_email_activation_email()