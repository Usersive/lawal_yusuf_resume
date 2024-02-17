from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from cvitae.models import Education, Hobbies, LeadershipRole, PersonalDetail, Portfolio, Professional_member, ProfileUpdate, Project, Skill, SocialLink
# Create your views here.


def email_compose(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
        full_name,
        message,
        settings.EMAIL_HOST_USER,
        [email])
        
        
        messages.success(request, "Message sent successfully!")
        return redirect('email_compose')
    
    return render(request, 'cvitae/email_compose.html')


def profile(request):
    edit_profile = ProfileUpdate.objects.all()
    context ={
        'edit_profile': edit_profile,
        
    }
    return render(request, 'cvitae/profile.html', context)

def skillupdate(request):
    skill = Skill.objects.all()
    context ={
        'skill': skill,
    }
    return render(request, 'cvitae/skill.html', context)

def hobbies(request):
    hobby = Hobbies.objects.all()
    context ={
        'hobby':hobby,
    }
    return render(request, 'cvitae/hobby.html', context)

def personal_details(request):
    details = PersonalDetail.objects.all()
    context ={
        'details':details,
    }
    return render(request, 'cvitae/hobby.html', context)

def education(request):
    edu_details = Education.objects.all()
    context ={
        'edu_details':edu_details,
    }
    return render(request, 'cvitae/edu_detail.html', context)

def experience(request):
    exp_details = Education.objects.all()
    context ={
        'exp_details':exp_details,
    }
    return render(request, 'cvitae/exp_detail.html', context)

def social(request):
    social_links = SocialLink.objects.all()
    context ={
        'social_links': social_links,
    }
    return render(request, 'cvitae/social.html', context)

def leader(request):
    leadership = LeadershipRole.objects.all()
    context ={
        'leadership':leadership,
    }
    return render(request, 'cvitae/leader.html', context)

def professional(request):
    prof_member = Professional_member.objects.all()
    context ={
        'prof_member':prof_member,
    }
    return render(request, 'cvitae/leader.html', context)

def portfolio(request):
    portfolio_detail = Portfolio.objects.all()
    context ={
        'portfolio_detail':portfolio_detail,
    }
    return render(request, 'cvitae/portfolio.html', context)


def project(request):
    project_detail = Project.objects.all()
    context ={
        'project_detail':project_detail,
    }
    return render(request, 'cvitae/project.html', context)