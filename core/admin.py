from django.contrib import admin

from core.models import Course, Lesson

admin.site.site_header = 'Custom Admin Panel'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','status','combine') # neyi  display etmek isteyirikse
    list_display_links = ('title','author')  # ustune tikladiqda edite gedir
    list_filter = ('title',)  # filterlemekdir
    search_fields = ('title',) # title__startwith => o demekdirki yazilan nedirse ancaq onu axtar

    # list_editable = ('price','status')  # daxile girmeden editlemek olur
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
    list_display = ('title','course')
    list_filter = ('course',)
    # autocomplete_fields = ('course',)
    raw_id_fields = ('course',)
    ordering= ('-title',)
    list_per_page =4 
    # pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
