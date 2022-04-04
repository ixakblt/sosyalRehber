# Bu araç @keyiflerolsun katkıları ile | @KekikAkademi için yazılmıştır.
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from tabulate import tabulate
import json

veriler = BeautifulSoup(open('bakalim.html', encoding='utf-8'), 'lxml')
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
                break

essiz = [dict(sozluk) for sozluk in set(tuple(liste_ici.items()) for liste_ici in liste)]
essiz = sorted(essiz, key=lambda sozluk: sozluk['adi'])

print(f'''
Orj : {len(liste)}
Dis : {len(essiz)}
''')

with open('bakalim.json', "w+", encoding='utf-8') as dosya:
    dosya.write(json.dumps(essiz, ensure_ascii=False, indent=2, sort_keys=False))

with open('bakalim.md', "w+", encoding='utf-8') as dosya:
    dosya.write(tabulate(essiz, headers='keys', tablefmt='github'))

with open('bakalim.vcf', "a+", encoding='utf-8') as dosya:
    for kisi in essiz:
        try:
            dosya.write(f"""BEGIN:VCARD
VERSION:3.0
FN:{kisi['adi']}
N:{kisi['adi']};;;
TEL;TYPE=CELL:{kisi['no']}
EMAIL;TYPE=INTERNET:{kisi['mail']}
END:VCARD
""")
        except KeyError:
            dosya.write(f"""BEGIN:VCARD
VERSION:3.0
FN:{kisi['adi']}
N:{kisi['adi']};;;
TEL;TYPE=CELL:{kisi['no']}
END:VCARD
""")