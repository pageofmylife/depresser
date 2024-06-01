# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import qdarktheme

class Ui_Depresser(object):
    def setupUi(self, Depresser):
        Depresser.setObjectName("Depresser")
        Depresser.setFixedSize(800, 600)
        Depresser.setStyleSheet("")
        self.MainWidget = QtWidgets.QWidget(parent=Depresser)
        self.MainWidget.setObjectName("MainWidget")
        self.PageObject = QtWidgets.QStackedWidget(parent=self.MainWidget)
        self.PageObject.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.PageObject.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.PageObject.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.PageObject.setObjectName("PageObject")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.DepresserLabel = QtWidgets.QLabel(parent=self.main_page)
        self.DepresserLabel.setGeometry(QtCore.QRect(10, 10, 761, 351))
        self.DepresserLabel.setStyleSheet("font: 700 72pt \"한컴 말랑말랑 Bold\";")
        self.DepresserLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DepresserLabel.setObjectName("DepresserLabel")
        self.CompressButton = QtWidgets.QPushButton(parent=self.main_page)
        self.CompressButton.setGeometry(QtCore.QRect(140, 340, 201, 91))
        self.CompressButton.setObjectName("CompressButton")
        self.ExtractButton = QtWidgets.QPushButton(parent=self.main_page)
        self.ExtractButton.setGeometry(QtCore.QRect(440, 340, 201, 91))
        self.ExtractButton.setObjectName("ExtractButton")
        self.PageObject.addWidget(self.main_page)
        self.Unzipper = QtWidgets.QWidget()
        self.Unzipper.setObjectName("Unzipper")
        self.ExtracterSettingGroup = QtWidgets.QGroupBox(parent=self.Unzipper)
        self.ExtracterSettingGroup.setGeometry(QtCore.QRect(10, 150, 761, 121))
        self.ExtracterSettingGroup.setObjectName("ExtracterSettingGroup")
        self.ExtensionComboBox = QtWidgets.QComboBox(parent=self.ExtracterSettingGroup)
        self.ExtensionComboBox.setGeometry(QtCore.QRect(50, 60, 151, 31))
        self.ExtensionComboBox.setObjectName("ExtensionComboBox")
        self.ExtensionComboBox.addItem("")
        self.ExtensionComboBox.addItem("")
        self.ExtensionComboBox.addItem("")
        self.ExtensionComboBox.addItem("")
        self.ExtensionComboBox.addItem("")
        self.ExtensionComboBox.addItem("")
        self.ExtensionComboBox.addItem("")
        self.ExtensionLabel = QtWidgets.QLabel(parent=self.ExtracterSettingGroup)
        self.ExtensionLabel.setGeometry(QtCore.QRect(50, 40, 151, 16))
        self.ExtensionLabel.setObjectName("ExtensionLabel")
        self.FilePathTextEdit = QtWidgets.QTextEdit(parent=self.ExtracterSettingGroup)
        self.FilePathTextEdit.setGeometry(QtCore.QRect(230, 60, 151, 31))
        self.FilePathTextEdit.setObjectName("FilePathTextEdit")
        self.FindZippedFileButton = QtWidgets.QPushButton(parent=self.ExtracterSettingGroup)
        self.FindZippedFileButton.setGeometry(QtCore.QRect(390, 60, 75, 31))
        self.FindZippedFileButton.setObjectName("FindZippedFileButton")
        self.PathToUnzipTextEdit = QtWidgets.QTextEdit(parent=self.ExtracterSettingGroup)
        self.PathToUnzipTextEdit.setGeometry(QtCore.QRect(480, 60, 151, 31))
        self.PathToUnzipTextEdit.setObjectName("PathToUnzipTextEdit")
        self.FindExtractToFolderButton = QtWidgets.QPushButton(parent=self.ExtracterSettingGroup)
        self.FindExtractToFolderButton.setGeometry(QtCore.QRect(640, 60, 75, 31))
        self.FindExtractToFolderButton.setObjectName("FindExtractToFolderButton")
        self.FindZippedFileLabel4 = QtWidgets.QLabel(parent=self.ExtracterSettingGroup)
        self.FindZippedFileLabel4.setGeometry(QtCore.QRect(230, 40, 231, 16))
        self.FindZippedFileLabel4.setObjectName("FindZippedFileLabel4")
        self.ExtractToLabel = QtWidgets.QLabel(parent=self.ExtracterSettingGroup)
        self.ExtractToLabel.setGeometry(QtCore.QRect(480, 40, 231, 16))
        self.ExtractToLabel.setObjectName("ExtractToLabel")
        self.ExtractLog = QtWidgets.QGroupBox(parent=self.Unzipper)
        self.ExtractLog.setGeometry(QtCore.QRect(10, 280, 761, 281))
        self.ExtractLog.setObjectName("ExtractLog")
        self.LogTextEdit = QtWidgets.QTextEdit(parent=self.ExtractLog)
        self.LogTextEdit.setGeometry(QtCore.QRect(10, 60, 741, 211))
        self.LogTextEdit.setObjectName("LogTextEdit")
        self.ProgressBar = QtWidgets.QProgressBar(parent=self.ExtractLog)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 20, 741, 31))
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ProgressBar.setTextVisible(False)
        self.ProgressBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.ProgressBar.setInvertedAppearance(False)
        self.ProgressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ExtracterStyledLabel = QtWidgets.QLabel(parent=self.Unzipper)
        self.ExtracterStyledLabel.setGeometry(QtCore.QRect(0, 0, 771, 141))
        self.ExtracterStyledLabel.setStyleSheet("font: 700 72pt \"한컴 말랑말랑 Bold\";")
        self.ExtracterStyledLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ExtracterStyledLabel.setObjectName("ExtracterStyledLabel")
        self.PageObject.addWidget(self.Unzipper)
        self.Zipper = QtWidgets.QWidget()
        self.Zipper.setObjectName("Zipper")
        self.ZipperSettingGroup = QtWidgets.QGroupBox(parent=self.Zipper)
        self.ZipperSettingGroup.setGeometry(QtCore.QRect(10, 150, 761, 181))
        self.ZipperSettingGroup.setObjectName("ZipperSettingGroup")
        self.ExtensionComboBox_2 = QtWidgets.QComboBox(parent=self.ZipperSettingGroup)
        self.ExtensionComboBox_2.setGeometry(QtCore.QRect(50, 60, 151, 51))
        self.ExtensionComboBox_2.setObjectName("ExtensionComboBox_2")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionComboBox_2.addItem("")
        self.ExtensionLabel_2 = QtWidgets.QLabel(parent=self.ZipperSettingGroup)
        self.ExtensionLabel_2.setGeometry(QtCore.QRect(50, 40, 151, 16))
        self.ExtensionLabel_2.setObjectName("ExtensionLabel_2")
        self.FilePathTextEdit_2 = QtWidgets.QTextEdit(parent=self.ZipperSettingGroup)
        self.FilePathTextEdit_2.setGeometry(QtCore.QRect(230, 60, 431, 51))
        self.FilePathTextEdit_2.setObjectName("FilePathTextEdit_2")
        self.FindFilesButton = QtWidgets.QPushButton(parent=self.ZipperSettingGroup)
        self.FindFilesButton.setGeometry(QtCore.QRect(670, 60, 75, 51))
        self.FindFilesButton.setObjectName("FindFilesButton")
        self.PathToZipTextEdit = QtWidgets.QTextEdit(parent=self.ZipperSettingGroup)
        self.PathToZipTextEdit.setGeometry(QtCore.QRect(50, 140, 611, 31))
        self.PathToZipTextEdit.setObjectName("PathToZipTextEdit")
        self.FindZipToFolderButton = QtWidgets.QPushButton(parent=self.ZipperSettingGroup)
        self.FindZipToFolderButton.setGeometry(QtCore.QRect(670, 140, 75, 31))
        self.FindZipToFolderButton.setObjectName("FindZipToFolderButton")
        self.FindFilesLabel = QtWidgets.QLabel(parent=self.ZipperSettingGroup)
        self.FindFilesLabel.setGeometry(QtCore.QRect(230, 40, 231, 16))
        self.FindFilesLabel.setObjectName("FindFilesLabel")
        self.ExtractToLabel_2 = QtWidgets.QLabel(parent=self.ZipperSettingGroup)
        self.ExtractToLabel_2.setGeometry(QtCore.QRect(50, 120, 691, 16))
        self.ExtractToLabel_2.setObjectName("ExtractToLabel_2")
        self.ExtracterStyledLabel_2 = QtWidgets.QLabel(parent=self.Zipper)
        self.ExtracterStyledLabel_2.setGeometry(QtCore.QRect(0, 0, 771, 141))
        self.ExtracterStyledLabel_2.setStyleSheet("font: 700 72pt \"한컴 말랑말랑 Bold\";")
        self.ExtracterStyledLabel_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ExtracterStyledLabel_2.setObjectName("ExtracterStyledLabel_2")
        self.ZipperLogGroup = QtWidgets.QGroupBox(parent=self.Zipper)
        self.ZipperLogGroup.setGeometry(QtCore.QRect(10, 340, 761, 221))
        self.ZipperLogGroup.setObjectName("ZipperLogGroup")
        self.ZipperLogText = QtWidgets.QTextEdit(parent=self.ZipperLogGroup)
        self.ZipperLogText.setGeometry(QtCore.QRect(10, 60, 741, 211))
        self.ZipperLogText.setObjectName("ZipperLogText")
        self.ZipProgressBar = QtWidgets.QProgressBar(parent=self.ZipperLogGroup)
        self.ZipProgressBar.setGeometry(QtCore.QRect(10, 20, 741, 31))
        self.ZipProgressBar.setProperty("value", 0)
        self.ZipProgressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ZipProgressBar.setTextVisible(False)
        self.ZipProgressBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.ZipProgressBar.setInvertedAppearance(False)
        self.ZipProgressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.ZipProgressBar.setObjectName("ZipProgressBar")
        self.PageObject.addWidget(self.Zipper)
        Depresser.setCentralWidget(self.MainWidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Depresser)
        self.statusbar.setObjectName("statusbar")
        Depresser.setStatusBar(self.statusbar)

        self.ExtractButton.clicked.connect(lambda : self.change_page(1))
        self.CompressButton.clicked.connect(lambda : self.change_page(2))

        self.retranslateUi(Depresser)
        self.PageObject.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Depresser)

    def change_page(self, pagenum) :
        self.PageObject.setCurrentIndex(pagenum)
        
    def retranslateUi(self, Depresser):
        _translate = QtCore.QCoreApplication.translate
        Depresser.setWindowTitle(_translate("Depresser", "MainWindow"))
        self.DepresserLabel.setText(_translate("Depresser", "Depresser"))
        self.CompressButton.setText(_translate("Depresser", "Zip"))
        self.ExtractButton.setText(_translate("Depresser", "Unzip"))
        self.ExtracterSettingGroup.setTitle(_translate("Depresser", "Extracter Setting"))
        self.ExtensionComboBox.setItemText(0, _translate("Depresser", "auto"))
        self.ExtensionComboBox.setItemText(1, _translate("Depresser", ".zip"))
        self.ExtensionComboBox.setItemText(2, _translate("Depresser", ".tar"))
        self.ExtensionComboBox.setItemText(3, _translate("Depresser", ".tar.gz"))
        self.ExtensionComboBox.setItemText(4, _translate("Depresser", ".tar.bz2"))
        self.ExtensionComboBox.setItemText(5, _translate("Depresser", ".rar"))
        self.ExtensionComboBox.setItemText(6, _translate("Depresser", ".7z"))
        self.ExtensionLabel.setText(_translate("Depresser", "Extension"))
        self.FilePathTextEdit.setPlaceholderText(_translate("Depresser", "Unzip file path"))
        self.FindZippedFileButton.setText(_translate("Depresser", "Find"))
        self.PathToUnzipTextEdit.setPlaceholderText(_translate("Depresser", "Path to unzip"))
        self.FindExtractToFolderButton.setText(_translate("Depresser", "Find folder"))
        self.FindZippedFileLabel4.setText(_translate("Depresser", "Find zipped file"))
        self.ExtractToLabel.setText(_translate("Depresser", "Extract to"))
        self.ExtractLog.setTitle(_translate("Depresser", "Extracter log"))
        self.ExtracterStyledLabel.setText(_translate("Depresser", "Unzipper"))
        self.ZipperSettingGroup.setTitle(_translate("Depresser", "Zipper Setting"))
        self.ExtensionComboBox_2.setItemText(0, _translate("Depresser", "auto"))
        self.ExtensionComboBox_2.setItemText(1, _translate("Depresser", ".zip"))
        self.ExtensionComboBox_2.setItemText(2, _translate("Depresser", ".tar"))
        self.ExtensionComboBox_2.setItemText(3, _translate("Depresser", ".tar.gz"))
        self.ExtensionComboBox_2.setItemText(4, _translate("Depresser", ".tar.bz2"))
        self.ExtensionComboBox_2.setItemText(5, _translate("Depresser", ".rar"))
        self.ExtensionComboBox_2.setItemText(6, _translate("Depresser", ".7z"))
        self.ExtensionLabel_2.setText(_translate("Depresser", "Extension"))
        self.FilePathTextEdit_2.setPlaceholderText(_translate("Depresser", "Unzip file path (seperated by \", \")"))
        self.FindFilesButton.setText(_translate("Depresser", "Find"))
        self.PathToZipTextEdit.setPlaceholderText(_translate("Depresser", "Path to unzip"))
        self.FindZipToFolderButton.setText(_translate("Depresser", "Find folder"))
        self.FindFilesLabel.setText(_translate("Depresser", "Find files for zip"))
        self.ExtractToLabel_2.setText(_translate("Depresser", "Zip to"))
        self.ExtracterStyledLabel_2.setText(_translate("Depresser", "Zipper"))
        self.ZipperLogGroup.setTitle(_translate("Depresser", "Zipper log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Depresser = QtWidgets.QMainWindow()
    ui = Ui_Depresser()
    ui.setupUi(Depresser)
    qdarktheme.setup_theme()
    Depresser.show()
    sys.exit(app.exec())
