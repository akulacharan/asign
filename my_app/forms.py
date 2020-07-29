from django import forms
from .models import Customer



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username','date_of_birth','mobile','email','passport_num','image','password','confirm_pasword')

        labels = {
            'username'          : 'Full Name',
            'date_of_birth'     :  'D.O.B(dd/mm/yy)',
            'mobile'            :  'Mobile',
            'email'             :      'Email',
            'passport_num'      :  'Passport-Num',
            'image'             :  'Profile-pic',
            'password'          :  'Password',
            'confirm_pasword'  :  'Confirm-Password',
         }

    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)

        # for removing any mandatory fields in form
        self.fields['image'].required = False
        self.fields['confirm_pasword'].required= True



