from django.shortcuts import render
from django.http import request
from django.http import JsonResponse
from .forms import StudentForm
import openai

# Create your views here.
def home(request):
    msg={}
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        input = request.POST['input']

        #GPT-3 Api
        openai.api_key = "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"
        responce = openai.Completion.create(
            engine = "davinci-instruct-beta",
            prompt = input,
            temperature = 0.1,
            max_tokens = 1000,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        content = responce.choices[0].text.split('.')
        msg = responce.choices[0].text
        print('res', msg)
        return render(request,'home.html',{'form':fm,'response':msg})
    else:
        fm = StudentForm() 
    return render(request,'home.html',{'form':fm})
