from django.shortcuts import render

def home(request):
   context = {}

   test = 'hello world'
   context['test'] = test
   return render(request, 'app/home.html', context)
