from django import forms

LEYES_CHOICES = [
    ('constitución política de los estados unidos mexicanos','Constitución política de los Estados Unidos Mexicanos'),
    ('ley del impuesto sobre la renta','Ley del impuesto sobre la renta'),
    ('ley general de salud','Ley general de salud'),
    ('ley general de educación','Ley general de educación'),
    ('ley general de acceso de las mujeres a una vida libre de violencia','Ley general de acceso de las mujeres a una vida libre de violencia'),
    ('ley del impuesto al valor agregado','Ley del impuesto al valor agregado'),
    ('ley orgánica del congreso general de los estados unidos mexicanos','Ley orgánica del congreso general de los Estados Unidos Mexicanos'),
    ('ley federal del trabajo','Ley federal del trabajo'),
    ('ley federal de derechos','Ley federal de derechos'),
    ('código penal federal','Código penal federal'),
    ('Decreto','Decreto'),
    ('','Vacío'),
]

OPCIONES = [
    ('aprobadas','Aprobadas'),
    ('desechadas','Desechadas'),
]

SEXENIO = [
    ('epn','EPN'),
    ('amlo','AMLO'),
    ('todos','TODOS')
]

class UserForm(forms.Form):
    tipo = forms.CharField(label='¿Qué tipo de iniciativas buscas?',widget=forms.Select(choices=OPCIONES))
    ley_modificada = forms.CharField(label='¿Qué ley modifican?',widget=forms.Select(choices=LEYES_CHOICES))
    sexenio = forms.CharField(label='¿En qué sexenio?',widget=forms.Select(choices=SEXENIO))
    limit = forms.IntegerField(label='¿Cuántas quieres que te muestre?')

class UserFormId(forms.Form):
    id = forms.IntegerField(label="¿Cúal es el id 1 de la iniciativa que quieres ver?")
    id_2 = forms.IntegerField(label="¿Cúal es el id 2 de la iniciativa que quieres ver?")
    id_3 = forms.IntegerField(label="¿Cúal es el id 3 de la iniciativa que quieres ver?")
    id_4 = forms.IntegerField(label="¿Cúal es el id 4 de la iniciativa que quieres ver?")
    id_5 = forms.IntegerField(label="¿Cúal es el id 5 de la iniciativa que quieres ver?")