from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import register

#importing algorithm
from genetics.algorithm import main

@register.filter
def get_range(value):
    return range(value)

def index(request):
    # creating dummy array
    retVal = main(9,4)

    context = {
        'arr':retVal['solved_2d_array']
    }
    return render(request,'index.html', context)


