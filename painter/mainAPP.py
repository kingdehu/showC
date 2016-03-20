from PyQt4 import QtCore, QtGui
from ui_PaintOnAPanel import Ui_Dialog
from Painter import Painter
from Shapes import Shapes
from Colour3 import Colour3 

class CreateUI(QtGui.QDialog, Ui_Dialog):
    Brush = True
    DrawingShapes = Shapes()
    IsPainting = False
    IsEraseing = False

    CurrentColour = Colour3(0,0,0)
    CurrentWidth = 10
    ShapeNum = 0
    IsMouseing = False
    PaintPanel = 0
    #Constructor
    def __init__(self):
        super(QtGui.QDialog,self).__init__()
        self.setupUi(self)
        self.setObjectName('Rig Helper')
        self.PaintPanel = Painter(self)
        self.PaintPanel.close()
        self.DrawingFrame.insertWidget(0,self.PaintPanel)
        self.DrawingFrame.setCurrentWidget(self.PaintPanel)
        self.Establish_Connections()
    
    def SwitchBrush(self):
        if(self.Brush == True):
            self.Brush = False
        else:
            self.Brush = True
    
    def ChangeColour(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.CurrentColour = Colour3(col.red(),col.green(),col.blue())
   
    def ChangeThickness(self,num):
        self.CurrentWidth = num
            
    def ClearSlate(self):
        self.DrawingShapes = Shapes()
        self.PaintPanel.repaint()  
        
              
    def Establish_Connections(self):
        QtCore.QObject.connect(self.BrushErase_Button, QtCore.SIGNAL("clicked()"),self.SwitchBrush)
        QtCore.QObject.connect(self.ChangeColour_Button, QtCore.SIGNAL("clicked()"),self.ChangeColour)
        QtCore.QObject.connect(self.Clear_Button, QtCore.SIGNAL("clicked()"),self.ClearSlate)
        QtCore.QObject.connect(self.Thickness_Spinner, QtCore.SIGNAL("valueChanged(int)"),self.ChangeThickness)
        
    
#check if another instance exsists.
if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = CreateUI()
    mainWindow.show()
    sys.exit(app.exec_())