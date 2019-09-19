/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout_2;
    QTabWidget *CentralTab;
    QWidget *MainBag;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QSpacerItem *verticalSpacer;
    QPushButton *refresh;
    QTableView *maintable;
    QWidget *IIS;
    QGridLayout *gridLayout_3;
    QMenuBar *menuBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->setEnabled(true);
        MainWindow->resize(920, 594);
        MainWindow->setMinimumSize(QSize(920, 594));
        MainWindow->setMaximumSize(QSize(920, 594));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout_2 = new QGridLayout(centralWidget);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        CentralTab = new QTabWidget(centralWidget);
        CentralTab->setObjectName(QStringLiteral("CentralTab"));
        CentralTab->setMinimumSize(QSize(891, 531));
        CentralTab->setMaximumSize(QSize(902, 535));
        QFont font;
        font.setFamily(QStringLiteral("MS Shell Dlg 2"));
        font.setPointSize(8);
        CentralTab->setFont(font);
        CentralTab->setToolTipDuration(-1);
        CentralTab->setStyleSheet(QLatin1String("QTabWidget::pane { \n"
" min-width: 10ex;\n"
" padding: 5px;\n"
" border: 2px solid #C4C4C7;\n"
"border-bottom-color:rgb(75, 177, 255);\n"
"	border-top-color: rgb(75, 177, 255);\n"
"	border-left-color: rgb(75, 177, 255);\n"
"	border-right-color: rgb(75, 177, 255);\n"
"} \n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C7;\n"
"	border-bottom-color: rgb(255, 143, 14);\n"
"	border-top-color: rgb(255, 143, 14);\n"
"	border-left-color: rgb(255, 143, 14);\n"
"	border-right-color: rgb(255, 143, 14);\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 10ex;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f"
                        "4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; \n"
"   border: 2px solid #C4C4C7;\n"
"	border-bottom-color:rgb(79, 255, 15);\n"
"	border-top-color: rgb(79, 255, 15);\n"
"	border-left-color: rgb(79, 255, 15);\n"
"	border-right-color: rgb(79, 255, 15);\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 10ex;\n"
"    padding: 5px;\n"
"}\n"
""));
        MainBag = new QWidget();
        MainBag->setObjectName(QStringLiteral("MainBag"));
        QFont font1;
        font1.setFamily(QStringLiteral("Segoe UI"));
        font1.setPointSize(9);
        font1.setBold(false);
        font1.setWeight(50);
        MainBag->setFont(font1);
        gridLayoutWidget = new QWidget(MainBag);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(0, 0, 871, 481));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 1, 1, 1, 1);

        refresh = new QPushButton(gridLayoutWidget);
        refresh->setObjectName(QStringLiteral("refresh"));

        gridLayout->addWidget(refresh, 0, 1, 1, 1);

        maintable = new QTableView(gridLayoutWidget);
        maintable->setObjectName(QStringLiteral("maintable"));
        QFont font2;
        font2.setPointSize(8);
        maintable->setFont(font2);

        gridLayout->addWidget(maintable, 0, 0, 2, 1);

        CentralTab->addTab(MainBag, QString());
        IIS = new QWidget();
        IIS->setObjectName(QStringLiteral("IIS"));
        CentralTab->addTab(IIS, QString());

        gridLayout_2->addWidget(CentralTab, 0, 0, 1, 1);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setSpacing(6);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));

        gridLayout_2->addLayout(gridLayout_3, 1, 0, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 920, 21));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        CentralTab->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
#ifndef QT_NO_TOOLTIP
        CentralTab->setToolTip(QString());
#endif // QT_NO_TOOLTIP
        refresh->setText(QApplication::translate("MainWindow", "PushButton", nullptr));
        CentralTab->setTabText(CentralTab->indexOf(MainBag), QApplication::translate("MainWindow", "\320\234\320\276\320\271 \320\277\320\276\321\200\321\202\321\204\320\265\320\273\321\214", nullptr));
        CentralTab->setTabText(CentralTab->indexOf(IIS), QApplication::translate("MainWindow", "\320\230\320\230\320\241", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
