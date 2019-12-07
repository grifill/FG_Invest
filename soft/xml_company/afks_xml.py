# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= АФК Система ===============================================
# ===================================================================

BUY = {
    0: {"data": '19.11.2019', "price": '15.309', "count": '200'},
    1: {"data": '28.11.2019', "price": '15.043', "count": '100'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="АФК Система",
    ComppanyName="АФК Система",
    ComppanyCode="AFKS",
    ComppanyVal="rubl",
    ComppanyBuyLevel="10",
    ComppanySellLevel="80",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/afks.xml','utf-8')
    exit(1)