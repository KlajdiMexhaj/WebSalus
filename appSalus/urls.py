from . import views
from django.urls import path
from django.views.i18n import set_language


urlpatterns = [
    path("",views.home,name="home"),
    path("mjeket/",views.mjeket,name="mjeket"),
    path("mjeket_detail/<str:pk>/",views.mjeket_detail,name="mjeket_detail"),
    path("specialitet/",views.specialitet,name="specialitet"),
    path("specialitet_detail/<str:pk>/",views.specialitet_detail,name="specialitet_detail"),
    path("check-up/",views.checkup,name="checkup"),
    path("about/",views.about,name="about"),
    path("klinikaefertilizimit/",views.klinikaefertilizimit,name="klinikaefertilizimit"),
    path("klinikaferte_detail/<str:pk>/",views.klinikaferte_detail,name="klinikaferte_detail"),
    path("AeMC/",views.aemc,name="aemc"),
    path("kartaeshendetit/",views.kartaeshendetit,name="kartaeshendetit"),
    path("artikuj-informues/",views.artikuj_informues,name="artikuj_informues"),
    path("artinfodetail/<str:pk>/",views.artinfodetail,name="artinfodetail"),
    path("contact/",views.contact,name="contact"),
    path("politikaeprivatesise/",views.politikaeprivatesise,name="politikaeprivatesise"),
    path("artikujt_informues_AeMC/",views.aemc,name="artikujt_informues_AeMC"),
    path("artinfodetail_Aemc/<str:pk>/",views.artikujt_informuesAeMC,name="artikujt_informuesAeMC"),
    path("artikuj_informues_KartaInSalus/",views.kartaeshendetit,name="artikuj_informues_KartaInSalus"),
    path("artinfodetail_InSalus/<str:pk>/",views.artikujt_informuesInSalus,name="artikujt_informuesInSalus"),
    path("artikujt_informues_DonnaSalus/",views.klinikaefertilizimit,name="artikujt_informues_DonnaSalus"),
    path("artinfodetail_DonnaSalas/<str:pk>/",views.artikujt_informuesDonnaSalus,name="artikujt_informuesDonnaSalus"),
    path("navbar/",views.navbar,name="navbar"),
    path("translate/",views.translate,name="translate"),
    path('set_language/', set_language, name='set_language'),  # Language switcher URL
    path('videos/', views.video_list, name='video_list'),
    path('search/', views.search, name='search'),




]