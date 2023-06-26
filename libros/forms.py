from django.forms import ModelForm
from .models import Libro, Autor

class LibroCreateForm(ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        
class AutorCreateForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']