# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from bs4 import BeautifulSoup
from tabulate import tabulate
import json


veriler = BeautifulSoup(open('kisiler.html'), 'lxml')
liste   =  []

for kisi in veriler.findAll(class_='-xVjU f2nsG'):
    try:
        kisi_adi    = kisi.find(class_='yMV6Z').text
        kisi_no     = kisi.find(class_='ufG8g').text
        kisi_no     = f'90{kisi_no}' if kisi_no.startswith('5') and len(kisi_no) == 10 else kisi_no

        try:
            kisi_no = int(kisi_no)
        except:
            pass
    except:
        pass

    if type(kisi_no) == int:
        liste.append({
            'adi' : kisi_adi,
            'no'  : f'+{kisi_no}' if str(kisi_no).startswith('90') else kisi_no
        })

    else:
        for kisi in liste:
            try:
                ad, no = kisi.values()
            except:
                pass

            if ad == kisi_adi:
                kisi.update({'mail' : kisi_no})

essiz = [dict(sozluk) for sozluk in set(tuple(liste_ici.items()) for liste_ici in liste)]


# print(json.dumps(essiz, sort_keys=True, indent=2, ensure_ascii=False))
print(tabulate(essiz, headers='keys', tablefmt='psql'))
# print(f'''
# Orj : {len(liste)}
# Dis : {len(essiz)}
# ''')