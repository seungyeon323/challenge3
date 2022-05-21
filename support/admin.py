from django.contrib import admin

from .models import Faq, Inquiry, Answer
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title','content','category')
    
    search_fields= ('title',)
    list_filter = ('category',)
    

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display =('category','title','created_at','created_by',)
    
    search_fields =('title','email','phone',)
    
    list_filter =('category',) 

    inlines = [AnswerInline,]

#@admin.register(Answer)
#class AnswerModelAdmin(admin.ModelAdmin):
#    pass