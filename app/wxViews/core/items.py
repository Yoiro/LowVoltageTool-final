import wx
from app.Models.networknode import NetworkNode
from wx.lib.floatcanvas import FloatCanvas as FC
from app.Models.network import Network
from app.wxViews.patterns.observable import Observable


class NodeRepr(FC.Circle):
    """Contains GUI info and model info"""
    counter = 0
    def __init__(self, pos=(0,0), diameter=0, node: NetworkNode = NetworkNode()):
        super(NodeRepr, self).__init__(XY=pos, Diameter=diameter)
        self.backingNode = node
        self.pos = pos
        self.d = diameter
        self.id = NodeRepr.counter
        NodeRepr.counter += 1

    def draw(self, dc, WorldToPixel, ScaleWorldToPixel, HTdc=None):
        gc = wx.GraphicsContext.Create(dc)
        (XY, WH) = self.SetupDraw(gc, WorldToPixel, ScaleWorldToPixel, HTdc)

        path = gc.CreatePath()
        center = XY
        radius = WH[0] * 0.5

        path.AddCircle(center[0], center[1], radius)


class NetworkRepr(Observable):
    def __init__(self):
        super(NetworkRepr, self).__init__()
        self.network = Network()
        self.nodes_repr = []
        self.branches_repr = []
        self.users_repr = []
        self.pv_repr = []
        self.items = []

    def addNode(self, node):
        self.nodes_repr.append(node)
        self.items.extend(self.nodes_repr)

    def deleteNode(self, node):
        self.nodes_repr.remove(node)
        self.items.remove(node)

    def updateNode(self, node, index):
        self.nodes_repr[index] = node
        self.items[self.nodes_repr.index(node)] = node

    def addBranch(self, branch):
        self.branches_repr.append(branch)
        self.items.extend(self.nodes_repr)

    def deleteBranch(self, branch):
        self.branches_repr.remove(branch)
        self.items.remove(branch)

    def updateBranch(self, branch, index):
        self.branches_repr[index] = branch
        self.items[self.branches_repr.index(branch)] = branch
