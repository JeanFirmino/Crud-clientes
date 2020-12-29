from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from registros.views import home, listagem, categoriasUpdateView,categoriasCreateView, delete

# É mais conveniente deixar a home como a primeira
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', home),
    path('home/', login_required(listagem), name='url_listagem'),
    path('update/<int:pk>/', login_required(categoriasUpdateView.as_view()), name='url_update'),
    path('delete/<int:pk>/', login_required(delete), name='url_delete'),
    path('novo/', login_required(categoriasCreateView.as_view()), name= 'url_novo'),
]
