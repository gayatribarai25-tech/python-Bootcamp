'''Create a contacts.csv with Name and Phone columns and at least 5 rows. Read it back with DictReader and print only contacts whose name starts with a letter of your choice.'''


import csv
with open("contacts.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Phone"])
    writer.writerow(["Amit", "12345"])
    writer.writerow(["Priya", "23456"])
    writer.writerow(["Anjali", "34567"])
    writer.writerow(["Rahul", "45678"])
    writer.writerow(["Arjun", "56789"])

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].startswith("A"):
            print(row)
