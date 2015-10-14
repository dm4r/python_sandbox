# for number in range (1, 100):
#    if number % 3 == 0:
#        print(number)

actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

for x, y in actors.iteritems():
    print(x, y)

# Could also be
# for keys, values in actors.items():
#    print(keys, values)
