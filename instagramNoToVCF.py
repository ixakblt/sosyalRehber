#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/*
------------------------------------
ixakblt - ibrahim AKBULUT
------------------------------------
Web Site :ixakblt
------------------------------------
All Sites : @ixakblt
------------------------------------
*/
"""
#################################
#   İnstagram Ccontactsto vcf  / ixakblt  #
#################################
from bs4 import BeautifulSoup
import unicodedata
veri = """
HTML KODU BURAYA GELECEK
"""
try:
    sonno = open("ixrehber.vcf","a")
    soup = BeautifulSoup(veri,"lxml")
    veri =soup.select("body > div > div")
    for i in veri:
        for j in i.select("div > div._33l-y > h1"):
            if "arabic" in unicodedata.name(j.text[0]).lower():
                ad = "ixakblt Arapca"
            elif "hammer and sickle" in unicodedata.name(j.text[-1]).lower():
                ad = "{}".format(j.text[0:-1])
            else:
                ad = j.text
        for k in i.select("div > div:nth-child(2) > h1"):
            if "@" in k.text:
                soyad = " "
            elif k.text[0] !=   "0":
                soyad = "{}{}".format("0",k.text)
            else:
                soyad =k.text
            vcfscript = """
BEGIN:VCARD
VERSION:2.1
N:{};;;
FN:{}
TEL;CELL:{}
END:VCARD
    """.format(ad,ad,soyad)
            sonno.write(vcfscript)
    sonno.close()
except:
    pass
