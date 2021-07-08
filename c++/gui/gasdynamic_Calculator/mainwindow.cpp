#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "isentropicflow.h"
#include <iostream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Add items to Combo Box
    ui->combobox_options->addItem("Mach number");
    ui->combobox_options->addItem("T/T0");
    ui->combobox_options->addItem("p/p0");
    ui->combobox_options->addItem("rho/rho0");
    ui->combobox_options->addItem("A/A*(sub)");
    ui->combobox_options->addItem("A/A*(sup)");
    ui->combobox_options->addItem("Mach angle (deg.)");
    ui->combobox_options->addItem("P-M angle (deg.)");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btn_calculate_clicked()
{
    double input = ui->led_INPUT->text().toDouble();
    double gamma = ui->led_gamma->text().toDouble();
    int type = ui->combobox_options->currentIndex();

    // std::cout<<"Type = " << type << std::endl;
    // std::cout<<"Input = " << input << std::endl;
    isentropicFlow pos1(1, type, input, gamma);
    pos1.printResults();

    // set line_edits to calculated Values
    ui->led_machnumber->setText(QString::number(pos1.ma));
    ui->led_machAngle->setText(QString::number(pos1.MachAngle));
    ui->led_pdp0->setText(QString::number(pos1.pdp0));
    ui->led_TdT0->setText(QString::number(pos1.TdT0));
    ui->led_pmAngle->setText(QString::number(pos1.PM_Angle));
    ui->led_rhodrho0->setText(QString::number(pos1.rhodrho0));
    ui->led_AdAstar->setText(QString::number(pos1.AdAstar));
    ui->led_machStar->setText(QString::number(pos1.machStar));

    // TODO:
    ui->led_pdpstar->setText(QString::number(pos1.ma));
    ui->led_TdTstar->setText(QString::number(pos1.ma));
    ui->led_rhodrhostar->setText(QString::number(pos1.ma));
}
