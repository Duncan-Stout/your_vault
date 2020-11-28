from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Vault'

urlpatterns = [

    path('vault_shelf/', views.vault_shelf, name='vault_shelf'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('s_item/<int:item_id>/', views.s_item, name='s_item')

    
] 