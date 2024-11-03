import math

x, y = 0, 0
movement = [("UP", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)]

for dir, steps in movement:
    if dir == "UP":
        y += steps
    elif dir == "DOWN":
        y -= steps
    elif dir == "LEFT":
        x += steps
    elif dir == "RIGHT":
        x -= steps

#calculate distance from origin
distance = math.sqrt(x**2 + y**2)

print(f"Distance from origin {distance}")