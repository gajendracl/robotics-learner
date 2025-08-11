def battery_status(battery):
     #Check battery level and return status message.
    if battery > 75:
        return "Battery is full. Ready for heavy tasks!"
    elif battery > 40:
        return "Battery okay. Proceed with caution."
    elif battery > 15:
        return "Battery low. Please recharge soon."
    else:
        return "Battery critically low. Entering sleep mode."

def countdown(start):
    # Countdown from a given number to zero.
    while start > 0:
        print(f"T-minus {start}")
        start -= 1
    print("Mission Started!")

print("🤖 Robot Status Checker")

# Ask for battery percentage
battery = int(input("Enter battery percentage (0-100): "))
print(battery_status(battery))

# Ask for countdown start
countdown_start = int(input("Enter countdown start number: "))
countdown(countdown_start)