#import soil
from soil import sample
#print(dir(soil))
'''
def sample():
    import random
    return random.uniform(10, 100)
'''
def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        print(f"Moisture is {moisture}%")

    print("Time to water!")
main()