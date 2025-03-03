jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

pocet_pismen = [len(jmeno) for jmeno in jmena]
print(pocet_pismen)

velka_pismena = [jmeno.upper() for jmeno in jmena]
print(velka_pismena)

plus_a = [jmeno + "a" for jmeno in jmena]
print(plus_a)

male_koncovka = [jmeno.lower() + "@email.cz" for jmeno in jmena]
print(male_koncovka)
