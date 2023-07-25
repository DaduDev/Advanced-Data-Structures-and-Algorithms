import random

# Example of a reliability objective function (can be customized for your specific problem)
def reliability_function(components):
    # Simulated reliability function for demonstration purposes
    return sum(components) / len(components)

# Genetic Algorithm function to optimize the reliability design problem
def genetic_algorithm_reliability_design(num_components, population_size, generations, mutation_rate):
    # Generate an initial population randomly
    population = [[random.randint(0, 1) for _ in range(num_components)] for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate the fitness of each individual in the population
        fitness = [reliability_function(individual) for individual in population]

        # Select parents for the next generation using tournament selection
        parents = []
        for _ in range(population_size // 2):
            candidate1, candidate2 = random.choices(population, weights=fitness, k=2)
            parents.append(candidate1 if fitness[population.index(candidate1)] > fitness[population.index(candidate2)] else candidate2)

        # Crossover - apply uniform crossover to create new offspring
        offspring = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1]
            child1 = [parent1[j] if random.random() < 0.5 else parent2[j] for j in range(num_components)]
            child2 = [parent2[j] if random.random() < 0.5 else parent1[j] for j in range(num_components)]
            offspring.extend([child1, child2])

        # Mutation - apply mutation to the offspring
        for individual in offspring:
            for i in range(num_components):
                if random.random() < mutation_rate:
                    individual[i] = 1 - individual[i]

        # Replace the old population with the new offspring
        population = offspring

    # Select the best individual as the final solution
    best_individual = max(population, key=lambda x: reliability_function(x))
    return best_individual, reliability_function(best_individual)

# Example usage
num_components = 10
population_size = 100
generations = 100
mutation_rate = 0.1

best_solution, best_reliability = genetic_algorithm_reliability_design(num_components, population_size, generations, mutation_rate)
print("Best Configuration:", best_solution)
print("Best Reliability:", best_reliability)
