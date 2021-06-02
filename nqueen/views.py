from django.shortcuts import redirect, render

# Create your views here.

# importing algorithm
from genetics.algorithm import main, population

import numpy

# altered for the time being

generationTrack = []
totalGenerations = 0
generationCounter = 0
numberQueens = 0
populationSize = 0
gotoParent = False
retVal = {}


def index(request):
    return render(request, 'inputForm.html')

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


def solution(request):
    


    global generationTrack, numberQueens, populationSize, totalGenerations
    global retVal, gotoParent
    print("generationCounter" , generationCounter)
    if(not gotoParent):
        n = int(request.GET.get('n'))
        p = int(request.GET.get('p'))
        print(n,p)
        gotoParent = False
        retVal = main(n,p)

    generationTrack = retVal['generationTrack']
    numberQueens = retVal['numberQueen']
    populationSize = retVal['populationSize']
    totalGenerations = retVal['generation']



    context = {
        'arr': retVal['solved_2d_array'],
        'numberQuenns': retVal['numberQueen'],
        'PopulationSize': retVal['populationSize'],
        'Generation': retVal['generation'],
    }
    # print(context)
    return render(request, 'index.html', context)


def showParent(request):
    global generationTrack
    global generationCounter, numberQueens, populationSize, totalGenerations

    generationCounter = generationCounter + 1
    currentGeneration = totalGenerations - generationCounter

    arr1 = numpy.zeros((numberQueens, numberQueens))

    print(arr1)

    solvedQueens = generationTrack[currentGeneration-1][0]
    # print(solvedQueens)
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1

    arr2 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1]
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1


    context = {
        'arr1': arr1,
        'arr2': arr2,
        'numberQuenns': numberQueens,
        'PopulationSize': populationSize,
        'currentGeneration': currentGeneration,
    }

    # print(context)

    return render(request, "showParents.html", context)


def showChild(request):

    global generationTrack,gotoParent
    global generationCounter, numberQueens, populationSize, totalGenerations

    

    generationCounter = generationCounter - 1
    currentGeneration = totalGenerations - generationCounter
    
    print("currentGeneration : ",currentGeneration)
    print("generationCounter" , generationCounter)
    if(generationCounter <= 1):
        generationCounter = 0   #he 0 ki 1 bghava lagel
        gotoParent = True
        return solution(request)


    arr1 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][0]
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1

    arr2 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1]
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1

    print(generationCounter, numberQueens,
            populationSize, totalGenerations)
    print(generationTrack)
    context = {
        'arr1': arr1,
        'arr2': arr2,
        'numberQuenns': numberQueens,
        'PopulationSize': populationSize,
        'currentGeneration': currentGeneration,
    }

    # print(context)

    return render(request, "showParents.html", context)