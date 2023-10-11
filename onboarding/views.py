from django.shortcuts import render

def home(request):
   context = {}

   test = 'hello world'
   context['test'] = test
   return render(request, 'app/home.html', context)



def onboarding(request):
   return render(request, 'onboarding/index.html')



def onboardingStep(request, step):
   return render(request, f'onboarding/step{step}.html')
