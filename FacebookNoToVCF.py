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
#   FacebookCcontactsto vcf  / ixakblt   #
#################################
from bs4 import BeautifulSoup
import lxml

dosya = open("fblist.html",encoding="utf-8")
yazilacaknolar = open("ixrehberforfb.vcf","a",encoding="utf-8")
soup = BeautifulSoup(dosya.read(),"lxml")

kisiler = soup.find_all("div",attrs={"class":"_3-95 _a6-g"})

for i in kisiler:
    try:
        isim = i.find("div",attrs={"class":"_2ph_ _a6-h _a6-i"}).text
        no = i.find("div",attrs={"class":"_a6_p"}).text
        vcfscript = """
BEGIN:VCARD
VERSION:2.1
N:{};;;
FN:{}
TEL;CELL:{}
END:VCARD

""".format(isim,"",no)
    except:
        continue
    yazilacaknolar.write(vcfscript)

yazilacaknolar.close()
