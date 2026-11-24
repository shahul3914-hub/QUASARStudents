production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 250, 15, 50),
]

for batch in production:
    print(batch)

##
batch_id = int(input("Enter Batch ID: "))
name = input("Enter Product Name: ")
produced = int(input("Enter Units Produced: "))
defective = int(input("Enter Defective Units: "))
cost = int(input("Enter Cost per Unit: "))

new_batch = (batch_id, name, produced, defective, cost)
production.append(new_batch)

print("Batch added!")
for batch in production:
    print(batch)

##
def total_cost(production):
    total = 0
    for batch in production:
        units = batch[2]
        cost = batch[4]
        total = total + units * cost
    return total

print("Total manufacturing cost:", total_cost(production))
##
def defect_percentage(production):
    total_produced = 0
    total_defective = 0
    for batch in production:
        total_produced = total_produced + batch[2]
        total_defective = total_defective + batch[3]
    return (total_defective / total_produced) * 100

print("Overall defect percentage:", defect_percentage(production))

##
high_defect = list(filter(lambda batch: batch[3] > 10, production))

for batch in high_defect:
    print(batch)
##
accepted = list(map(lambda batch: batch[2] - batch[3], production))

print(accepted)
##
batch_cost = lambda batch: batch[2] * batch[4]

for batch in production:
    print(batch[0], batch_cost(batch))