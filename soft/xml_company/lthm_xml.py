# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Livent Corporation ========================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '10.21', "count": '10'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Livent",
    ComppanyName="Livent Corporation",
    ComppanyCode="LTHM",
    ComppanyVal="doll",
    ComppanyBuyLevel="5",
    ComppanySellLevel="50",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/lthm.xml','utf-8')
    exit(1)