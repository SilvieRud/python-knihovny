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

# rezek = [hlas[0] for hlas in hlasy]
# dolezal = [hlas[1] for hlas in hlasy]
# bednar = [hlas[2] for hlas in hlasy]
# brotz = [hlas[3] for hlas in hlasy]
# kaspar = [hlas[4] for hlas in hlasy]
# print(sum(rezek), sum(dolezal), sum(bednar), sum(brotz), sum(kaspar))

hlasy_kandidatu = [sum(hlas) for hlas in zip(*hlasy)]
print(hlasy_kandidatu)

hlasy_kandidatu = [sum(hlas) for hlas in zip(*hlasy)]
print(max(hlasy_kandidatu))
print()

volebni_ucast = [sum(hlas) for hlas in hlasy]
print(volebni_ucast, max(volebni_ucast), min(volebni_ucast))

