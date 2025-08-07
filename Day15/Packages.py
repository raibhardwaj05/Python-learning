from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)



