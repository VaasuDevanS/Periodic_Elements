PeriodicElements
****************

A python API/console script for the periodic table elements. 

Created by Vaasu Devan S <vaasuceg.96@gmail.com>

Github Url https://www.github.com/VaasuDevanS

Installation
************

>>> pip install periodicelements

Basic Usage
************
Getting the Values
=============================================

for Python 3.X Series,

>>> from elements import elements

for Python2.X Series,

>>> import elements


>>> elements.H
<Hydrogen Element>
>>> elements.hydrogen.AtomicMass
'1.00794 amu'

show() method
=============================================

>>> elements.H.show()
Name: Hydrogen
Symbol: H
AtomicNumber: 1
AtomicMass: 1.00794 amu
MeltingPoint: {'Farenheit': -434.45203, 'Celsius': -259.14, 'Kelvin': 14.009985}
BoilingPoint: {'Farenheit': -423.166, 'Celsius': -252.87, 'Kelvin': 20.280005}
Protons_Electrons: 1
Neutrons: 0
Classification: Non-Metal
CrystalStructure: Hexagonal
Density: 0.08988 g/cm3 (@293k)
Color: colorless
Discovery: {'NameOrigin': 'From Greek words hudor (water) & gennan (generate)', 'Discoverer': 'Henry Cavendish', 'Year': '1766'}
Uses: Balloons & Metal Refining
ObtainedFrom: mines, oil, gas wells

get() method
=======================================================

>>> data=elements.H.get()     #or elements.hydrogen.get()
>>> print data
{'BoilingPoint': {'Farenheit': -423.166, 'Celsius': -252.87, 'Kelvin': 20.280005}, 'Name': 'Hydrogen', 'Density': '0.08988 g/cm3 (@293k)', 'CrystalStructure': 'Hexagonal', 'AtomicMass': '1.00794 amu', 'Discovery': {'NameOrigin': 'From Greek words hudor (water) & gennan (generate)', 'Discoverer': 'Henry Cavendish', 'Year': '1766'}, 'MeltingPoint': {'Farenheit': -434.45203, 'Celsius': -259.14, 'Kelvin': 14.009985}, 'ObtainedFrom': 'mines, oil, gas wells', 'Classification': 'Non-Metal', 'Color': 'colorless', 'Symbol': 'H', 'AtomicNumber': 1, 'Protons_Electrons': '1', 'Uses': 'Balloons & Metal Refining', 'Neutrons': '0'}

compare() method
****************
>>> elements.compare(elements.Au,elements.He)
=====================================================
Property          | Gold                Helium
#####################################################
Symbol            | Au                  He
AtomicNumber      | 79                  2
AtomicMass        | 196.96655 amu       4.002602 amu
Classification    | Transition Metal    Noble Gas
CrystalStructure  | Cubic               Hexagonal
Density           | 19.32 g/cm3         0.1785 g/cm3
Color             | Gold                colorless
=====================================================

Element types
*************
[Alkali_Metals, Alkaline_Earth_Metals, Halogens, Metalloids, Rare_Earth_Elements, Rare_Gases, Noble_Gases, Transition_Metals, Non_Metals, Others]


>>> elements.Alkali_Metals
[<Cesium Element>, <Francium Element>, <Lithium Element>, <Potassium Element>, <Rubidium Element>, <Sodium Element>]


keys
****

Find for any element from the keys ['AtomicMass', 'AtomicNumber', 'BoilingPoint', 'Classification', 'Color', 'CrystalStructure', 'Density', 'Discovery', 'MeltingPoint', 'Name', 'Neutrons', 'ObtainedFrom', 'Protons_Electrons', 'Symbol', 'Uses']

>>> elements.Au.Discovery
{'NameOrigin': 'From the Old English word geolo (yellow)', 'Discoverer': 'Unknown', 'Year': 'circa3000BC'}
>>> print elements.Si.MeltingPoint
{'Farenheit': 2570.0, 'Celsius': 1410.0, 'Kelvin': 1683.15}

Periodic table
================
>>> print elements.Table  # print(elements.Table)
  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  -------------
              -------------------------------------------------------------
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------
