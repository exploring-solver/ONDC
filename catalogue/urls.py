from django.urls import path
from . import views


urlpatterns = [
    path('get/', views.GetCatalogues.as_view(), name='get_catalouges'),
    path('create/', views.CreateCatalogue.as_view(), name='create_catalouge'),
    path('get-all/', views.GetAllCatalogues.as_view(), name='get_all_catalouges'),
    path('categories/', views.get_all_categories, name='get_all_categories'),
]

