from django.shortcuts import render
from datetime import datetime

from cvitae.models import Education, Experience, Hobbies, LeadershipRole, PersonalDetail, Professional_member, ProfileUpdate,  Skill, SocialLink



def index(request):
    edit_profile = ProfileUpdate.objects.all()
    skill = Skill.objects.all()
    hobby = Hobbies.objects.all()
    details = PersonalDetail.objects.all()
    edu_detail = Education.objects.all()
    exp_detail = Experience.objects.all()
    social_links = SocialLink.objects.all()
    leaders = LeadershipRole.objects.all()
    prof_member = Professional_member.objects.all()
   
    
    context ={
        'edit_profile': edit_profile,
        'skill': skill,
        'hobby': hobby,
        'details': details,
        'edu_detail': edu_detail,
        'exp_detail': exp_detail,
        'social_links': social_links,
        'leaders': leaders,
        'prof_member': prof_member,
      
    }
    return render (request, 'index.html', context)




def current_year(request):
    year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})