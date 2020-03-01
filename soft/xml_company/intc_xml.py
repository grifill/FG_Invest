# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Intel Corporation =========================================
# ===================================================================

BUY = {
    0: {"data": '1.03.2020', "price": '61.7', "count": '2'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Intel Corp",
    ComppanyName="Intel",
    ComppanyCode="INTC",
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
    xml_test_gen('./runtime/intc.xml','utf-8')
    exit(1)