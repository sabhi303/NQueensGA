from django.shortcuts import redirect, render

# Create your views here.

# importing algorithm
from genetics.algorithm import main

# altered for the time being

def solution(request):
    return render(request,'inputForm.html')

# def index(request):
#     # n = int(request.GET.get('n'))
#     # p = int(request.GET.get('p'))
#     retVal = main(8,4)

#     context = {
#         'arr':retVal['solved_2d_array'],
#         'numberQuenns': retVal['numberQueen'],
#         'PopulationSize': retVal['populationSize'],
#         'Generation': retVal['generation'],
#     }
#     # print(context)
#     return render(request,'index.html', context)


def index(request):
    retVal = main(8,4)

    context = {
        'arr':retVal['solved_2d_array'],
        'numberQuenns': retVal['numberQueen'],
        'PopulationSize': retVal['populationSize'],
        'Generation': retVal['generation'],
    }
    # print(context)
    return render(request,'showParents.html',context)
















# def solution(request):
#     n = int(request.POST.get('n'))
#     p = int(request.POST.get('p'))

#     retVal = main(n, p)

#     context = {
#          'arr':retVal['solved_2d_array']
#      }
#     return render(request,'index.html', context)

# # def index(request):
# #     # creating dummy array
# #     retVal = main(9,4)

# #     context = {
# #         'arr':retVal['solved_2d_array']
# #     }
# #     return render(request,'index.html', context)
