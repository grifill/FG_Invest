#-------------------------------------------------
#
# Project created by QtCreator 2019-10-15T13:30:01
#
#-------------------------------------------------

QT       += core gui\
            printsupport\
            xml

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = FG_InvestPC
TEMPLATE = app
DESTDIR = ./../

VERSION= 0.0.1
QMAKE_TARGET_COMPANY= FGU
QMAKE_TARGET_PRODUCT= FG_InvestPC
QMAKE_TARGET_DESCRIPTION= Investing PC program
QMAKE_TARGET_COPYRIGHT= Filatov Grigoriy

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        mainwindow.cpp

HEADERS += \
        mainwindow.h

FORMS += \
    mainwindow.ui

RESOURCES += \
    icos.qrc

DISTFILES += \
    _runtime/icocomp/alrs_ico.ico \
    _runtime/icocomp/mtlr_ico.ico \
    _runtime/icocomp/poly_ico.ico \
    _runtime/icocomp/rual_ico.ico \
    _runtime/compfiles/1_poly.xml \
    _runtime/compfiles/company_icos.ini \
    _runtime/icocomp/atvi_ico.ico \
    _runtime/icocomp/endp_ico.ico \
    _runtime/icocomp/m_ico.ico \
    _runtime/icocomp/mu_ico.ico \
    _runtime/icocomp/nok_ico.ico \
    _runtime/icocomp/veon_ico.ico \
    _runtime/icocomp/afks_ico.ico \
    _runtime/icocomp/alrs_ico.ico \
    _runtime/icocomp/atvi_ico.ico \
    _runtime/icocomp/chmf_ico.ico \
    _runtime/icocomp/endp_ico.ico \
    _runtime/icocomp/enpldr_ico.ico \
    _runtime/icocomp/gazp_ico.ico \
    _runtime/icocomp/hear_ico.ico \
    _runtime/icocomp/m_ico.ico \
    _runtime/icocomp/mtlr_ico.ico \
    _runtime/icocomp/mu_ico.ico \
    _runtime/icocomp/nlmk_ico.ico \
    _runtime/icocomp/nok_ico.ico \
    _runtime/icocomp/nvtk_ico.ico \
    _runtime/icocomp/okgb_ico.ico \
    _runtime/icocomp/poly_ico.ico \
    _runtime/icocomp/qiwidr_ico.ico \
    _runtime/icocomp/rual_ico.ico \
    _runtime/icocomp/sber_ico.ico \
    _runtime/icocomp/selg_ico.ico \
    _runtime/icocomp/tatnp_ico.ico \
    _runtime/icocomp/veon_ico.ico \
    _runtime/icocomp/vtbr_ico.ico \
    _runtime/icocomp/yndx_ico.ico
