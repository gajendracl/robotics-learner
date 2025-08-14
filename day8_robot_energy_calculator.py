def energy_calculator(weight, distance):
    # energy calculation
    energy = weight * distance * 0.5
    return energy

# Number of robots
no_of_robots = int(input("Enter the number of robots: "))

robots_energy = []
for i in range(no_of_robots):
    weight = float(input(f"Enter weight for robot {i+1}: "))
    distance = float(input(f"Enter distance for robot {i+1}: "))
    robots_energy.append(energy_calculator(weight, distance))

for index, energy in enumerate(robots_energy):
    print(f"Energy for robot {index+1}: {energy}")
