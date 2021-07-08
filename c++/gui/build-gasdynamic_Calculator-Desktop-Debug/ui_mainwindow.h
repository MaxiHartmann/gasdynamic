/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.11.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QPushButton *btn_calculate;
    QComboBox *combobox_options;
    QLabel *label_12;
    QLineEdit *led_INPUT;
    QLineEdit *led_gamma;
    QGridLayout *gridLayout_2;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *led_pmAngle;
    QLabel *label_3;
    QLineEdit *led_machAngle;
    QLineEdit *led_pdp0;
    QLineEdit *led_machnumber;
    QLineEdit *led_TdTstar;
    QLineEdit *led_rhodrho0;
    QLineEdit *led_rhodrhostar;
    QLineEdit *led_TdT0;
    QLineEdit *led_pdpstar;
    QLabel *label_8;
    QLabel *label_7;
    QLabel *label_10;
    QLabel *label_6;
    QLabel *label_9;
    QLineEdit *led_AdAstar;
    QLabel *label_11;
    QLineEdit *led_machStar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(781, 211);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        centralWidget->setEnabled(true);
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        btn_calculate = new QPushButton(centralWidget);
        btn_calculate->setObjectName(QStringLiteral("btn_calculate"));

        gridLayout->addWidget(btn_calculate, 0, 2, 1, 1);

        combobox_options = new QComboBox(centralWidget);
        combobox_options->setObjectName(QStringLiteral("combobox_options"));

        gridLayout->addWidget(combobox_options, 0, 0, 1, 1);

        label_12 = new QLabel(centralWidget);
        label_12->setObjectName(QStringLiteral("label_12"));

        gridLayout->addWidget(label_12, 0, 3, 1, 1);

        led_INPUT = new QLineEdit(centralWidget);
        led_INPUT->setObjectName(QStringLiteral("led_INPUT"));

        gridLayout->addWidget(led_INPUT, 0, 1, 1, 1);

        led_gamma = new QLineEdit(centralWidget);
        led_gamma->setObjectName(QStringLiteral("led_gamma"));

        gridLayout->addWidget(led_gamma, 0, 4, 1, 1);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_2, 1, 0, 1, 1);

        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_4, 0, 2, 1, 1);

        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_5, 0, 4, 1, 1);

        led_pmAngle = new QLineEdit(centralWidget);
        led_pmAngle->setObjectName(QStringLiteral("led_pmAngle"));

        gridLayout_2->addWidget(led_pmAngle, 0, 5, 1, 1);

        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_3, 2, 0, 1, 1);

        led_machAngle = new QLineEdit(centralWidget);
        led_machAngle->setObjectName(QStringLiteral("led_machAngle"));

        gridLayout_2->addWidget(led_machAngle, 0, 3, 1, 1);

        led_pdp0 = new QLineEdit(centralWidget);
        led_pdp0->setObjectName(QStringLiteral("led_pdp0"));

        gridLayout_2->addWidget(led_pdp0, 1, 1, 1, 1);

        led_machnumber = new QLineEdit(centralWidget);
        led_machnumber->setObjectName(QStringLiteral("led_machnumber"));

        gridLayout_2->addWidget(led_machnumber, 0, 1, 1, 1);

        led_TdTstar = new QLineEdit(centralWidget);
        led_TdTstar->setObjectName(QStringLiteral("led_TdTstar"));

        gridLayout_2->addWidget(led_TdTstar, 2, 5, 1, 1);

        led_rhodrho0 = new QLineEdit(centralWidget);
        led_rhodrho0->setObjectName(QStringLiteral("led_rhodrho0"));

        gridLayout_2->addWidget(led_rhodrho0, 1, 3, 1, 1);

        led_rhodrhostar = new QLineEdit(centralWidget);
        led_rhodrhostar->setObjectName(QStringLiteral("led_rhodrhostar"));

        gridLayout_2->addWidget(led_rhodrhostar, 2, 3, 1, 1);

        led_TdT0 = new QLineEdit(centralWidget);
        led_TdT0->setObjectName(QStringLiteral("led_TdT0"));

        gridLayout_2->addWidget(led_TdT0, 1, 5, 1, 1);

        led_pdpstar = new QLineEdit(centralWidget);
        led_pdpstar->setObjectName(QStringLiteral("led_pdpstar"));

        gridLayout_2->addWidget(led_pdpstar, 2, 1, 1, 1);

        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_8, 2, 4, 1, 1);

        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_7, 1, 4, 1, 1);

        label_10 = new QLabel(centralWidget);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_10, 2, 6, 1, 1);

        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_6, 1, 2, 1, 1);

        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_9, 2, 2, 1, 1);

        led_AdAstar = new QLineEdit(centralWidget);
        led_AdAstar->setObjectName(QStringLiteral("led_AdAstar"));

        gridLayout_2->addWidget(led_AdAstar, 2, 7, 1, 1);

        label_11 = new QLabel(centralWidget);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_11, 0, 6, 1, 1);

        led_machStar = new QLineEdit(centralWidget);
        led_machStar->setObjectName(QStringLiteral("led_machStar"));

        gridLayout_2->addWidget(led_machStar, 0, 7, 1, 1);


        gridLayout->addLayout(gridLayout_2, 1, 0, 1, 5);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Isentropic Flow Calculator", nullptr));
        btn_calculate->setText(QApplication::translate("MainWindow", "Calculate", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "Gamma = ", nullptr));
        led_INPUT->setText(QApplication::translate("MainWindow", "2.0", nullptr));
        led_gamma->setText(QApplication::translate("MainWindow", "1.4", nullptr));
        label->setText(QApplication::translate("MainWindow", "Machnumber = ", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "p/p0 = ", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Mach angle = ", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "P-M angle = ", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "p/p* = ", nullptr));
        label_8->setText(QApplication::translate("MainWindow", "T/T* = ", nullptr));
        label_7->setText(QApplication::translate("MainWindow", "T/T0 = ", nullptr));
        label_10->setText(QApplication::translate("MainWindow", "A/A* = ", nullptr));
        label_6->setText(QApplication::translate("MainWindow", "rho/rho0 = ", nullptr));
        label_9->setText(QApplication::translate("MainWindow", "rho/rho* = ", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "Ma* = ", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
