from app.wxviews.panels import *
from wx.lib.floatcanvas.FloatCanvas import FloatCanvas
from app.wxviews.items.noderepr import NodeRepr
from app.wxviews.drawers.nodedrawer import NodeDrawer


class PaintPanel(wx.Panel):
    """Canvas to let people draw networks"""
    def __init__(self, parent):
        super(PaintPanel, self).__init__(parent=parent)
        self.network = Engine.Instance().network

        szr = wx.BoxSizer()
        self.canvas = FloatCanvas(parent=self)
        szr.Add(self.canvas, proportion=1, flag=wx.EXPAND)
        self.SetSizer(szr)

        self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.canvas.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

        # The following is called a lambda expression:
        # It allows us to define functions on-the-go.
        # It is no more than a function without definition.
        self.canvas.Bind(wx.EVT_LEFT_UP, lambda event, panel=self.canvas: self.OnLeftClick(event))
        self.canvas.Bind(wx.EVT_PAINT, self.OnWindowBack)
        self.canvas.Bind(wx.EVT_HIBERNATE)

    def OnWindowBack(self, event):
        pass

    def OnLeftClick(self, event):
        if Engine.Instance().toolbarClicked:
            dc = wx.ClientDC(self.canvas)
            if Engine.Instance().item == "Node":
                x, y = event.GetX(), event.GetY()
                frontNode = NodeRepr()
                frontNode.circle = FC.Circle(XY=(x, y), Diameter=NodeDrawer.size)
                dc.DrawCircle(frontNode.circle.XY[0], frontNode.circle.XY[1], NodeDrawer.size/2)
                Engine.Instance().releaseFocus()
                Engine.Instance().AddNode(frontNode)
