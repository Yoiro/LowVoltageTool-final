from wx.grid import Grid
from wx.lib.floatcanvas.FloatCanvas import FloatCanvas
from app.wxViews.core import Engine
from app.wxViews.core.items import *
from app.wxViews.core.drawers import NodeDrawer
from app.wxViews.patterns.observer import Observer


class ToolBar(wx.Panel):
    """Tool Bar with buttons for drawing"""
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent=parent)
        layout = wx.GridSizer(rows=5, cols=1, gap=(parent.GetSize()[0]/50, parent.GetSize()[1]/50))
        # Node, Branch, Bracket, User, PV
        self.node_btn = wx.Button(self, id=wx.ID_ANY, label="Node")
        self.branch_btn = wx.Button(self, id=wx.ID_ANY, label="Branch")
        self.user_btn = wx.Button(self, id=wx.ID_ANY, label="User")
        self.pv_btn = wx.Button(self, id=wx.ID_ANY, label="PV")
        self.eraser_btn = wx.Button(self, id=wx.ID_ANY, label="Eraser")

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
            if source.GetLabel() == "Node":
                # Initialize Drawer state
                print("build node enabled")
                Engine.Instance().drawer = NodeDrawer()
                Engine.Instance().item = "Node"
            elif source.GetLabel() == "Branch":
                # Initialize Drawer state
                print("Imma draw a Branch :D")
            elif source.GetLabel() == "User":
                # Initialize Drawer state
                print("Imma put a User huehuehue")
            elif source.GetLabel() == "PV":
                # Initialize Drawer state
                print("PRAISE THE SUN YOU MOFO")
            else:
                # Initialize Drawer state
                print("IMMA ERASE YOU AND NO ONE WILL KNOW YOU EVER EXISTED HUEHUEHUARHUEHAUHRUAE")
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
        self.initGUI()

    def initGUI(self):
        # Vertical Box Layout
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        # Tabbed Panel
        notebook = TabbedGrid(self)
        # Add the button to launch the load flow
        loadflow_btn = wx.Button(self, id=wx.ID_ANY, label="Launch a Load Flow")
        # set layouts
        low_szr = wx.BoxSizer(orient=wx.HORIZONTAL)
        low_szr.Add(loadflow_btn, 1, flag=wx.EXPAND)
        sizer.Add(notebook.notebook, proportion=4.5, flag=wx.TOP|wx.EXPAND)
        sizer.Add(low_szr, proportion=0.5, flag=wx.BOTTOM)
        self.SetSizerAndFit(sizer)

        self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)


class TabbedGrid(Observer):
    def __init__(self, parent):
        super(TabbedGrid, self).__init__()
        # Get Top level network
        self.network = Engine.Instance().network
        Engine.Instance().network.register(self)
        self.notebook = wx.Notebook(parent, id=wx.ID_ANY)
        # Initialize Tabs
        self.tab1 = wx.grid.Grid(self.notebook, id=wx.ID_ANY, name="IN")
        self.tab1.CreateGrid(len(self.network.items), 5)
        self.tab1.ShowScrollbars(wx.SHOW_SB_DEFAULT, wx.SHOW_SB_DEFAULT)
        self.tab2 = wx.grid.Grid(self.notebook, id=wx.ID_ANY, name="OUT")
        self.tab2.CreateGrid(len(self.network.items), 5)
        self.tab2.ShowScrollbars(wx.SHOW_SB_DEFAULT, wx.SHOW_SB_DEFAULT)
        # Add Tabs to the Tabbed Panel
        self.notebook.AddPage(self.tab1, "IN")
        self.notebook.AddPage(self.tab2, "OUT")
        # Binding events
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

        self.notebook.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.tab1.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.tab2.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.notebook.GetSelection()
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.notebook.GetSelection()
        event.Skip()

    def update(self, *args, **kwargs):
        self.network = Engine.Instance().network
        for item in self.network.items:
            print(item)
        print("Network updated!")

    def GetValue(self, row, col):
        return str(self.network.item[row][col])

