from PyQt4 import QtGui,QtCore
from Point import Point

class Painter(QtGui.QWidget):
    ParentLink = 0
    MouseLoc = Point(0,0)  
    LastPos = Point(0,0)  
    def __init__(self,parent):
        super(Painter, self).__init__()
        self.ParentLink = parent
        self.MouseLoc = Point(0,0)
        self.LastPos = Point(0,0) 
    #Mouse down event
    def mousePressEvent(self, event): 
        if(self.ParentLink.Brush == True):
            self.ParentLink.IsPainting = True
            self.ParentLink.ShapeNum += 1
            self.LastPos = Point(0,0)
        else:
            self.ParentLink.IsEraseing = True      
    #Mouse Move event        
    def mouseMoveEvent(self, event):
        if(self.ParentLink.IsPainting == True):
            self.MouseLoc = Point(event.x(),event.y())
            if((self.LastPos.X != self.MouseLoc.X) and (self.LastPos.Y != self.MouseLoc.Y)):
                self.LastPos =  Point(event.x(),event.y())
                self.ParentLink.DrawingShapes.NewShape(self.LastPos,self.ParentLink.CurrentWidth,self.ParentLink.CurrentColour,self.ParentLink.ShapeNum)
            self.repaint()
        if(self.ParentLink.IsEraseing == True):
            self.MouseLoc = Point(event.x(),event.y())
            self.ParentLink.DrawingShapes.RemoveShape(self.MouseLoc,10)     
            self.repaint()        
                
    #Mose Up Event         
    def mouseReleaseEvent(self, event):
        if(self.ParentLink.IsPainting == True):
            self.ParentLink.IsPainting = False
        if(self.ParentLink.IsEraseing == True):
            self.ParentLink.IsEraseing = False  
    
    def paintEvent(self,event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawLines(event, painter)
        painter.end()
        
    def drawLines(self, event, painter):
        painter.setRenderHint(QtGui.QPainter.Antialiasing);
        
        for i in range(self.ParentLink.DrawingShapes.NumberOfShapes()-1):
            
            T = self.ParentLink.DrawingShapes.GetShape(i)
            T1 = self.ParentLink.DrawingShapes.GetShape(i+1)
        
            if(T.ShapeNumber == T1.ShapeNumber):
                pen = QtGui.QPen(QtGui.QColor(T.Colour.R,T.Colour.G,T.Colour.B), T.Width/2, QtCore.Qt.SolidLine)
                painter.setPen(pen)
                painter.drawLine(T.Location.X,T.Location.Y,T1.Location.X,T1.Location.Y)
        
#Main UI Class

