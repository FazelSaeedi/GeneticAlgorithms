import random
import datetime

# Solving of guessPassword





# Generate a Guess
def generateParent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes) , len(geneSet))           # generate SampleSize
        genes.extend(random.sample(geneSet , sampleSize))              # select as many random genes as SampleSize
    return ''.join(genes)                                              # return a String



# Fitness
def get_fitness(guess):
    return sum(1 for expected , actual in zip(target , guess)          # check which character is selected correctly
               if expected == actual)                                  # return 1 if two character are equal and then return number of all equals
                                                                       # e.g : if target = "ABCD" and guess is "ABD" get_fitness return 3 because A=A , B=B , D=D

# Mutate

def mutate(parent):
    index = random.randrange(0 , len(parent))                          # select random index from parent
    childGenes = list(parent)                                          # convert cildString to List
    newGene , alternate = random.sample(geneSet , 2 )                  # select 2 sample from geneSet
                                                                       # if selected random index != selected first sample from geneSet
                                                                       #   replace newGene otherwise replace alternate gene
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)


# Display

def display(guess):
    timeD = datetime.datetime.now() - startTime                       # calculate time of each iteration
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess , fitness , str(timeD)))       # illustrate information of each iteration


# Genes

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXUZ!."
target  = "My Password!"

# Main

random.seed()
startTime = datetime.datetime.now()
bestParent = generateParent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)



while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child