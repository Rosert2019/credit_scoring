from django import forms


class single_form(forms.Form):
    amount_choises =(
    ('0', 'M_8000'),
    ('13', 'M_8000_11630'),
    ('18', 'M_1130_15600'),
    ('25', 'M_15600'),)
  
    amount = forms.ChoiceField(choices = amount_choises)

    age_choises =(
    ('21', 'A_33'),
    ('12', 'A_33_44'),
    ('4', 'A_44_54'),
    ('0', 'A_54'),)
  
    age = forms.ChoiceField(choices = age_choises)

    duration_choises =(
    ('0', 'D_48'),
    ('48', 'D_60'),)

    duration = forms.ChoiceField(choices = duration_choises)

    rate_choises =(
    ('0', 'R_6'),
    ('4', 'R_5_7'),
    ('5', 'R_7_8'),
    ('6', 'R_8'),)
  
    rate = forms.ChoiceField(choices = rate_choises)


