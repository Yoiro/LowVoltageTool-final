from app.models.network import Network
from app.wxviews.patterns.observer import Observable


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
        self.items.append(node)
        self.update_observers()

    def deleteNode(self, node):
        self.nodes_repr.remove(node)
        self.items.remove(node)
        self.update_observers()

    def updateNode(self, node, index):
        self.nodes_repr[index] = node
        self.items[self.nodes_repr.index(node)] = node
        self.update_observers()

    def addBranch(self, branch):
        self.branches_repr.append(branch)
        self.items.append(branch)
        self.update_observers()

    def deleteBranch(self, branch):
        self.branches_repr.remove(branch)
        self.items.remove(branch)
        self.update_observers()

    def updateBranch(self, branch, index):
        self.branches_repr[index] = branch
        self.items[self.branches_repr.index(branch)] = branch
        self.update_observers()
