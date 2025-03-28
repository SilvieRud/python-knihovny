def obrat_slovnik(slovnik):
    return {hodnota: klic for klic, hodnota in slovnik.items()}

slovnik = {"pes": "dog", "kočka": "cat", "had": "snake"}
print(obrat_slovnik(slovnik))