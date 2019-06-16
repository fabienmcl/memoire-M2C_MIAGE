import csv
import random
import math
import operator
import numpy

movieSet = []
userSet = []


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
        return (dataset)

def generateMovieType(data):
    type = set([])
    for x in range(len(data)-1) : 
        type.add(data[x][len(data[x])-1])
        #print(data[x][len(data[x])-1])
    print(type)

def generateHashSimple(data):
    hash = {}
    for x in range(len(data)-1):
        hash[data[x][0]] = data[x][len(data[x])-1]
    print(hash)

def generateUserAlea(data):
    hashUser = {}
    #print(data)
    i = 0
    while i != 5 :
        userMovieRating = [random.randint(0,5) for _ in range(len(data)-1)]
        name = 'user'+str(i)
        hashUser[name] = userMovieRating
        i+=1
    #print(hashUser)

def generateUserPerfect():
    print("creating a perfect user list : ")
    
    fabien = [0, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
    print('Fabien (user on which we will apply the recommendation) : ',fabien)
    #comdie+ dernier SF
    mathieu = [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,1]
    print('Mathieu (Comedie+Jurassic World) : ',mathieu)
    #SF
    marjolaine = [0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,4]
    print('Marjolaine (SF):',marjolaine)
    #SF -1
    croc = [0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1]
    print('Crocmou (SF-1):',croc)
    return [fabien,croc,mathieu,marjolaine,]

def getTypeRating(data,typeSelect):
    occurrence = 0
    total = 0
    for x in range(len(data)):
        if getMovieType(x) == typeSelect and data[x] != 0 : 
            occurrence+=1
            total+=data[x]
    return total/occurrence if occurrence!=0 else None




def euclideanDistance(instance1, instance2):
    distance = 0
    length = len(instance1)-1
    for x in range(length):
        if instance1[x] != 0 or instance2[x] != 0:
            #distance += euclidean_distances(instance1[x],instance2[x])
            distance +=numpy.linalg.norm(instance1[x] - instance2[x])
	return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    #length = len(testInstance)-1
    for x in range(len(trainingSet)):
        if numpy.array_equal(testInstance, trainingSet[x]) == False: 
            dist = euclideanDistance(testInstance, trainingSet[x])
            distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    #k for max accpet
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors




def predictions(dataSet):
    #print(dataSet)
    #pour chaque ligne
    #get les plus proche voisin
    neighborsSort = getNeighbors(dataSet,dataSet[0],3)
    #print(neighborsSort)
    #print(movieSet)
    userPredict = []
    #for z in range(len(dataSet[0])):
    y = len(dataSet[0])-1
    #print(dataSet[0][y])
    #print(movieSet[y])
    for y in range(len(dataSet[0])):
        if dataSet[0][y] == 0 : 
            userPredict.append(generatePredictions(neighborsSort,y,getTypeRating(dataSet[0],getMovieType(y)),dataSet[0]))
        else: 
            userPredict.append(dataSet[0][y])
    '''  
    if dataSet[0][y] == 0 : 
        print("if 0")
            #pour chaque film non vu
            #print(getMovieType(y))
            #print(getTypeRating(dataSet[0],getMovieType(y)))
        userPredict.append(generatePredictions(neighborsSort,y,getTypeRating(dataSet[0],getMovieType(y)),dataSet[0]))
    else: 
        userPredict.append(dataSet[0][y])
    '''
    return printPredict(dataSet[0],userPredict)
    


def printPredict(before,after):
    print('Predict for Fabien')
    print("- - - - - - - - - - - - - - - - - - -")       
    print(after)
    for x in range(len(before)):
        if before[x] != after[x]:
            print('new rating : ',after[x],' for ',movieSet[x])
    print("- - - - - - - - - - - - - - - - - - -")


def applyDelta(a, b):
    #determiner si qui est a ou b 
    if a == b : 
        return 1
    else : 
        a = float(a/5)
        b = float(b/5)
        if a > b : 
            a+=1
            b+=1
        return sum([a,b])/len([a,b])
def averageRatingGlobal(userSelect):
    occurrence = 0
    total = 0
    for x in range(len(userSelect)-1):
        total+=userSelect[x]
        occurrence+=1
    return total/occurrence


def generateRating(a,b):
    delta = applyDelta(a,b)
    print ('x')

def cleanNeighbors(neighbors, position):
    result = []
    for x in range(len(neighbors)):
        if neighbors[x][position] != 0 : 
            result.append(neighbors[x])
    return result

def getMovieType(position): 
    return movieSet[position][3]

def distance(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result
def sortNeighbors(userSelect,typeRating,neighbors,position):
    distances = []
    
    #print(typeRating)
    for x in range(len(neighbors)):
        neighborTypeRating = getTypeRating(neighbors[x],getMovieType(position))
        #print(neighborTypeRating)
        if neighborTypeRating != None : 
            dist = distance(typeRating,neighborTypeRating)
            #print ('distabce')
            #print(dist)
            distances.append((neighbors[x], dist))

    distances.sort(key=operator.itemgetter(1))
    #print(distances)
    neighbors = []
    for x in range(len(distances)):
        neighbors.append(distances[x][0])
    return neighbors
  
  
    '''
    print("je suppose que tout les voisins sont extremement proche")
    print("donc d'une valeur egale")
    print("il faut trier la liste selon leur appetence envers le type et celui de l'utilisateur")
    print ("sort by type rating")
    return neighbors
'''
def generatePredictions(neighbors, position,typeRating,userSelect):
    # 1 - virer ceux qu'
    #print("generate predict")
    neighbors = cleanNeighbors(neighbors,position)
    #print(neighbors)
    neighbors = sortNeighbors(userSelect,typeRating,neighbors,position)
    #print(getMovieType(position))
    #print(len(neighbors[0]))
    #print(neighbors)
    #print(movieSet[position])

    default = 0
    for x in range(len(neighbors)-1):
        neighborTypeRating = getTypeRating(neighbors[x],getMovieType(position))
        if neighborTypeRating != None and typeRating != None and neighbors[x][position]!=0 :
            #print('if')
            #averaage rating type 
            #delta
            delta = applyDelta(neighborTypeRating,typeRating)
            #rating x delta
            return neighbors[x][position]*delta
        elif neighborTypeRating != None and typeRating == None and neighbors[x][position]!=0: 
            #print('elif')
            #averaage rating global 
            userSelectAVG = averageRatingGlobal(userSelect)
            neighborSelectAVG = averageRatingGlobal(neighbors[x])
            #delta
            delta = applyDelta(neighborSelectAVG,userSelectAVG)
            #rating x delta
            return neighbors[x][position]*delta
    #print('default choice')
    return default
    #print('x')

def printHelloWorld():
    print('##################################################')
    print('#                                                #')
    print('#               Recommender system               #')
    print('#                                                #')
    print('#                 Fabien MICHEL                  #')
    print('#                                                #')
    print('#               M2C MIAGE 2018-2019              #')
    print('#                                                #')
    print('##################################################')
def main():
    printHelloWorld()
    trainingSet=[]
    testSet=[]
    split = 0.67
    global movieSet
    movieSet = loadDataset('movie.txt', split, trainingSet, testSet)
    #print '\n'.join([str(x) for x in movieSet])
    #generateMovieType(movieSet
    #generateHashSimple(movieSet)
    
    
    #generateUserAlea(movieSet)
    print("- - - - - - - - - - - - - - - - - - -")
    userList = generateUserPerfect()
    print("- - - - - - - - - - - - - - - - - - -")
    predictions(userList)


main()
