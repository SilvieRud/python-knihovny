hlasy = [
    [78774, 43179, 225111, 144799, 242854],
    [91062, 22451, 17475, 53391, 46450],
    [179186, 216499, 4493, 156305, 61222],
    [9619, 53476, 926, 64737, 34566],
    [66904, 85730, 27271, 12964, 38041],
    [118755, 1929, 30426, 25178, 31952],
    [64467, 40993, 81181, 39392, 4335],
    [11221, 97970, 26179, 98539, 112578],
    [171064, 7638, 8752, 96666, 39738],
    [74235, 101680, 18920, 45904, 1922],
    [39309, 1505, 10531, 30458, 40228],
    [131584, 1812, 241122, 22267, 99326],
    [194133, 39985, 200997, 28229, 20780],
    [66188, 51607, 15977, 177272, 17664]
]

prvni = [round((hlas/sum(hlasy[0]))*100, 2) for hlas in hlasy[0]]
druhy = [round((hlas/sum(hlasy[1]))*100, 2) for hlas in hlasy[1]]
treti = [round((hlas/sum(hlasy[2]))*100, 2) for hlas in hlasy[2]]
ctvrty = [round((hlas/sum(hlasy[3]))*100, 2) for hlas in hlasy[3]]
paty = [round((hlas/sum(hlasy[4]))*100, 2) for hlas in hlasy[4]]
sesty = [round((hlas/sum(hlasy[5]))*100, 2) for hlas in hlasy[5]]
sedmy = [round((hlas/sum(hlasy[6]))*100, 2) for hlas in hlasy[6]]
osmy = [round((hlas/sum(hlasy[7]))*100, 2) for hlas in hlasy[7]]
devaty = [round((hlas/sum(hlasy[8]))*100, 2) for hlas in hlasy[8]]
desaty = [round((hlas/sum(hlasy[9]))*100, 2) for hlas in hlasy[9]]
jedenacty = [round((hlas/sum(hlasy[10]))*100, 2) for hlas in hlasy[10]]
dvanacty = [round((hlas/sum(hlasy[11]))*100, 2) for hlas in hlasy[11]]
trinacty = [round((hlas/sum(hlasy[12]))*100, 2) for hlas in hlasy[12]]
ctrnacty = [round((hlas/sum(hlasy[13]))*100, 2) for hlas in hlasy[13]]

print(prvni, druhy, treti, ctvrty, paty, sesty, sedmy, osmy, devaty, desaty, jedenacty, dvanacty, trinacty, ctrnacty, sep="\n")


