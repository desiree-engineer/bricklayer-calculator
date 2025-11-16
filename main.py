print("WELCOME TO THE BRICKLAYER CALCULATOR")
print("AVAILABLE CALCULATIONS:"
    "\n1 - Area Calculation"
    "\n2 - Volume Calculation"
    "\n3 - Brick Quantity Calculation"
    "\n4 - Slope Calculation"
    "\n5 - Centimeters to Meters Conversion"
    "\n6 - Meters to Centimeters Conversion"
    "\n7 - Square Meters to Square Centimeters Conversion"
    "\n8 - Square Centimeters to Square Meters Conversion\n"
)

selecao = int(input("Enter the code of the calculation you want to perform: "))

if selecao == 1:
    width = float(input("Enter the width in meters: "))
    length = float(input("Enter the length in meters: "))
    area = width * length
    print("Starting area calculation...")
    print(f"The area is: {area} m²")

elif selecao == 2:
    length = float(input("Enter the length in meters: "))
    width = float(input("Enter the width in meters: "))
    height = float(input("Enter the height in meters: "))
    volume = length * width * height
    print("Starting volume calculation...")
    print(f"The volume is: {volume} m³")

elif selecao == 3:
    brick_quantity = int(input("Enter the quantity of bricks (considering 30x30 bricks): "))
    area = float(input("Enter the area value: "))
    total_bricks = int(area / 0.09)
    total_bricks_with_loss = int(total_bricks * 1.10)
    print("Starting brick quantity calculation...")
    print(f"Total bricks without loss: {total_bricks}")
    print(f"Total bricks with 10% loss: {total_bricks_with_loss}")

elif selecao == 4:
    height_difference = float(input("Enter the height difference in centimeters: "))
    length = float(input("Enter the length in meters: "))
    slope = (height_difference / (length * 100)) * 100
    print("Starting slope calculation...")
    print(f"The slope is: {slope}%")

elif selecao == 5:
    centimeters = float(input("Enter the value in centimeters: "))
    
    meters = centimeters / 100
    print("Starting centimeter-to-meter conversion...")
    print(f"{centimeters} cm is equal to {meters} m")

elif selecao == 6:
    meters = float(input("Enter the value in meters: "))
    
    centimeters = meters * 100
    print("Starting meter-to-centimeter conversion...")
    print(f"{meters} m is equal to {centimeters} cm")

elif selecao == 7:
    m2 = float(input("Enter the value in square meters: "))
    
    cm2 = m2 * 10000
    print("Starting m² to cm² conversion...")
    print(f"{m2} m² is equal to {cm2} cm²")

elif selecao == 8:
    cm2 = float(input("Enter the value in square centimeters: "))
    
    m2 = cm2 / 10000
    print("Starting cm² to m² conversion...")
    print(f"{cm2} cm² is equal to {m2} m²")

else:
    print("Invalid option. Try again.")
