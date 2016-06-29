# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:09:14 2016

@author: Claudio
"""

import urllib
import re


import os #Limpa a tela
os.system('cls')

# 6/2/2016 IPDO-01-06-2016

link_site = "http://www.ons.org.br/publicacao/ipdo/Ano_2016/M%C3%AAs_05/"
#link_site = "http://www.ons.org.br/publicacao/ipdo/Ano_2016/"
month = '05'
year = '2016'


# Baixa os arquivos pdf do site e coloca em uma pasta local
def download_file_pdf(link_site, month, year):

    num_days = count_days_month(year, month)
    days_month = range(1, num_days + 1)

# A nomenclaruta do arquivo tem "zero" na frente de 01-09, depois não! Como o 10!
    for day in days_month:
        if day < 10:
            pdf_name = "IPDO-0" + str(day) + "-" + month + "-" + year + ".pdf"
            urllib.urlretrieve(link_site + pdf_name, pdf_name)
        elif day >= 10:
            pdf_name = "IPDO-" + str(day) + "-" + month + "-" + year + ".pdf"
            urllib.urlretrieve(link_site + pdf_name, pdf_name)

# Conta quantos dias existem no intervalo de um mês
def count_days_month(year, month):
    from datetime import date

# mês inicial
    first_date = date(int(year), int(month), 1)
    ord_first_date = date.toordinal(first_date)

# mês seguinte
    if month == '12':
        last_date = date(int(year) + 1, 1, 1)   # Próximo ano, mês 1
    else:
        last_date = date(int(year), int(month) + 1, 1) # Mesmo ano, Próximo mês

    ord_last_date = date.toordinal(last_date)

    days_month = ord_last_date- ord_first_date

    return days_month

download_file_pdf(link_site, month, year)
