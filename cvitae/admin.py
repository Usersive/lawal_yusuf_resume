from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, LeadershipRole, Portfolio, ProfileUpdate, PersonalDetail, Skill, Hobbies
from .models import Education, Experience, SocialLink, Professional_member, Project
from django.utils.html import format_html

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links=('email', 'first_name', 'last_name')
    readonly_fields=('last_login', 'date_joined')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
    
class HorenAdminArea(admin.AdminSite):
    site_header = 'CV Amdin Area'
    
blog_site = HorenAdminArea(name='HorenAdmin')




class ProfileUpdateAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40"  style="border-radius:50%;">'.format(object.image.url))
    thumbnail.short_description = 'Profile Image'
    list_display = ['thumbnail', 'first_name', 'middle_name', 'last_name', 'email',]
    list_display_links=('thumbnail', 'first_name', 'middle_name',)


class PersonalDetailAdmin(admin.ModelAdmin):
    list_display=('date_of_birth', 'phone_number', 'gender', 'marital_status', 'state', 'natinality')
    list_display_links=('date_of_birth', 'phone_number', 'gender')
    

class SkillAdmin(admin.ModelAdmin):
    list_display=('skill', 'skill_percent',)
    list_display_links=('skill', 'skill_percent',)

class EducationAdmin(admin.ModelAdmin):
    list_display=('education', 'education_year',)
    list_display_links=('education', 'education_year',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display=('experience', 'experience_year',)
    list_display_links=('experience', 'experience_year',)
    
class HobbiesAdmin(admin.ModelAdmin):
    list_display=('hobbies',)
    list_display_links=('hobbies',)

class LeadershipRoleAdmin(admin.ModelAdmin):
    list_display=('title','department',)
    list_display_links=('title','department',)

class Professional_memberAdmin(admin.ModelAdmin):
    list_display=('title','degree_certificate',)
    list_display_links=('title','degree_certificate',)

class ProjectAdmin(admin.ModelAdmin):
    list_display=('program_name','project_title',)
    list_display_links=('program_name','project_title',)


class PortfolioAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40"  style="border-radius:50%;">'.format(object.image.url))
    thumbnail.short_description = 'Portfolio Image'
    list_display = ['thumbnail', 'title', 'description', ]
    list_display_links=('thumbnail', 'title', 'description',)



admin.site.register(SocialLink)

admin.site.register(Account, AccountAdmin)
admin.site.register(ProfileUpdate, ProfileUpdateAdmin)
admin.site.register(PersonalDetail, PersonalDetailAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Hobbies, HobbiesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(LeadershipRole, LeadershipRoleAdmin)
admin.site.register(Professional_member, Professional_memberAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
