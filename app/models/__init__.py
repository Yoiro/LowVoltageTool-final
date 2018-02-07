"""
Describes how an electrical network is designed and also how we implemented it.
Modules:
========
  - bracket: Contains the class Bracket.
  - network: Contains the class Network.
  - networkbranch: Contains the class NetworkBranch.
  - networknode: Contains the class NetworkNode.
  - networkuser: Contains the class NetworkUser.
  - simulationlf: Contains the class SimulationLF. Is also the CLI entrypoint.
  - singleton: Contains the classes Singleton and NetworkManager (will be usable in a further version of the tool)
  - timestamp: Contains the enum Timestamp.
"""


from . import bracket, network, networkbranch, networknode, networkuser, simulationlf, singleton, timestamp