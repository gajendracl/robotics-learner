print("🤖 Robot Decision-Maker")

# Ask for battery percentage
battery = int(input("Enter battery percentage: "))

if battery > 75:
    print("Battery is full. Ready for heavy tasks!")
elif battery > 40:
    print("Battery okay. Proceed with caution.")
elif battery > 15:
    print("Battery low. Please recharge soon.")
else:
    print("Battery critically low. Abort mission.")

# Mission countdown
print("Starting mission countdown:")
for i in range(5, 0, -1):
    print(f"T-minus {i}")
print("Mission started!")
