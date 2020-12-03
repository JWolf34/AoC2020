import numpy

# Part 1
def numTreesHit(forest, hslope, vslope):
    row = 0
    col = 0
    maxrows = len(forest) - 1
    maxcols = len(forest[0]) - 1
    tree = "#"
    square = "."
    numTreesHit = 0

    
    while row <= maxrows:
        if forest[row][col] == tree:
            numTreesHit += 1
        row += vslope
        col += hslope
        # loop columns back around
        if col >= maxcols:
            col -= maxcols

    return numTreesHit

#Part 2
def numTreesHitPerSlope(forest):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    sumNumTreesHit = []

    for slope in slopes:
        hslope = slope[0]
        vslope = slope[1]
        sumNumTreesHit.append(numTreesHit(forest, hslope, vslope))
    
    return sumNumTreesHit


#Part 2 (cont)
def multiplyInList(lst):
    result = 1
    for i in lst:
        result *= i
    return result


    


def createForest():
    f = open("input.txt", "r")
    forest = f.readlines()

    return forest

def printForest(forest):
    for row in forest:
        print(row)


if __name__ == "__main__":
    forest = createForest()
    #printForest(forest)
    #print(numTreesHit(forest, 3, 1))
    sumNumTreesHit = numTreesHitPerSlope(forest)
    print(multiplyInList(sumNumTreesHit))
