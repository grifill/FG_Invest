# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= ПАО Мечел =================================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '64.41', "count": '50'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Мечел",
    ComppanyName="ПАО Мечел",
    ComppanyCode="MTLR",
    ComppanyVal="rubl",
    ComppanyBuyLevel="40",
    ComppanySellLevel="300",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/mtlr.xml','utf-8')
    exit(1)