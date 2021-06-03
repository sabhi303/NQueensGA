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
p=''


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
    global retVal, gotoParent, p
    print(gotoParent)
    print("generationCounter" , generationCounter)
    if(not gotoParent):
        
        n = int(request.GET.get('n'))
        p = request.GET.get('p')
        print(n,p.split(','))
        retVal = main(n,p.split(','))
    else:
        gotoParent = False
    print(gotoParent)

    generationTrack = retVal['generationTrack']
    numberQueens = retVal['numberQueen']
    populationSize = retVal['populationSize']
    totalGenerations = retVal['generation']
    mid=0
    if(numberQueens%2==0):
        mid=numberQueens/2
    else:
        mid=(numberQueens//2)+1

    context1 = {
        'mid':mid,
        'solvedQueens' : retVal['solvedQueens'],
        'arr': retVal['solved_2d_array'],
        'numberQuenns': retVal['numberQueen'],
        'PopulationSize': retVal['populationSize'],
        'Generation': retVal['generation'],
        'p' : p
    }
    # print(context)
    return render(request, 'index.html', context1)


def showParent(request):
    global generationTrack
    global generationCounter, numberQueens, populationSize, totalGenerations
    # if(totalGenerations-generationCounter<=1):
    #     alert='t'
    # else:
    #     generationCounter = generationCounter + 1
    # currentGeneration = totalGenerations - generationCounter
    currentGeneration=int(request.GET.get('gen'))
    print(currentGeneration)
    if(currentGeneration>1):
        currentGeneration-=1

    arr1 = numpy.zeros((numberQueens, numberQueens))

    print(arr1)

    solvedQueens = generationTrack[currentGeneration-1][0]
    # print(solvedQueens)
    bd={}
    fd={}
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1

        add=ielem+solvedQueens[ielem]
        sub=ielem-solvedQueens[ielem]
        if(add in fd):
            arr1[ielem][solvedQueens[ielem] - 1] = 2
            arr1[fd[add]][solvedQueens[fd[add]] - 1] = 2
        else:
            fd[add]=ielem
        if(sub in bd):
            arr1[ielem][solvedQueens[ielem] - 1] = 2
            arr1[bd[sub]][solvedQueens[bd[sub]] - 1] = 2
        else:
            bd[sub]=ielem

    
    arr2 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1]
    bd={}
    fd={}
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1

        add=ielem+solvedQueens[ielem]
        sub=ielem-solvedQueens[ielem]
        if(add in fd):
            arr2[ielem][solvedQueens[ielem] - 1] = 2
            arr2[fd[add]][solvedQueens[fd[add]] - 1] = 2
        else:
            fd[add]=ielem
        if(sub in bd):
            arr2[ielem][solvedQueens[ielem] - 1] = 2
            arr2[bd[sub]][solvedQueens[bd[sub]] - 1] = 2
        else:
            bd[sub]=ielem


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

    

    # generationCounter = generationCounter - 1
    # currentGeneration = totalGenerations - generationCounter
    currentGeneration=int(request.GET.get('gen'))
    # print("currentGeneration : ",currentGeneration)
    # print("generationCounter" , generationCounter)
    # if(generationCounter < 1):
    #     generationCounter = 0   #he 0 ki 1 bghava lagel
    #     gotoParent = True
    #     return solution(request)
    if(currentGeneration>=totalGenerations-1):
        gotoParent = True
        return solution(request)
    else:
        currentGeneration+=1

    arr1 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][0]
    bd={}
    fd={}
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1

        add=ielem+solvedQueens[ielem]
        sub=ielem-solvedQueens[ielem]
        if(add in fd):
            arr1[ielem][solvedQueens[ielem] - 1] = 2
            arr1[fd[add]][solvedQueens[fd[add]] - 1] = 2
        else:
            fd[add]=ielem
        if(sub in bd):
            arr1[ielem][solvedQueens[ielem] - 1] = 2
            arr1[bd[sub]][solvedQueens[bd[sub]] - 1] = 2
        else:
            bd[sub]=ielem

    arr2 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1]
    bd={}
    fd={}
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1

        add=ielem+solvedQueens[ielem]
        sub=ielem-solvedQueens[ielem]
        if(add in fd):
            arr2[ielem][solvedQueens[ielem] - 1] = 2
            arr2[fd[add]][solvedQueens[fd[add]] - 1] = 2
        else:
            fd[add]=ielem
        if(sub in bd):
            arr2[ielem][solvedQueens[ielem] - 1] = 2
            arr2[bd[sub]][solvedQueens[bd[sub]] - 1] = 2
        else:
            bd[sub]=ielem

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