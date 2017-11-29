from app.wxViews.core.items import NetworkRepr
from app.wxViews.patterns.singleton import Singleton


@Singleton
class Engine:
    def __init__(self):
        self.toolbarClicked = False
        self.network = NetworkRepr()
        self.drawer = None
        self.item = None

    def OnRightClick(self, event):
        if self.toolbarClicked:
            self.toolbarClicked = False
            print("ok négro désolé")
            # Reinitialize drawer state
        event.Skip()

    def releaseFocus(self):
        self.toolbarClicked = False
        self.drawer = None
        self.item = None

    def AddNode(self, node):
        self.network.addNode(node)

    def RemoveNode(self, node):
        self.network.deleteNode(node)

    def UpdateNode(self, node):
        i = self.network.nodes_repr.index(node)
        self.network.updateNode(node, i)
