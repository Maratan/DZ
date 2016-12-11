from django.http import Http404
from django.shortcuts import render, redirect
from DZ.models import Tovar
from django.contrib.auth.decorators import login_required
from django import forms


def index(request):
    return render(request, 'index.html')


@login_required
def products(request):
    product = Tovar.objects.all()
    return render(request, 'products.html', {'product': product})

def trash(request):
    return render(request, 'trash.html')

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ['name', 'image', 'text', 'cout']

    def __init__(self, user, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self,commit=False):
        instance = super(CreateProductForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()

        return instance

@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('Tovar')
    else:
        form = CreateProductForm(request.user)

    return render(request, 'create_product.html', {'form': form})

@login_required
def korzina(request, name):
    try:
        tov = Tovar.objects.get(name=name)
    except Tovar.DoesNotExist:
        raise Http404

    return render(request, 'products.html', {'addz': request.tovar.zakaz_on(tov)})

@login_required
def add_trash(request, tovar_id):
    try:
        trash_to = Tovar.objects.get(pk=tovar_id)
        if trash_to != request.tovar and not request.tovar.zakaz_on(trash_to):
            request.tovar.zakaz_on.add(trash_to)
    except Tovar.DoesNotExist:
        raise Http404

    return redirect('Tovar', name=trash_to.name)


@login_required
def del_trash(request, tovar_id):
    try:
        trash_to = Tovar.objects.get(pk=tovar_id)
        if trash_to != request.tovar and request.tovar.zakaz_on(trash_to):
            request.tovar.zakaz_on.remove(trash_to)
    except Tovar.DoesNotExist:
        raise Http404

    return redirect('Tovar', name=trash_to.name)