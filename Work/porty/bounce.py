

def calculate_bounce(height):
    return round(height * 3/5, 4)

num_bounces = 10
i = 1
height = 60
while num_bounces >= i:
    print(i, height)
    height = calculate_bounce(height)
    i = i + 1
