from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    EXTRAS_CHOICES = [
        ('airport_shuttle', 'Airport Shuttle'),
        ('breakfast', 'Breakfast Included'),
        ('early_checkin', 'Early Check-in'),
        ('late_checkout', 'Late Check-out'),
        ('room_with_view', 'Room with a View'),
    ]

    extras = forms.MultipleChoiceField(
        required=False,
        choices=EXTRAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    # children field will be automatically generated from model (PositiveSmallIntegerField)

    class Meta:
        model = Reservation
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'nationality',
            'children',
            'extras',
            'agree',
            'check_in_date',
            'check_out_date',
        ]
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.extras:
            self.initial.setdefault('extras', self.instance.extras.split(','))

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in_date')
        check_out = cleaned_data.get('check_out_date')
        agree = cleaned_data.get('agree')

        if agree is False:
            self.add_error('agree', 'You must agree before booking.')

        if check_in and check_out and check_out <= check_in:
            self.add_error('check_out_date', 'Check-out must be after check-in.')

        return cleaned_data

    def clean_extras(self):
        extras = self.cleaned_data.get('extras', [])
        return ','.join(extras)
