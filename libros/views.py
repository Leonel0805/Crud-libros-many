from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroCreateForm, AutorCreateForm
from .models import Libro, Autor
# Create your views here.
def home (request):
    return render(request, 'home.html')

def libros(request):
    
    libros = Libro.objects.all().prefetch_related('autor')
    #autores = Libro.objects.filter(autor__)
    return render(request, 'libros.html',{
        'libros': libros,
    })

def crear_libro(request):
    
    if request.method == 'GET':
        return render(request, 'crear_libro.html',{
            'form': LibroCreateForm
        })
        
    elif request.method == 'POST':
        form = LibroCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('libros')
        else:
            return render(request, 'crear_libro.html',{
            'form': LibroCreateForm,
            'error': 'error al crear libro'
        })
            
def edit_libro(request, id_libro):
    
    libro = get_object_or_404(Libro, pk=id_libro)
    
    if request.method == 'GET':
        form = LibroCreateForm(instance=libro)
        return render(request, 'edit.html',{
            'form':form
        })
        
    elif request.method == 'POST':
        form = LibroCreateForm(request.POST, instance=libro)
        
        if form.is_valid():
            form.save()
            return redirect('libros') 
        else:
            return render(request, 'edit.html',{
                'form':form,
                'error': 'error al actualizar'
            })              
            
def eliminar_libro(request, id_libro):
    libro = get_object_or_404(Libro, pk=id_libro)
    
    if request.method == 'GET':
        return render(request, 'eliminar.html')
    
    elif request.method == 'POST':
        libro.delete()
        return redirect('libros')
    
    


def crear_autor(request):
    
    if request.method == 'GET':
        return render(request, 'crear_autor.html',{
            'form': AutorCreateForm
        })

    elif request.method == 'POST':
        form = AutorCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('libros')
        
        else:
            return render(request, 'crear_autor.html',{
            'form': AutorCreateForm,
            'error': 'Error al crear Autor'
        })
                        