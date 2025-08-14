# Nested Dictionary Example
# Ask for number of robots

robots = {}
number_of_robots = int(input("Enter number of robots: "))

for i in range(number_of_robots):
    # Get robot name
    robot_name = input(f"Enter name of robot {i + 1}: ")
    robot_weight = float(input(f"Enter weight of robot {i + 1} (in kg): "))

    robot_parts = []
    number_of_parts = int(input(f"Enter number of parts for {robot_name}: "))
    for j in range(number_of_parts):
        part_name = input(f"Enter name of part {j + 1} ")
        robot_parts.append(part_name)
    # Store robot data in the dictionary
    robots[robot_name] = {
        'weight': robot_weight,
        'parts': robot_parts
    }
# Display all robot data
for name, info in robots.items():
    print(f"Robot Name: {name}")
    print(f"  Weight: {info['weight']} kg")
    print(f"  Parts: {', '.join(info['parts'])}")