# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Macy's ====================================================
# ===================================================================

BUY = {
    0: {"data": '18.11.2019', "price": '17.17', "count": '2'},
    1: {"data": '19.11.2019', "price": '15.10', "count": '1'},
    2: {"data": '21.11.2019', "price": '14.71', "count": '2'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Macy's",
    ComppanyName="Macy",
    ComppanyCode="M",
    ComppanyVal="doll",
    ComppanyBuyLevel="10",
    ComppanySellLevel="35",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/m.xml','utf-8')
    exit(1)