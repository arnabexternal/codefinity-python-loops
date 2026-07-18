# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

for travel in travel_costs:
    i = 0
    new_travel = []
    i = 0
    for i in range(0,len(travel)):
        if travel[i] <= 100:
            new_travel.append('Cheap')
        else:
            new_travel.append(travel[i])
        i += 1
    processed_expenses.append(new_travel)
        

# Testing
print('Processed Travel Expenses:', processed_expenses)