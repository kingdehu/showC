from PyQt4 import QtCore, QtGui

from RenderArea import RenderArea
from ui_mainWindows import Ui_mainWindows

class mainAPP(QtGui.QWidget, Ui_mainWindows):
    
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.setupUi(self)
        self.mRenderArea = RenderArea(self)
        self.mRenderArea.close()
        self.DrawFrame.insertWidget(0,self.mRenderArea)
        self.DrawFrame.setCurrentWidget(self.mRenderArea)
        print self.mRenderArea.getContentsMargins()
        text = QtGui.QPainterPath()
        font = QtGui.QFont()
        font.setPixelSize(180)
        fontBoundingRect = QtGui.QFontMetrics(font).boundingRect("C")
        text.addText(-QtCore.QPointF(fontBoundingRect.center()), font, "C")
        self.mRenderArea.setShape(text)
        QtCore.QObject.connect(self.pb_UR, QtCore.SIGNAL("clicked()"),self.testclick)
        
    def testclick(self):
        print "eeee"
        
        
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = mainAPP()
    window.show()
    sys.exit(app.exec_())
        