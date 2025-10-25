def CalculateInsuranceDiscount(DriverAge, HadAccident, YearsLicenceHeld):
    if DriverAge >= 25:
        if HadAccident:
            return 0
        else:
            return 5
    elif HadAccident:
        if YearsLicenceHeld < 3:
            return -10
        else:
            return 0
    else:
        if YearsLicenceHeld < 3:
            return 0
        else:
            return 5
DriverAge = 23 #INTEGER
HadAccident = True #BOOLEAN
YearsLicenceHeld = 2 #INTEGER
print("The discount on your insurance is", CalculateInsuranceDiscount(DriverAge, HadAccident, YearsLicenceHeld))