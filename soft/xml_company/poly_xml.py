# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= POLYMETAL =================================================
# ===================================================================

BUY = {
    0: {"data": '08.08.2019', "price": '839.5', "count": '1'},
    1: {"data": '09.08.2019', "price": '840.5', "count": '3'},
    2: {"data": '09.08.2019', "price": '840.7', "count": '1'},
    3: {"data": '12.08.2019', "price": '831.0', "count": '2'},
    4: {"data": '13.08.2019', "price": '835.0', "count": '1'},
    5: {"data": '14.08.2019', "price": '828.0', "count": '1'},
    6: {"data": '16.08.2019', "price": '864.0', "count": '1'},
}

SELL = {
}

DIV = {
    0: {"data": '27.09.2019', "price": '0.2', "count": '10'},
}


DESC = dict(
    Title="Polymetal",
    ComppanyName="Полиметалл",
    ComppanyCode="POLY",
    ComppanyVal="rubl",
    ComppanyBuyLevel="850",
    ComppanySellLevel="1500",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/1_poly.xml','utf-8')
    exit(1)