from django.conf.urls import url
from django.urls import path
from cancer_app import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('welcomeAdmin/',views.welcomeAdmin,name='welcomeAdmin'),
    path('welcomeLab/',views.welcomeLab,name='welcomeLab'),
    path('breastAccuracy/',views.breastAccuracy,name='breastAccuracy'),
    path('prostateAccuracy/',views.prostateAccuracy,name='prostateAccuracy'),
    path('testBreast/',views.testBreast,name='testBreast'),
    path('testProstate/',views.testProstate,name='testProstate'),
    # path('executescript/',views.index_script,name='execute'),
    path('patient_detail_P/',views.patient_detail_P,name='patient_detail_P'),
    path('patient_detail_B/',views.patient_detail_B,name='patient_detail_B'),
    path('admin_statistics/',views.admin_statistics,name='admin_statistics'),
    path('admin_statistics1/',views.admin_statistics1,name='admin_statistics1'),
    path('patientTested/',views.patientTested,name='patientInfo'),
    path('p_dim_red/',views.p_dim_red,name='p_dim_red'),
    path('b_dim_red/',views.b_dim_red,name='b_dim_red'),
    path('breast_chart/',views.breast_chart,name='breast_chart'),
    path('prostate_chart/',views.prostate_chart,name='prostate_chart'),
    path('result_chart/',views.result_chart,name='result_chart'),
    path('test1/',views.test1,name="test1"),
    path('test2/',views.test2,name="test2"),
    ]
