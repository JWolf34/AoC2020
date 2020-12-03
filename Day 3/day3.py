
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
