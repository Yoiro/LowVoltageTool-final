import wx
from app.wxViews.core.items import NetworkRepr
from app.wxViews.patterns.singleton import Singleton


@Singleton
class Engine:
    def __init__(self):
        self.toolbarClicked = False
        self.network = NetworkRepr()
        self.drawer = None
        self.item = None

    def OnRightClick(event):
        if Engine.toolbarClicked:
            Engine.toolbarClicked = False
            print("ok négro désolé")
            # Reinitialize drawer state
        event.Skip()

    def releaseFocus():
        Engine.toolbarClicked = False
        Engine.drawer = None
        Engine.item = None

    def AddNode(node):
        Engine.network.addNode(node)

    def RemoveNode(node):
        Engine.network.deleteNode(node)

    def UpdateNode(node):
        i = Engine.network.nodes_repr.index(node)
        Engine.network.updateNode(node, i)
