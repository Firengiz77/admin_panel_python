from django.contrib import admin
from core.models import Classes, Course, Grade, Lesson, Person
from django.db.models import Avg
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django import forms

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

class PersonAdminForm(forms.ModelForm):
    class Meta:
        model =Person
        fields = "__all__"

        def clean_first_name(self):
            if self.cleaned_data['first_name'] == 'admin':
                raise forms.ValidationsError("No admin")
            return self.cleaned_data['first_name']



class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','show_average')
    list_display_links = ('last_name','first_name')
    ordering = ('-last_name','first_name')
    fields = ('first_name','last_name','classes')


    def get_form(self,request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['first_name'].label = "First Name (Human)"
        return form
    

    @admin.display(description='Average')
    def show_average(self, obj):
        result =  Grade.objects.filter(person = obj).aggregate(Avg('grade'))
        return result['grade__avg']
    
    

class ClassesAdmin(admin.ModelAdmin):
    list_display = ('name','year','view_student_link')
    list_filter = ('year',)

    def view_student_link(self,obj):
        count =  obj.person_set.count()  # burda ki person -> modelde column qeyd olunub o yeni person __set de elave edilib
        url = (
            reverse("admin:core_person_changelist")  # core folder name, person model name, changelist is which action we want to show
                    + "?"
                    + urlencode({"courses__id": f"{obj.id}"})
                    
        )
        return format_html("<a href='{}'>{} Students</a>",url, count)



class GradeAdmin(admin.ModelAdmin):
    pass



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Classes,ClassesAdmin)
admin.site.register(Grade,GradeAdmin)