import math

# figuring out angle between these two vectors
# (0,1,0) (sin(a)cos(b), cos(a)cos(b)), sin(b)) point found with trig on the vector of the new position
# does not account for how much the device has to rotate, as long as both numbers are equal and within 90 it will be 45 degrees
def angle_calculator(a, b):
    a = math.radians(a)
    b = math.radians(b)

    c1 = [0,1,0]
    c2 = [1,0,0]
    
    top = (c1[0] * math.sin(a) * math.cos(b)) + (math.cos(a) * math.cos(b) * c1[1]) + (c1[2] * math.sin(b))
    bot = math.sqrt(c1[0] ** 2 + c1[1] ** 2 + c1[2] ** 2) * (math.sqrt((math.sin(a) * math.cos(b)) ** 2 + (math.cos(a) * math.cos(b)) **2 + (math.sin(b))** 2))
    ans = math.acos(top / bot)

    top2 = (c2[0] * math.sin(a) * math.cos(b)) + (math.cos(a) * math.cos(b) * c2[1] * 0) + (c2[2] * math.sin(b))
    bot2 = math.sqrt(c2[0] ** 2 + c2[1] ** 2 + c2[2] ** 2) * (math.sqrt((math.sin(a) * math.cos(b)) ** 2 + (math.cos(a) * math.cos(b)) **2 * 0 + (math.sin(b))** 2))
    ans2 = math.acos(top2 / bot2)

    return [math.degrees(ans2), math.degrees(ans)]



while True:
    a = int(input('What is the degrees of first rotation (rotating to the right)? '))
    b = int(input('What is the degrees of second rotation? (rotating forward) '))

    ans = angle_calculator(a,b)
    print(f'rotate the device {ans[0]} degrees to the left, the angle it down {ans[1]} degrees.')
    user_input = input()

    if user_input == 'b':
        break