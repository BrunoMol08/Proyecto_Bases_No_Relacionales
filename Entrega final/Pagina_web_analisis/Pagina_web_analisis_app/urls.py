from django.urls import path

from Pagina_web_analisis_app import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('analisis_EPN_AMLO',views.analisis_EPN_AMLO,name="Analisis EPN vs AMLO"),
    path('analisis_tf_idf',views.analisis_tf_idf,name="Analisis TF IDF"),
    path('tf_idf',views.tf_idf,name="TF IDF"),
    path('contacto',views.contacto,name='Contacto'),
    path('consulta_tf_idf',views.consutla_tf_idf, name='Consulta_tf_id'),
    path('quienes_somos',views.quienes_somos, name='Quienes somos'),
    path('que_hacemos',views.que_hacemos, name='Que hacemos'),
    path('busqueda_iniciativas', views.busqueda_iniciativas, name="Busqueda iniciativas"),
    path('busqueda_id',views.busqueda_id, name="Busqueda id"),
    path('definicion_tfidf', views.def_tfidf, name="Definición tfidf"),
]