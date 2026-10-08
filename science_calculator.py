print("SCIENCE CALCULATOR")
print("1. Ohm's Law")
print("2. Kinetic Energy")
print("3. Speed")
print("4. Weight")

choice = int(input("Enter your choice: "))

if choice == 1:
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (ohm): "))
    print("Voltage =", I * R, "V")

elif choice == 2:
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    print("Kinetic Energy =", 0.5 * m * v * v, "J")

elif choice == 3:
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    print("Speed =", distance / time, "m/s")

elif choice == 4:
    m = float(input("Enter mass (kg): "))
    g = 9.8
    print("Weight =", m * g, "N")

else:
    print("Invalid choice")
