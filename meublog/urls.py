from django.urls import path
from . import views

app_name = 'meublog'

urlpatterns = [
    path('', views.ListarPostsView.as_view(), name='listar_posts'),
    #path('', views.listar_posts, name='listar_posts'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:slug>/', views.DetalharPostView.as_view(), name='detalhe'),
    #path('<int:ano>/<int:mes>/<int:dia>/<slug:slug>/',
    #     views.detalhar_post, name='detalhe'),
    path('enviarpost/<int:pk>/', views.FormContatoView.as_view(),
         name='enviarpost'),
    path('comentarpost/<int:pk>/', views.ComentarPostView.as_view(), name='comentarpost'),
]