#Ask for No.of robots
num_of_robots = int(input("Enter the number of robots: "))
robot_names = []

# Get the names of the robots
for i in range(num_of_robots):
    name = input(f"Enter the name of robot {i + 1}: ")
    robot_names.append(name)

# Ask for the number of parts
number_of_parts = int(input("Enter the number of parts for each robot: "))
robot_parts = []

# Get the parts for each robot
for i in range(number_of_parts):
    part = input(f"Enter the name of part {i + 1} for each robot: ")
    robot_parts.append(part)

# check parts of each robot
for robo_name in robot_names:
    for part in robot_parts:
        print(f"checking {part} for {robo_name}...")
        
    
