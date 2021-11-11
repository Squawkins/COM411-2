import csv

def load_data(fpath):
    print("Loading Data! ")
    with open(fpath) as file:
        loaded = csv.reader(file)
        headings = next(loaded)

        for i in loaded:
            records.append(i)

    print("Done! ")

def display_menu():
    print("Please select one of the following options:\n[1] Display the names of all passengers\n[2] Display the number of passengers that survived\n[3] Display the number of passengers per gender\n[4] Display the number of passengers per age group\n[5] Display the number of survivors per age group\n")
    response = int(input())
    return response

def display_passenger_names():
    print("The names of the passengers are: ")
    for i in records:
        name = i[3]
        print(name)

def display_num_survivors():
    survived = 0

    for i in records:
        survival = int(i[1])
        if survival == 1:
            survived += 1
    print(f"{survived} passengers survived")

def display_passengers_per_gender():
    female = 0
    male = 0

    for i in records:
        gender = i[4]
        if gender.lower() == "male":
            male += 1
        else:
            female += 1

    print(f"male: {male}, female: {female}")

def display_passengers_per_age_group():
    child = 0
    adult = 0
    elderly = 0

    for i in records:
        if i[5] != "":
            age = float(i[5])
            if age < 18:
                child = child + 1
            elif age < 65:
                adult = adult + 1
            else:
                elderly = elderly + 1

    print(f"children: {child}, adults: {adult}, elderly: {elderly}")


def display_survivors_per_age_group():
    child = 0
    adult = 0
    elderly = 0
    child_survivor = 0
    adult_survivor = 0
    elderly_survivor = 0

    for i in records:
        survived = int(i[1])
        if i[5] != "":
            age = float(i[5])
            if age < 18:
                child += 1
                if survived == 1:
                    child_survivor += 1
            elif age < 65:
                adult += 1
                if survived == 1:
                    adult_survivor += 1
            else:
                elderly += 1
                if survived == 1:
                    elderly_survivor += 1

    print(
        f"children: {child_survivor}/{child}, adults: {adult_survivor}/{adult}, elderly: {elderly_survivor}/{elderly}")

def run():
  load_data("titanic.csv")
  recordcount = len(records)
  print(f"Successfully loaded {recordcount} records ")

  choice = display_menu()
  print(f"You have selected option: {choice} ")

  if choice == 1:
    display_passenger_names()
  elif choice == 2:
    display_num_survivors()
  elif choice == 3:
    display_passengers_per_gender()
  elif choice == 4:
    display_passengers_per_age_group()
  elif choice == 5:
    display_survivors_per_age_group()
  else:
    print("Invalid Option! ")

records = []
headings = []

if __name__ == "main":
    run()
