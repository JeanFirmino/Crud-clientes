from django.contrib import admin
from django.urls import path
from registros.views import home, listagem, novo_dado, ClienteUpdateView, delete

# É mais conveniente deixar a home como a primeira
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', listagem, name='url_listagem'),
    path('update/<int:pk>/', ClienteUpdateView.as_view(), name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('novo/', novo_dado, name= "novo"),
]
