
def numTreesHit(forest, hslope, vslope):
    row = 0
    col = 0
    maxrows = len(forest)
    maxcols = len(forest[0])
    tree = "#"
    square = "."
    numTreesHit = 0

    
    while row <= maxrows and col <= maxcols:
        if forest[row][col] == tree:
            numTreesHit += 1
        row += vslope
        col += hslope

    return numTreesHit

    


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

    print(numTreesHit(forest, 3, 1))
