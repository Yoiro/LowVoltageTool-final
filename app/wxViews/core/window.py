import wx
from app.wxViews.core.panels import DetailsPanel, PaintPanel, ToolBar
from app.wxViews.core import Engine


class LowVoltageTool(wx.Frame):
    """Main Window"""
    def __init__(self, parent):
        super(LowVoltageTool, self).__init__(parent, title="Low Voltage Tool")
        # Binding models to GUI
        self.initUI()
        self.Show(True)
        self.Maximize(True)

    def initUI(self):
        # Horizontal box layout
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Creating Menu bar
        self.menu = wx.MenuBar()
        self.initMenu(self.menu)

        # Main business of the application
        # Creating Panels
        self.mainpanel = wx.Panel(self, wx.ID_ANY)
        self.toolbar = ToolBar(self.mainpanel)
        self.paint_panel = PaintPanel(self.mainpanel)
        self.details_panel = DetailsPanel(self.mainpanel)
        # Adding them to the main one
        # Add(item, size, flags)
        # Proportion lets the Sizer manage the sizes of items according to its value
        hbox.Add(self.toolbar, proportion=0.5, flag=wx.LEFT|wx.EXPAND)
        hbox.Add(self.paint_panel, proportion=2.5, flag=wx.CENTER|wx.EXPAND)
        hbox.Add(self.details_panel, proportion=1, flag=wx.RIGHT|wx.EXPAND)

        self.mainpanel.SetSizer(hbox)
        self.mainpanel.Bind(wx.EVT_RIGHT_UP, Engine.OnRightClick)
        self.SetMenuBar(self.menu)

    def OnExitApp(self, event):
        self.Destroy()

    def initMenu(self, menu):
        # Creating a Menu [File]
        file_menu = wx.Menu()
        # Creating an Option [Quit]
        quit_item = file_menu.Append(wx.ID_EXIT, "&Quit", "Leave Low Voltage Tool")
        # Binding the Event_Menu of the Quit_Item Option to the custom OnQuit() method
        menu.Bind(wx.EVT_MENU, self.OnQuit, quit_item)
        menu.Append(file_menu, "&File")

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App(0)
    frame = LowVoltageTool(None)
    app.MainLoop()
