from django.urls import path

#from apps.mascota.views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('nuevo/', views.mascota_view, name='m_crear'),
    path('nuevo/', views.MascotaCreate.as_view(), name='m_crear'),
    #path('lista/', views.mascota_list, name='m_listar'),
    path('lista/', views.MascotaList.as_view(), name='m_listar'),
    #path('editar/<int:id_mascota>/', views.mascota_edit, name='m_editar'),
    path('editar/<int:pk>/', views.MascotaEditar.as_view(), name='m_editar'),
    #path('eliminar/<int:id_mascota>/', views.mascota_delete, name='m_eliminar'),
    path('eliminar/<int:pk>/', views.MascotaEliminar.as_view(), name='m_eliminar'),
    #re_path(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
]