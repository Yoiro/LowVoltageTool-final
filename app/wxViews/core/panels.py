from wx.lib.floatcanvas.FloatCanvas import FloatCanvas
from app.wxViews.core import Engine
from app.wxViews.core.items import *
from app.wxViews.core.drawers import NodeDrawer
from app.wxViews.core.table import TabbedGrid



class ToolBar(wx.Panel):
    """Tool Bar with buttons for drawing"""
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent=parent)
        layout = wx.GridSizer(rows=5, cols=1, gap=(parent.GetSize()[0]/50, parent.GetSize()[1]/50))
        # Node, Branch, Bracket, User, PV
        self.node_btn = wx.Button(self, id=wx.ID_ANY, label="Node", name="node")
        self.branch_btn = wx.Button(self, id=wx.ID_ANY, label="Branch", name="branch")
        self.user_btn = wx.Button(self, id=wx.ID_ANY, label="User", name="user")
        self.pv_btn = wx.Button(self, id=wx.ID_ANY, label="PV", name="pv")
        self.eraser_btn = wx.Button(self, id=wx.ID_ANY, label="Eraser", name="eraser")

        self.bindEvents()

        self.add = layout.Add(self.node_btn, flag=wx.EXPAND)
        layout.Add(self.branch_btn, flag=wx.EXPAND)
        layout.Add(self.user_btn, flag=wx.EXPAND)
        layout.Add(self.pv_btn, flag=wx.EXPAND)
        layout.Add(self.eraser_btn, flag=wx.EXPAND)

        self.SetSizer(layout)
        self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

    def bindEvents(self):
        # Event binding
        self.node_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.node_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.branch_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.branch_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.user_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.user_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.pv_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.pv_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.eraser_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.eraser_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

    def OnButtonClicked(self, event):
        source = event.GetEventObject()
        if not Engine.Instance().toolbarClicked:
            Engine.Instance().toolbarClicked = True
            if source.GetName() == "node":
                # Initialize Drawer state
                Engine.Instance().drawer = NodeDrawer()
                Engine.Instance().item = "Node"
            elif source.GetName() == "branch":
                # Initialize Drawer state
                pass
            elif source.GetName() == "user":
                # Initialize Drawer state
                pass
            elif source.GetName() == "pv":
                # Initialize Drawer stavte
                pass
            else:
                # Initialize Drawer state
                pass
        event.Skip()


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


class DetailsPanel(wx.Panel):
    """Show network elements and their values"""
    def __init__(self, parent):
        super(DetailsPanel, self).__init__(parent=parent)
        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.initGUI()

    def initGUI(self):
        # Vertical Box Layout
        # Tabbed Panel
        notebook = TabbedGrid(self)
        # Add the button to launch the load flow
        loadflow_btn = wx.Button(self, id=wx.ID_ANY, label="Launch a Load Flow")
        # set layouts
        low_szr = wx.BoxSizer(orient=wx.HORIZONTAL)
        low_szr.Add(loadflow_btn, 1, flag=wx.EXPAND)
        self.sizer.Add(notebook.notebook, proportion=4.5, flag=wx.TOP|wx.EXPAND)
        self.sizer.Add(low_szr, proportion=0.5, flag=wx.BOTTOM)
        self.SetSizerAndFit(self.sizer)

        self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
