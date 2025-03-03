nazvy = [
    'Někdo to rád horké, extended edition',
    'Adéla ještě nevečeřela',
    'Kulový blesk'
]
delky = [136, 105, 82]

trvani = [f"{delka // 60}:{delka % 60}" for delka in delky]
print(trvani)
