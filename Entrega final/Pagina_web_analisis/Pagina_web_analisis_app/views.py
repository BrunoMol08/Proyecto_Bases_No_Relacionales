from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail

from django.conf import settings
from Pagina_web_analisis_app.proyecto_bases import id_token, id_propuesta_ley
from Pagina_web_analisis_app.forms import UserForm, UserFormId
from Pagina_web_analisis_app.carga_data import obtener_datos, obtener_id

# Create your views here.

def home(request):

    return render(request,'Pagina_web_analisis_app/home.html')

def analisis_EPN_AMLO(request):

    return render(request,'Pagina_web_analisis_app/analisis_EPN_AMLO.html')

def analisis_tf_idf(request):

    return render(request,'Pagina_web_analisis_app/analisis_tf_idf.html')

def tf_idf(request):

    return render(request,'Pagina_web_analisis_app/tf_idf.html')

def quienes_somos(request):

    return render(request,'Pagina_web_analisis_app/quienes_somos.html')

def que_hacemos(request):

    return render(request,'Pagina_web_analisis_app/que_hacemos.html')

def consutla_tf_idf(request):

    if request.GET['id_token'] and request.GET['id_iniciativa']:

        try:

            id_tok = request.GET['id_token']

            id_token(id_tok)

            id_iniciativa = request.GET['id_iniciativa']

            dic = id_propuesta_ley(int(id_iniciativa))

            dic['iniciativa'] = id_iniciativa

            return render(request, "Pagina_web_analisis_app/resultados_tfidf.html",dic)
        except:
            
            return render(request,"Pagina_web_analisis_app/salida_err_execute.html")

    else:
        
        return render(request,"Pagina_web_analisis_app/salida_err.html")

def contacto(request):

    if request.method == "POST":

        try: 
            subject = request.POST['asunto']

            message = request.POST['mensaje'] + " " + request.POST['nombre'] + " " + request.POST['email']

            email_from = settings.EMAIL_HOST_USER

            recipient_list = ["bmolinaz@itam.mx"]

            send_mail(subject,message,email_from,recipient_list)

            return render(request, "Pagina_web_analisis_app/salida.html")

        except:

            return render(request, "Pagina_web_analisis_app/salida_err.html")
    else:
        
        return render(request, 'Pagina_web_analisis_app/contacto.html')

def busqueda_iniciativas(request):
    
    if request.method == "GET":
        
        busqueda = UserForm(request.GET)

        if busqueda.is_valid():
            datos = busqueda.cleaned_data

            try:
                tipo = datos['tipo']
                ley = datos['ley_modificada']
                sexenio = datos['sexenio']
                cant = datos.get('limit','')

                dic = {}
                lista = obtener_datos(tipo,ley,sexenio,cant)
                dic["resultados"] = lista

                return render(request,"Pagina_web_analisis_app/resultados_busqueda.html",dic)

            except:

                return render(request,"Pagina_web_analisis_app/salida_err_busqueda.html")
    else:

        busqueda = UserForm()

    return render(request,"Pagina_web_analisis_app/busqueda_iniciativas.html",{'form':busqueda})


def busqueda_id(request):
    
    if request.method == "GET":
        
        busqueda = UserFormId(request.GET)

        if busqueda.is_valid():
            datos = busqueda.cleaned_data

            try:
                id = datos.get('id','')
                id_2 = datos.get('id_2','')
                id_3 = datos.get('id_3','')
                id_4 = datos.get('id_4','')
                id_5 = datos.get('id_5','')

                dic = {}
                lista = obtener_id(id,id_2,id_3,id_4,id_5)
                dic["resultados"] = lista

                return render(request,"Pagina_web_analisis_app/resultados_id.html",dic)

            except:

                return render(request,"Pagina_web_analisis_app/salida_err_busqueda.html")
    else:

        busqueda = UserForm()

    return render(request,"Pagina_web_analisis_app/busqueda_id.html",{'form':busqueda})

def def_tfidf(request):

    return render(request,'Pagina_web_analisis_app/definicion_tfidf.html')