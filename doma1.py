veky = [35, 12, 44, 11, 18, 21, 28, 18]

do_osmnacti = [int(18-vek) for vek in veky]
print(do_osmnacti)

plnoletost = [(vek >= 18) for vek in veky]
print(plnoletost)

osmnact = [(vek == 18) for vek in veky]
print(osmnact)
