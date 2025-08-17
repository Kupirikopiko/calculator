import math

history = []  # records previous answers
while True:
    if (history):
        print(f"Answer history: {history}")
    while True:
        response = int(input("What shape would you want to calculate today?"
                             "\n1-Square"
                             "\n2-Rectangle"
                             "\n3-Triangle"
                             "\n4-Circle"
                             "\n:"))
        if 1 > response or response >= 5:
            print("Please choose a valid number.")
        else:
            break
    match response:
        case 1:
            print("You chose Square!")
            side = int(input("Provide the value for the side: "))
            squareArea = side ** 2
            print(f"The area of the square is: {squareArea}")
            history.append(squareArea)
        case 2:
            print("You chose Rectangle!")
            length = float(input("Provide the value for the length: "))
            width = float(input("Provide the value for the width: "))
            rectangleArea = length * width
            print(f"The area of the rectangle is: {rectangleArea}")
            history.append(rectangleArea)
        case 3:
            print("You chose Triangle!")
            height = float(input("Provide the value for the height: "))
            base = float(input("Provide the value for the base: "))
            triangleArea = (height * base) / 2
            print(f"The area of the triangle: {triangleArea}")
            history.append(triangleArea)
        case 4:
            print("You chose Circle!")
            radius = float(input("Provide the value for the radius: "))
            circleArea = (math.pi * radius) ** 2
            print(f"The area of the circle is: {circleArea}")
            history.append(circleArea)

    loop = input("Do you want to calculate again?"
                 "\nYes or No\n:")
    if loop.strip().lower() in ["No", "N", "n", "no", "NO"]:
        print("Got it! Going back...")
        break
    else:
        print("Goodbye!")
        print(f"Answer history: {history}")
