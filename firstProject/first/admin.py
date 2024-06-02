from django.contrib import admin
from  .models import CarVariety, CarReview, Store, CarCertificate

# Register your models here.
class CarReviewInline(admin.TabularInline):
    model = CarReview
    extra = 2

class CarVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CarReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('car_varities',)

class CarCertificateAdmin(admin.ModelAdmin):
    list_display = ('car', 'certificate_number')

admin.site.register(CarVariety, CarVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(CarCertificate, CarCertificateAdmin)
