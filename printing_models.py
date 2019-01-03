# start with some designs that need to be printed.
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

# simulate printing each design until none are left.
#move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    #simulate creating a 3d print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#simulate all completed models
print("\n The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
