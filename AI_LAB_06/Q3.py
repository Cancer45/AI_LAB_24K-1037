import random
import math

def mathsFunc(x):
    return (x*x) + 2*x

def runGenetic(p_size, x_range, generations, mutation_rate):
    # initialize population
    population = random.sample(range(0, x_range), p_size)

    for generation in range(generations):
        # generate fitness scores
        fitness_scores = [mathsFunc(individual) for individual in population]
        # sort population according to fitness scores
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        # identify parents
        parents = sorted_population[:len(population)//2]
        # generate bin vals
        bit_size = math.ceil(math.log(x_range, 2))
        bins = [[int(b) for b in bin(p)[2:].zfill(bit_size)] for p in parents]
        # perform crossover
        point = random.randint(1, bit_size - 2)
        # breed & mutate
        new_population = [bins[0].copy()]
        for i in range(1, p_size):
            parent1, parent2 = random.sample(bins, 2)
            child = parent1[:point] + parent2[point:]

            if random.random() < mutation_rate:
                rand_val = random.randint(0, bit_size - 1)
                child[rand_val] = child[rand_val] ^ 1

            new_population.append(child)
        # bin to int
        population = [int("".join(map(str, b)), 2) for b in new_population] 

    best_x = population[0]
    best_fitness = mathsFunc(best_x)
    best_chromo = bin(best_x)[2:].zfill(bit_size)

    print(f"Best Chromosome: {best_chromo}")
    print(f"Best value of x: {best_x}")
    print(f"Best fitness value: {best_fitness}")

runGenetic(10, 32, 15, 0.1)
