# robot_data = {
#     "motor" : "In Good Condition",
#     "sensor" : "Needs Maintenance",
#     "battery" : "Needs Replacement"
# }

# for part, status in robot_data.items():
#     print(f"Part: {part}, Status: {status}")


# Ask for number of robots
num_of_robots = int(input("Enter the number of robots: "))

# Create a dictionary to store robot data for each robot
robots = {}

for i in range(num_of_robots):

    name = input(f"Enter the name of robot {i + 1}: ")

    robot_info = {}
    robot_info["motor"] = input(f"Enter the status of motor for robot {i + 1}: ")
    robot_info["sensor"] = input(f"Enter the status of sensor for robot {i + 1}: ")
    robot_info["battery"] = input(f"Enter the status of battery for robot {i + 1}: ")
    robot_info["camera"] = input(f"Enter the status of camera for robot {i + 1}: ")

    robots[name] = robot_info

# display robot data
for name, info in robots.items():
    print(f"Robot Name: {name}")
    for part, status in info.items():
        print(f"  Part: {part}, Status: {status}")
