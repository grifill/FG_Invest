#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMenu>
#include <QMenuBar>

#include <QString>
#include <QStringList>
#include "QStandardItemModel"
#include "QStandardItem"
#include <QTableWidgetItem>
#include <QSettings>
#include <QImage>
#include <QFile>

#include <QtXml>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_refresh_clicked();

private:
    Ui::MainWindow *ui;
    QMenu *fileMenu;

    void createMenu();
    void BAGTable_Create();
    void BAGTable_Icons_Set();
    void addElementDataToList();
};

#endif // MAINWINDOW_H
