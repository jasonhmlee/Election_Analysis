print("Hello World")

type(3)
type('a')
ballots = 1,341
ballots
type(73.81)

counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
counties.insert(2,"El Paso"
counties.pop(3)
counties[2] = "Jefferson
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
counties_tuple[:2]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict.keys()

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for i in len(counties):
    print(counties[i])

