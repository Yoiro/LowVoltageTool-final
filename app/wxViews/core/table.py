from app.wxViews.patterns.observer import Observer
from app.wxViews.core.engine import Engine
from wx.grid import Grid
import wx


class TabbedGrid(Observer):
    def __init__(self, parent):
        super(TabbedGrid, self).__init__()
        # Register as an observer of Top level network
        Engine.Instance().network.register(self)
        self.parent = parent
        self.notebook = wx.Notebook(parent, id=wx.ID_ANY)
        # Initialize Tabs
        self.tab1 = InputGrid(self.notebook)
        self.tab2 = OutputGrid(self.notebook)

        self.init_GUI()
        self.bind_events()

    def init_GUI(self):
        # Add Tabs to the Tabbed Panel
        self.notebook.AddPage(self.tab1.grid, "Input")
        self.notebook.AddPage(self.tab2.grid, "Output")

    def bind_events(self):
        # Binding events
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
        self.notebook.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

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
        cells = [item for item in self.network.items]
        # Update, Add, Fill cells here

    def GetValue(self, row, col):
        return str(self.network.item[row][col])


class InputGrid(Observer):
    def __init__(self, parent):
        super(InputGrid, self).__init__()
        self.grid = wx.grid.Grid(parent=parent, id=wx.ID_ANY, name="Input")
        Engine.Instance().network.register(self)
        self.init_GUI()
        self.bind_events()

    def init_GUI(self):
        self.grid.CreateGrid(len(Engine.Instance().network.items), 5)

    def bind_events(self):
        self.grid.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)


class OutputGrid(Observer):
    def __init__(self, parent):
        super(OutputGrid, self).__init__()
        Engine.Instance().network.register(self)
        self.grid = wx.grid.Grid(parent=parent, id=wx.ID_ANY, name="Input")
        self.init_GUI()

    def init_GUI(self):
        self.grid.CreateGrid(len(Engine.Instance().network.items), 5)

    def bind_events(self):
        self.grid.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
