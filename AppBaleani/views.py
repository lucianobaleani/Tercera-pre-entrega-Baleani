from django.shortcuts import render
from .models import Comic, Author, Editorial
from .forms import ComicForm, AuthorForm, EditorialForm


def home(request):
    return render(request, "home.html")


# CRUD Autores
def authors(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name = info["name"]
            role = info["role"]
            nationality = info["nationality"]
            author = Author(name=name, role=role, nationality=nationality)
            author.save()
            message = "Autor Creado!!"
        else:
            message = "Datos Incorrectos"
        authors = Author.objects.all()
        author_form = AuthorForm()
        return render(
            request,
            "authors.html",
            {
                "message": message,
                "form": author_form,
                "authors": authors,
            },
        )
    else:
        author_form = AuthorForm()
        authors = Author.objects.all()

    return render(
        request,
        "authors.html",
        {"form": author_form, "authors": authors},
    )


def edit_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            author.name = info["name"]
            author.role = info["role"]
            author.nationality = info["nationality"]
            author.save()
            message = "Autor Modificado!"
            authors = Author.objects.all()
            author_form = AuthorForm()
            return render(
                request,
                "authors.html",
                {
                    "message": message,
                    "form": author_form,
                    "authors": authors,
                },
            )
    else:
        author_form = AuthorForm(
            initial={
                "name": author.name,
                "role": author.role,
                "nationality": author.nationality,
            }
        )
        return render(
            request,
            "editAuthor.html",
            {"form": author_form, "author": author},
        )


def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    authors = Author.objects.all()
    author_form = AuthorForm()
    message = "Autor eliminado"
    return render(
        request,
        "authors.html",
        {
            "message": message,
            "form": author_form,
            "authors": authors,
        },
    )


def author_result(request):
    return render(request, "author_result.html")


def search_author(request):
    name = request.GET["name"]
    if name != "":
        authors = Author.objects.filter(name__icontains=name)
        return render(request, "author_result.html", {"authors": authors})
    return render(
        request,
        "searchAuthor.html",
        {"message": "Por favor inserte un Nombre"},
    )


# CRUD EDITORIALES


def editorials(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name = info["name"]
            country = info["country"]
            state = info["state"]
            editorial = Editorial(name=name, country=country, state=state)
            editorial.save()
            message = "Editorial Creada!!"
        else:
            message = "Datos Incorrectos"
        editorials = Editorial.objects.all()
        editorial_form = EditorialForm()
        return render(
            request,
            "editorials.html",
            {
                "message": message,
                "form": editorial_form,
                "editorials": editorials,
            },
        )
    else:
        editorials = Editorial.objects.all()
        editorial_form = EditorialForm()

    return render(
        request,
        "editorials.html",
        {"form": editorial_form, "editorials": editorials},
    )


def edit_editorial(request, id):
    editorial = Editorial.objects.get(id=id)
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            editorial.name = info["name"]
            editorial.country = info["country"]
            editorial.state = info["state"]
            editorial.save()
            message = "Autor Modificado!"
            editorials = Editorial.objects.all()
            editorial_form = EditorialForm()
            return render(
                request,
                "editorials.html",
                {
                    "message": message,
                    "form": editorial_form,
                    "editorials": editorials,
                },
            )
    else:
        editorial_form = EditorialForm(
            initial={
                "name": editorial.name,
                "country": editorial.country,
                "state": editorial.state,
            }
        )
        return render(
            request,
            "editEditorial.html",
            {"form": editorial_form, "editorial": editorial},
        )


def delete_editorial(request, id):
    editorial = Editorial.objects.get(id=id)
    editorial.delete()
    editorials = Editorial.objects.all()
    editorial_form = EditorialForm()
    message = "Editorial eliminada"
    return render(
        request,
        "editorials.html",
        {
            "message": message,
            "form": editorial_form,
            "editorials": editorials,
        },
    )


def editorial_result(request):
    return render(request, "editorial_result.html")


def search_editorial(request):
    name = request.GET["name"]
    if name != "":
        editorials = Editorial.objects.filter(name__icontains=name)
        return render(request, "editorial_result.html", {"editorials": editorials})
    return render(
        request,
        "searchEditorial.html",
        {"message": "Por favor inserte una Editorial"},
    )


# CRUD COMICS


def comics(request):
    if request.method == "POST":
        form = ComicForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name = info["name"]
            published_year = info["published_year"]
            editorial = info["editorial"]
            comic = Comic(name=name, published_year=published_year, editorial=editorial)
            comic.save()
            message = "Comic Creado!!"
        else:
            message = "Datos Incorrectos"
        comics = Comic.objects.all()
        comic_form = ComicForm()

        return render(
            request,
            "comics.html",
            {
                "message": message,
                "form": comic_form,
                "comics": comics,
            },
        )
    else:
        comics = Comic.objects.all()
        comic_form = ComicForm()
    return render(
        request,
        "comics.html",
        {"form": comic_form, "comics": comics},
    )


def edit_comic(request, id):
    comic = Comic.objects.get(id=id)
    if request.method == "POST":
        form = ComicForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            comic.name = info["name"]
            comic.published_year = info["published_year"]
            comic.editorial = info["editorial"]
            comic.save()
            message = "Comic Modificado!"
            comics = Comic.objects.all()
            comic_form = ComicForm()
            return render(
                request,
                "comics.html",
                {
                    "message": message,
                    "form": comic_form,
                    "comics": comics,
                },
            )
    else:
        comic_form = ComicForm(
            initial={
                "name": comic.name,
                "published_year": comic.published_year,
                "editorial": comic.editorial,
            }
        )
        return render(
            request,
            "editComic.html",
            {"form": comic_form, "comic": comic},
        )


def delete_comic(request, id):
    comic = Comic.objects.get(id=id)
    comic.delete()
    comics = Comic.objects.all()
    comic_form = ComicForm()
    message = "Comic eliminado"
    return render(
        request,
        "comics.html",
        {
            "message": message,
            "form": comic_form,
            "comics": comics,
        },
    )


def comic_result(request):
    return render(request, "comic_result.html")


def search_comic(request):
    name = request.GET["name"]
    if name != "":
        comics = Comic.objects.filter(name__icontains=name)
        return render(request, "comic_result.html", {"comics": comics})
    return render(
        request,
        "searchComic.html",
        {"message": "Por favor inserte un Nombre para buscar Comics"},
    )
