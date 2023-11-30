from zxcvbn import zxcvbn

strength = {
    3: 'Strong',
    4: 'Very Srong'
}


def checkStrength(password):
    result = zxcvbn(password)
    score = result['score']
    scoreStrength = "Strength: " + strength[score]
    return score, scoreStrength


if __name__ == "__main__":
    checkStrength('sAJSHDgfj')
