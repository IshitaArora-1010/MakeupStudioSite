from  django import forms
from .models import Feedback
class Appointment_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        labels = {
            'Contact_no': 'Contact No',
            'Instagram_handle': 'Instagram handle'
        }

# class Enquiry_form(forms.ModelForm):
#     class Meta:
#         model = Enquiry
#         fields = '__all__'
#
#         labels = {
#             'Contact_no': 'Contact No'
#         }