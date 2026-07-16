# Source - https://stackoverflow.com/a/30795432
# Posted by Raniz
# Retrieved 2026-07-15, License - CC BY-SA 3.0

import math, random

def get_random_point(radius):
    while True:
        # Generate the random point
        x = random.randint(-radius, radius)
        y = random.randint(-radius, radius)
        # Check that it is inside the circle
        if math.sqrt(x ** 2 + y ** 2) < radius:
            # Return it
            return (x, y)
