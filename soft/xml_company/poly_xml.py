# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= POLYMETAL =================================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '839.1', "count": '1'}
}

SELL = {
}

DIV = {
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
    xml_test_gen('./runtime/poly.xml','utf-8')
    exit(1)