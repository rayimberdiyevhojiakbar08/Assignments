count = int(input("Enter the number of rice bags: "))

def classify(counts):
    total = 0
    below = 0
    inrange = 0
    above = 0
    for i in range(counts):
        weights = int(input("Enter the rice bag weight: "))
        total += weights
        if weights < 498:
            below += 1
            print("Below in range")
        elif weights >= 498 and weights <= 502:
            inrange += 1
            print("In range")
        else:
            above += 1
            print("Above in range")

    print("Below range ", below)
    print("In range ", inrange)
    print("Above range ", above)
    return total

total = classify(count)

def calculate_average(count,total):
    print("Average weight: ", total/count)


calculate_average(count,total)