from django import forms

from .models import BookAppointment, Qrcode


class BookAppointmentForm(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = [
            'name',
            'email',
            'phone',
            'date',
            'picktime',
            'people',
            'type_of',
            'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
                'type': 'text',
                'name': 'name',
                'id': 'name',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars',
            }),

            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Your Email',
                'data-rule': 'email',
                'data-msg': 'Please enter a valid email',
            }),

            'phone': forms.NumberInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'name': 'phone',
                'id': 'phone',
                'placeholder': 'Your Phone',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars',
            }),

            'date': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'name': 'date',
                'id': 'date',
                'placeholder': 'Date',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 10 chars',
            }),

            'picktime': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'name': 'picktime',
                'id': 'picktime',
                'placeholder': 'Time',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars',
            }),

            'people': forms.NumberInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'name': 'people',
                'min': 1,
                'id': 'people',
                'placeholder': '# of people',
                'data-rule': 'minlen:1',
                'data-msg': 'Please enter at least 1 person',
            }),

            'type_of': forms.Select(attrs={
                'class': 'form-control',
                'id': 'type_of',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'name': 'message',
                'rows': '5',
                'placeholder': 'Message',
            })

        }


class QrCodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = [
            'name',
            'email',
            'phone',
            'date',
            'picktime',
            'people',
            'message',
        ]
