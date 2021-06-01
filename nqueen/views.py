from django.shortcuts import redirect, render

# Create your views here.

# importing algorithm
from genetics.algorithm import main


def index(request):

    retVal = main(6,20)

    context = {
        'arr':retVal['solved_2d_array'],
        'numberQuenns': retVal['numberQueen'],
        'PopulationSize': retVal['populationSize'],
        'Generation': retVal['generation'],
    }
    print(context)
    return render(request,'indextemp.html', context)


def solution(request):
    n = int(request.POST.get('n'))
    p = int(request.POST.get('p'))

    retVal = main(n, p)

    context = {
         'arr':retVal['solved_2d_array']
     }
    return render(request,'index.html', context)

# def index(request):
#     # creating dummy array
#     retVal = main(9,4)

#     context = {
#         'arr':retVal['solved_2d_array']
#     }
#     return render(request,'index.html', context)
