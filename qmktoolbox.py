import keyboardlist
import mculist
import requests
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.localFileLbl = QtWidgets.QLabel(self.centralwidget)
        self.localFileLbl.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.localFileLbl.setObjectName("localFileLbl")
        self.microLbl = QtWidgets.QLabel(self.centralwidget)
        self.microLbl.setGeometry(QtCore.QRect(550, 10, 71, 16))
        self.microLbl.setObjectName("microLbl")
        self.localFileComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.localFileComboBox.setGeometry(QtCore.QRect(20, 30, 441, 22))
        self.localFileComboBox.setObjectName("localFileComboBox")
        self.microSelectComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.microSelectComboBox.setGeometry(QtCore.QRect(550, 30, 201, 22))
        self.microSelectComboBox.setObjectName("microSelectComboBox")
        self.keyboardFromLbl = QtWidgets.QLabel(self.centralwidget)
        self.keyboardFromLbl.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.keyboardFromLbl.setObjectName("keyboardFromLbl")
        self.keymapLbl = QtWidgets.QLabel(self.centralwidget)
        self.keymapLbl.setGeometry(QtCore.QRect(210, 70, 47, 13))
        self.keymapLbl.setObjectName("keymapLbl")
        self.flashEnabledLbl = QtWidgets.QLabel(self.centralwidget)
        self.flashEnabledLbl.setGeometry(QtCore.QRect(470, 70, 81, 16))
        self.flashEnabledLbl.setObjectName("flashEnabledLbl")
        self.autoFlashCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.autoFlashCheck.setGeometry(QtCore.QRect(600, 100, 81, 17))
        self.autoFlashCheck.setObjectName("autoFlashCheck")
        self.flashBtn = QtWidgets.QPushButton(self.centralwidget)
        self.flashBtn.setGeometry(QtCore.QRect(600, 70, 75, 23))
        self.flashBtn.setObjectName("flashBtn")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(680, 70, 75, 23))
        self.resetBtn.setObjectName("resetBtn")
        self.keyboardFromComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.keyboardFromComboBox.setGeometry(QtCore.QRect(20, 90, 181, 22))
        self.keyboardFromComboBox.setObjectName("keyboardFromComboBox")
        self.keymapComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.keymapComboBox.setGeometry(QtCore.QRect(210, 90, 141, 22))
        self.keymapComboBox.setObjectName("keymapComboBox")
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setGeometry(QtCore.QRect(360, 90, 75, 23))
        self.loadBtn.setObjectName("loadBtn")
        self.openFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openFileBtn.setGeometry(QtCore.QRect(470, 30, 75, 23))
        self.openFileBtn.setObjectName("openFileBtn")
        self.dfuCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.dfuCheck.setGeometry(QtCore.QRect(450, 90, 70, 17))
        self.dfuCheck.setObjectName("dfuCheck")
        self.stm32Check = QtWidgets.QCheckBox(self.centralwidget)
        self.stm32Check.setGeometry(QtCore.QRect(450, 110, 70, 17))
        self.stm32Check.setObjectName("stm32Check")
        self.halfkayCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.halfkayCheck.setGeometry(QtCore.QRect(520, 90, 70, 17))
        self.halfkayCheck.setObjectName("halfkayCheck")
        self.caterinaCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.caterinaCheck.setGeometry(QtCore.QRect(520, 110, 70, 17))
        self.caterinaCheck.setObjectName("caterinaCheck")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(23, 140, 721, 461))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Add Basic Text to Textbox
        self.plainTextEdit.insertPlainText("QMK Toolbox (http://qmk.fm/toolbox)\n")
        self.plainTextEdit.insertPlainText("Supporting following bootloaders:\n")
        self.plainTextEdit.insertPlainText(" - DFU (Atmel, LUFA) via dfu-programmer (http://dfu-programmer.github.io/)\n")
        self.plainTextEdit.insertPlainText(" - Caterina (Arduino, Pro Micro) via avrdude (http://nongnu.org/avrdude/)\n")
        self.plainTextEdit.insertPlainText(" - Halfkay (Teensy, Ergodox EZ) via teensy_loader_cli (https://pjrc.com/teensy/loader_cli.html)\n")
        self.plainTextEdit.insertPlainText(" - STM32 (ARM) via dfu-util (http://dfu-util.sourceforge.net/)\n")
        self.plainTextEdit.insertPlainText(" - Kiibohd (ARM) via dfu-util (http://dfu-util.sourceforge.net/)\n")
        self.plainTextEdit.insertPlainText("And the following ISP flasher protocols:\n")
        self.plainTextEdit.insertPlainText(" - USBTiny (AVR Pocket)\n")
        self.plainTextEdit.insertPlainText(" - AVRISP (Arduino ISP)\n")
        self.plainTextEdit.insertPlainText(" - USBASP (AVR ISP)\n")

        #Add Keyboards from QMK API to the Keyboard List
        for i in keyboardlist.keyboards:
            self.keyboardFromComboBox.addItem(i)

        #Keymap doesnt work on windows
        self.keymapComboBox.addItem("default")
        
        #Add Microcontrollers
        for i in mculist.mculist:
            self.microSelectComboBox.addItem(i)

        #Connect User Selection Function to Button/Combobox
        self.openFileBtn.clicked.connect(self.browse)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QMK Toolbox"))
        self.localFileLbl.setText(_translate("MainWindow", "Local File"))
        self.microLbl.setText(_translate("MainWindow", "Microcontroller"))
        self.keyboardFromLbl.setText(_translate("MainWindow", "Keyboard from qmk.fm"))
        self.keymapLbl.setText(_translate("MainWindow", "Keymap"))
        self.flashEnabledLbl.setText(_translate("MainWindow", "Flashers Enabled"))
        self.autoFlashCheck.setText(_translate("MainWindow", "Auto-Flash"))
        self.flashBtn.setText(_translate("MainWindow", "Flash"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.openFileBtn.setText(_translate("MainWindow", "Open"))
        self.dfuCheck.setText(_translate("MainWindow", "DFU"))
        self.stm32Check.setText(_translate("MainWindow", "STM32"))
        self.halfkayCheck.setText(_translate("MainWindow", "Halfkay"))
        self.caterinaCheck.setText(_translate("MainWindow", "Caterina"))
    
    #User selects file adds to ComboBox
    def browse(self):
        localFilePath=localFilePath, _ =QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', "" , "Firmware Files (*.bin *.hex)")
        self.localFileComboBox.addItem(localFilePath)
        return(localFilePath)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
