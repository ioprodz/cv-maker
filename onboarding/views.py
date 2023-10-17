from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserInfo, JobInfo, Skills
from formtools.wizard.views import SessionWizardView

class ContactWizard(SessionWizardView):
   form_list = [UserInfo, JobInfo, Skills]
   template_name = 'onboarding/index.html'
   
   def done(self, form_list, **kwargs):
      user_info   = form_list[0].save()
      job_info    = form_list[1].save()
      skills      = form_list[2].save()
      
      return HttpResponse('Form Submitted !')
        
def home(request):
   context = {}

   return render(request, 'app/home.html', context)