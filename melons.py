melon_names = {
    1: "Honeydew",
    2: "Crenshaw",
    3: "Crane",
    4: "Casaba",
    5: "Cantaloupe",
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

melon_info = {}

for index, melon in melon_names.items():
    melon_info[melon] = {'seedless': melon_seedlessness[index], 'price': melon_prices[index]}
# print melon_info