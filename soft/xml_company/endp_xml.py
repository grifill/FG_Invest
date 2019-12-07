# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Endo Pharmaceuticals ======================================
# ===================================================================

BUY = {
    0: {"data": '22.10.2019', "price": '4.70', "count": '2'},
    1: {"data": '30.10.2019', "price": '4.55', "count": '2'},
    2: {"data": '31.10.2019', "price": '4.44', "count": '1'},
    3: {"data": '5.11.2019', "price": '4.55', "count": '5'},
    4: {"data": '7.11.2019', "price": '4.28', "count": '2'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Endo Pharmaceuticals",
    ComppanyName="Endo",
    ComppanyCode="ENDP",
    ComppanyVal="doll",
    ComppanyBuyLevel="3",
    ComppanySellLevel="15",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/endp.xml','utf-8')
    exit(1)