#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/*
ixakblt - ibrahim AKBULUT
-------------------------------
 https://ixakblt.site
-------------------------------
https://ixakblt.com
-------------------------------
*/
"""


#################################
#   FacebookCcontactsto vcf  / ixakblt   #
#################################
from bs4 import BeautifulSoup

dosya = open("fblist.html",encoding="utf-8")
yazilacaknolar = open("ixrehberforfb.vcf","a",encoding="utf-8")
soup = BeautifulSoup(dosya.read(),"lxml")

kisiler = soup.find_all("div",attrs={"class":"pam _3-95 _2pi0 _2lej uiBoxWhite noborder"})

for i in kisiler:
    try:
        isim = i.find("div",attrs={"class":"_3-96 _2pio _2lek _2lel"}).text
        soyisim = i.find("div",attrs={"class":"_3hls"}).text
        vcfscript = """
BEGIN:VCARD
VERSION:2.1
N:{};;;
FN:{}
TEL;CELL:{}
END:VCARD


""".format(isim,isim,soyisim)
        print(vcfscript)
    except:
        continue
    yazilacaknolar.write(vcfscript)

yazilacaknolar.close()
