
from django.contrib import admin
from  .models import Author, Book, Course, Student

# Register your models here.
admin.site.register(Author)

admin.site.register(Course)



class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','numpages','in_stock')
admin.site.register(Book,BookAdmin)

#class StudentAdmin(admin.ModelAdmin):
 #   list_display = ('studentdetails','course_no','title','textbook')
#admin.register(Course,CourseAdmin)""
