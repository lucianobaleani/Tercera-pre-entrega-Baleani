from django.urls import path
from .views import *

urlpatterns = [
    # HOME
    path("", home, name="home"),
    # AUTORES
    path("autores/", authors, name="authors"),
    path("editarAutor/<id>", edit_author, name="editAuthor"),
    path("eliminarAutor/<id>", delete_author, name="deleteAuthor"),
    path("buscarAutor/", search_author, name="searchAuthor"),
    path("resultadoAutores/", author_result, name="author_result"),
    # COMICS
    path("comics/", comics, name="comics"),
    path("editarComic/<id>", edit_comic, name="editComic"),
    path("eliminarComic/<id>", delete_comic, name="deleteComic"),
    path("buscarComic/", search_comic, name="searchComic"),
    path("resultadoComic/", comic_result, name="Comic_result"),
    # EDITORIAL
    path("editorials/", editorials, name="editorials"),
    path("editarEditorial/<id>", edit_editorial, name="editEditorial"),
    path("eliminarEditorial/<id>", delete_editorial, name="deleteEditorial"),
    path("buscarEditorial/", search_editorial, name="searchEditorial"),
    path("resultadoAutores/", editorial_result, name="editorial_result"),
]
