"""Contains class Engine."""


from app.wxviews.items.networkrepr import NetworkRepr
from app.wxviews.patterns.singleton import Singleton


@Singleton
class Engine:
    """This class handles top-level information that needs to be transited between GUI items."""
    def __init__(self):
        self.toolbarClicked = False
        self.network = NetworkRepr()
        self.drawer = None
        self.item = None

    def OnRightClick(self, event):
        if self.toolbarClicked:
            self.toolbarClicked = False
            # Reinitialize drawer state
            self.drawer = None
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


if __name__ == '__main__':
    pass
