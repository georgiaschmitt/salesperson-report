

#If you have time, feel free to implement your suggested improvements

"""Generate sales report showing total melons each salesperson sold."""

# This initializes two lists, one called salespeople and one called melons_sold
# Suggestion: I think rewriting this into a dictionary with salespeople as
# keys and melons sold as values would be simpler.
salespeople = [] 
melons_sold = []

# This loops over each line in a file object
f = open('sales-report.txt')
for line in f:
    line = line.rstrip() # Remove trailing whitespace after each line
    entries = line.split('|') # Splits lines into lists by '|'

    # This gets and assigns the name of each salesperson and the number of
    #melons they've sold
    salesperson = entries[0]
    melons = int(entries[2])

    # If the salesperson is already in the list of salespeople, 
    # find them and add to the number of melons they've sold
    # If not, add them to the list of salespeople and append
    #the number of melon's they've sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# For every salesperson, print a statement saying how many melons each sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


################################################################################
# REFACTORED VERSION 
"""Generate sales report showing total melons each salesperson sold."""

