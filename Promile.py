print("""Let's get calculate
Your Alcohol Volume""")

#The Formula of detect consumed alcohol in gram
def grA(Vol, AC, c):
    return Vol * AC * c * 10

#Widmark formula - Blood Alcohol Content
##male
def BACm(grA, W, cm, t):
    return (grA / (W * 1000 * cm)) * 100 - (t * 0.015)
##female
def BACf(grA, W, cf, t):
    return (grA / (W * 1000 * cf)) * 100 - (t * 0.015)

print("What is your Gender?")

while True:

    gender = input("(m/f): ")
    
    if gender in ('m', 'f'):

        if gender == 'm':
            W = float(input("What is your Weight (kg): "))
            cm = 0.68
            t = float(input("How long have you been drinking? (H): "))
            Vol = float(input("How many liters of alcohol did you consume? (L): "))
            AC = float(input("What percentage of alcohol did you consume? (%): "))
            c = 0.789
            BACm = ((Vol * AC * c * 10) / (W * 1000 * cm)) * 100 - (t * 0.015)
            print("Your Approximate Blood Alcohol Content is %.3f in percentage." % (BACm))
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break
            
            else:
                print("What is your Gender?")
                
        elif gender == 'f':
            W = float(input("What is your Weight (kg): "))
            cf = 0.55
            t = float(input("How long have you been drinking? (H): "))
            Vol = float(input("How many liters of alcohol did you consume? (L): "))
            AC = float(input("What percentage of alcohol do you consume? (%): "))
            c = 0.789
            BACf = ((Vol * AC * c * 10) / (W * 1000 * cf)) * 100 - (t * 0.015)
            print("Your Approximate Blood Alcohol Content is %.3f in percentage." % (BACf))
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break
            
            else:
                print("What is your Gender?")