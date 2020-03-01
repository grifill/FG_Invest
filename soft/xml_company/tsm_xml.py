# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Taiwan Semiconductor Manufacturing Company ================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '58.67', "count": '1'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="TSMC",
    ComppanyName="Taiwan Semiconductor Manufacturing Company",
    ComppanyCode="TSM",
    ComppanyVal="doll",
    ComppanyBuyLevel="40",
    ComppanySellLevel="100",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/tsm.xml','utf-8')
    exit(1)