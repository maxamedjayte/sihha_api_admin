from django.contrib import admin
from api.models import *
# Register your models he.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('fullName','theImage','socialSituation','number','age','sex')
    # ordering: 
    search_fields=('fullName','number','socialSituation','sex','status')

@admin.register(ProbQuestion)
class ProbQuestionAdmin(admin.ModelAdmin):
    list_display=('probQuestionCategory','nuucaSuaasha','som','arb','eng')
    # ordering: 
    search_fields=('probQuestionCategory','nuucaSuaasha','som','arb','eng')
admin.site.register(ProbAnswer)

@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display=('theUser','theProductInfo','quantity','orderTime','status','userTaked')
    # ordering: 
    ordering = ['-status']
    search_fields=('fullName','theProductInfo__name','orderTime','status')

admin.site.register(ProductCategory)
admin.site.register(SendNotification)
admin.site.register(AppointmentCategory)
@admin.register(DoctorAppointment)
class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display=('theUser','doctorAssignedDated','theCategory','appointmentMeetingLink','sessionEnded')
    # ordering: 
    search_fields=('theUser','appointmentMeetingLink','theCategory','doctorAssignedDated','sessionEnded')


@admin.register(PatientResult)
class PatientResultAdmin(admin.ModelAdmin):
    list_display=('theUser','resultTitle','resultDate')
    # ordering: 
    search_fields=('theUser','resultTitle','resultDate')





admin.site.register(ChildProbAnswer)
admin.site.register(ShikhCategory)
admin.site.register(UserProductsRoutine)
@admin.register(AdkarWithTalo)
class AdkarWithTaloAdmin(admin.ModelAdmin):
    list_display=('name','readingCount','created')
    # ordering: 
    search_fields=('name','readingCount','created')
@admin.register(ListeningCilajWithQuran)
class ListeningCilajWithQuranAdmin(admin.ModelAdmin):
    list_display=('name','theShikh','text')
    # ordering: 
    search_fields=('name','theShikh','text')
admin.site.register(RoutineTime)

@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display=('name','theImage','isRoutine','category','price','dateRegistred')
    # ordering: 
    search_fields=('name','isRoutine','category','price','dateRegistred')

@admin.register(WaafiMarchentConfig)
class WaafiMarchentConfigAdmin(admin.ModelAdmin):
    list_display=('merchantUid','apiUserId','apiKey')
    # ordering: 



admin.site.register(UserAnswerInformation)
admin.site.register(ProbQuestionCategory)
admin.site.register(AppInformation)
admin.site.register(SubscriptionFeatures)
admin.site.register(ProductsInTheBug)
admin.site.register(UserChildAdkarWithProduct)
