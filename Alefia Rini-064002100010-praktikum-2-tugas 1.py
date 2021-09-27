# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:07:45 2021

@author: ALEFIA RINI
NAMA : Alefia Rini Mutmainnah
NIM  : 064002100010
"""

import math

a = float(input("masukkan nilai a: "))
b = float(input("masukkan nilai b: "))

hasil = a + b 
print("jumlah a dan b: ",hasil)

hasil = a - b 
print("selisih antara a dengan b: ", abs(hasil))

hasil = a * b 
print("hasil kali a dan b: ", hasil)

hasil = a % b
print("sisa pembagian a dengan b: ", hasil)

hasil = a / b
print("pembagian a dan b:", hasil)

hasil = math.log10(a)
print("log (a) :", hasil)

hasil = a ** b
print("pangkat a dan b:", hasil)
