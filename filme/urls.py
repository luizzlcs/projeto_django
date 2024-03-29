# url -   view - template


from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilmes

app_name = "filme"

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("filmes/", Homefilmes.as_view(), name="homefilmes"),
    path("filmes/<int:pk>", Detalhesfilmes.as_view(), name="detalhesfilme")
]
