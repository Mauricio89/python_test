from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .forms import MascotaForm
from apps.mascota.models import Mascota

# Create your views here.

def index(request):
    #return HttpResponse("Index")
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:m_listar')
    else:
        form = MascotaForm()
    return render(request, 'mascota/m_form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:m_listar')
    return render(request, 'mascota/m_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:m_listar')
    return render(request, 'mascota/m_delete.html', {'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    paginate_by = 100
    #template_name = 'mascota/mascota_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']=timezone.now()
        return context

class MascotaCreate(CreateView):
    template_name = 'mascota/m_form.html'
    form_class = MascotaForm
    success_url = '/mascota/lista/'
    #model = Mascota
    #form_class = MascotaForm
    #fields = "__all__" 
    #success_url = reverse_lazy('mascota:m_listar')

    def form_valid(self, form):
        return super().form_valid(form)

class MascotaEditar(UpdateView):
    model = Mascota
    template_name = 'mascota/m_form.html'
    form_class = MascotaForm
    success_url = '/mascota/lista/'

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     #return get_object(Mascota, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

class MascotaEliminar(DeleteView):
    model = Mascota
    template_name = 'mascota/m_delete.html'
    form_class = MascotaForm
    success_url = '/mascota/lista/'

    def form_valid(self, form):
        return super().form_valid(form)