distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    #for name in distances.keys():
    #    print(f"{name} is {distances[name]} Km from Earth")
    for distance in distances.values():
        print(f"{distance} km is {convert(distance)} m")

def convert(km):
    return km * 1000

main()