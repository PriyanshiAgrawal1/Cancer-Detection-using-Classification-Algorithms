from django.shortcuts import render
from django.http import HttpResponse
from cancer_app import test_algo
from cancer_app import without_k_folds
from cancer_app import without_k_folds_breast
from cancer_app import with_k_folds
from cancer_app import with_k_folds_breast
from cancer_app.models import patient
from django.template import loader
from cancer_app.models import svmP,dtP,lrP,rfP,nbP,svmB,dtB,lrB,rfB,nbB,svmB_D,dtB_D,lrB_D,rfB_D,nbB_D,svmP_D,dtP_D,lrP_D,rfP_D,nbP_D
from cancer_app import test_algo
from cancer_app import breast_dr
from cancer_app import prostate_dr
import populate
# Create your views here.

admin_login = "fal"
lab_login = "fal"

def test(request):
    return HttpResponse("Hi there")

def bird_first_page(request):
    return render(request,'cancer/bird_first_page.html')

def image_input(request):
    return render(request,'cancer/image_input.html')

def bird_statistics(request):
    return render(request,'cancer/bird_statistics.html')

def how_it_works(request):
    return render(request,'cancer/how_it_works.html')

def about_us(request):
    return render(request,'cancer/about_us.html')

def index(request):
    # my_dict = {'insert':test.solve()}
    return render(request,'cancer/login.html')

def login(request):
    dict = {'admin_login':admin_login,'lab_login':lab_login}
    return render(request,'cancer/login.html',context=dict)

def admin_statistics1(request):
    return render(request,'cancer/admin_statistics_1.html')

def welcomeAdmin(request):
    # return HttpResponse(admin_login);
    svmP_list = svmP.objects.order_by('-svmP_date')
    dtP_list=dtP.objects.order_by('-dtP_date')
    lrP_list=lrP.objects.order_by('-lrP_date')
    rfP_list=rfP.objects.order_by('-rfP_date')
    nbP_list=nbP.objects.order_by('-nbP_date')

    def avg_smvP():
        sum_svmP_0 = 0
        count_svmP_0 = 0
        sum_svmP_5 = 0
        count_svmP_5 = 0
        sum_svmP_10 = 0
        count_svmP_10 = 0
        sum_svmP_15 = 0
        count_svmP_15 = 0
        sum_svmP_20 = 0
        count_svmP_20 = 0
        for var in svmP_list:
            sum_svmP_0+=var.svmP_fold_0
            sum_svmP_5+=var.svmP_fold_5
            sum_svmP_10+=var.svmP_fold_10
            sum_svmP_15+=var.svmP_fold_15
            sum_svmP_20+=var.svmP_fold_20
            count_svmP_0+=1
            count_svmP_5+=1
            count_svmP_10+=1
            count_svmP_15+=1
            count_svmP_20+=1
        return (round(sum_svmP_0/count_svmP_0,2),round(sum_svmP_5/count_svmP_5,2),round(sum_svmP_10/count_svmP_10,2),round(sum_svmP_15/count_svmP_15,2),round(sum_svmP_20/count_svmP_20,2))
    avg_svmP_0,avg_svmP_5,avg_svmP_10,avg_svmP_15,avg_svmP_20 = avg_smvP()

    def avg_dtP():
        sum_dtP_0=0
        count_dtP_0=0
        sum_dtP_5=0
        count_dtP_5=0
        sum_dtP_10=0
        count_dtP_10=0
        sum_dtP_15=0
        count_dtP_15=0
        sum_dtP_20=0
        count_dtP_20=0
        for var in dtP_list:
            sum_dtP_0+=var.dtP_fold_0
            sum_dtP_5+=var.dtP_fold_5
            sum_dtP_10+=var.dtP_fold_10
            sum_dtP_15+=var.dtP_fold_15
            sum_dtP_20+=var.dtP_fold_20
            count_dtP_0+=1
            count_dtP_5+=1
            count_dtP_10+=1
            count_dtP_15+=1
            count_dtP_20+=1
        return(round(sum_dtP_0/count_dtP_0,2),round(sum_dtP_5/count_dtP_5,2),round(sum_dtP_10/count_dtP_10,2),round(sum_dtP_15/count_dtP_15,2),round(sum_dtP_20/count_dtP_20,2))
    avg_dtP_0,avg_dtP_5,avg_dtP_10,avg_dtP_15,avg_dtP_20 = avg_dtP()

    def avg_lrP():
        sum_lrP_0=0
        count_lrP_0=0
        sum_lrP_5=0
        count_lrP_5=0
        sum_lrP_10=0
        count_lrP_10=0
        sum_lrP_15=0
        count_lrP_15=0
        sum_lrP_20=0
        count_lrP_20=0
        for var in lrP_list:
            sum_lrP_0+=var.lrP_fold_0
            sum_lrP_5+=var.lrP_fold_5
            sum_lrP_10+=var.lrP_fold_10
            sum_lrP_15+=var.lrP_fold_15
            sum_lrP_20+=var.lrP_fold_20
            count_lrP_0+=1
            count_lrP_5+=1
            count_lrP_10+=1
            count_lrP_15+=1
            count_lrP_20+=1
        return(round(sum_lrP_0/count_lrP_0,2),round(sum_lrP_5/count_lrP_5,2),round(sum_lrP_10/count_lrP_10,2),round(sum_lrP_15/count_lrP_15,2),round(sum_lrP_20/count_lrP_20,2))
    avg_lrP_0,avg_lrP_5,avg_lrP_10,avg_lrP_15,avg_lrP_20 = avg_lrP()

    def avg_rfP():
        sum_rfP_0=0
        count_rfP_0=0
        sum_rfP_5=0
        count_rfP_5=0
        sum_rfP_10=0
        count_rfP_10=0
        sum_rfP_15=0
        count_rfP_15=0
        sum_rfP_20=0
        count_rfP_20=0
        for var in rfP_list:
            sum_rfP_0+=var.rfP_fold_0
            sum_rfP_5+=var.rfP_fold_5
            sum_rfP_10+=var.rfP_fold_10
            sum_rfP_15+=var.rfP_fold_15
            sum_rfP_20+=var.rfP_fold_20
            count_rfP_0+=1
            count_rfP_5+=1
            count_rfP_10+=1
            count_rfP_15+=1
            count_rfP_20+=1
        return(round(sum_rfP_0/count_rfP_0,2),round(sum_rfP_5/count_rfP_5,2),round(sum_rfP_10/count_rfP_10,2),round(sum_rfP_15/count_rfP_15,2),round(sum_rfP_20/count_rfP_20,2))
    avg_rfP_0,avg_rfP_5,avg_rfP_10,avg_rfP_15,avg_rfP_20 = avg_rfP()

    def avg_nbP():
        sum_nbP_0=0
        count_nbP_0=0
        sum_nbP_5=0
        count_nbP_5=0
        sum_nbP_10=0
        count_nbP_10=0
        sum_nbP_15=0
        count_nbP_15=0
        sum_nbP_20=0
        count_nbP_20=0
        for var in nbP_list:
            sum_nbP_0+=var.nbP_fold_0
            sum_nbP_5+=var.nbP_fold_5
            sum_nbP_10+=var.nbP_fold_10
            sum_nbP_15+=var.nbP_fold_15
            sum_nbP_20+=var.nbP_fold_20
            count_nbP_0+=1
            count_nbP_5+=1
            count_nbP_10+=1
            count_nbP_15+=1
            count_nbP_20+=1
        return(round(sum_nbP_0/count_nbP_0,2),round(sum_nbP_5/count_nbP_5,2),round(sum_nbP_10/count_nbP_10,2),round(sum_nbP_15/count_nbP_15,2),round(sum_nbP_20/count_nbP_20,2))
    avg_nbP_0,avg_nbP_5,avg_nbP_10,avg_nbP_15,avg_nbP_20 = avg_nbP()

    svm_final_avg = round((avg_svmP_0+avg_svmP_5+avg_svmP_10+avg_svmP_15+avg_svmP_20)/5,2)
    dt_final_avg = round((avg_dtP_0+avg_dtP_5+avg_dtP_10+avg_dtP_15+avg_dtP_20)/5,2)
    lr_final_avg = round((avg_lrP_0+avg_lrP_5+avg_lrP_10+avg_lrP_15+avg_lrP_20)/5,2)
    rf_final_avg = round((avg_rfP_0+avg_rfP_5+avg_rfP_10+avg_rfP_15+avg_rfP_20)/5,2)
    nb_final_avg = round((avg_nbP_0+avg_nbP_5+avg_nbP_10+avg_nbP_15+avg_nbP_20)/5,2)



    svmB_list = svmB.objects.order_by('-svmB_date')
    dtB_list=dtB.objects.order_by('-dtB_date')
    lrB_list=lrB.objects.order_by('-lrB_date')
    rfB_list=rfB.objects.order_by('-rfB_date')
    nbB_list=nbB.objects.order_by('-nbB_date')
    def avg_smvB():
        sum_svmB_0 = 0
        count_svmB_0 = 0
        sum_svmB_5 = 0
        count_svmB_5 = 0
        sum_svmB_10 = 0
        count_svmB_10 = 0
        sum_svmB_15 = 0
        count_svmB_15 = 0
        sum_svmB_20 = 0
        count_svmB_20 = 0
        for var in svmB_list:
            sum_svmB_0+=var.svmB_fold_0
            sum_svmB_5+=var.svmB_fold_5
            sum_svmB_10+=var.svmB_fold_10
            sum_svmB_15+=var.svmB_fold_15
            sum_svmB_20+=var.svmB_fold_20
            count_svmB_0+=1
            count_svmB_5+=1
            count_svmB_10+=1
            count_svmB_15+=1
            count_svmB_20+=1
        return (round(sum_svmB_0/count_svmB_0,2),round(sum_svmB_5/count_svmB_5,2),round(sum_svmB_10/count_svmB_10,2),round(sum_svmB_15/count_svmB_15,2),round(sum_svmB_20/count_svmB_20,2))
    avg_svmB_0,avg_svmB_5,avg_svmB_10,avg_svmB_15,avg_svmB_20 = avg_smvB()

    def avg_dtB():
        sum_dtB_0=0
        count_dtB_0=0
        sum_dtB_5=0
        count_dtB_5=0
        sum_dtB_10=0
        count_dtB_10=0
        sum_dtB_15=0
        count_dtB_15=0
        sum_dtB_20=0
        count_dtB_20=0
        for var in dtB_list:
            sum_dtB_0+=var.dtB_fold_0
            sum_dtB_5+=var.dtB_fold_5
            sum_dtB_10+=var.dtB_fold_10
            sum_dtB_15+=var.dtB_fold_15
            sum_dtB_20+=var.dtB_fold_20
            count_dtB_0+=1
            count_dtB_5+=1
            count_dtB_10+=1
            count_dtB_15+=1
            count_dtB_20+=1
        return(round(sum_dtB_0/count_dtB_0,2),round(sum_dtB_5/count_dtB_5,2),round(sum_dtB_10/count_dtB_10,2),round(sum_dtB_15/count_dtB_15,2),round(sum_dtB_20/count_dtB_20,2))
    avg_dtB_0,avg_dtB_5,avg_dtB_10,avg_dtB_15,avg_dtB_20 = avg_dtB()

    def avg_lrB():
        sum_lrB_0=0
        count_lrB_0=0
        sum_lrB_5=0
        count_lrB_5=0
        sum_lrB_10=0
        count_lrB_10=0
        sum_lrB_15=0
        count_lrB_15=0
        sum_lrB_20=0
        count_lrB_20=0
        for var in lrB_list:
            sum_lrB_0+=var.lrB_fold_0
            sum_lrB_5+=var.lrB_fold_5
            sum_lrB_10+=var.lrB_fold_10
            sum_lrB_15+=var.lrB_fold_15
            sum_lrB_20+=var.lrB_fold_20
            count_lrB_0+=1
            count_lrB_5+=1
            count_lrB_10+=1
            count_lrB_15+=1
            count_lrB_20+=1
        return(round(sum_lrB_0/count_lrB_0,2),round(sum_lrB_5/count_lrB_5,2),round(sum_lrB_10/count_lrB_10,2),round(sum_lrB_15/count_lrB_15,2),round(sum_lrB_20/count_lrB_20,2))
    avg_lrB_0,avg_lrB_5,avg_lrB_10,avg_lrB_15,avg_lrB_20 = avg_lrB()

    def avg_rfB():
        sum_rfB_0=0
        count_rfB_0=0
        sum_rfB_5=0
        count_rfB_5=0
        sum_rfB_10=0
        count_rfB_10=0
        sum_rfB_15=0
        count_rfB_15=0
        sum_rfB_20=0
        count_rfB_20=0
        for var in rfB_list:
            sum_rfB_0+=var.rfB_fold_0
            sum_rfB_5+=var.rfB_fold_5
            sum_rfB_10+=var.rfB_fold_10
            sum_rfB_15+=var.rfB_fold_15
            sum_rfB_20+=var.rfB_fold_20
            count_rfB_0+=1
            count_rfB_5+=1
            count_rfB_10+=1
            count_rfB_15+=1
            count_rfB_20+=1
        return(round(sum_rfB_0/count_rfB_0,2),round(sum_rfB_5/count_rfB_5,2),round(sum_rfB_10/count_rfB_10,2),round(sum_rfB_15/count_rfB_15,2),round(sum_rfB_20/count_rfB_20,2))
    avg_rfB_0,avg_rfB_5,avg_rfB_10,avg_rfB_15,avg_rfB_20 = avg_rfB()

    def avg_nbB():
        sum_nbB_0=0
        count_nbB_0=0
        sum_nbB_5=0
        count_nbB_5=0
        sum_nbB_10=0
        count_nbB_10=0
        sum_nbB_15=0
        count_nbB_15=0
        sum_nbB_20=0
        count_nbB_20=0
        for var in nbB_list:
            sum_nbB_0+=var.nbB_fold_0
            sum_nbB_5+=var.nbB_fold_5
            sum_nbB_10+=var.nbB_fold_10
            sum_nbB_15+=var.nbB_fold_15
            sum_nbB_20+=var.nbB_fold_20
            count_nbB_0+=1
            count_nbB_5+=1
            count_nbB_10+=1
            count_nbB_15+=1
            count_nbB_20+=1
        return(round(sum_nbB_0/count_nbB_0,2),round(sum_nbB_5/count_nbB_5,2),round(sum_nbB_10/count_nbB_10,2),round(sum_nbB_15/count_nbB_15,2),round(sum_nbB_20/count_nbB_20,2))
    avg_nbB_0,avg_nbB_5,avg_nbB_10,avg_nbB_15,avg_nbB_20 = avg_nbB()

    svm_final_avg_B = round((avg_svmB_0+avg_svmB_5+avg_svmB_10+avg_svmB_15+avg_svmB_20)/5,2)
    dt_final_avg_B = round((avg_dtB_0+avg_dtB_5+avg_dtB_10+avg_dtB_15+avg_dtB_20)/5,2)
    lr_final_avg_B = round((avg_lrB_0+avg_lrB_5+avg_lrB_10+avg_lrB_15+avg_lrB_20)/5,2)
    rf_final_avg_B = round((avg_rfB_0+avg_rfB_5+avg_rfB_10+avg_rfB_15+avg_rfB_20)/5,2)
    nb_final_avg_B = round((avg_nbB_0+avg_nbB_5+avg_nbB_10+avg_nbB_15+avg_nbB_20)/5,2)

    return render(request,'cancer/welcomeAdmin.html',context={'svm_final_avg_B':svm_final_avg_B,'dt_final_avg_B':dt_final_avg_B,'lr_final_avg_B':lr_final_avg_B,'rf_final_avg_B':rf_final_avg_B,'nb_final_avg_B':nb_final_avg_B,
                                                              'svm_final_avg':svm_final_avg,'dt_final_avg':dt_final_avg,'lr_final_avg':lr_final_avg,'rf_final_avg':rf_final_avg,'nb_final_avg':nb_final_avg})


def welcomeLab(request):
    patient_info=patient.objects.order_by('id')
    count_B = 0
    count_P = 0
    count_total = 0
    count_P_M = 0
    count_B_M = 0
    for var in patient_info:
        if var.test_type == "Prostate Cancer":
            if var.result == "MALIGNANT":
                count_P_M+=1
            count_P+=1
            count_total+=1
        else:
            if var.result == "MALIGNANT":
                count_B_M+=1
            count_B+=1
            count_total+=1
    test_P_M = round((count_P_M/count_P),2)*100
    test_B_M = round((count_B_M/count_B),2)*100
    test_M = round(((count_P_M+count_B_M)/count_total),2)*100
    return render(request,'cancer/welcomeLab.html',context={'test_P_M':test_P_M,'test_B_M':test_B_M,'test_M':test_M})

def result_chart(request):
    patient_info=patient.objects.order_by('id')
    count_B = 0
    count_P = 0
    count_total = 0
    count_P_M = 0
    count_B_M = 0
    for var in patient_info:
        if var.test_type == "Prostate Cancer":
            if var.result == "MALIGNANT":
                count_P_M+=1
            count_P+=1
            count_total+=1
        else:
            if var.result == "MALIGNANT":
                count_B_M+=1
            count_B+=1
            count_total+=1
    test_P = round((count_P/count_total),2)*100
    test_P_M = round((count_P_M/count_P),2)*100
    test_B_M = round((count_B_M/count_B),2)*100
    test_M = round(((count_P_M+count_B_M)/count_total),2)*100
    test_P_M1 = round((count_P_M/count_total),2)*100
    test_B_M1 = round((count_B_M/count_total),2)*100
    test_B = 100-test_M
    return render(request,'cancer/result_chart.html',context={'test_P_M':test_P_M,'test_B_M':test_B_M,'test_M':test_M,'test_P':test_P,'test_B':test_B,'test_B_M1':test_B_M1,'test_P_M1':test_P_M1})

def testBreast(request):
    return render(request,'cancer/testBreast.html')

def testProstate(request):
    return render(request,'cancer/testProstate.html')

def p_dim_red(request):
    my_dict = populate.populate_dim_P()
    svmPD_list = svmP_D.objects.order_by('-svmPD_date')
    dtPD_list=dtP_D.objects.order_by('-dtPD_date')
    lrPD_list=lrP_D.objects.order_by('-lrPD_date')
    rfPD_list=rfP_D.objects.order_by('-rfPD_date')
    nbPD_list=nbP_D.objects.order_by('-nbPD_date')

    def avg_smvPD():
        sum_svmPD_0 = 0
        count_svmPD_0 = 0
        sum_svmPD_5 = 0
        count_svmPD_5 = 0
        sum_svmPD_10 = 0
        count_svmPD_10 = 0
        sum_svmPD_15 = 0
        count_svmPD_15 = 0
        sum_svmPD_20 = 0
        count_svmPD_20 = 0
        for var in svmPD_list:
            sum_svmPD_0+=var.svmPD_fold_0
            sum_svmPD_5+=var.svmPD_fold_5
            sum_svmPD_10+=var.svmPD_fold_10
            sum_svmPD_15+=var.svmPD_fold_15
            sum_svmPD_20+=var.svmPD_fold_20
            count_svmPD_0+=1
            count_svmPD_5+=1
            count_svmPD_10+=1
            count_svmPD_15+=1
            count_svmPD_20+=1
        return (round(sum_svmPD_0/count_svmPD_0,2),round(sum_svmPD_5/count_svmPD_5,2),round(sum_svmPD_10/count_svmPD_10,2),round(sum_svmPD_15/count_svmPD_15,2),round(sum_svmPD_20/count_svmPD_20,2))
    avg_svmPD_0,avg_svmPD_5,avg_svmPD_10,avg_svmPD_15,avg_svmPD_20 = avg_smvPD()

    def avg_dtPD():
        sum_dtPD_0=0
        count_dtPD_0=0
        sum_dtPD_5=0
        count_dtPD_5=0
        sum_dtPD_10=0
        count_dtPD_10=0
        sum_dtPD_15=0
        count_dtPD_15=0
        sum_dtPD_20=0
        count_dtPD_20=0
        for var in dtPD_list:
            sum_dtPD_0+=var.dtPD_fold_0
            sum_dtPD_5+=var.dtPD_fold_5
            sum_dtPD_10+=var.dtPD_fold_10
            sum_dtPD_15+=var.dtPD_fold_15
            sum_dtPD_20+=var.dtPD_fold_20
            count_dtPD_0+=1
            count_dtPD_5+=1
            count_dtPD_10+=1
            count_dtPD_15+=1
            count_dtPD_20+=1
        return(round(sum_dtPD_0/count_dtPD_0,2),round(sum_dtPD_5/count_dtPD_5,2),round(sum_dtPD_10/count_dtPD_10,2),round(sum_dtPD_15/count_dtPD_15,2),round(sum_dtPD_20/count_dtPD_20,2))
    avg_dtPD_0,avg_dtPD_5,avg_dtPD_10,avg_dtPD_15,avg_dtPD_20 = avg_dtPD()

    def avg_lrPD():
        sum_lrPD_0=0
        count_lrPD_0=0
        sum_lrPD_5=0
        count_lrPD_5=0
        sum_lrPD_10=0
        count_lrPD_10=0
        sum_lrPD_15=0
        count_lrPD_15=0
        sum_lrPD_20=0
        count_lrPD_20=0
        for var in lrPD_list:
            sum_lrPD_0+=var.lrPD_fold_0
            sum_lrPD_5+=var.lrPD_fold_5
            sum_lrPD_10+=var.lrPD_fold_10
            sum_lrPD_15+=var.lrPD_fold_15
            sum_lrPD_20+=var.lrPD_fold_20
            count_lrPD_0+=1
            count_lrPD_5+=1
            count_lrPD_10+=1
            count_lrPD_15+=1
            count_lrPD_20+=1
        return(round(sum_lrPD_0/count_lrPD_0,2),round(sum_lrPD_5/count_lrPD_5,2),round(sum_lrPD_10/count_lrPD_10,2),round(sum_lrPD_15/count_lrPD_15,2),round(sum_lrPD_20/count_lrPD_20,2))
    avg_lrPD_0,avg_lrPD_5,avg_lrPD_10,avg_lrPD_15,avg_lrPD_20 = avg_lrPD()

    def avg_rfPD():
        sum_rfPD_0=0
        count_rfPD_0=0
        sum_rfPD_5=0
        count_rfPD_5=0
        sum_rfPD_10=0
        count_rfPD_10=0
        sum_rfPD_15=0
        count_rfPD_15=0
        sum_rfPD_20=0
        count_rfPD_20=0
        for var in rfPD_list:
            sum_rfPD_0+=var.rfPD_fold_0
            sum_rfPD_5+=var.rfPD_fold_5
            sum_rfPD_10+=var.rfPD_fold_10
            sum_rfPD_15+=var.rfPD_fold_15
            sum_rfPD_20+=var.rfPD_fold_20
            count_rfPD_0+=1
            count_rfPD_5+=1
            count_rfPD_10+=1
            count_rfPD_15+=1
            count_rfPD_20+=1
        return(round(sum_rfPD_0/count_rfPD_0,2),round(sum_rfPD_5/count_rfPD_5,2),round(sum_rfPD_10/count_rfPD_10,2),round(sum_rfPD_15/count_rfPD_15,2),round(sum_rfPD_20/count_rfPD_20,2))
    avg_rfPD_0,avg_rfPD_5,avg_rfPD_10,avg_rfPD_15,avg_rfPD_20 = avg_rfPD()

    def avg_nbPD():
        sum_nbPD_0=0
        count_nbPD_0=0
        sum_nbPD_5=0
        count_nbPD_5=0
        sum_nbPD_10=0
        count_nbPD_10=0
        sum_nbPD_15=0
        count_nbPD_15=0
        sum_nbPD_20=0
        count_nbPD_20=0
        for var in nbPD_list:
            sum_nbPD_0+=var.nbPD_fold_0
            sum_nbPD_5+=var.nbPD_fold_5
            sum_nbPD_10+=var.nbPD_fold_10
            sum_nbPD_15+=var.nbPD_fold_15
            sum_nbPD_20+=var.nbPD_fold_20
            count_nbPD_0+=1
            count_nbPD_5+=1
            count_nbPD_10+=1
            count_nbPD_15+=1
            count_nbPD_20+=1
        return(round(sum_nbPD_0/count_nbPD_0,2),round(sum_nbPD_5/count_nbPD_5,2),round(sum_nbPD_10/count_nbPD_10,2),round(sum_nbPD_15/count_nbPD_15,2),round(sum_nbPD_20/count_nbPD_20,2))
    avg_nbPD_0,avg_nbPD_5,avg_nbPD_10,avg_nbPD_15,avg_nbPD_20 = avg_nbPD()

    svm_final_avg_PD = round((avg_svmPD_0+avg_svmPD_5+avg_svmPD_10+avg_svmPD_15+avg_svmPD_20)/5,2)
    dt_final_avg_PD = round((avg_dtPD_0+avg_dtPD_5+avg_dtPD_10+avg_dtPD_15+avg_dtPD_20)/5,2)
    lr_final_avg_PD = round((avg_lrPD_0+avg_lrPD_5+avg_lrPD_10+avg_lrPD_15+avg_lrPD_20)/5,2)
    rf_final_avg_PD = round((avg_rfPD_0+avg_rfPD_5+avg_rfPD_10+avg_rfPD_15+avg_rfPD_20)/5,2)
    nb_final_avg_PD = round((avg_nbPD_0+avg_nbPD_5+avg_nbPD_10+avg_nbPD_15+avg_nbPD_20)/5,2)


    return render(request,'cancer/p_dim_red.html',context={'my_dict':my_dict,'svmPD_list':svmPD_list,'dtPD_list':dtPD_list,'lrPD_list':lrPD_list,'rfPD_list':rfPD_list,'nbPD_list':nbPD_list,'avg_svmPD_0':avg_svmPD_0,'avg_svmPD_5':avg_svmPD_5,'avg_svmPD_10':avg_svmPD_10,'avg_svmPD_15':avg_svmPD_15,'avg_svmPD_20':avg_svmPD_20,
                                                                  'avg_dtPD_0':avg_dtPD_0,'avg_dtPD_5':avg_dtPD_5,'avg_dtPD_10':avg_dtPD_10,'avg_dtPD_15':avg_dtPD_15,'avg_dtPD_20':avg_dtPD_20,'avg_lrPD_0':avg_lrPD_0,'avg_lrPD_5':avg_lrPD_5,'avg_lrPD_10':avg_lrPD_10,'avg_lrPD_15':avg_lrPD_15,'avg_lrPD_20':avg_lrPD_20,
                                                                  'avg_rfPD_0':avg_rfPD_0,'avg_rfPD_5':avg_rfPD_5,'avg_rfPD_10':avg_rfPD_10,'avg_rfPD_15':avg_rfPD_15,'avg_rfPD_20':avg_rfPD_20,'avg_nbPD_0':avg_nbPD_0,'avg_nbPD_5':avg_nbPD_5,'avg_nbPD_10':avg_nbPD_10,'avg_nbPD_15':avg_nbPD_15,'avg_nbPD_20':avg_nbPD_20,
                                                                  'svm_final_avg_PD':svm_final_avg_PD,'dt_final_avg_PD':dt_final_avg_PD,'lr_final_avg_PD':lr_final_avg_PD,'rf_final_avg_PD':rf_final_avg_PD,'nb_final_avg_PD':nb_final_avg_PD})


def breast_chart(request):
    svmB_list = svmB.objects.order_by('-svmB_date')
    dtB_list=dtB.objects.order_by('-dtB_date')
    lrB_list=lrB.objects.order_by('-lrB_date')
    rfB_list=rfB.objects.order_by('-rfB_date')
    nbB_list=nbB.objects.order_by('-nbB_date')
    def avg_smvB():
        sum_svmB_0 = 0
        count_svmB_0 = 0
        sum_svmB_5 = 0
        count_svmB_5 = 0
        sum_svmB_10 = 0
        count_svmB_10 = 0
        sum_svmB_15 = 0
        count_svmB_15 = 0
        sum_svmB_20 = 0
        count_svmB_20 = 0
        for var in svmB_list:
            sum_svmB_0+=var.svmB_fold_0
            sum_svmB_5+=var.svmB_fold_5
            sum_svmB_10+=var.svmB_fold_10
            sum_svmB_15+=var.svmB_fold_15
            sum_svmB_20+=var.svmB_fold_20
            count_svmB_0+=1
            count_svmB_5+=1
            count_svmB_10+=1
            count_svmB_15+=1
            count_svmB_20+=1
        return (round(sum_svmB_0/count_svmB_0,2),round(sum_svmB_5/count_svmB_5,2),round(sum_svmB_10/count_svmB_10,2),round(sum_svmB_15/count_svmB_15,2),round(sum_svmB_20/count_svmB_20,2))
    avg_svmB_0,avg_svmB_5,avg_svmB_10,avg_svmB_15,avg_svmB_20 = avg_smvB()

    def avg_dtB():
        sum_dtB_0=0
        count_dtB_0=0
        sum_dtB_5=0
        count_dtB_5=0
        sum_dtB_10=0
        count_dtB_10=0
        sum_dtB_15=0
        count_dtB_15=0
        sum_dtB_20=0
        count_dtB_20=0
        for var in dtB_list:
            sum_dtB_0+=var.dtB_fold_0
            sum_dtB_5+=var.dtB_fold_5
            sum_dtB_10+=var.dtB_fold_10
            sum_dtB_15+=var.dtB_fold_15
            sum_dtB_20+=var.dtB_fold_20
            count_dtB_0+=1
            count_dtB_5+=1
            count_dtB_10+=1
            count_dtB_15+=1
            count_dtB_20+=1
        return(round(sum_dtB_0/count_dtB_0,2),round(sum_dtB_5/count_dtB_5,2),round(sum_dtB_10/count_dtB_10,2),round(sum_dtB_15/count_dtB_15,2),round(sum_dtB_20/count_dtB_20,2))
    avg_dtB_0,avg_dtB_5,avg_dtB_10,avg_dtB_15,avg_dtB_20 = avg_dtB()

    def avg_lrB():
        sum_lrB_0=0
        count_lrB_0=0
        sum_lrB_5=0
        count_lrB_5=0
        sum_lrB_10=0
        count_lrB_10=0
        sum_lrB_15=0
        count_lrB_15=0
        sum_lrB_20=0
        count_lrB_20=0
        for var in lrB_list:
            sum_lrB_0+=var.lrB_fold_0
            sum_lrB_5+=var.lrB_fold_5
            sum_lrB_10+=var.lrB_fold_10
            sum_lrB_15+=var.lrB_fold_15
            sum_lrB_20+=var.lrB_fold_20
            count_lrB_0+=1
            count_lrB_5+=1
            count_lrB_10+=1
            count_lrB_15+=1
            count_lrB_20+=1
        return(round(sum_lrB_0/count_lrB_0,2),round(sum_lrB_5/count_lrB_5,2),round(sum_lrB_10/count_lrB_10,2),round(sum_lrB_15/count_lrB_15,2),round(sum_lrB_20/count_lrB_20,2))
    avg_lrB_0,avg_lrB_5,avg_lrB_10,avg_lrB_15,avg_lrB_20 = avg_lrB()

    def avg_rfB():
        sum_rfB_0=0
        count_rfB_0=0
        sum_rfB_5=0
        count_rfB_5=0
        sum_rfB_10=0
        count_rfB_10=0
        sum_rfB_15=0
        count_rfB_15=0
        sum_rfB_20=0
        count_rfB_20=0
        for var in rfB_list:
            sum_rfB_0+=var.rfB_fold_0
            sum_rfB_5+=var.rfB_fold_5
            sum_rfB_10+=var.rfB_fold_10
            sum_rfB_15+=var.rfB_fold_15
            sum_rfB_20+=var.rfB_fold_20
            count_rfB_0+=1
            count_rfB_5+=1
            count_rfB_10+=1
            count_rfB_15+=1
            count_rfB_20+=1
        return(round(sum_rfB_0/count_rfB_0,2),round(sum_rfB_5/count_rfB_5,2),round(sum_rfB_10/count_rfB_10,2),round(sum_rfB_15/count_rfB_15,2),round(sum_rfB_20/count_rfB_20,2))
    avg_rfB_0,avg_rfB_5,avg_rfB_10,avg_rfB_15,avg_rfB_20 = avg_rfB()

    def avg_nbB():
        sum_nbB_0=0
        count_nbB_0=0
        sum_nbB_5=0
        count_nbB_5=0
        sum_nbB_10=0
        count_nbB_10=0
        sum_nbB_15=0
        count_nbB_15=0
        sum_nbB_20=0
        count_nbB_20=0
        for var in nbB_list:
            sum_nbB_0+=var.nbB_fold_0
            sum_nbB_5+=var.nbB_fold_5
            sum_nbB_10+=var.nbB_fold_10
            sum_nbB_15+=var.nbB_fold_15
            sum_nbB_20+=var.nbB_fold_20
            count_nbB_0+=1
            count_nbB_5+=1
            count_nbB_10+=1
            count_nbB_15+=1
            count_nbB_20+=1
        return(round(sum_nbB_0/count_nbB_0,2),round(sum_nbB_5/count_nbB_5,2),round(sum_nbB_10/count_nbB_10,2),round(sum_nbB_15/count_nbB_15,2),round(sum_nbB_20/count_nbB_20,2))
    avg_nbB_0,avg_nbB_5,avg_nbB_10,avg_nbB_15,avg_nbB_20 = avg_nbB()

    svm_final_avg_B = round((avg_svmB_0+avg_svmB_5+avg_svmB_10+avg_svmB_15+avg_svmB_20)/5,2)
    dt_final_avg_B = round((avg_dtB_0+avg_dtB_5+avg_dtB_10+avg_dtB_15+avg_dtB_20)/5,2)
    lr_final_avg_B = round((avg_lrB_0+avg_lrB_5+avg_lrB_10+avg_lrB_15+avg_lrB_20)/5,2)
    rf_final_avg_B = round((avg_rfB_0+avg_rfB_5+avg_rfB_10+avg_rfB_15+avg_rfB_20)/5,2)
    nb_final_avg_B = round((avg_nbB_0+avg_nbB_5+avg_nbB_10+avg_nbB_15+avg_nbB_20)/5,2)

    return render(request,'cancer/breast_chart.html',context={'svmB_list':svmB_list,'dtB_list':dtB_list,'lrB_list':lrB_list,'rfB_list':rfB_list,'nbB_list':nbB_list,'avg_svmB_0':avg_svmB_0,'avg_svmB_5':avg_svmB_5,'avg_svmB_10':avg_svmB_10,'avg_svmB_15':avg_svmB_15,'avg_svmB_20':avg_svmB_20,
                                                                  'avg_dtB_0':avg_dtB_0,'avg_dtB_5':avg_dtB_5,'avg_dtB_10':avg_dtB_10,'avg_dtB_15':avg_dtB_15,'avg_dtB_20':avg_dtB_20,'avg_lrB_0':avg_lrB_0,'avg_lrB_5':avg_lrB_5,'avg_lrB_10':avg_lrB_10,'avg_lrB_15':avg_lrB_15,'avg_lrB_20':avg_lrB_20,
                                                                  'avg_rfB_0':avg_rfB_0,'avg_rfB_5':avg_rfB_5,'avg_rfB_10':avg_rfB_10,'avg_rfB_15':avg_rfB_15,'avg_rfB_20':avg_rfB_20,'avg_nbB_0':avg_nbB_0,'avg_nbB_5':avg_nbB_5,'avg_nbB_10':avg_nbB_10,'avg_nbB_15':avg_nbB_15,'avg_nbB_20':avg_nbB_20,
                                                                  'svm_final_avg_B':svm_final_avg_B,'dt_final_avg_B':dt_final_avg_B,'lr_final_avg_B':lr_final_avg_B,'rf_final_avg_B':rf_final_avg_B,'nb_final_avg_B':nb_final_avg_B})


def prostate_chart(request):
    svmP_list = svmP.objects.order_by('-svmP_date')
    dtP_list=dtP.objects.order_by('-dtP_date')
    lrP_list=lrP.objects.order_by('-lrP_date')
    rfP_list=rfP.objects.order_by('-rfP_date')
    nbP_list=nbP.objects.order_by('-nbP_date')
    def avg_smvP():
        sum_svmP_0 = 0
        count_svmP_0 = 0
        sum_svmP_5 = 0
        count_svmP_5 = 0
        sum_svmP_10 = 0
        count_svmP_10 = 0
        sum_svmP_15 = 0
        count_svmP_15 = 0
        sum_svmP_20 = 0
        count_svmP_20 = 0
        for var in svmP_list:
            sum_svmP_0+=var.svmP_fold_0
            sum_svmP_5+=var.svmP_fold_5
            sum_svmP_10+=var.svmP_fold_10
            sum_svmP_15+=var.svmP_fold_15
            sum_svmP_20+=var.svmP_fold_20
            count_svmP_0+=1
            count_svmP_5+=1
            count_svmP_10+=1
            count_svmP_15+=1
            count_svmP_20+=1
        return (round(sum_svmP_0/count_svmP_0,2),round(sum_svmP_5/count_svmP_5,2),round(sum_svmP_10/count_svmP_10,2),round(sum_svmP_15/count_svmP_15,2),round(sum_svmP_20/count_svmP_20,2))
    avg_svmP_0,avg_svmP_5,avg_svmP_10,avg_svmP_15,avg_svmP_20 = avg_smvP()

    def avg_dtP():
        sum_dtP_0=0
        count_dtP_0=0
        sum_dtP_5=0
        count_dtP_5=0
        sum_dtP_10=0
        count_dtP_10=0
        sum_dtP_15=0
        count_dtP_15=0
        sum_dtP_20=0
        count_dtP_20=0
        for var in dtP_list:
            sum_dtP_0+=var.dtP_fold_0
            sum_dtP_5+=var.dtP_fold_5
            sum_dtP_10+=var.dtP_fold_10
            sum_dtP_15+=var.dtP_fold_15
            sum_dtP_20+=var.dtP_fold_20
            count_dtP_0+=1
            count_dtP_5+=1
            count_dtP_10+=1
            count_dtP_15+=1
            count_dtP_20+=1
        return(round(sum_dtP_0/count_dtP_0,2),round(sum_dtP_5/count_dtP_5,2),round(sum_dtP_10/count_dtP_10,2),round(sum_dtP_15/count_dtP_15,2),round(sum_dtP_20/count_dtP_20,2))
    avg_dtP_0,avg_dtP_5,avg_dtP_10,avg_dtP_15,avg_dtP_20 = avg_dtP()

    def avg_lrP():
        sum_lrP_0=0
        count_lrP_0=0
        sum_lrP_5=0
        count_lrP_5=0
        sum_lrP_10=0
        count_lrP_10=0
        sum_lrP_15=0
        count_lrP_15=0
        sum_lrP_20=0
        count_lrP_20=0
        for var in lrP_list:
            sum_lrP_0+=var.lrP_fold_0
            sum_lrP_5+=var.lrP_fold_5
            sum_lrP_10+=var.lrP_fold_10
            sum_lrP_15+=var.lrP_fold_15
            sum_lrP_20+=var.lrP_fold_20
            count_lrP_0+=1
            count_lrP_5+=1
            count_lrP_10+=1
            count_lrP_15+=1
            count_lrP_20+=1
        return(round(sum_lrP_0/count_lrP_0,2),round(sum_lrP_5/count_lrP_5,2),round(sum_lrP_10/count_lrP_10,2),round(sum_lrP_15/count_lrP_15,2),round(sum_lrP_20/count_lrP_20,2))
    avg_lrP_0,avg_lrP_5,avg_lrP_10,avg_lrP_15,avg_lrP_20 = avg_lrP()

    def avg_rfP():
        sum_rfP_0=0
        count_rfP_0=0
        sum_rfP_5=0
        count_rfP_5=0
        sum_rfP_10=0
        count_rfP_10=0
        sum_rfP_15=0
        count_rfP_15=0
        sum_rfP_20=0
        count_rfP_20=0
        for var in rfP_list:
            sum_rfP_0+=var.rfP_fold_0
            sum_rfP_5+=var.rfP_fold_5
            sum_rfP_10+=var.rfP_fold_10
            sum_rfP_15+=var.rfP_fold_15
            sum_rfP_20+=var.rfP_fold_20
            count_rfP_0+=1
            count_rfP_5+=1
            count_rfP_10+=1
            count_rfP_15+=1
            count_rfP_20+=1
        return(round(sum_rfP_0/count_rfP_0,2),round(sum_rfP_5/count_rfP_5,2),round(sum_rfP_10/count_rfP_10,2),round(sum_rfP_15/count_rfP_15,2),round(sum_rfP_20/count_rfP_20,2))
    avg_rfP_0,avg_rfP_5,avg_rfP_10,avg_rfP_15,avg_rfP_20 = avg_rfP()

    def avg_nbP():
        sum_nbP_0=0
        count_nbP_0=0
        sum_nbP_5=0
        count_nbP_5=0
        sum_nbP_10=0
        count_nbP_10=0
        sum_nbP_15=0
        count_nbP_15=0
        sum_nbP_20=0
        count_nbP_20=0
        for var in nbP_list:
            sum_nbP_0+=var.nbP_fold_0
            sum_nbP_5+=var.nbP_fold_5
            sum_nbP_10+=var.nbP_fold_10
            sum_nbP_15+=var.nbP_fold_15
            sum_nbP_20+=var.nbP_fold_20
            count_nbP_0+=1
            count_nbP_5+=1
            count_nbP_10+=1
            count_nbP_15+=1
            count_nbP_20+=1
        return(round(sum_nbP_0/count_nbP_0,2),round(sum_nbP_5/count_nbP_5,2),round(sum_nbP_10/count_nbP_10,2),round(sum_nbP_15/count_nbP_15,2),round(sum_nbP_20/count_nbP_20,2))
    avg_nbP_0,avg_nbP_5,avg_nbP_10,avg_nbP_15,avg_nbP_20 = avg_nbP()

    svm_final_avg = round((avg_svmP_0+avg_svmP_5+avg_svmP_10+avg_svmP_15+avg_svmP_20)/5,2)
    dt_final_avg = round((avg_dtP_0+avg_dtP_5+avg_dtP_10+avg_dtP_15+avg_dtP_20)/5,2)
    lr_final_avg = round((avg_lrP_0+avg_lrP_5+avg_lrP_10+avg_lrP_15+avg_lrP_20)/5,2)
    rf_final_avg = round((avg_rfP_0+avg_rfP_5+avg_rfP_10+avg_rfP_15+avg_rfP_20)/5,2)
    nb_final_avg = round((avg_nbP_0+avg_nbP_5+avg_nbP_10+avg_nbP_15+avg_nbP_20)/5,2)

    return render(request,'cancer/prostate_chart.html',context={'svmP_list':svmP_list,'dtP_list':dtP_list,'lrP_list':lrP_list,'rfP_list':rfP_list,'nbP_list':nbP_list,'avg_svmP_0':avg_svmP_0,'avg_svmP_5':avg_svmP_5,'avg_svmP_10':avg_svmP_10,'avg_svmP_15':avg_svmP_15,'avg_svmP_20':avg_svmP_20,
                                                                  'avg_dtP_0':avg_dtP_0,'avg_dtP_5':avg_dtP_5,'avg_dtP_10':avg_dtP_10,'avg_dtP_15':avg_dtP_15,'avg_dtP_20':avg_dtP_20,'avg_lrP_0':avg_lrP_0,'avg_lrP_5':avg_lrP_5,'avg_lrP_10':avg_lrP_10,'avg_lrP_15':avg_lrP_15,'avg_lrP_20':avg_lrP_20,
                                                                  'avg_rfP_0':avg_rfP_0,'avg_rfP_5':avg_rfP_5,'avg_rfP_10':avg_rfP_10,'avg_rfP_15':avg_rfP_15,'avg_rfP_20':avg_rfP_20,'avg_nbP_0':avg_nbP_0,'avg_nbP_5':avg_nbP_5,'avg_nbP_10':avg_nbP_10,'avg_nbP_15':avg_nbP_15,'avg_nbP_20':avg_nbP_20,
                                                                  'svm_final_avg':svm_final_avg,'dt_final_avg':dt_final_avg,'lr_final_avg':lr_final_avg,'rf_final_avg':rf_final_avg,'nb_final_avg':nb_final_avg})



def test_graphs(request):

    return render(request,'cancer/test_graphs.html')

def breastAccuracy(request):
    my_dict_b = populate.populate_data_b()
    svmB_list = svmB.objects.order_by('-svmB_date')
    dtB_list=dtB.objects.order_by('-dtB_date')
    lrB_list=lrB.objects.order_by('-lrB_date')
    rfB_list=rfB.objects.order_by('-rfB_date')
    nbB_list=nbB.objects.order_by('-nbB_date')
    def avg_smvB():
        sum_svmB_0 = 0
        count_svmB_0 = 0
        sum_svmB_5 = 0
        count_svmB_5 = 0
        sum_svmB_10 = 0
        count_svmB_10 = 0
        sum_svmB_15 = 0
        count_svmB_15 = 0
        sum_svmB_20 = 0
        count_svmB_20 = 0
        for var in svmB_list:
            sum_svmB_0+=var.svmB_fold_0
            sum_svmB_5+=var.svmB_fold_5
            sum_svmB_10+=var.svmB_fold_10
            sum_svmB_15+=var.svmB_fold_15
            sum_svmB_20+=var.svmB_fold_20
            count_svmB_0+=1
            count_svmB_5+=1
            count_svmB_10+=1
            count_svmB_15+=1
            count_svmB_20+=1
        return (round(sum_svmB_0/count_svmB_0,2),round(sum_svmB_5/count_svmB_5,2),round(sum_svmB_10/count_svmB_10,2),round(sum_svmB_15/count_svmB_15,2),round(sum_svmB_20/count_svmB_20,2))
    avg_svmB_0,avg_svmB_5,avg_svmB_10,avg_svmB_15,avg_svmB_20 = avg_smvB()

    def avg_dtB():
        sum_dtB_0=0
        count_dtB_0=0
        sum_dtB_5=0
        count_dtB_5=0
        sum_dtB_10=0
        count_dtB_10=0
        sum_dtB_15=0
        count_dtB_15=0
        sum_dtB_20=0
        count_dtB_20=0
        for var in dtB_list:
            sum_dtB_0+=var.dtB_fold_0
            sum_dtB_5+=var.dtB_fold_5
            sum_dtB_10+=var.dtB_fold_10
            sum_dtB_15+=var.dtB_fold_15
            sum_dtB_20+=var.dtB_fold_20
            count_dtB_0+=1
            count_dtB_5+=1
            count_dtB_10+=1
            count_dtB_15+=1
            count_dtB_20+=1
        return(round(sum_dtB_0/count_dtB_0,2),round(sum_dtB_5/count_dtB_5,2),round(sum_dtB_10/count_dtB_10,2),round(sum_dtB_15/count_dtB_15,2),round(sum_dtB_20/count_dtB_20,2))
    avg_dtB_0,avg_dtB_5,avg_dtB_10,avg_dtB_15,avg_dtB_20 = avg_dtB()

    def avg_lrB():
        sum_lrB_0=0
        count_lrB_0=0
        sum_lrB_5=0
        count_lrB_5=0
        sum_lrB_10=0
        count_lrB_10=0
        sum_lrB_15=0
        count_lrB_15=0
        sum_lrB_20=0
        count_lrB_20=0
        for var in lrB_list:
            sum_lrB_0+=var.lrB_fold_0
            sum_lrB_5+=var.lrB_fold_5
            sum_lrB_10+=var.lrB_fold_10
            sum_lrB_15+=var.lrB_fold_15
            sum_lrB_20+=var.lrB_fold_20
            count_lrB_0+=1
            count_lrB_5+=1
            count_lrB_10+=1
            count_lrB_15+=1
            count_lrB_20+=1
        return(round(sum_lrB_0/count_lrB_0,2),round(sum_lrB_5/count_lrB_5,2),round(sum_lrB_10/count_lrB_10,2),round(sum_lrB_15/count_lrB_15,2),round(sum_lrB_20/count_lrB_20,2))
    avg_lrB_0,avg_lrB_5,avg_lrB_10,avg_lrB_15,avg_lrB_20 = avg_lrB()

    def avg_rfB():
        sum_rfB_0=0
        count_rfB_0=0
        sum_rfB_5=0
        count_rfB_5=0
        sum_rfB_10=0
        count_rfB_10=0
        sum_rfB_15=0
        count_rfB_15=0
        sum_rfB_20=0
        count_rfB_20=0
        for var in rfB_list:
            sum_rfB_0+=var.rfB_fold_0
            sum_rfB_5+=var.rfB_fold_5
            sum_rfB_10+=var.rfB_fold_10
            sum_rfB_15+=var.rfB_fold_15
            sum_rfB_20+=var.rfB_fold_20
            count_rfB_0+=1
            count_rfB_5+=1
            count_rfB_10+=1
            count_rfB_15+=1
            count_rfB_20+=1
        return(round(sum_rfB_0/count_rfB_0,2),round(sum_rfB_5/count_rfB_5,2),round(sum_rfB_10/count_rfB_10,2),round(sum_rfB_15/count_rfB_15,2),round(sum_rfB_20/count_rfB_20,2))
    avg_rfB_0,avg_rfB_5,avg_rfB_10,avg_rfB_15,avg_rfB_20 = avg_rfB()

    def avg_nbB():
        sum_nbB_0=0
        count_nbB_0=0
        sum_nbB_5=0
        count_nbB_5=0
        sum_nbB_10=0
        count_nbB_10=0
        sum_nbB_15=0
        count_nbB_15=0
        sum_nbB_20=0
        count_nbB_20=0
        for var in nbB_list:
            sum_nbB_0+=var.nbB_fold_0
            sum_nbB_5+=var.nbB_fold_5
            sum_nbB_10+=var.nbB_fold_10
            sum_nbB_15+=var.nbB_fold_15
            sum_nbB_20+=var.nbB_fold_20
            count_nbB_0+=1
            count_nbB_5+=1
            count_nbB_10+=1
            count_nbB_15+=1
            count_nbB_20+=1
        return(round(sum_nbB_0/count_nbB_0,2),round(sum_nbB_5/count_nbB_5,2),round(sum_nbB_10/count_nbB_10,2),round(sum_nbB_15/count_nbB_15,2),round(sum_nbB_20/count_nbB_20,2))
    avg_nbB_0,avg_nbB_5,avg_nbB_10,avg_nbB_15,avg_nbB_20 = avg_nbB()

    svm_final_avg_B = round((avg_svmB_0+avg_svmB_5+avg_svmB_10+avg_svmB_15+avg_svmB_20)/5,2)
    dt_final_avg_B = round((avg_dtB_0+avg_dtB_5+avg_dtB_10+avg_dtB_15+avg_dtB_20)/5,2)
    lr_final_avg_B = round((avg_lrB_0+avg_lrB_5+avg_lrB_10+avg_lrB_15+avg_lrB_20)/5,2)
    rf_final_avg_B = round((avg_rfB_0+avg_rfB_5+avg_rfB_10+avg_rfB_15+avg_rfB_20)/5,2)
    nb_final_avg_B = round((avg_nbB_0+avg_nbB_5+avg_nbB_10+avg_nbB_15+avg_nbB_20)/5,2)

    return render(request,'cancer/breastAccuracy.html',context={'my_dict_b':my_dict_b,'svmB_list':svmB_list,'dtB_list':dtB_list,'lrB_list':lrB_list,'rfB_list':rfB_list,'nbB_list':nbB_list,'avg_svmB_0':avg_svmB_0,'avg_svmB_5':avg_svmB_5,'avg_svmB_10':avg_svmB_10,'avg_svmB_15':avg_svmB_15,'avg_svmB_20':avg_svmB_20,
                                                                  'avg_dtB_0':avg_dtB_0,'avg_dtB_5':avg_dtB_5,'avg_dtB_10':avg_dtB_10,'avg_dtB_15':avg_dtB_15,'avg_dtB_20':avg_dtB_20,'avg_lrB_0':avg_lrB_0,'avg_lrB_5':avg_lrB_5,'avg_lrB_10':avg_lrB_10,'avg_lrB_15':avg_lrB_15,'avg_lrB_20':avg_lrB_20,
                                                                  'avg_rfB_0':avg_rfB_0,'avg_rfB_5':avg_rfB_5,'avg_rfB_10':avg_rfB_10,'avg_rfB_15':avg_rfB_15,'avg_rfB_20':avg_rfB_20,'avg_nbB_0':avg_nbB_0,'avg_nbB_5':avg_nbB_5,'avg_nbB_10':avg_nbB_10,'avg_nbB_15':avg_nbB_15,'avg_nbB_20':avg_nbB_20,
                                                                  'svm_final_avg_B':svm_final_avg_B,'dt_final_avg_B':dt_final_avg_B,'lr_final_avg_B':lr_final_avg_B,'rf_final_avg_B':rf_final_avg_B,'nb_final_avg_B':nb_final_avg_B})

def prostateAccuracy(request):
    my_dict = populate.populate_data()
    svmP_list = svmP.objects.order_by('-svmP_date')
    dtP_list=dtP.objects.order_by('-dtP_date')
    lrP_list=lrP.objects.order_by('-lrP_date')
    rfP_list=rfP.objects.order_by('-rfP_date')
    nbP_list=nbP.objects.order_by('-nbP_date')
    def avg_smvP():
        sum_svmP_0 = 0
        count_svmP_0 = 0
        sum_svmP_5 = 0
        count_svmP_5 = 0
        sum_svmP_10 = 0
        count_svmP_10 = 0
        sum_svmP_15 = 0
        count_svmP_15 = 0
        sum_svmP_20 = 0
        count_svmP_20 = 0
        for var in svmP_list:
            sum_svmP_0+=var.svmP_fold_0
            sum_svmP_5+=var.svmP_fold_5
            sum_svmP_10+=var.svmP_fold_10
            sum_svmP_15+=var.svmP_fold_15
            sum_svmP_20+=var.svmP_fold_20
            count_svmP_0+=1
            count_svmP_5+=1
            count_svmP_10+=1
            count_svmP_15+=1
            count_svmP_20+=1
        return (round(sum_svmP_0/count_svmP_0,2),round(sum_svmP_5/count_svmP_5,2),round(sum_svmP_10/count_svmP_10,2),round(sum_svmP_15/count_svmP_15,2),round(sum_svmP_20/count_svmP_20,2))
    avg_svmP_0,avg_svmP_5,avg_svmP_10,avg_svmP_15,avg_svmP_20 = avg_smvP()

    def avg_dtP():
        sum_dtP_0=0
        count_dtP_0=0
        sum_dtP_5=0
        count_dtP_5=0
        sum_dtP_10=0
        count_dtP_10=0
        sum_dtP_15=0
        count_dtP_15=0
        sum_dtP_20=0
        count_dtP_20=0
        for var in dtP_list:
            sum_dtP_0+=var.dtP_fold_0
            sum_dtP_5+=var.dtP_fold_5
            sum_dtP_10+=var.dtP_fold_10
            sum_dtP_15+=var.dtP_fold_15
            sum_dtP_20+=var.dtP_fold_20
            count_dtP_0+=1
            count_dtP_5+=1
            count_dtP_10+=1
            count_dtP_15+=1
            count_dtP_20+=1
        return(round(sum_dtP_0/count_dtP_0,2),round(sum_dtP_5/count_dtP_5,2),round(sum_dtP_10/count_dtP_10,2),round(sum_dtP_15/count_dtP_15,2),round(sum_dtP_20/count_dtP_20,2))
    avg_dtP_0,avg_dtP_5,avg_dtP_10,avg_dtP_15,avg_dtP_20 = avg_dtP()

    def avg_lrP():
        sum_lrP_0=0
        count_lrP_0=0
        sum_lrP_5=0
        count_lrP_5=0
        sum_lrP_10=0
        count_lrP_10=0
        sum_lrP_15=0
        count_lrP_15=0
        sum_lrP_20=0
        count_lrP_20=0
        for var in lrP_list:
            sum_lrP_0+=var.lrP_fold_0
            sum_lrP_5+=var.lrP_fold_5
            sum_lrP_10+=var.lrP_fold_10
            sum_lrP_15+=var.lrP_fold_15
            sum_lrP_20+=var.lrP_fold_20
            count_lrP_0+=1
            count_lrP_5+=1
            count_lrP_10+=1
            count_lrP_15+=1
            count_lrP_20+=1
        return(round(sum_lrP_0/count_lrP_0,2),round(sum_lrP_5/count_lrP_5,2),round(sum_lrP_10/count_lrP_10,2),round(sum_lrP_15/count_lrP_15,2),round(sum_lrP_20/count_lrP_20,2))
    avg_lrP_0,avg_lrP_5,avg_lrP_10,avg_lrP_15,avg_lrP_20 = avg_lrP()

    def avg_rfP():
        sum_rfP_0=0
        count_rfP_0=0
        sum_rfP_5=0
        count_rfP_5=0
        sum_rfP_10=0
        count_rfP_10=0
        sum_rfP_15=0
        count_rfP_15=0
        sum_rfP_20=0
        count_rfP_20=0
        for var in rfP_list:
            sum_rfP_0+=var.rfP_fold_0
            sum_rfP_5+=var.rfP_fold_5
            sum_rfP_10+=var.rfP_fold_10
            sum_rfP_15+=var.rfP_fold_15
            sum_rfP_20+=var.rfP_fold_20
            count_rfP_0+=1
            count_rfP_5+=1
            count_rfP_10+=1
            count_rfP_15+=1
            count_rfP_20+=1
        return(round(sum_rfP_0/count_rfP_0,2),round(sum_rfP_5/count_rfP_5,2),round(sum_rfP_10/count_rfP_10,2),round(sum_rfP_15/count_rfP_15,2),round(sum_rfP_20/count_rfP_20,2))
    avg_rfP_0,avg_rfP_5,avg_rfP_10,avg_rfP_15,avg_rfP_20 = avg_rfP()

    def avg_nbP():
        sum_nbP_0=0
        count_nbP_0=0
        sum_nbP_5=0
        count_nbP_5=0
        sum_nbP_10=0
        count_nbP_10=0
        sum_nbP_15=0
        count_nbP_15=0
        sum_nbP_20=0
        count_nbP_20=0
        for var in nbP_list:
            sum_nbP_0+=var.nbP_fold_0
            sum_nbP_5+=var.nbP_fold_5
            sum_nbP_10+=var.nbP_fold_10
            sum_nbP_15+=var.nbP_fold_15
            sum_nbP_20+=var.nbP_fold_20
            count_nbP_0+=1
            count_nbP_5+=1
            count_nbP_10+=1
            count_nbP_15+=1
            count_nbP_20+=1
        return(round(sum_nbP_0/count_nbP_0,2),round(sum_nbP_5/count_nbP_5,2),round(sum_nbP_10/count_nbP_10,2),round(sum_nbP_15/count_nbP_15,2),round(sum_nbP_20/count_nbP_20,2))
    avg_nbP_0,avg_nbP_5,avg_nbP_10,avg_nbP_15,avg_nbP_20 = avg_nbP()

    svm_final_avg = round((avg_svmP_0+avg_svmP_5+avg_svmP_10+avg_svmP_15+avg_svmP_20)/5,2)
    dt_final_avg = round((avg_dtP_0+avg_dtP_5+avg_dtP_10+avg_dtP_15+avg_dtP_20)/5,2)
    lr_final_avg = round((avg_lrP_0+avg_lrP_5+avg_lrP_10+avg_lrP_15+avg_lrP_20)/5,2)
    rf_final_avg = round((avg_rfP_0+avg_rfP_5+avg_rfP_10+avg_rfP_15+avg_rfP_20)/5,2)
    nb_final_avg = round((avg_nbP_0+avg_nbP_5+avg_nbP_10+avg_nbP_15+avg_nbP_20)/5,2)

    return render(request,'cancer/prostateAccuracy.html',context={'my_dict':my_dict,'svmP_list':svmP_list,'dtP_list':dtP_list,'lrP_list':lrP_list,'rfP_list':rfP_list,'nbP_list':nbP_list,'avg_svmP_0':avg_svmP_0,'avg_svmP_5':avg_svmP_5,'avg_svmP_10':avg_svmP_10,'avg_svmP_15':avg_svmP_15,'avg_svmP_20':avg_svmP_20,
                                                                  'avg_dtP_0':avg_dtP_0,'avg_dtP_5':avg_dtP_5,'avg_dtP_10':avg_dtP_10,'avg_dtP_15':avg_dtP_15,'avg_dtP_20':avg_dtP_20,'avg_lrP_0':avg_lrP_0,'avg_lrP_5':avg_lrP_5,'avg_lrP_10':avg_lrP_10,'avg_lrP_15':avg_lrP_15,'avg_lrP_20':avg_lrP_20,
                                                                  'avg_rfP_0':avg_rfP_0,'avg_rfP_5':avg_rfP_5,'avg_rfP_10':avg_rfP_10,'avg_rfP_15':avg_rfP_15,'avg_rfP_20':avg_rfP_20,'avg_nbP_0':avg_nbP_0,'avg_nbP_5':avg_nbP_5,'avg_nbP_10':avg_nbP_10,'avg_nbP_15':avg_nbP_15,'avg_nbP_20':avg_nbP_20,
                                                                  'svm_final_avg':svm_final_avg,'dt_final_avg':dt_final_avg,'lr_final_avg':lr_final_avg,'rf_final_avg':rf_final_avg,'nb_final_avg':nb_final_avg})

def index_script(request):
    my_dict = {'this1':execute_this.exec()}
    return render(request,'cancer/index.html',context=my_dict)

def test1(request):
    import pandas as pd
    import csv
    patient_id = request.POST.get('p_patient_id','')
    radius = request.POST.get('p_radius','')
    texture = request.POST.get('p_texture','')
    perimeter = request.POST.get('p_perimeter','')
    area = request.POST.get('p_area','')
    smoothness = request.POST.get('p_smoothness','')
    compactness = request.POST.get('p_compactness','')
    symmetry = request.POST.get('p_symmetry','')
    fd = request.POST.get('p_fd','')
    # filename_patient = "TP_"+str(patient_id)+".csv"
    response = HttpResponse(content_type='text/csv')
    filename = "TP_"+str(patient_id)
    response['Content-Disposition'] = "attachment; filename=\"" + filename + ".csv\""
    # response['Content-Disposition'] = 'attachment; filename="TP.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','radius','texture','perimeter','area','smoothness','compactness','symmetry','fractal_dimension'])
    data = []
    data.append(patient_id)
    data.append(radius)
    data.append(texture)
    data.append(perimeter)
    data.append(area)
    data.append(smoothness)
    data.append(compactness)
    data.append(symmetry)
    data.append(fd)
    writer.writerow(data)
    return response
    # return HttpResponse(first_name)
    # return render(request,'cancer/test1.html')

def test2(request):
    import pandas as pd
    import csv
    patient_id = request.POST.get('b_patient_id','')
    radius = request.POST.get('b_radius','')
    texture = request.POST.get('b_texture','')
    perimeter = request.POST.get('b_perimeter','')
    area = request.POST.get('b_area','')
    smoothness = request.POST.get('b_smoothness','')
    compactness = request.POST.get('b_compactness','')
    symmetry = request.POST.get('b_symmetry','')
    fd = request.POST.get('b_fd','')
    # filename_patient = "TP_"+str(patient_id)+".csv"
    response = HttpResponse(content_type='text/csv')
    filename = "TB_"+str(patient_id)
    response['Content-Disposition'] = "attachment; filename=\"" + filename + ".csv\""
    # response['Content-Disposition'] = 'attachment; filename="TP.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','radius','texture','perimeter','area','smoothness','compactness','symmetry','fractal_dimension'])
    data = []
    data.append(patient_id)
    data.append(radius)
    data.append(texture)
    data.append(perimeter)
    data.append(area)
    data.append(smoothness)
    data.append(compactness)
    data.append(symmetry)
    data.append(fd)
    writer.writerow(data)
    return response
    # return HttpResponse(first_name)
    # return render(request,'cancer/test1.html')

def patient_detail_P(request):
    import pandas as pd
    import csv
    first_name = request.POST.get('p_p_fname','')
    last_name = request.POST.get('p_p_lname','')
    dob = request.POST.get('p_p_dob','')
    gender = request.POST.get('p_p_gender','')
    blood_grp = request.POST.get('p_p_bg','')
    parents_name = request.POST.get('p_pn','')
    spouse_name = request.POST.get('p_sn','')
    # patient_id = request.POST.get('p_patient_id','')
    genomecsv = request.POST.get('p_genome_csv','')
    genome_csv = str(genomecsv)
    result_prostate,id,radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension = test_algo.test_Prostate(genome_csv)
    patient_detail_Pdict = {'first_name':first_name,'last_name':last_name,'dob':dob,'gender':gender,'blood_grp':blood_grp,'parents_name':parents_name,'spouse_name':spouse_name,'result':result_prostate,'radius':radius,'texture':texture,'perimeter':perimeter,'area':area,'smoothness':smoothness,'compactness':compactness,'symmetry':symmetry,'fractal_dimension':fractal_dimension}
    populate.populate_patient_dataP(patient_detail_Pdict)
    return render(request,'cancer/testProstate.html',context={'patient_detail_Pdict':patient_detail_Pdict,'result_prostate':result_prostate,'patient_id':id})


def patient_detail_B(request):
    import pandas as pd
    import csv
    first_name = request.POST.get('b_p_fname','')
    last_name = request.POST.get('b_p_lname','')
    dob = request.POST.get('b_p_dob','')
    gender = request.POST.get('b_p_gender','')
    blood_grp = request.POST.get('b_p_bg','')
    parents_name = request.POST.get('b_pn','')
    spouse_name = request.POST.get('b_sn','')
    # patient_id = request.POST.get('b_patient_id','')
    genomecsv = request.POST.get('b_genome_csv','')
    genome_csv = str(genomecsv)
    result_breast,id,radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension = test_algo.test_Breast(genome_csv)
    patient_detail_Bdict = {'first_name':first_name,'last_name':last_name,'dob':dob,'gender':gender,'blood_grp':blood_grp,'parents_name':parents_name,'spouse_name':spouse_name,'result':result_breast,'radius':radius,'texture':texture,'perimeter':perimeter,'area':area,'smoothness':smoothness,'compactness':compactness,'symmetry':symmetry,'fractal_dimension':fractal_dimension}
    populate.populate_patient_dataB(patient_detail_Bdict)
    return render(request,'cancer/testBreast.html',context={'patient_detail_Bdict':patient_detail_Bdict,'result_breast':result_breast,'patient_id':id})


def patientTested(request):
    patient_info=patient.objects.order_by('id')
    return render(request,'cancer/patientTested.html',context={'patient_info':patient_info})


def b_dim_red(request):
    my_dict = populate.populate_dim_B()
    svmBD_list = svmB_D.objects.order_by('-svmBD_date')
    dtBD_list=dtB_D.objects.order_by('-dtBD_date')
    lrBD_list=lrB_D.objects.order_by('-lrBD_date')
    rfBD_list=rfB_D.objects.order_by('-rfBD_date')
    nbBD_list=nbB_D.objects.order_by('-nbBD_date')

    def avg_smvBD():
        sum_svmBD_0 = 0
        count_svmBD_0 = 0
        sum_svmBD_5 = 0
        count_svmBD_5 = 0
        sum_svmBD_10 = 0
        count_svmBD_10 = 0
        sum_svmBD_15 = 0
        count_svmBD_15 = 0
        sum_svmBD_20 = 0
        count_svmBD_20 = 0
        for var in svmBD_list:
            sum_svmBD_0+=var.svmBD_fold_0
            sum_svmBD_5+=var.svmBD_fold_5
            sum_svmBD_10+=var.svmBD_fold_10
            sum_svmBD_15+=var.svmBD_fold_15
            sum_svmBD_20+=var.svmBD_fold_20
            count_svmBD_0+=1
            count_svmBD_5+=1
            count_svmBD_10+=1
            count_svmBD_15+=1
            count_svmBD_20+=1
        return (round(sum_svmBD_0/count_svmBD_0,2),round(sum_svmBD_5/count_svmBD_5,2),round(sum_svmBD_10/count_svmBD_10,2),round(sum_svmBD_15/count_svmBD_15,2),round(sum_svmBD_20/count_svmBD_20,2))
    avg_svmBD_0,avg_svmBD_5,avg_svmBD_10,avg_svmBD_15,avg_svmBD_20 = avg_smvBD()

    def avg_dtBD():
        sum_dtBD_0=0
        count_dtBD_0=0
        sum_dtBD_5=0
        count_dtBD_5=0
        sum_dtBD_10=0
        count_dtBD_10=0
        sum_dtBD_15=0
        count_dtBD_15=0
        sum_dtBD_20=0
        count_dtBD_20=0
        for var in dtBD_list:
            sum_dtBD_0+=var.dtBD_fold_0
            sum_dtBD_5+=var.dtBD_fold_5
            sum_dtBD_10+=var.dtBD_fold_10
            sum_dtBD_15+=var.dtBD_fold_15
            sum_dtBD_20+=var.dtBD_fold_20
            count_dtBD_0+=1
            count_dtBD_5+=1
            count_dtBD_10+=1
            count_dtBD_15+=1
            count_dtBD_20+=1
        return(round(sum_dtBD_0/count_dtBD_0,2),round(sum_dtBD_5/count_dtBD_5,2),round(sum_dtBD_10/count_dtBD_10,2),round(sum_dtBD_15/count_dtBD_15,2),round(sum_dtBD_20/count_dtBD_20,2))
    avg_dtBD_0,avg_dtBD_5,avg_dtBD_10,avg_dtBD_15,avg_dtBD_20 = avg_dtBD()

    def avg_lrBD():
        sum_lrBD_0=0
        count_lrBD_0=0
        sum_lrBD_5=0
        count_lrBD_5=0
        sum_lrBD_10=0
        count_lrBD_10=0
        sum_lrBD_15=0
        count_lrBD_15=0
        sum_lrBD_20=0
        count_lrBD_20=0
        for var in lrBD_list:
            sum_lrBD_0+=var.lrBD_fold_0
            sum_lrBD_5+=var.lrBD_fold_5
            sum_lrBD_10+=var.lrBD_fold_10
            sum_lrBD_15+=var.lrBD_fold_15
            sum_lrBD_20+=var.lrBD_fold_20
            count_lrBD_0+=1
            count_lrBD_5+=1
            count_lrBD_10+=1
            count_lrBD_15+=1
            count_lrBD_20+=1
        return(round(sum_lrBD_0/count_lrBD_0,2),round(sum_lrBD_5/count_lrBD_5,2),round(sum_lrBD_10/count_lrBD_10,2),round(sum_lrBD_15/count_lrBD_15,2),round(sum_lrBD_20/count_lrBD_20,2))
    avg_lrBD_0,avg_lrBD_5,avg_lrBD_10,avg_lrBD_15,avg_lrBD_20 = avg_lrBD()

    def avg_rfBD():
        sum_rfBD_0=0
        count_rfBD_0=0
        sum_rfBD_5=0
        count_rfBD_5=0
        sum_rfBD_10=0
        count_rfBD_10=0
        sum_rfBD_15=0
        count_rfBD_15=0
        sum_rfBD_20=0
        count_rfBD_20=0
        for var in rfBD_list:
            sum_rfBD_0+=var.rfBD_fold_0
            sum_rfBD_5+=var.rfBD_fold_5
            sum_rfBD_10+=var.rfBD_fold_10
            sum_rfBD_15+=var.rfBD_fold_15
            sum_rfBD_20+=var.rfBD_fold_20
            count_rfBD_0+=1
            count_rfBD_5+=1
            count_rfBD_10+=1
            count_rfBD_15+=1
            count_rfBD_20+=1
        return(round(sum_rfBD_0/count_rfBD_0,2),round(sum_rfBD_5/count_rfBD_5,2),round(sum_rfBD_10/count_rfBD_10,2),round(sum_rfBD_15/count_rfBD_15,2),round(sum_rfBD_20/count_rfBD_20,2))
    avg_rfBD_0,avg_rfBD_5,avg_rfBD_10,avg_rfBD_15,avg_rfBD_20 = avg_rfBD()

    def avg_nbBD():
        sum_nbBD_0=0
        count_nbBD_0=0
        sum_nbBD_5=0
        count_nbBD_5=0
        sum_nbBD_10=0
        count_nbBD_10=0
        sum_nbBD_15=0
        count_nbBD_15=0
        sum_nbBD_20=0
        count_nbBD_20=0
        for var in nbBD_list:
            sum_nbBD_0+=var.nbBD_fold_0
            sum_nbBD_5+=var.nbBD_fold_5
            sum_nbBD_10+=var.nbBD_fold_10
            sum_nbBD_15+=var.nbBD_fold_15
            sum_nbBD_20+=var.nbBD_fold_20
            count_nbBD_0+=1
            count_nbBD_5+=1
            count_nbBD_10+=1
            count_nbBD_15+=1
            count_nbBD_20+=1
        return(round(sum_nbBD_0/count_nbBD_0,2),round(sum_nbBD_5/count_nbBD_5,2),round(sum_nbBD_10/count_nbBD_10,2),round(sum_nbBD_15/count_nbBD_15,2),round(sum_nbBD_20/count_nbBD_20,2))
    avg_nbBD_0,avg_nbBD_5,avg_nbBD_10,avg_nbBD_15,avg_nbBD_20 = avg_nbBD()

    svm_final_avg_BD = round((avg_svmBD_0+avg_svmBD_5+avg_svmBD_10+avg_svmBD_15+avg_svmBD_20)/5,2)
    dt_final_avg_BD = round((avg_dtBD_0+avg_dtBD_5+avg_dtBD_10+avg_dtBD_15+avg_dtBD_20)/5,2)
    lr_final_avg_BD = round((avg_lrBD_0+avg_lrBD_5+avg_lrBD_10+avg_lrBD_15+avg_lrBD_20)/5,2)
    rf_final_avg_BD = round((avg_rfBD_0+avg_rfBD_5+avg_rfBD_10+avg_rfBD_15+avg_rfBD_20)/5,2)
    nb_final_avg_BD = round((avg_nbBD_0+avg_nbBD_5+avg_nbBD_10+avg_nbBD_15+avg_nbBD_20)/5,2)


    return render(request,'cancer/b_dim_red.html',context={'my_dict':my_dict,'svmBD_list':svmBD_list,'dtBD_list':dtBD_list,'lrBD_list':lrBD_list,'rfBD_list':rfBD_list,'nbBD_list':nbBD_list,'avg_svmBD_0':avg_svmBD_0,'avg_svmBD_5':avg_svmBD_5,'avg_svmBD_10':avg_svmBD_10,'avg_svmBD_15':avg_svmBD_15,'avg_svmBD_20':avg_svmBD_20,
                                                                  'avg_dtBD_0':avg_dtBD_0,'avg_dtBD_5':avg_dtBD_5,'avg_dtBD_10':avg_dtBD_10,'avg_dtBD_15':avg_dtBD_15,'avg_dtBD_20':avg_dtBD_20,'avg_lrBD_0':avg_lrBD_0,'avg_lrBD_5':avg_lrBD_5,'avg_lrBD_10':avg_lrBD_10,'avg_lrBD_15':avg_lrBD_15,'avg_lrBD_20':avg_lrBD_20,
                                                                  'avg_rfBD_0':avg_rfBD_0,'avg_rfBD_5':avg_rfBD_5,'avg_rfBD_10':avg_rfBD_10,'avg_rfBD_15':avg_rfBD_15,'avg_rfBD_20':avg_rfBD_20,'avg_nbBD_0':avg_nbBD_0,'avg_nbBD_5':avg_nbBD_5,'avg_nbBD_10':avg_nbBD_10,'avg_nbBD_15':avg_nbBD_15,'avg_nbBD_20':avg_nbBD_20,
                                                                  'svm_final_avg_BD':svm_final_avg_BD,'dt_final_avg_BD':dt_final_avg_BD,'lr_final_avg_BD':lr_final_avg_BD,'rf_final_avg_BD':rf_final_avg_BD,'nb_final_avg_BD':nb_final_avg_BD})


def admin_statistics(request):

    svmB_list = svmB.objects.order_by('-svmB_date')
    dtB_list=dtB.objects.order_by('-dtB_date')
    lrB_list=lrB.objects.order_by('-lrB_date')
    rfB_list=rfB.objects.order_by('-rfB_date')
    nbB_list=nbB.objects.order_by('-nbB_date')
    def avg_smvB():
        sum_svmB_0 = 0
        count_svmB_0 = 0
        sum_svmB_5 = 0
        count_svmB_5 = 0
        sum_svmB_10 = 0
        count_svmB_10 = 0
        sum_svmB_15 = 0
        count_svmB_15 = 0
        sum_svmB_20 = 0
        count_svmB_20 = 0
        for var in svmB_list:
            sum_svmB_0+=var.svmB_fold_0
            sum_svmB_5+=var.svmB_fold_5
            sum_svmB_10+=var.svmB_fold_10
            sum_svmB_15+=var.svmB_fold_15
            sum_svmB_20+=var.svmB_fold_20
            count_svmB_0+=1
            count_svmB_5+=1
            count_svmB_10+=1
            count_svmB_15+=1
            count_svmB_20+=1
        return (round(sum_svmB_0/count_svmB_0,2),round(sum_svmB_5/count_svmB_5,2),round(sum_svmB_10/count_svmB_10,2),round(sum_svmB_15/count_svmB_15,2),round(sum_svmB_20/count_svmB_20,2))
    avg_svmB_0,avg_svmB_5,avg_svmB_10,avg_svmB_15,avg_svmB_20 = avg_smvB()

    def avg_dtB():
        sum_dtB_0=0
        count_dtB_0=0
        sum_dtB_5=0
        count_dtB_5=0
        sum_dtB_10=0
        count_dtB_10=0
        sum_dtB_15=0
        count_dtB_15=0
        sum_dtB_20=0
        count_dtB_20=0
        for var in dtB_list:
            sum_dtB_0+=var.dtB_fold_0
            sum_dtB_5+=var.dtB_fold_5
            sum_dtB_10+=var.dtB_fold_10
            sum_dtB_15+=var.dtB_fold_15
            sum_dtB_20+=var.dtB_fold_20
            count_dtB_0+=1
            count_dtB_5+=1
            count_dtB_10+=1
            count_dtB_15+=1
            count_dtB_20+=1
        return(round(sum_dtB_0/count_dtB_0,2),round(sum_dtB_5/count_dtB_5,2),round(sum_dtB_10/count_dtB_10,2),round(sum_dtB_15/count_dtB_15,2),round(sum_dtB_20/count_dtB_20,2))
    avg_dtB_0,avg_dtB_5,avg_dtB_10,avg_dtB_15,avg_dtB_20 = avg_dtB()

    def avg_lrB():
        sum_lrB_0=0
        count_lrB_0=0
        sum_lrB_5=0
        count_lrB_5=0
        sum_lrB_10=0
        count_lrB_10=0
        sum_lrB_15=0
        count_lrB_15=0
        sum_lrB_20=0
        count_lrB_20=0
        for var in lrB_list:
            sum_lrB_0+=var.lrB_fold_0
            sum_lrB_5+=var.lrB_fold_5
            sum_lrB_10+=var.lrB_fold_10
            sum_lrB_15+=var.lrB_fold_15
            sum_lrB_20+=var.lrB_fold_20
            count_lrB_0+=1
            count_lrB_5+=1
            count_lrB_10+=1
            count_lrB_15+=1
            count_lrB_20+=1
        return(round(sum_lrB_0/count_lrB_0,2),round(sum_lrB_5/count_lrB_5,2),round(sum_lrB_10/count_lrB_10,2),round(sum_lrB_15/count_lrB_15,2),round(sum_lrB_20/count_lrB_20,2))
    avg_lrB_0,avg_lrB_5,avg_lrB_10,avg_lrB_15,avg_lrB_20 = avg_lrB()

    def avg_rfB():
        sum_rfB_0=0
        count_rfB_0=0
        sum_rfB_5=0
        count_rfB_5=0
        sum_rfB_10=0
        count_rfB_10=0
        sum_rfB_15=0
        count_rfB_15=0
        sum_rfB_20=0
        count_rfB_20=0
        for var in rfB_list:
            sum_rfB_0+=var.rfB_fold_0
            sum_rfB_5+=var.rfB_fold_5
            sum_rfB_10+=var.rfB_fold_10
            sum_rfB_15+=var.rfB_fold_15
            sum_rfB_20+=var.rfB_fold_20
            count_rfB_0+=1
            count_rfB_5+=1
            count_rfB_10+=1
            count_rfB_15+=1
            count_rfB_20+=1
        return(round(sum_rfB_0/count_rfB_0,2),round(sum_rfB_5/count_rfB_5,2),round(sum_rfB_10/count_rfB_10,2),round(sum_rfB_15/count_rfB_15,2),round(sum_rfB_20/count_rfB_20,2))
    avg_rfB_0,avg_rfB_5,avg_rfB_10,avg_rfB_15,avg_rfB_20 = avg_rfB()

    def avg_nbB():
        sum_nbB_0=0
        count_nbB_0=0
        sum_nbB_5=0
        count_nbB_5=0
        sum_nbB_10=0
        count_nbB_10=0
        sum_nbB_15=0
        count_nbB_15=0
        sum_nbB_20=0
        count_nbB_20=0
        for var in nbB_list:
            sum_nbB_0+=var.nbB_fold_0
            sum_nbB_5+=var.nbB_fold_5
            sum_nbB_10+=var.nbB_fold_10
            sum_nbB_15+=var.nbB_fold_15
            sum_nbB_20+=var.nbB_fold_20
            count_nbB_0+=1
            count_nbB_5+=1
            count_nbB_10+=1
            count_nbB_15+=1
            count_nbB_20+=1
        return(round(sum_nbB_0/count_nbB_0,2),round(sum_nbB_5/count_nbB_5,2),round(sum_nbB_10/count_nbB_10,2),round(sum_nbB_15/count_nbB_15,2),round(sum_nbB_20/count_nbB_20,2))
    avg_nbB_0,avg_nbB_5,avg_nbB_10,avg_nbB_15,avg_nbB_20 = avg_nbB()

    svm_final_avg_B = round((avg_svmB_0+avg_svmB_5+avg_svmB_10+avg_svmB_15+avg_svmB_20)/5,2)
    dt_final_avg_B = round((avg_dtB_0+avg_dtB_5+avg_dtB_10+avg_dtB_15+avg_dtB_20)/5,2)
    lr_final_avg_B = round((avg_lrB_0+avg_lrB_5+avg_lrB_10+avg_lrB_15+avg_lrB_20)/5,2)
    rf_final_avg_B = round((avg_rfB_0+avg_rfB_5+avg_rfB_10+avg_rfB_15+avg_rfB_20)/5,2)
    nb_final_avg_B = round((avg_nbB_0+avg_nbB_5+avg_nbB_10+avg_nbB_15+avg_nbB_20)/5,2)

    svmBD_list = svmB_D.objects.order_by('-svmBD_date')
    dtBD_list=dtB_D.objects.order_by('-dtBD_date')
    lrBD_list=lrB_D.objects.order_by('-lrBD_date')
    rfBD_list=rfB_D.objects.order_by('-rfBD_date')
    nbBD_list=nbB_D.objects.order_by('-nbBD_date')

    def avg_smvBD():
        sum_svmBD_0 = 0
        count_svmBD_0 = 0
        sum_svmBD_5 = 0
        count_svmBD_5 = 0
        sum_svmBD_10 = 0
        count_svmBD_10 = 0
        sum_svmBD_15 = 0
        count_svmBD_15 = 0
        sum_svmBD_20 = 0
        count_svmBD_20 = 0
        for var in svmBD_list:
            sum_svmBD_0+=var.svmBD_fold_0
            sum_svmBD_5+=var.svmBD_fold_5
            sum_svmBD_10+=var.svmBD_fold_10
            sum_svmBD_15+=var.svmBD_fold_15
            sum_svmBD_20+=var.svmBD_fold_20
            count_svmBD_0+=1
            count_svmBD_5+=1
            count_svmBD_10+=1
            count_svmBD_15+=1
            count_svmBD_20+=1
        return (round(sum_svmBD_0/count_svmBD_0,2),round(sum_svmBD_5/count_svmBD_5,2),round(sum_svmBD_10/count_svmBD_10,2),round(sum_svmBD_15/count_svmBD_15,2),round(sum_svmBD_20/count_svmBD_20,2))
    avg_svmBD_0,avg_svmBD_5,avg_svmBD_10,avg_svmBD_15,avg_svmBD_20 = avg_smvBD()

    def avg_dtBD():
        sum_dtBD_0=0
        count_dtBD_0=0
        sum_dtBD_5=0
        count_dtBD_5=0
        sum_dtBD_10=0
        count_dtBD_10=0
        sum_dtBD_15=0
        count_dtBD_15=0
        sum_dtBD_20=0
        count_dtBD_20=0
        for var in dtBD_list:
            sum_dtBD_0+=var.dtBD_fold_0
            sum_dtBD_5+=var.dtBD_fold_5
            sum_dtBD_10+=var.dtBD_fold_10
            sum_dtBD_15+=var.dtBD_fold_15
            sum_dtBD_20+=var.dtBD_fold_20
            count_dtBD_0+=1
            count_dtBD_5+=1
            count_dtBD_10+=1
            count_dtBD_15+=1
            count_dtBD_20+=1
        return(round(sum_dtBD_0/count_dtBD_0,2),round(sum_dtBD_5/count_dtBD_5,2),round(sum_dtBD_10/count_dtBD_10,2),round(sum_dtBD_15/count_dtBD_15,2),round(sum_dtBD_20/count_dtBD_20,2))
    avg_dtBD_0,avg_dtBD_5,avg_dtBD_10,avg_dtBD_15,avg_dtBD_20 = avg_dtBD()

    def avg_lrBD():
        sum_lrBD_0=0
        count_lrBD_0=0
        sum_lrBD_5=0
        count_lrBD_5=0
        sum_lrBD_10=0
        count_lrBD_10=0
        sum_lrBD_15=0
        count_lrBD_15=0
        sum_lrBD_20=0
        count_lrBD_20=0
        for var in lrBD_list:
            sum_lrBD_0+=var.lrBD_fold_0
            sum_lrBD_5+=var.lrBD_fold_5
            sum_lrBD_10+=var.lrBD_fold_10
            sum_lrBD_15+=var.lrBD_fold_15
            sum_lrBD_20+=var.lrBD_fold_20
            count_lrBD_0+=1
            count_lrBD_5+=1
            count_lrBD_10+=1
            count_lrBD_15+=1
            count_lrBD_20+=1
        return(round(sum_lrBD_0/count_lrBD_0,2),round(sum_lrBD_5/count_lrBD_5,2),round(sum_lrBD_10/count_lrBD_10,2),round(sum_lrBD_15/count_lrBD_15,2),round(sum_lrBD_20/count_lrBD_20,2))
    avg_lrBD_0,avg_lrBD_5,avg_lrBD_10,avg_lrBD_15,avg_lrBD_20 = avg_lrBD()

    def avg_rfBD():
        sum_rfBD_0=0
        count_rfBD_0=0
        sum_rfBD_5=0
        count_rfBD_5=0
        sum_rfBD_10=0
        count_rfBD_10=0
        sum_rfBD_15=0
        count_rfBD_15=0
        sum_rfBD_20=0
        count_rfBD_20=0
        for var in rfBD_list:
            sum_rfBD_0+=var.rfBD_fold_0
            sum_rfBD_5+=var.rfBD_fold_5
            sum_rfBD_10+=var.rfBD_fold_10
            sum_rfBD_15+=var.rfBD_fold_15
            sum_rfBD_20+=var.rfBD_fold_20
            count_rfBD_0+=1
            count_rfBD_5+=1
            count_rfBD_10+=1
            count_rfBD_15+=1
            count_rfBD_20+=1
        return(round(sum_rfBD_0/count_rfBD_0,2),round(sum_rfBD_5/count_rfBD_5,2),round(sum_rfBD_10/count_rfBD_10,2),round(sum_rfBD_15/count_rfBD_15,2),round(sum_rfBD_20/count_rfBD_20,2))
    avg_rfBD_0,avg_rfBD_5,avg_rfBD_10,avg_rfBD_15,avg_rfBD_20 = avg_rfBD()

    def avg_nbBD():
        sum_nbBD_0=0
        count_nbBD_0=0
        sum_nbBD_5=0
        count_nbBD_5=0
        sum_nbBD_10=0
        count_nbBD_10=0
        sum_nbBD_15=0
        count_nbBD_15=0
        sum_nbBD_20=0
        count_nbBD_20=0
        for var in nbBD_list:
            sum_nbBD_0+=var.nbBD_fold_0
            sum_nbBD_5+=var.nbBD_fold_5
            sum_nbBD_10+=var.nbBD_fold_10
            sum_nbBD_15+=var.nbBD_fold_15
            sum_nbBD_20+=var.nbBD_fold_20
            count_nbBD_0+=1
            count_nbBD_5+=1
            count_nbBD_10+=1
            count_nbBD_15+=1
            count_nbBD_20+=1
        return(round(sum_nbBD_0/count_nbBD_0,2),round(sum_nbBD_5/count_nbBD_5,2),round(sum_nbBD_10/count_nbBD_10,2),round(sum_nbBD_15/count_nbBD_15,2),round(sum_nbBD_20/count_nbBD_20,2))
    avg_nbBD_0,avg_nbBD_5,avg_nbBD_10,avg_nbBD_15,avg_nbBD_20 = avg_nbBD()

    svm_final_avg_BD = round((avg_svmBD_0+avg_svmBD_5+avg_svmBD_10+avg_svmBD_15+avg_svmBD_20)/5,2)
    dt_final_avg_BD = round((avg_dtBD_0+avg_dtBD_5+avg_dtBD_10+avg_dtBD_15+avg_dtBD_20)/5,2)
    lr_final_avg_BD = round((avg_lrBD_0+avg_lrBD_5+avg_lrBD_10+avg_lrBD_15+avg_lrBD_20)/5,2)
    rf_final_avg_BD = round((avg_rfBD_0+avg_rfBD_5+avg_rfBD_10+avg_rfBD_15+avg_rfBD_20)/5,2)
    nb_final_avg_BD = round((avg_nbBD_0+avg_nbBD_5+avg_nbBD_10+avg_nbBD_15+avg_nbBD_20)/5,2)

    svmPD_list = svmP_D.objects.order_by('-svmPD_date')
    dtPD_list=dtP_D.objects.order_by('-dtPD_date')
    lrPD_list=lrP_D.objects.order_by('-lrPD_date')
    rfPD_list=rfP_D.objects.order_by('-rfPD_date')
    nbPD_list=nbP_D.objects.order_by('-nbPD_date')

    def avg_smvPD():
        sum_svmPD_0 = 0
        count_svmPD_0 = 0
        sum_svmPD_5 = 0
        count_svmPD_5 = 0
        sum_svmPD_10 = 0
        count_svmPD_10 = 0
        sum_svmPD_15 = 0
        count_svmPD_15 = 0
        sum_svmPD_20 = 0
        count_svmPD_20 = 0
        for var in svmPD_list:
            sum_svmPD_0+=var.svmPD_fold_0
            sum_svmPD_5+=var.svmPD_fold_5
            sum_svmPD_10+=var.svmPD_fold_10
            sum_svmPD_15+=var.svmPD_fold_15
            sum_svmPD_20+=var.svmPD_fold_20
            count_svmPD_0+=1
            count_svmPD_5+=1
            count_svmPD_10+=1
            count_svmPD_15+=1
            count_svmPD_20+=1
        return (round(sum_svmPD_0/count_svmPD_0,2),round(sum_svmPD_5/count_svmPD_5,2),round(sum_svmPD_10/count_svmPD_10,2),round(sum_svmPD_15/count_svmPD_15,2),round(sum_svmPD_20/count_svmPD_20,2))
    avg_svmPD_0,avg_svmPD_5,avg_svmPD_10,avg_svmPD_15,avg_svmPD_20 = avg_smvPD()

    def avg_dtPD():
        sum_dtPD_0=0
        count_dtPD_0=0
        sum_dtPD_5=0
        count_dtPD_5=0
        sum_dtPD_10=0
        count_dtPD_10=0
        sum_dtPD_15=0
        count_dtPD_15=0
        sum_dtPD_20=0
        count_dtPD_20=0
        for var in dtPD_list:
            sum_dtPD_0+=var.dtPD_fold_0
            sum_dtPD_5+=var.dtPD_fold_5
            sum_dtPD_10+=var.dtPD_fold_10
            sum_dtPD_15+=var.dtPD_fold_15
            sum_dtPD_20+=var.dtPD_fold_20
            count_dtPD_0+=1
            count_dtPD_5+=1
            count_dtPD_10+=1
            count_dtPD_15+=1
            count_dtPD_20+=1
        return(round(sum_dtPD_0/count_dtPD_0,2),round(sum_dtPD_5/count_dtPD_5,2),round(sum_dtPD_10/count_dtPD_10,2),round(sum_dtPD_15/count_dtPD_15,2),round(sum_dtPD_20/count_dtPD_20,2))
    avg_dtPD_0,avg_dtPD_5,avg_dtPD_10,avg_dtPD_15,avg_dtPD_20 = avg_dtPD()

    def avg_lrPD():
        sum_lrPD_0=0
        count_lrPD_0=0
        sum_lrPD_5=0
        count_lrPD_5=0
        sum_lrPD_10=0
        count_lrPD_10=0
        sum_lrPD_15=0
        count_lrPD_15=0
        sum_lrPD_20=0
        count_lrPD_20=0
        for var in lrPD_list:
            sum_lrPD_0+=var.lrPD_fold_0
            sum_lrPD_5+=var.lrPD_fold_5
            sum_lrPD_10+=var.lrPD_fold_10
            sum_lrPD_15+=var.lrPD_fold_15
            sum_lrPD_20+=var.lrPD_fold_20
            count_lrPD_0+=1
            count_lrPD_5+=1
            count_lrPD_10+=1
            count_lrPD_15+=1
            count_lrPD_20+=1
        return(round(sum_lrPD_0/count_lrPD_0,2),round(sum_lrPD_5/count_lrPD_5,2),round(sum_lrPD_10/count_lrPD_10,2),round(sum_lrPD_15/count_lrPD_15,2),round(sum_lrPD_20/count_lrPD_20,2))
    avg_lrPD_0,avg_lrPD_5,avg_lrPD_10,avg_lrPD_15,avg_lrPD_20 = avg_lrPD()

    def avg_rfPD():
        sum_rfPD_0=0
        count_rfPD_0=0
        sum_rfPD_5=0
        count_rfPD_5=0
        sum_rfPD_10=0
        count_rfPD_10=0
        sum_rfPD_15=0
        count_rfPD_15=0
        sum_rfPD_20=0
        count_rfPD_20=0
        for var in rfPD_list:
            sum_rfPD_0+=var.rfPD_fold_0
            sum_rfPD_5+=var.rfPD_fold_5
            sum_rfPD_10+=var.rfPD_fold_10
            sum_rfPD_15+=var.rfPD_fold_15
            sum_rfPD_20+=var.rfPD_fold_20
            count_rfPD_0+=1
            count_rfPD_5+=1
            count_rfPD_10+=1
            count_rfPD_15+=1
            count_rfPD_20+=1
        return(round(sum_rfPD_0/count_rfPD_0,2),round(sum_rfPD_5/count_rfPD_5,2),round(sum_rfPD_10/count_rfPD_10,2),round(sum_rfPD_15/count_rfPD_15,2),round(sum_rfPD_20/count_rfPD_20,2))
    avg_rfPD_0,avg_rfPD_5,avg_rfPD_10,avg_rfPD_15,avg_rfPD_20 = avg_rfPD()

    def avg_nbPD():
        sum_nbPD_0=0
        count_nbPD_0=0
        sum_nbPD_5=0
        count_nbPD_5=0
        sum_nbPD_10=0
        count_nbPD_10=0
        sum_nbPD_15=0
        count_nbPD_15=0
        sum_nbPD_20=0
        count_nbPD_20=0
        for var in nbPD_list:
            sum_nbPD_0+=var.nbPD_fold_0
            sum_nbPD_5+=var.nbPD_fold_5
            sum_nbPD_10+=var.nbPD_fold_10
            sum_nbPD_15+=var.nbPD_fold_15
            sum_nbPD_20+=var.nbPD_fold_20
            count_nbPD_0+=1
            count_nbPD_5+=1
            count_nbPD_10+=1
            count_nbPD_15+=1
            count_nbPD_20+=1
        return(round(sum_nbPD_0/count_nbPD_0,2),round(sum_nbPD_5/count_nbPD_5,2),round(sum_nbPD_10/count_nbPD_10,2),round(sum_nbPD_15/count_nbPD_15,2),round(sum_nbPD_20/count_nbPD_20,2))
    avg_nbPD_0,avg_nbPD_5,avg_nbPD_10,avg_nbPD_15,avg_nbPD_20 = avg_nbPD()

    svm_final_avg_PD = round((avg_svmPD_0+avg_svmPD_5+avg_svmPD_10+avg_svmPD_15+avg_svmPD_20)/5,2)
    dt_final_avg_PD = round((avg_dtPD_0+avg_dtPD_5+avg_dtPD_10+avg_dtPD_15+avg_dtPD_20)/5,2)
    lr_final_avg_PD = round((avg_lrPD_0+avg_lrPD_5+avg_lrPD_10+avg_lrPD_15+avg_lrPD_20)/5,2)
    rf_final_avg_PD = round((avg_rfPD_0+avg_rfPD_5+avg_rfPD_10+avg_rfPD_15+avg_rfPD_20)/5,2)
    nb_final_avg_PD = round((avg_nbPD_0+avg_nbPD_5+avg_nbPD_10+avg_nbPD_15+avg_nbPD_20)/5,2)

    svmP_list = svmP.objects.order_by('-svmP_date')
    dtP_list=dtP.objects.order_by('-dtP_date')
    lrP_list=lrP.objects.order_by('-lrP_date')
    rfP_list=rfP.objects.order_by('-rfP_date')
    nbP_list=nbP.objects.order_by('-nbP_date')
    def avg_smvP():
        sum_svmP_0 = 0
        count_svmP_0 = 0
        sum_svmP_5 = 0
        count_svmP_5 = 0
        sum_svmP_10 = 0
        count_svmP_10 = 0
        sum_svmP_15 = 0
        count_svmP_15 = 0
        sum_svmP_20 = 0
        count_svmP_20 = 0
        for var in svmP_list:
            sum_svmP_0+=var.svmP_fold_0
            sum_svmP_5+=var.svmP_fold_5
            sum_svmP_10+=var.svmP_fold_10
            sum_svmP_15+=var.svmP_fold_15
            sum_svmP_20+=var.svmP_fold_20
            count_svmP_0+=1
            count_svmP_5+=1
            count_svmP_10+=1
            count_svmP_15+=1
            count_svmP_20+=1
        return (round(sum_svmP_0/count_svmP_0,2),round(sum_svmP_5/count_svmP_5,2),round(sum_svmP_10/count_svmP_10,2),round(sum_svmP_15/count_svmP_15,2),round(sum_svmP_20/count_svmP_20,2))
    avg_svmP_0,avg_svmP_5,avg_svmP_10,avg_svmP_15,avg_svmP_20 = avg_smvP()

    def avg_dtP():
        sum_dtP_0=0
        count_dtP_0=0
        sum_dtP_5=0
        count_dtP_5=0
        sum_dtP_10=0
        count_dtP_10=0
        sum_dtP_15=0
        count_dtP_15=0
        sum_dtP_20=0
        count_dtP_20=0
        for var in dtP_list:
            sum_dtP_0+=var.dtP_fold_0
            sum_dtP_5+=var.dtP_fold_5
            sum_dtP_10+=var.dtP_fold_10
            sum_dtP_15+=var.dtP_fold_15
            sum_dtP_20+=var.dtP_fold_20
            count_dtP_0+=1
            count_dtP_5+=1
            count_dtP_10+=1
            count_dtP_15+=1
            count_dtP_20+=1
        return(round(sum_dtP_0/count_dtP_0,2),round(sum_dtP_5/count_dtP_5,2),round(sum_dtP_10/count_dtP_10,2),round(sum_dtP_15/count_dtP_15,2),round(sum_dtP_20/count_dtP_20,2))
    avg_dtP_0,avg_dtP_5,avg_dtP_10,avg_dtP_15,avg_dtP_20 = avg_dtP()

    def avg_lrP():
        sum_lrP_0=0
        count_lrP_0=0
        sum_lrP_5=0
        count_lrP_5=0
        sum_lrP_10=0
        count_lrP_10=0
        sum_lrP_15=0
        count_lrP_15=0
        sum_lrP_20=0
        count_lrP_20=0
        for var in lrP_list:
            sum_lrP_0+=var.lrP_fold_0
            sum_lrP_5+=var.lrP_fold_5
            sum_lrP_10+=var.lrP_fold_10
            sum_lrP_15+=var.lrP_fold_15
            sum_lrP_20+=var.lrP_fold_20
            count_lrP_0+=1
            count_lrP_5+=1
            count_lrP_10+=1
            count_lrP_15+=1
            count_lrP_20+=1
        return(round(sum_lrP_0/count_lrP_0,2),round(sum_lrP_5/count_lrP_5,2),round(sum_lrP_10/count_lrP_10,2),round(sum_lrP_15/count_lrP_15,2),round(sum_lrP_20/count_lrP_20,2))
    avg_lrP_0,avg_lrP_5,avg_lrP_10,avg_lrP_15,avg_lrP_20 = avg_lrP()

    def avg_rfP():
        sum_rfP_0=0
        count_rfP_0=0
        sum_rfP_5=0
        count_rfP_5=0
        sum_rfP_10=0
        count_rfP_10=0
        sum_rfP_15=0
        count_rfP_15=0
        sum_rfP_20=0
        count_rfP_20=0
        for var in rfP_list:
            sum_rfP_0+=var.rfP_fold_0
            sum_rfP_5+=var.rfP_fold_5
            sum_rfP_10+=var.rfP_fold_10
            sum_rfP_15+=var.rfP_fold_15
            sum_rfP_20+=var.rfP_fold_20
            count_rfP_0+=1
            count_rfP_5+=1
            count_rfP_10+=1
            count_rfP_15+=1
            count_rfP_20+=1
        return(round(sum_rfP_0/count_rfP_0,2),round(sum_rfP_5/count_rfP_5,2),round(sum_rfP_10/count_rfP_10,2),round(sum_rfP_15/count_rfP_15,2),round(sum_rfP_20/count_rfP_20,2))
    avg_rfP_0,avg_rfP_5,avg_rfP_10,avg_rfP_15,avg_rfP_20 = avg_rfP()

    def avg_nbP():
        sum_nbP_0=0
        count_nbP_0=0
        sum_nbP_5=0
        count_nbP_5=0
        sum_nbP_10=0
        count_nbP_10=0
        sum_nbP_15=0
        count_nbP_15=0
        sum_nbP_20=0
        count_nbP_20=0
        for var in nbP_list:
            sum_nbP_0+=var.nbP_fold_0
            sum_nbP_5+=var.nbP_fold_5
            sum_nbP_10+=var.nbP_fold_10
            sum_nbP_15+=var.nbP_fold_15
            sum_nbP_20+=var.nbP_fold_20
            count_nbP_0+=1
            count_nbP_5+=1
            count_nbP_10+=1
            count_nbP_15+=1
            count_nbP_20+=1
        return(round(sum_nbP_0/count_nbP_0,2),round(sum_nbP_5/count_nbP_5,2),round(sum_nbP_10/count_nbP_10,2),round(sum_nbP_15/count_nbP_15,2),round(sum_nbP_20/count_nbP_20,2))
    avg_nbP_0,avg_nbP_5,avg_nbP_10,avg_nbP_15,avg_nbP_20 = avg_nbP()

    svm_final_avg = round((avg_svmP_0+avg_svmP_5+avg_svmP_10+avg_svmP_15+avg_svmP_20)/5,2)
    dt_final_avg = round((avg_dtP_0+avg_dtP_5+avg_dtP_10+avg_dtP_15+avg_dtP_20)/5,2)
    lr_final_avg = round((avg_lrP_0+avg_lrP_5+avg_lrP_10+avg_lrP_15+avg_lrP_20)/5,2)
    rf_final_avg = round((avg_rfP_0+avg_rfP_5+avg_rfP_10+avg_rfP_15+avg_rfP_20)/5,2)
    nb_final_avg = round((avg_nbP_0+avg_nbP_5+avg_nbP_10+avg_nbP_15+avg_nbP_20)/5,2)

    return render(request,'cancer/admin_statistics.html', context={'svm_final_avg_PD':svm_final_avg_PD,'dt_final_avg_PD':dt_final_avg_PD,'lr_final_avg_PD':lr_final_avg_PD,'rf_final_avg_PD':rf_final_avg_PD,'nb_final_avg_PD':nb_final_avg_PD,
                                                                    'svm_final_avg_BD':svm_final_avg_BD,'dt_final_avg_BD':dt_final_avg_BD,'lr_final_avg_BD':lr_final_avg_BD,'rf_final_avg_BD':rf_final_avg_BD,'nb_final_avg_BD':nb_final_avg_BD,
                                                                    'svm_final_avg_B':svm_final_avg_B,'dt_final_avg_B':dt_final_avg_B,'lr_final_avg_B':lr_final_avg_B,'rf_final_avg_B':rf_final_avg_B,'nb_final_avg_B':nb_final_avg_B,
                                                                    'svm_final_avg':svm_final_avg,'dt_final_avg':dt_final_avg,'lr_final_avg':lr_final_avg,'rf_final_avg':rf_final_avg,'nb_final_avg':nb_final_avg})
