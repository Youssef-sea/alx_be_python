# pattern_drawing.py

while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

row_count = 0
while row_count < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row_count += 1