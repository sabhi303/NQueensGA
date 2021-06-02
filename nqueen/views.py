from django.shortcuts import redirect, render

# Create your views here.

# importing algorithm
from genetics.algorithm import main, population

import numpy

# altered for the time being

generationTrack = []
totalGenerations = 0
generationCounter = 1
numberQueens = 0
populationSize = 0

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

    global generationTrack, numberQueens, populationSize,totalGenerations
    generationTrack = retVal['generationTrack']
    numberQueens = retVal['numberQueen']
    populationSize = retVal['populationSize']
    totalGenerations = retVal['generation'] 

    
    context = {
        'arr':retVal['solved_2d_array'],
        'numberQuenns': retVal['numberQueen'],
        'PopulationSize': retVal['populationSize'],
        'Generation': retVal['generation'],
    }
    # print(context)
    temp = showParent(request)
    return temp

def showParent(request):
    global generationTrack
    global generationCounter, numberQueens, populationSize, totalGenerations
    
    currentGeneration = totalGenerations - generationCounter
    generationCounter = generationCounter + 1 
    
    arr1 = numpy.zeros((numberQueens,numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][0] 
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1
    
    arr2 = numpy.zeros((numberQueens,numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1] 
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1
    

    print(generationCounter, numberQueens, populationSize, totalGenerations)
    print(generationTrack)
    context = {
        'arr1':arr1,
        'arr2':arr2,
        'numberQuenns': numberQueens,
        'PopulationSize': populationSize,
        'Generation': totalGenerations,
    }

    print(context)

    return render(request, "showParents.html", context)

















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
