# This is a lbs to kg conveter app
pouns = float(input("Please enter the mass in lb that you would like to convert to kg: "))
kg = 2.20462 
new_mass = pouns / kg
print("The converted mass in kg is:",pouns / kg)
earth = new_mass * 9.807
print("Your weight on Earth is:",earth, "Newtons")
moon = new_mass * 1.62
print("Your weight on the Moon is:",moon, "Newtons")
per_moon_earth = moon / earth * 100  #the percentage of the weight on the moon in comparison to what is experience on earth
print("The percentage of the weight on the Moon in comparison to what is experience on Earth:",per_moon_earth, "%")
print("The percentage of the weight on the Moon in comparison to what is experience on Earth as an integer is",round(per_moon_earth), "%")

