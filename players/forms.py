from django.forms import ModelForm
from players.models import jogadores

# Create the form class.
class JogadoresForm(ModelForm):
    class Meta:
        model = jogadores
        fields = ['nome', 'posicao', 'numero'   ]
