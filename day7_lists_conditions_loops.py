distances = [20, 80, 50, 5, 123]

for d in distances:
    if d > 50:
        print(f"Distance {d} -> path clear.")
    elif d > 20:
        print(f"Distance {d} -> proceed with caution.")
    else:
        print(f"Distance {d} -> stop. obstacle ahead.")