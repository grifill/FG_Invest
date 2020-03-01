# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Nokia Corporation =========================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '3.83', "count": '75'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Nokia",
    ComppanyName="Nokia Corporation",
    ComppanyCode="NOK",
    ComppanyVal="doll",
    ComppanyBuyLevel="4",
    ComppanySellLevel="100",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/nok.xml','utf-8')
    exit(1)