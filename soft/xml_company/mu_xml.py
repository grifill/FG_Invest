# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Micron Technology =========================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '49.93', "count": '2'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Micron Technology",
    ComppanyName="Micron",
    ComppanyCode="MU",
    ComppanyVal="doll",
    ComppanyBuyLevel="25",
    ComppanySellLevel="100",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/mu.xml','utf-8')
    exit(1)