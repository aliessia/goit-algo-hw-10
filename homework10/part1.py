from pulp import LpMaximize, LpProblem, LpVariable, lpSum
model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)
x = LpVariable(name="lemonade", lowBound=0, cat="Integer")
y = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")
model += lpSum([x, y]), "Total Drinks Produced"
model += (2 * x + y <= 100), "Water Constraint"
model += (x <= 50), "Sugar Constraint"
model += (x <= 30), "Lemon Juice Constraint"
model += (2 * y <= 40), "Fruit Puree Constraint"
model.solve()
lemonade_production = x.varValue
fruit_juice_production = y.varValue
total_production = lemonade_production + fruit_juice_production

print(f"Кількість виробленого Лимонаду: {lemonade_production}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice_production}")
print(f"Загальна кількість вироблених напоїв: {total_production}")
