# This function calculate the vertical motion of a ball thrown up in the air
# -*- coding: utf-8 -*-
print("Let's get calculate\nThe vertical motion of a ball thrown up in the air")
def ball(v0, g, t, y):
    return v0 * t - 0,5 * g * t**2

print("What is your language preference.")
print("English")
print("Turkish")

while True:

    choice = input("Enter choice(EN/TR): ")

    if choice in ('EN', 'TR'):

        if choice == 'EN':
            v0 = float(input("Initial Velocity (m/s): "))
            g = 9.80665
            t = float(input("Time (s): "))
            y = v0 * t - 0.5 * g * t**2
            print("At t=%g s, the height of the ball is %.2f m." % (t, y))
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break
            
            else:
                print("Invalid Input")

        elif choice == 'TR':
            v0 = float(input("Başlangıç Hızı (m/s): "))
            g = 9.80665
            t = float(input("Zaman (s): "))
            y = v0 * t - 0.5 * g * t**2
            print("%g saniyede topun yüksekliği %.2f metredir." %(t,y))
            next_calculation = input("Yeni bir hesaplama yapmak ister misin? (Evet/Hayır): ")
            if next_calculation == "Hayır":
              break
            
            else:
                print("Invalid Input")