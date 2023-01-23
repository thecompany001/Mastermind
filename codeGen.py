import requests

def getRandomCode(num, min, max, col, base, format, rnd):
    url = 'https://www.random.org/integers/?num=' + str(num) + '&min=' + str(min) + '&max=' + str(
        max) + '&col=' + str(col) + '&base=' + str(base) + '&format=' + format + '&rnd=' + rnd
    response = requests.get(url)

    randCode = response.text

    # remove 'u' from the list output of randCode
    randCode = str(randCode)

    randomNumbers = randCode.split()

    return randomNumbers


def getUniqueCode(num, min, max, col, base, format, rnd):
    # remove duplication
    numbers = getRandomCode(num, min, max, col, base, format, rnd)

    while (len(numbers) != len(set(numbers))):
        numbers = getRandomCode(num, min, max, col, base, format, rnd)
    return numbers