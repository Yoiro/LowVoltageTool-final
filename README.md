# LowVoltageTool
---------------------------------------------------------------
**Low Voltage Tool** is the project I made for my Bachelor's thesis at Haute Ecole Louvain en Hainaut - Mons. This project is being built
under the watch of Electrical Engineering Service of Mons' Polytechnic Faculty (GELE). All the rights of the project are reserved to GELE.

## Overview
---------------------------------------------------------------

### Libraries

python==3.6.0
anytree==2.0.0
Kivy==1.10.0
openpyxl==2.4.4
numpy==1.13.1
scipy==0.19.1

------
### Tasks 
- [x] Build a model structure
- [x] Translate load-flow algorithm from Matlab to Python
- [x] Build a basis for implementing a Graphical User Inteface
- [ ] Finish the GUI

See more on this [Trello](https://trello.com/b/EAq94Q1x/outil-basse-tension-gui)

-----
### Model Classes
----
#### Bracket
**Bracket** corresponds to an association between a *NetworkNode* and a *NetworkBranch*
#### Network
**Network** contains the list of all *Brackets* involved in an electrical network. We will be able to navigate through it by using this class.

#### NetworkBranch
**NetworkBranch** is basically the representation of a cable, which means that it'll have a bit of attributes: *phases*, *length*, resistance *r*, reactance *x*, and a maximum amount of electricity it can handle *Imax*. This class will also allow us to calculate its own impedance by the mean of the method **calculate_impedance()**

#### NetworkNode
**NetworkNode** will be a physical spot where the network will be divided. It will possess an *identifier*, a *parent*, a list of *NetworkUser*, the *voltage_min* and the *voltage_max*.

#### NetworkUser
**NetworkUser** represents some... user... of the ...network. It is most likely a house, connected to the network by some phases and consuming some power. To simplify things, we have chosen to split the power into two attributes: *P* standing for the real part of the power and *Q* standing for its complex/imaginary part. 

#### NetworkManager
This class is a bit special. In some way it will implement the Singleton desgin pattern by inheriting of the metaclass **Singleton**. Its behaviour will be as follow: we will be able to instanciate many objects of NetworkManager, but each of them will refer to the same memory address.

#### SimulationLF
**SimulationLF** is the class in which all the magic happens. It will define our load-flow algorithm, our grid-definition (the way we will represent the network programatically) but also it will be the class that will be called if we launch the Low Voltage Tool in console mode.

---------------------------
### Graphic View Classes
----
#### MenuBar
Implements a simple Menu/Action bar with 'save', 'load', 'quit', and 'new' options.

#### LowVoltageTool
This class represent the main widget for our **LowVoltageTollApp** application.

=================================================================
### Panels

=================================================================
#### ButtonPanel
This one will conain a GridLayout with clickable buttons to enter build mode for the different network elements: 'NetworkNode', 'NetworkBranch', 'Accumulator', 'User', 'PhotoVoltaic Panel', ...

#### ElementsPanel
In this panel we will show the details of a selected element.

#### NetworkDrawPanel
This one will be our canvas. The user will be able to draw a network in this panel by adding nodes, branches, brackets, pvs, users, ...


=================================================================
### Graphic Items

=================================================================
#### NodeRepr
This class will be linked to a NetworkNode item and will also implement graphic instructions such as position in the network being drawn.

#### BranchRepr
This one will work the same way as **NodeRepr** but it will be linked to a branch.

#### NetworkRepr
This class will contain lists of all graphics items that are present into the drawing area.

-----
