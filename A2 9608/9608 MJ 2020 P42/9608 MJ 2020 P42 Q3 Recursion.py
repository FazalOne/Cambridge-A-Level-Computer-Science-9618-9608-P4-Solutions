def IsPalindrome(CheckWord):
    if len(CheckWord) <= 1:
        return True
    if CheckWord[0] != CheckWord[-1]:
        return False
    else:
        return IsPalindrome(CheckWord[1:-1])

def FindPower(Base, Exp):
    if Exp == 0:
        return 1
    else:
        Value = Base * FindPower(Base, Exp - 1)
        return Value