# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Southwestern Energy Company ===============================
# ===================================================================

BUY = {
    0: {"data": '26.11.2019', "price": '1.87', "count": '5'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Southwestern Energy Company",
    ComppanyName="Southwestern Energy",
    ComppanyCode="SWN",
    ComppanyVal="doll",
    ComppanyBuyLevel="1",
    ComppanySellLevel="30",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/swn.xml','utf-8')
    exit(1)