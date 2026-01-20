from django.contrib import admin

from core.models import Course, Lesson

admin.site.site_header = 'Custom Admin Panel'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','status','combine') # neyi  display etmek isteyirikse
    list_display_links = ('title','author')  # ustune tikladiqda edite gedir
    # exclude = ('title',)  # fields-in tersidi
    # fields = ('title','author',('price','status'),) # neyi formda istifade etmek isteyirikse (()) qruplasdirmaqdir
    # fieldsets = (
    #     (None,{
    #         'fields':('title','description','author',)
    #     }),
    #     ('Extra Info',{
    #         'classes':('collapse','wide',),
    #         'fields' : ('price','status',)
    #     }))
    # fieldsetle bezi goruntu olaraq duzelisleri ede bilirik


    @admin.display(description='New name')  # short_description ile eyni isi gorur
    def combine(self,obj):
        return f"{obj.title} - {obj.price}"   # elave column yarada bilir
    
    combine.short_description = "Complete Name"  # admin paneldeki adlandirilmasidi


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
