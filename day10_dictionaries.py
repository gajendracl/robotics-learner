# Ask for number of robots
num_of_robots = int(input("Enter number of robots: "))

# Dictionary to store all robot data
robots = {}

# Collect robot data
for i in range(num_of_robots):
    name = input(f"\nEnter name of robot {i+1}: ")
    
    # Create a dictionary for this robot's details
    robot_info = {}
    num_parts = int(input(f"Enter number of parts for {name}: "))
    
    for p in range(num_parts):
        part_name = input(f"Enter name of part {p+1}: ")
        part_status = input(f"Enter status of {part_name}: ")
        robot_info[part_name] = part_status
    
    # Store robot's info in main robots dictionary
    robots[name] = robot_info

# Show all robot data
print("\n--- Robot Diagnostics ---")
for robot_name, info in robots.items():
    print(f"\n{robot_name} Details:")
    for part, status in info.items():
        print(f"  {part} → {status}")

# Search feature
while True:
    search_robot = input("\nEnter a robot name to check (or 'exit' to quit): ")
    if search_robot.lower() == 'exit':
        break
    
    if search_robot in robots:
        search_part = input(f"Enter the part to check for {search_robot}: ")
        if search_part in robots[search_robot]:
            print(f"{search_robot}'s {search_part} Status: {robots[search_robot][search_part]}")
        else:
            print(f"{search_robot} does not have a part named '{search_part}'.")
    else:
        print("Robot not found!")
