from django.contrib import admin
from cancer_app.models import svmP
from cancer_app.models import dtP
from cancer_app.models import lrP
from cancer_app.models import rfP
from cancer_app.models import nbP
from cancer_app.models import svmB
from cancer_app.models import dtB
from cancer_app.models import lrB
from cancer_app.models import rfB
from cancer_app.models import nbB
from cancer_app.models import svmP_D
from cancer_app.models import dtP_D
from cancer_app.models import lrP_D
from cancer_app.models import rfP_D
from cancer_app.models import nbP_D
from cancer_app.models import svmB_D
from cancer_app.models import dtB_D
from cancer_app.models import lrB_D
from cancer_app.models import rfB_D
from cancer_app.models import nbB_D
from cancer_app.models import patient



# Register your models here.

admin.site.register(svmP)
admin.site.register(dtP)
admin.site.register(lrP)
admin.site.register(nbP)
admin.site.register(rfP)
admin.site.register(svmP_D)
admin.site.register(dtP_D)
admin.site.register(lrP_D)
admin.site.register(nbP_D)
admin.site.register(rfP_D)
admin.site.register(svmB)
admin.site.register(dtB)
admin.site.register(lrB)
admin.site.register(nbB)
admin.site.register(rfB)
admin.site.register(svmB_D)
admin.site.register(dtB_D)
admin.site.register(lrB_D)
admin.site.register(nbB_D)
admin.site.register(rfB_D)
admin.site.register(patient)
