from PyQt4 import QtCore, QtGui

NoTransformation, Translate, Rotate, Scale = range(4)
class RenderArea(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RenderArea, self).__init__(parent)
        
        newFont = self.font()
        newFont.setPixelSize(12)
        self.setFont(newFont)

        fontMetrics = QtGui.QFontMetrics(newFont)
        self.xBoundingRect = fontMetrics.boundingRect("x")
        self.yBoundingRect = fontMetrics.boundingRect("y")
        self.shape = QtGui.QPainterPath()
        self.operations = []

    def setOperations(self, operations):
        self.operations = operations
        self.update()

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def minimumSizeHint(self):
        return QtCore.QSize(182, 182)

    def sizeHint(self):
        return QtCore.QSize(232, 232)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(event.rect(), QtGui.QBrush(QtCore.Qt.white))

        painter.translate(200, 200)

        painter.save()
        self.transformPainter(painter)
        self.drawShape(painter)
        painter.restore()

        #self.drawOutline(painter)

        self.transformPainter(painter)
        #self.drawCoordinates(painter)

    def drawShape(self, painter):
        painter.fillPath(self.shape, QtCore.Qt.blue)

    def transformPainter(self, painter):
        for operation in self.operations:
            if operation == Translate:
                painter.translate(50, 50)

            elif operation == Scale:
                painter.scale(0.75, 0.75)

            elif operation == Rotate:
                painter.rotate(60)

