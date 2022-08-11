from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Master, Info, Gallery, Application, Price, Work, Review, FAQ

# class MasterAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Master
#         fields = '__all__'
#
# class MasterAdmin(admin.ModelAdmin):
#     form = MasterAdminForm


admin.site.register(Master)
admin.site.register(Info)
admin.site.register(Gallery)
admin.site.register(Application)
admin.site.register(Price)
admin.site.register(Work)
admin.site.register(Review)
admin.site.register(FAQ)
# Register your models here.
