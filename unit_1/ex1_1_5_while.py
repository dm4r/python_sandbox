# The while statement example provided in Thinkful tutorial
# miles_run = 0
# running = True
#
# while running:
#    if miles_run <= 10:
#        print("Still running! On mile {}".format(miles_run))
#        miles_run += 1
#    else:
#        running = False
#
# print("Whew! I'm tired")

# Set the amount of miles left to get to LDN from LEI
miles_to_london = 102
# Set the mph we are traveling
mph_to_london = 2

# Set the amount of miles covered from LDN to LEI
miles_to_leicester = 0
# Set the mph we are traveling
mph_to_leicester = 1

# Set meet point stating "it's True, the miles traveled values DO NOT match
meet_point = True

# The while statement will continue while this
# resolves to True.  As soon as it is False, then the while loop will stop.
while meet_point:
#   if the two values DO NOT match, then continue the loop
    if miles_to_leicester != miles_to_london:
        print("Still on the road to London! Currently on mile {}".format(miles_to_london))
        miles_to_london -= 2
        print("Still on the road to Leicester! Currently on mile {}".format(miles_to_leicester))
        miles_to_leicester += 1
    else:
        meet_point = False

# Now that meet_point is False, because the miles traveled DO match for both
# travelers, we print which mile we met at on the road.
print("We met on the road at mile {}".format(miles_to_london))
