from django.db import models

# Create your models here.

class svmP(models.Model):
    svmP_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmP_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmP_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmP_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmP_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmP_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.svmP_fold_0)
        return str(self.svmP_fold_5)
        return str(self.svmP_fold_10)
        return str(self.svmP_fold_15)
        return str(self.svmP_fold_20)
        return str(self.svmP_date)

class svmB(models.Model):
    svmB_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmB_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmB_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmB_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmB_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmB_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.svmB_fold_0)
        return str(self.svmB_fold_5)
        return str(self.svmB_fold_10)
        return str(self.svmB_fold_15)
        return str(self.svmB_fold_20)
        return str(self.svmB_date)

class dtP(models.Model):
    dtP_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtP_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtP_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtP_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtP_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtP_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.dtP_fold_0)
        return str(self.dtP_fold_5)
        return str(self.dtP_fold_10)
        return str(self.dtP_fold_15)
        return str(self.dtP_fold_20)
        return str(self.dtP_date)

class dtB(models.Model):
    dtB_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtB_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtB_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtB_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtB_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtB_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.dtB_fold_0)
        return str(self.dtB_fold_5)
        return str(self.dtB_fold_10)
        return str(self.dtB_fold_15)
        return str(self.dtB_fold_20)
        return str(self.dtB_date)

class lrP(models.Model):
    lrP_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrP_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrP_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrP_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrP_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrP_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.lrP_fold_0)
        return str(self.lrP_fold_5)
        return str(self.lrP_fold_10)
        return str(self.lrP_fold_15)
        return str(self.lrP_fold_20)
        return str(self.lrP_date)

class lrB(models.Model):
    lrB_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrB_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrB_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrB_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrB_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrB_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.lrB_fold_0)
        return str(self.lrB_fold_5)
        return str(self.lrB_fold_10)
        return str(self.lrB_fold_15)
        return str(self.lrB_fold_20)
        return str(self.lrB_date)

class rfP(models.Model):
    rfP_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfP_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfP_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfP_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfP_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfP_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.rfP_fold_0)
        return str(self.rfP_fold_5)
        return str(self.rfP_fold_10)
        return str(self.rfP_fold_15)
        return str(self.rfP_fold_20)
        return str(self.rfP_date)

class rfB(models.Model):
    rfB_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfB_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfB_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfB_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfB_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfB_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.rfB_fold_0)
        return str(self.rfB_fold_5)
        return str(self.rfB_fold_10)
        return str(self.rfB_fold_15)
        return str(self.rfB_fold_20)
        return str(self.rfB_date)

class nbP(models.Model):
    nbP_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbP_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbP_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbP_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbP_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbP_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.nbP_fold_0)
        return str(self.nbP_fold_5)
        return str(self.nbP_fold_10)
        return str(self.nbP_fold_15)
        return str(self.nbP_fold_20)
        return str(self.nbP_date)

class nbB(models.Model):
    nbB_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbB_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbB_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbB_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbB_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbB_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.nbB_fold_0)
        return str(self.nbB_fold_5)
        return str(self.nbB_fold_10)
        return str(self.nbB_fold_15)
        return str(self.nbB_fold_20)
        return str(self.nbB_date)


class nbB_D(models.Model):
    nbBD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbBD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbBD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbBD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbBD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbBD_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.nbBD_fold_0)
        return str(self.nbBD_fold_5)
        return str(self.nbBD_fold_10)
        return str(self.nbBD_fold_15)
        return str(self.nbBD_fold_20)
        return str(self.nbBD_date)

class svmB_D(models.Model):
    svmBD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmBD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmBD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmBD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmBD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmBD_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.svmBD_fold_0)
        return str(self.svmBD_fold_5)
        return str(self.svmBD_fold_10)
        return str(self.svmBD_fold_15)
        return str(self.svmBD_fold_20)
        return str(self.svmBD_date)

class dtB_D(models.Model):
    dtBD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtBD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtBD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtBD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtBD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtBD_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.dtBD_fold_0)
        return str(self.dtBD_fold_5)
        return str(self.dtBD_fold_10)
        return str(self.dtBD_fold_15)
        return str(self.dtBD_fold_20)
        return str(self.dtBD_date)

class rfB_D(models.Model):
    rfBD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfBD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfBD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfBD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfBD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfBD_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.rfBD_fold_0)
        return str(self.rfBD_fold_5)
        return str(self.rfBD_fold_10)
        return str(self.rfBD_fold_15)
        return str(self.rfBD_fold_20)
        return str(self.rfBD_date)


class lrB_D(models.Model):
    lrBD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrBD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrBD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrBD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrBD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrBD_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.lrBD_fold_0)
        return str(self.lrBD_fold_5)
        return str(self.lrBD_fold_10)
        return str(self.lrBD_fold_15)
        return str(self.lrBD_fold_20)
        return str(self.lrBD_date)


class nbP_D(models.Model):
    nbPD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbPD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbPD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbPD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbPD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    nbPD_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.nbPD_fold_0)
        return str(self.nbPD_fold_5)
        return str(self.nbPD_fold_10)
        return str(self.nbPD_fold_15)
        return str(self.nbPD_fold_20)
        return str(self.nbPD_date)

class svmP_D(models.Model):
    svmPD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmPD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmPD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmPD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmPD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    svmPD_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.svmPD_fold_0)
        return str(self.svmPD_fold_5)
        return str(self.svmPD_fold_10)
        return str(self.svmPD_fold_15)
        return str(self.svmPD_fold_20)
        return str(self.svmPD_date)

class dtP_D(models.Model):
    dtPD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtPD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtPD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtPD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtPD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    dtPD_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.dtPD_fold_0)
        return str(self.dtPD_fold_5)
        return str(self.dtPD_fold_10)
        return str(self.dtPD_fold_15)
        return str(self.dtPD_fold_20)
        return str(self.dtPD_date)

class rfP_D(models.Model):
    rfPD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfPD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfPD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfPD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfPD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    rfPD_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.rfPD_fold_0)
        return str(self.rfPD_fold_5)
        return str(self.rfPD_fold_10)
        return str(self.rfPD_fold_15)
        return str(self.rfPD_fold_20)
        return str(self.rfPD_date)


class lrP_D(models.Model):
    lrPD_fold_0 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrPD_fold_5 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrPD_fold_10 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrPD_fold_15 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrPD_fold_20 = models.DecimalField(blank=True,null=True,max_digits=5,decimal_places=2)
    lrPD_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.lrPD_fold_0)
        return str(self.lrPD_fold_5)
        return str(self.lrPD_fold_10)
        return str(self.lrPD_fold_15)
        return str(self.lrPD_fold_20)
        return str(self.lrPD_date)



class patient(models.Model):
    test_type = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    blood_grp = models.CharField(max_length=4)
    parents_name = models.CharField(max_length=30,null=True,blank=True)
    spouse_name = models.CharField(max_length=30,null=True,blank=True)
    result = models.CharField(max_length=15)
    def __str__(self):
        return str(self.test_type)
        return str(self.first_name)
        return str(self.last_name)
        return str(self.dob)
        return str(self.gender)
        return str(self.blood_grp)
        return str(self.parents_name)
        return str(self.spouse_name)
        return str(self.result)
