import os
from django.shortcuts import render
from django.http import HttpResponse
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cancer_project.settings')

import django
django.setup()

from cancer_app.models import svmP
from cancer_app.models import svmB
from cancer_app.models import dtP
from cancer_app.models import dtB
from cancer_app.models import lrP
from cancer_app.models import lrB
from cancer_app.models import rfP
from cancer_app.models import rfB
from cancer_app.models import nbP
from cancer_app.models import nbB
from cancer_app.models import nbB_D
from cancer_app.models import nbP_D
from cancer_app.models import rfB_D
from cancer_app.models import rfP_D
from cancer_app.models import lrB_D
from cancer_app.models import lrP_D
from cancer_app.models import dtB_D
from cancer_app.models import dtP_D
from cancer_app.models import svmB_D
from cancer_app.models import svmP_D


from cancer_app.models import patient
from cancer_app import with_k_folds
from cancer_app import with_k_folds_breast
from cancer_app import without_k_folds
from cancer_app import without_k_folds_breast
from cancer_app import prostate_dr
from cancer_app import breast_dr

from cancer_app import views


def populate_data():
    svm0 = without_k_folds.svm()
    svm5 = with_k_folds.svm_5()
    svm10 = with_k_folds.svm_10()
    svm15 = with_k_folds.svm_15()
    svm20 = with_k_folds.svm_20()

    dt0 = without_k_folds.dt()
    dt5 = with_k_folds.dt_5()
    dt10 = with_k_folds.dt_10()
    dt15 = with_k_folds.dt_15()
    dt20 = with_k_folds.dt_20()

    lr0 = without_k_folds.lr()
    lr5 = with_k_folds.lr_5()
    lr10 = with_k_folds.lr_10()
    lr15 = with_k_folds.lr_15()
    lr20 = with_k_folds.lr_20()

    rf0 = without_k_folds.rf()
    rf5 = with_k_folds.rf_5()
    rf10 = with_k_folds.rf_10()
    rf15 = with_k_folds.rf_15()
    rf20 = with_k_folds.rf_20()

    nb0 = without_k_folds.nb()
    nb5 = with_k_folds.nb_5()
    nb10 = with_k_folds.nb_10()
    nb15 = with_k_folds.nb_15()
    nb20 = with_k_folds.nb_20()

    populate_svmP = svmP.objects.get_or_create(svmP_fold_0 = svm0, svmP_fold_5 = svm5, svmP_fold_10 = svm10, svmP_fold_15 = svm15, svmP_fold_20 = svm20)[0]
    populate_dtP = dtP.objects.get_or_create(dtP_fold_0 = dt0, dtP_fold_5 = dt5, dtP_fold_10 = dt10, dtP_fold_15 = dt15, dtP_fold_20 = dt20)[0]
    populate_lrP = lrP.objects.get_or_create(lrP_fold_0 = lr0, lrP_fold_5 = lr5, lrP_fold_10 = lr10, lrP_fold_15 = lr15, lrP_fold_20 = lr20)[0]
    populate_rfP = rfP.objects.get_or_create(rfP_fold_0 = rf0, rfP_fold_5 = rf5, rfP_fold_10 = rf10, rfP_fold_15 = rf15, rfP_fold_20 = rf20)[0]
    populate_nbP = nbP.objects.get_or_create(nbP_fold_0 = nb0, nbP_fold_5 = nb5, nbP_fold_10 = nb10, nbP_fold_15 = nb15, nbP_fold_20 = nb20)[0]

    my_dict = {'p_0_nb':nb0,'p_0_svm':svm0,'p_0_lr':lr0,'p_0_dt':dt0,'p_0_rf':rf0,
               'p_5_nb':nb5,'p_10_nb':nb10,'p_15_nb':nb15,'p_20_nb':nb20,
               'p_5_lr':lr5,'p_10_lr':lr10,'p_15_lr':lr15,'p_20_lr':lr20,
               'p_5_dt':dt5,'p_10_dt':dt10,'p_15_dt':dt15,'p_20_dt':dt20,
               'p_5_svm':svm5,'p_10_svm':svm10,'p_15_svm':svm15,'p_20_svm':svm20,
               'p_5_rf':rf5,'p_10_rf':rf10,'p_15_rf':rf15,'p_20_rf':rf20}
    return my_dict


def populate_dim_P():
    svm0 = prostate_dr.svm()
    svm5 = prostate_dr.svm_5()
    svm10 = prostate_dr.svm_10()
    svm15 = prostate_dr.svm_15()
    svm20 = prostate_dr.svm_20()

    dt0 = prostate_dr.dt()
    dt5 = prostate_dr.dt_5()
    dt10 = prostate_dr.dt_10()
    dt15 = prostate_dr.dt_15()
    dt20 = prostate_dr.dt_20()

    lr0 = prostate_dr.lr()
    lr5 = prostate_dr.lr_5()
    lr10 = prostate_dr.lr_10()
    lr15 = prostate_dr.lr_15()
    lr20 = prostate_dr.lr_20()

    rf0 = prostate_dr.rf()
    rf5 = prostate_dr.rf_5()
    rf10 = prostate_dr.rf_10()
    rf15 = prostate_dr.rf_15()
    rf20 = prostate_dr.rf_20()

    nb0 = prostate_dr.nb()
    nb5 = prostate_dr.nb_5()
    nb10 = prostate_dr.nb_10()
    nb15 = prostate_dr.nb_15()
    nb20 = prostate_dr.nb_20()

    populate_svmP_D = svmP_D.objects.get_or_create(svmPD_fold_0 = svm0, svmPD_fold_5 = svm5, svmPD_fold_10 = svm10, svmPD_fold_15 = svm15, svmPD_fold_20 = svm20)[0]
    populate_dtP_D = dtP_D.objects.get_or_create(dtPD_fold_0 = dt0, dtPD_fold_5 = dt5, dtPD_fold_10 = dt10, dtPD_fold_15 = dt15, dtPD_fold_20 = dt20)[0]
    populate_lrP_D = lrP_D.objects.get_or_create(lrPD_fold_0 = lr0, lrPD_fold_5 = lr5, lrPD_fold_10 = lr10, lrPD_fold_15 = lr15, lrPD_fold_20 = lr20)[0]
    populate_rfP_D = rfP_D.objects.get_or_create(rfPD_fold_0 = rf0, rfPD_fold_5 = rf5, rfPD_fold_10 = rf10, rfPD_fold_15 = rf15, rfPD_fold_20 = rf20)[0]
    populate_nbP_D = nbP_D.objects.get_or_create(nbPD_fold_0 = nb0, nbPD_fold_5 = nb5, nbPD_fold_10 = nb10, nbPD_fold_15 = nb15, nbPD_fold_20 = nb20)[0]

    my_dict = {'pd_0_nb':nb0,'pd_0_svm':svm0,'pd_0_lr':lr0,'pd_0_dt':dt0,'pd_0_rf':rf0,
               'pd_5_nb':nb5,'pd_10_nb':nb10,'pd_15_nb':nb15,'pd_20_nb':nb20,
               'pd_5_lr':lr5,'pd_10_lr':lr10,'pd_15_lr':lr15,'pd_20_lr':lr20,
               'pd_5_dt':dt5,'pd_10_dt':dt10,'pd_15_dt':dt15,'pd_20_dt':dt20,
               'pd_5_svm':svm5,'pd_10_svm':svm10,'pd_15_svm':svm15,'pd_20_svm':svm20,
               'pd_5_rf':rf5,'pd_10_rf':rf10,'pd_15_rf':rf15,'pd_20_rf':rf20}
    return my_dict


def populate_dim_B():
    svm0 = breast_dr.svm()
    svm5 = breast_dr.svm_5()
    svm10 = breast_dr.svm_10()
    svm15 = breast_dr.svm_15()
    svm20 = breast_dr.svm_20()

    dt0 = breast_dr.dt()
    dt5 = breast_dr.dt_5()
    dt10 = breast_dr.dt_10()
    dt15 = breast_dr.dt_15()
    dt20 = breast_dr.dt_20()

    lr0 = breast_dr.lr()
    lr5 = breast_dr.lr_5()
    lr10 = breast_dr.lr_10()
    lr15 = breast_dr.lr_15()
    lr20 = breast_dr.lr_20()

    rf0 = breast_dr.rf()
    rf5 = breast_dr.rf_5()
    rf10 = breast_dr.rf_10()
    rf15 = breast_dr.rf_15()
    rf20 = breast_dr.rf_20()

    nb0 = breast_dr.nb()
    nb5 = breast_dr.nb_5()
    nb10 = breast_dr.nb_10()
    nb15 = breast_dr.nb_15()
    nb20 = breast_dr.nb_20()

    populate_svmB_D = svmB_D.objects.get_or_create(svmBD_fold_0 = svm0, svmBD_fold_5 = svm5, svmBD_fold_10 = svm10, svmBD_fold_15 = svm15, svmBD_fold_20 = svm20)[0]
    populate_dtB_D = dtB_D.objects.get_or_create(dtBD_fold_0 = dt0, dtBD_fold_5 = dt5, dtBD_fold_10 = dt10, dtBD_fold_15 = dt15, dtBD_fold_20 = dt20)[0]
    populate_lrB_D = lrB_D.objects.get_or_create(lrBD_fold_0 = lr0, lrBD_fold_5 = lr5, lrBD_fold_10 = lr10, lrBD_fold_15 = lr15, lrBD_fold_20 = lr20)[0]
    populate_rfB_D = rfB_D.objects.get_or_create(rfBD_fold_0 = rf0, rfBD_fold_5 = rf5, rfBD_fold_10 = rf10, rfBD_fold_15 = rf15, rfBD_fold_20 = rf20)[0]
    populate_nbB_D = nbB_D.objects.get_or_create(nbBD_fold_0 = nb0, nbBD_fold_5 = nb5, nbBD_fold_10 = nb10, nbBD_fold_15 = nb15, nbBD_fold_20 = nb20)[0]

    my_dict = {'bd_0_nb':nb0,'bd_0_svm':svm0,'bd_0_lr':lr0,'bd_0_dt':dt0,'bd_0_rf':rf0,
               'bd_5_nb':nb5,'bd_10_nb':nb10,'bd_15_nb':nb15,'bd_20_nb':nb20,
               'bd_5_lr':lr5,'bd_10_lr':lr10,'bd_15_lr':lr15,'bd_20_lr':lr20,
               'bd_5_dt':dt5,'bd_10_dt':dt10,'bd_15_dt':dt15,'bd_20_dt':dt20,
               'bd_5_svm':svm5,'bd_10_svm':svm10,'bd_15_svm':svm15,'bd_20_svm':svm20,
               'bd_5_rf':rf5,'bd_10_rf':rf10,'bd_15_rf':rf15,'bd_20_rf':rf20}
    return my_dict


def populate_patient_dataP(my_dict):
    populate_patient = patient.objects.get_or_create(test_type = "Prostate Cancer", first_name= my_dict['first_name'], last_name = my_dict['last_name'], dob = my_dict['dob'], gender = my_dict['gender'], blood_grp = my_dict['blood_grp'], parents_name=my_dict['parents_name'], spouse_name = my_dict['spouse_name'], result = my_dict['result'])[0]

def populate_patient_dataB(my_dict):
    populate_patient = patient.objects.get_or_create(test_type = "Breast Cancer", first_name= my_dict['first_name'], last_name = my_dict['last_name'], dob = my_dict['dob'], gender = my_dict['gender'], blood_grp = my_dict['blood_grp'], parents_name=my_dict['parents_name'], spouse_name = my_dict['spouse_name'], result = my_dict['result'])[0]


def populate_data_b():
    svm0 = without_k_folds_breast.svm()
    svm5 = with_k_folds_breast.svm_5()
    svm10 = with_k_folds_breast.svm_10()
    svm15 = with_k_folds_breast.svm_15()
    svm20 = with_k_folds_breast.svm_20()

    dt0 = without_k_folds_breast.dt()
    dt5 = with_k_folds_breast.dt_5()
    dt10 = with_k_folds_breast.dt_10()
    dt15 = with_k_folds_breast.dt_15()
    dt20 = with_k_folds_breast.dt_20()

    lr0 = without_k_folds_breast.lr()
    lr5 = with_k_folds_breast.lr_5()
    lr10 = with_k_folds_breast.lr_10()
    lr15 = with_k_folds_breast.lr_15()
    lr20 = with_k_folds_breast.lr_20()

    rf0 = without_k_folds_breast.rf()
    rf5 = with_k_folds_breast.rf_5()
    rf10 = with_k_folds_breast.rf_10()
    rf15 = with_k_folds_breast.rf_15()
    rf20 = with_k_folds_breast.rf_20()

    nb0 = without_k_folds_breast.nb()
    nb5 = with_k_folds_breast.nb_5()
    nb10 = with_k_folds_breast.nb_10()
    nb15 = with_k_folds_breast.nb_15()
    nb20 = with_k_folds_breast.nb_20()


    populate_svmB = svmB.objects.get_or_create(svmB_fold_0 = svm0, svmB_fold_5 = svm5, svmB_fold_10 = svm10, svmB_fold_15 = svm15, svmB_fold_20 = svm20)[0]
    populate_dtB = dtB.objects.get_or_create(dtB_fold_0 = dt0, dtB_fold_5 = dt5, dtB_fold_10 = dt10, dtB_fold_15 = dt15, dtB_fold_20 = dt20)[0]
    populate_lrB = lrB.objects.get_or_create(lrB_fold_0 = lr0, lrB_fold_5 = lr5, lrB_fold_10 = lr10, lrB_fold_15 = lr15, lrB_fold_20 = lr20)[0]
    populate_rfB = rfB.objects.get_or_create(rfB_fold_0 = rf0, rfB_fold_5 = rf5, rfB_fold_10 = rf10, rfB_fold_15 = rf15, rfB_fold_20 = rf20)[0]
    populate_nbB = nbB.objects.get_or_create(nbB_fold_0 = nb0, nbB_fold_5 = nb5, nbB_fold_10 = nb10, nbB_fold_15 = nb15, nbB_fold_20 = nb20)[0]

    my_dict_b = {'b_0_nb':nb0,'b_0_svm':svm0,'b_0_dt':dt0,'b_0_rf':rf0,'b_0_lr':lr0,
               'b_5_nb':nb5,'b_10_nb':nb10,'b_15_nb':nb15,'b_20_nb':nb20,
               'b_5_lr':lr5,'b_10_lr':lr10,'b_15_lr':lr15,'b_20_lr':lr20,
               'b_5_dt':dt5,'b_10_dt':dt10,'b_15_dt':dt15,'b_20_dt':dt20,
               'b_5_svm':svm5,'b_10_svm':svm10,'b_15_svm':svm15,'b_20_svm':svm20,
               'b_5_rf':rf5,'b_10_rf':rf10,'b_15_rf':rf15,'b_20_rf':rf20}
    return my_dict_b
