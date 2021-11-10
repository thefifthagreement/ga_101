import random

# answer is imported from the answer.pyc
# it gives you the lenght of the anwser
# and the mean score of a population 
from answer import answer_len, is_answer, get_mean_score

def create_chromosome(chrom_size):
    # Create a chromosome as a string of the right size
    return " " * chrom_size

def selection(population):
    # select the best individuals
    return population[:2]

def crossover(parent1, parent2):
    # select half of the parent genetic material
    return parent1

def mutation(chrom):
    # random gene mutation
    return chrom

def create_population(pop_size, chrom_size):
    # create the base population
    return [create_chromosome(chrom_size) for _ in range(pop_size)]

def generation(population):
    # create a new generation
    
    # selection
    select = selection(population)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    
    # constant size of population
    while len(children) < len(population) - len(select):
        ## crossover
        parents = random.sample(select, k=2) # randomly selected
        child = crossover(parents[0], parents[1])
        
        ## mutation
        child = mutation(child)
        children.append(child)
    
    # return the new generation
    return select + children

def algorithm():
    chrom_size = answer_len()
    population_size = 20
    max_iter = 100
    iteration = 0
    max_score = 0.0

    # create the base population
    population = create_population(population_size, chrom_size)
    
    answers = []
    
    # while a solution has not been found :
    while not answers and iteration < max_iter:
        iteration += 1

        # create the next generation using the generation(population) function
        population = generation(population)
        
        # display the average score of the population
        score = get_mean_score(population)
        max_score = max(max_score, score)

        if iteration % 50 == 0:
            print(f'generation {iteration}: {score:.2%}')
    
        # check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
    
    # print the solution
    if answers:
        print(f"Well done the answer was found at iteration {iteration}:\n{answers[0]}")
    else:
        print(f"No solution found... (best score {max_score:.2%})")


if __name__ == "__main__":
    algorithm()
    
