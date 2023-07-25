def distance(city1, city2):
    # Calculate the Euclidean distance between two cities
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def nearest_neighbor_tsp(cities):
    num_cities = len(cities)
    unvisited_cities = set(range(1, num_cities))  # Excluding the starting city, which is 0
    current_city = 0
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    # Return to the starting city to complete the tour
    tour.append(0)

    return tour


# Example usage
cities = [(0, 0), (1, 2), (3, 3), (5, 1), (2, 5)]
tour = nearest_neighbor_tsp(cities)
print("Nearest Neighbor TSP Tour:", tour)
