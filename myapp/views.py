from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.urls import reverse
import requests
import sqlite3
from . import forms
from . import models



# info_blue = requests.get("https://www.infobae.com/pf/api/v3/content/fetch/foreign-currency?query=%7B%22component%22%3A%22foreignCurrency%22%2C%22endTime%22%3A%222023-10-18T23%3A59%3A00%22%2C%22interval%22%3A%22HOUR%22%2C%22mode%22%3A%22default%22%2C%22startTime%22%3A%222023-10-08T00%3A00%3A00%22%2C%22symbol%22%3A%22ARSB%3D%22%7D&d=1623&_website=infobae")
# info_blue_json = info_blue.json()

# info_oficial = requests.get("https://www.infobae.com/pf/api/v3/content/fetch/foreign-currency?query=%7B%22component%22%3A%22foreignCurrency%22%2C%22endTime%22%3A%222023-10-18T23%3A59%3A00%22%2C%22interval%22%3A%22HOUR%22%2C%22mode%22%3A%22default%22%2C%22startTime%22%3A%222023-10-08T00%3A00%3A00%22%2C%22symbol%22%3A%22ARS%3DBNAR%22%7D&d=1623&_website=infobae")
# info_oficial_json = info_oficial.json()

# dolar_blue_compra = info_blue_json["body"]["message"]["buyValue"]
# dolar_blue_venta = info_blue_json["body"]["message"]["sellValue"]
# dolar_oficial_compra = info_oficial_json["body"]["message"]["buyValue"]
# dolar_oficial_venta = info_oficial_json["body"]["message"]["sellValue"]

def index(request):
    return HttpResponse("Hola Mundo!")

# def dolar(request):
    # info = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    # info_json = info.json()
    
    # dolar_oficial_nombre = info_json[0]["casa"]["nombre"]
    # dolar_oficial_compra = info_json[0]["casa"]["compra"]
    # dolar_oficial_venta = info_json[0]["casa"]["venta"]
    
    # dolar_blue_nombre = info_json[1]["casa"]["nombre"]
    # dolar_blue_compra = info_json[1]["casa"]["compra"]
    # dolar_blue_venta = info_json[1]["casa"]["venta"]
    
    
    # html = f"""
    #     <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Dolar</title>
    # </head>
    # <body>
    #     <h1>Precios dolar</h1>
    #     <table style="border:1px solid black">
    #         <tr>
    #             <th></th>
    #             <th>{"Dolar Oficial"}</th>
    #             <th>{"Dolar Blue"}</th>
    #         </tr>
    #         <tr>
    #             <td><strong>Compra</strong></td>
    #             <td>{dolar_oficial_compra}</td>
    #             <td>{dolar_blue_compra}</td>
    #         </tr>            
    #         <tr>
    #             <td><strong>Venta</strong></td>
    #             <td>{dolar_oficial_venta}</td>
    #             <td>{dolar_blue_venta}</td>
    #         </tr>
    #     </table>
    # </body>
    # </html>
    
    # """
    # return HttpResponse(html)

# def dolar_service(request):
#     info = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
#     info_json = info.json()
    

#     dolar_oficial_nombre = info_json[0]["casa"]["nombre"]
#     dolar_oficial_compra = info_json[0]["casa"]["compra"]
#     dolar_oficial_venta = info_json[0]["casa"]["venta"]
    
#     dolar_blue_nombre = info_json[1]["casa"]["nombre"]
#     dolar_blue_compra = info_json[1]["casa"]["compra"]
#     dolar_blue_venta = info_json[1]["casa"]["venta"]
    
#     return JsonResponse({dolar_oficial_nombre:{"Compra":dolar_oficial_compra,"Venta":dolar_oficial_venta},dolar_blue_nombre:{"Compra":dolar_blue_compra,"Venta": dolar_blue_venta}})
    
def about(request):
    return HttpResponse("Curso de Django")


# SIN ORM

# def cursos(request):
#     conn = sqlite3.connect("db.sqlite3")
#     cursor = conn.cursor()
#     cursor.execute("SELECT nombre, inscriptos FROM myapp_curso")
#     cursos = cursor.fetchall()
#     conn.close()
#     ctx = {"cursos": cursos}
#     return render(request, "myapp/cursos.html", ctx)

# CON ORM

def cursos(request):
    cursos = models.Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)


## SIN ORM

# def nuevo_curso(request):
#     if request.method == "POST":
#         form = forms.FormularioCurso(request.POST)
#         if form.is_valid():
#             conn = sqlite3.connect("db.sqlite3")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO myapp_curso VALUES (?, ?)" , (form.cleaned_data["nombre"], form.cleaned_data["inscriptos"]) )
#             conn.commit()
#             conn.close()
#             return HttpResponseRedirect(reverse("cursos"))
#     else:
#         form = forms.FormularioCurso()
#         ctx = {"form": form}
#         return render(request, "myapp/nuevo_curso.html", ctx)

def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():           
            # models.Curso.objects.create(
            #     nombre=form.cleaned_data["nombre"], 
            #     inscriptos=form.cleaned_data["inscriptos"], 
            #     turno=form.cleaned_data["turno"]
            # )
            ## TODo ESO SE REDUCE A:
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:   
        form = forms.FormularioCurso()
        ctx = {"form": form}
        return render(request, "myapp/nuevo_curso.html", ctx)