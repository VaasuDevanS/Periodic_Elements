
# Source Code for elements Module
'''
Developer: VaasuDevanS
           www.github.com/VaasuDevanS (VaasuDevanS.github.io)
           vaasuceg.96@gmail.com
'''

from __future__ import print_function


about={'Version':'1.0','Developer':'VaasuDevan S','Email':'vaasuceg.96@gmail.com','url':'https://www.github.com/VaasuDevanS/periodic_elements','License':'GPL License'}

__version__='1.0'
__developer__="VaasuDevan S"
__email__="vaasuceg.96@gmail.com"
__url__="www.github.com/VaasuDevanS/periodic_elements"
__license__="GPL license"

class Elements:
    
    def __init__(self,Name,Symbol,AtomicNumber,AtomicMass,MeltingPoint,BoilingPoint,Protons_Electrons,Neutrons,Classification,CrystalStructure,Density,Color,Discovery,Uses,ObtainedFrom):
        
        self.Symbol=Symbol
        self.Name=Name
        self.AtomicNumber=int(AtomicNumber)
        self.AtomicMass=AtomicMass
        self.MeltingPoint=MeltingPoint
        self.BoilingPoint=BoilingPoint
        self.Classification=Classification
        self.CrystalStructure=CrystalStructure
        self.Density=Density
        self.Color=Color
        self.Discovery=Discovery
        self.Uses=Uses
        self.ObtainedFrom=ObtainedFrom
        self.Protons_Electrons=Protons_Electrons
        self.Neutrons=Neutrons
    
    def show(self):
                        
        print("Name: "+self.Name)
        print("Symbol: "+self.Symbol)
        print("AtomicNumber: "+str(self.AtomicNumber))
        print("AtomicMass: "+self.AtomicMass)
        print("MeltingPoint: "+str(self.MeltingPoint))
        print("BoilingPoint: "+str(self.BoilingPoint))
        print("Protons_Electrons: "+str(self.Protons_Electrons))
        print("Neutrons: "+str(self.Neutrons))
        print("Classification: "+self.Classification)
        print("CrystalStructure: "+self.CrystalStructure)
        print("Density: "+self.Density)
        print("Color: "+self.Color)
        print("Discovery: "+str(self.Discovery))
        print("Uses: "+self.Uses)
        print("ObtainedFrom: "+self.ObtainedFrom)
        
        
    def get(self):
        
        return {'Name':self.Name,'Symbol':self.Symbol,'AtomicNumber':self.AtomicNumber,'AtomicMass':self.AtomicMass,'MeltingPoint':self.MeltingPoint,'BoilingPoint':self.BoilingPoint,'Protons_Electrons':self.Protons_Electrons,'Neutrons':self.Neutrons,'Classification':self.Classification,'CrystalStructure':self.CrystalStructure,'Density':self.Density,'Color':self.Color,'Discovery':self.Discovery,'Uses':self.Uses,'ObtainedFrom':self.ObtainedFrom}
        
    
    def __repr__(self):
        
        return str("<"+self.Name+" Element>")
    

AllSymbols=['Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B', 'Ba', 'Be', 'Bh', 'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Co', 'Cr', 'Cs', 'Cu', 'Db', 'Dy', 'Er', 'Es', 'Eu', 'F', 'Fe', 'Fm', 'Fr', 'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'Hs', 'I', 'In', 'Ir', 'K', 'Kr', 'La', 'Li', 'Lr', 'Lu', 'Md', 'Mg', 'Mn', 'Mo', 'Mt', 'N', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'No', 'Np', 'O', 'Os', 'P', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re', 'Rf', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se', 'Sg', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm', 'U', 'Uub', 'Uun', 'Uuu', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr']

AllElements=['actinium', 'aluminum', 'americium', 'antimony', 'argon', 'arsenic', 'astatine', 'barium', 'berkelium', 'beryllium', 'bismuth', 'bohrium', 'boron', 'bromine', 'cadmium', 'calcium', 'californium', 'carbon', 'cerium', 'cesium', 'chlorine', 'chromium', 'cobalt', 'copper', 'curium', 'dubnium', 'dysprosium', 'einsteinium', 'erbium', 'europium', 'fermium', 'fluorine', 'francium', 'gadolinium', 'gallium', 'germanium', 'gold', 'hafnium', 'hassium', 'helium', 'holmium', 'hydrogen', 'indium', 'iodine', 'iridium', 'iron', 'krypton', 'lanthanum', 'lawrencium', 'lead', 'lithium', 'lutetium', 'magnesium', 'manganese', 'meitnerium', 'mendelevium', 'mercury', 'molybdenum', 'neodymium', 'neon', 'neptunium', 'nickel', 'niobium', 'nitrogen', 'nobelium', 'osmium', 'oxygen', 'palladium', 'phosphorus', 'platinum', 'plutonium', 'polonium', 'potassium', 'praseodymium', 'promethium', 'protactinium', 'radium', 'radon', 'rhenium', 'rhodium', 'rubidium', 'ruthenium', 'rutherfordium', 'samarium', 'scandium', 'seaborgium', 'selenium', 'silicon', 'silver', 'sodium', 'strontium', 'sulfur', 'tantalum', 'technetium', 'tellurium', 'terbium', 'thallium', 'thorium', 'thulium', 'tin', 'titanium', 'tungsten', 'ununbium', 'ununnilium', 'unununium', 'uranium', 'vanadium', 'xenon', 'ytterbium', 'yttrium', 'zinc', 'zirconium']


hydrogen=Elements(
'Hydrogen',
'H',
'1',
'1.00794 amu',
{'Celsius':-259.14,'Farenheit':-434.45203,'Kelvin':14.009985},
{'Celsius':-252.87,'Farenheit':-423.166,'Kelvin':20.280005},
'1',
'0',
'Non-Metal',
'Hexagonal',
'0.08988 g/cm3 (@293k)',
'colorless',
{'Year':'1766','Discoverer':'Henry Cavendish','NameOrigin':'From Greek words hudor (water) & gennan (generate)'},
'Balloons & Metal Refining',
'mines, oil, gas wells'
)    


boron=Elements(
'Boron',
'B',
'5',
'10.811 amu',
{'Celsius':2300.0,'Farenheit':4172.0,'Kelvin':2573.15},
{'Celsius':2550.0,'Farenheit':4622.0,'Kelvin':2823.15},
'5',
'6',
'Metalloid',
'Rhombohedral',
'2.34 g/cm3',
'brownish',
{'Year':'1808','Discoverer':'Sir Humphry Davy, J.L Gay-Lussac','NameOrigin':'From borax and carbon'},
'heat resistant alloys',
'kernite'
)


carbon=Elements(
'Carbon',
'C',
'6',
'12.0107 amu',
{'Celsius':3500.0,'Farenheit':6332.0,'Kelvin':3773.15},
{'Celsius':4827.0,'Farenheit':8720.6,'Kelvin':5100.15},
'6',
'6',
'Non-metal',
'Hexagonal',
'2.62 g/cm3',
'May be black',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Latin carbo (coal)'},
'steel, filters',
'burning with insufficient oxygen'
)

helium=Elements(
'Helium',
'He',
'2',
'4.002602 amu',
{'Celsius':-272.0,'Farenheit':-457.6,'Kelvin':1.15},
{'Celsius':-268.6,'Farenheit':-451.48,'Kelvin':4.549994},
'2',
'2',
'Noble Gas',
'Hexagonal',
'0.1785 g/cm3',
'colorless',
{'Year':'1895','Discoverer':'Sir William Ramsay','NameOrigin':'From the Greek word hlios (sun)'},
'balloons, deep sea diving',
'natural gas deposit, air'
)


lithium=Elements(
'Lithium',
'Li',
'3',
'6.941 amu',
{'Celsius':180.54,'Farenheit':356.972,'Kelvin':453.69},
{'Celsius':1347.0,'Farenheit':2456.6,'Kelvin':1620.15},
'3',
'4',
'Alkali Metal',
'Cubic',
'0.53 g/cm3',
'silvery',
{'Year':'1817','Discoverer':'Johann Arfvedson','NameOrigin':'From the Greek word lithos (stone)'},
'batteries, ceramics, lubricants',
'passing electric charge through melted lithium chloride, spodumene'
)


beryllium=Elements(
'Beryllium',
'Be',
'4',
'9.012182 amu',
{'Celsius':1278.0,'Farenheit':2332.4,'Kelvin':1551.15},
{'Celsius':2970.0,'Farenheit':5378.0,'Kelvin':3243.15},
'4',
'5',
'Alkaline Earth',
'Hexagonal',
'1.8477 g/cm3',
'gray',
{'Year':'1798','Discoverer':'Fredrich Wohler','NameOrigin':'From the mineral beryl'},
'spacecraft, missiles, aircraft',
'beryl, chrysoberyl'
)


nitrogen=Elements(
'Nitrogen',
'N',
'7',
'14.00674 amu',
{'Celsius':-209.9,'Farenheit':-345.81998,'Kelvin':63.250008},
{'Celsius':-195.8,'Farenheit':-320.44,'Kelvin':77.35},
'7',
'7',
'Non-metal',
'Hexagonal',
'1.2506 g/cm3',
'colorless',
{'Year':'1772','Discoverer':'Daniel Rutherford','NameOrigin':'Greek'},
'forms most of atmosphere',
'from liquid air'
)


oxygen=Elements(
'Oxygen',
'O',
'8',
'15.9994 amu',
{'Celsius':-218.4,'Farenheit':-361.12,'Kelvin':54.750008},
{'Celsius':-183.0,'Farenheit':-297.4,'Kelvin':90.15},
'8',
'8',
'Non-metal',
'Cubic',
'1.429 g/cm3',
'colorless',
{'Year':'1774','Discoverer':'Joseph Priestly','NameOrigin':'From the Greek words oxus (acid) and gennan (generate)'},
'supports life',
'from liquid air'
)


fluorine=Elements(
'Fluorine',
'F',
'9',
'18.998404 amu',
{'Celsius':-219.62,'Farenheit':-363.31598,'Kelvin':53.530006},
{'Celsius':-188.14,'Farenheit':-306.652,'Kelvin':85.01},
'9',
'10',
'Halogen',
'Cubic',
'1.696 g/cm3',
'Greenish',
{'Year':'1886','Discoverer':'Joseph Henri Moissan','NameOrigin':'From the Latin word fluo (flow)'},
'Refrigerants',
'mineral fluorite'
)


neon=Elements(
'Neon',
'Ne',
'10',
'20.1797 amu',
{'Celsius':-248.6,'Farenheit':-415.48,'Kelvin':24.549994},
{'Celsius':-246.1,'Farenheit':-410.98,'Kelvin':27.049994},
'10',
'10',
'Noble Gas',
'Cubic',
'0.901 g/cm3',
'colorless',
{'Year':'1898','Discoverer':'Sir William Ramsay','NameOrigin':'Form the Greek word neos (new)'},
'lighting',
'liquid air'
)


sodium=Elements(
'Sodium',
'Na',
'11',
'22.98977 amu',
{'Celsius':97.72,'Farenheit':207.9,'Kelvin':370.87},
{'Celsius':883,'Farenheit':1621,'Kelvin':1156},
'11',
'12',
'Alkali Metal',
'Cubic',
'0.971 g/cm3',
'silvery',
{'Year':'1807','Discoverer':'Sir Humphrey Davy','NameOrigin':'soda (Na2CO3)'},
'medicine, agriculture',
'table salts and other foods'
)


magnesium=Elements(
'Magnesium',
'Mg',
'12',
'24.305 amu',
{'Celsius':650.0,'Farenheit':1202.0,'Kelvin':923.15},
{'Celsius':1107.0,'Farenheit':2024.6,'Kelvin':1380.15},
'12',
'12',
'Alkaline Earth',
'Hexagonal',
'1.738 g/cm3',
'grayish',
{'Year':'1808','Discoverer':'Sir Humphrey Davy','NameOrigin':'Magnesia (City)'},
'airplanes, missiles',
'sea water'
)


aluminum=Elements(
'Aluminum',
'Al',
'13',
'26.981539 amu',
{'Celsius':660.37,'Farenheit':1220.666,'Kelvin':933.52},
{'Celsius':2467.0,'Farenheit':4472.6,'Kelvin':2740.15},
'13',
'14',
'Other Metals',
'Cubic',
'2.702 g/cm3',
'Silver',
{'Year':'1825','Discoverer':'Hans Christian Oersted','NameOrigin':'From the Latin word alumen'},
'airplanes, soda cans',
'bauxite'
)


silicon=Elements(
'Silicon',
'Si',
'14',
'28.0855 amu',
{'Celsius':1410.0,'Farenheit':2570.0,'Kelvin':1683.15},
{'Celsius':2355.0,'Farenheit':4271.0,'Kelvin':2628.15},
'14',
'14',
'Metalloid',
'Cubic',
'2.329 g/cm3',
'grey',
{'Year':'1823','Discoverer':'Jons Berzelius','NameOrigin':'From the Latin word silex (flint)'},
'glass, semiconductors',
'Second most abundant element.  Found in clay, granite, quartz, sand'
)


phosphorus=Elements(
'Phosphorus',
'P',
'15',
'30.97376 amu',
{'Celsius':44.1,'Farenheit':111.38,'Kelvin':317.25},
{'Celsius':280.0,'Farenheit':536.0,'Kelvin':553.15},
'15',
'16',
'Non-metal',
'Monoclinic',
'1.82 g/cm3',
'white',
{'Year':'1669','Discoverer':'Hennig Brand','NameOrigin':'From the Greek words phs (light) and phoros (bearer)'},
'fertilizers, detergents',
'phosphate rock'
)


sulfur=Elements(
'Sulfur',
'S',
'16',
'32.066 amu',
{'Celsius':112.8,'Farenheit':235.04001,'Kelvin':385.95},
{'Celsius':444.6,'Farenheit':832.28,'Kelvin':717.75},
'16',
'16',
'Non-metal',
'Orthorhombic',
'2.07 g/cm3',
'yellow',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Latin word sulfur (brimstone)'},
'matches, gunpowder, medicines',
'naturally'
)


chlorine=Elements(
'Chlorine',
'Cl',
'17',
'35.4527 amu',
{'Celsius':-100.98,'Farenheit':-149.764,'Kelvin':172.17},
{'Celsius':-34.6,'Farenheit':-30.279997,'Kelvin':238.55},
'17',
'18',
'Halogen',
'Orthorhombic',
'3.214 g/cm3',
'green',
{'Year':'1774','Discoverer':'Carl Wilhelm Scheele','NameOrigin':'From the Greek word khlros (green)'},
'Water purification, bleaches',
'Salt'
)


argon=Elements(
'Argon',
'Ar',
'18',
'39.948 amu',
{'Celsius':-189.3,'Farenheit':-308.74,'Kelvin':83.85},
{'Celsius':-186.0,'Farenheit':-302.8,'Kelvin':87.15},
'18',
'22',
'Noble Gas',
'Cubic',
'1.784 g/cm3',
'Colorless Gas',
{'Year':'1894','Discoverer':'Sir William Ramsay','NameOrigin':'From the Greek word argon (inactive)'},
'Lighting',
'air'
)


potassium=Elements(
'Potassium',
'K',
'19',
'39.0983 amu',
{'Celsius':63.65,'Farenheit':146.57,'Kelvin':336.8},
{'Celsius':774.0,'Farenheit':1425.2,'Kelvin':1047.15},
'19',
'20',
'Alkali Metal',
'Cubic',
'0.862 g/cm3',
'silvery',
{'Year':'1807','Discoverer':'Sir Humphrey Davy','NameOrigin':'potash'},
'glass, soap',
'minerals (carnallite)'
)


calcium=Elements(
'Calcium',
'Ca',
'20',
'40.078 amu',
{'Celsius':839.0,'Farenheit':1542.2,'Kelvin':1112.15},
{'Celsius':1484.0,'Farenheit':2703.2,'Kelvin':1757.15},
'20',
'20',
'Alkaline Earth',
'Cubic',
'1.55 g/cm3',
'Silvery',
{'Year':'1808','Discoverer':'Sir Humphrey Davy','NameOrigin':'From the latin word calcis (lime)'},
'life forms for bones and shells',
'chalk, limestone, marble.  3.5% of crust'
)


scandium=Elements(
'Scandium',
'Sc',
'21',
'44.95591 amu',
{'Celsius':1539.0,'Farenheit':2802.2,'Kelvin':1812.15},
{'Celsius':2832.0,'Farenheit':5129.6,'Kelvin':3105.15},
'21',
'24',
'Transition Metal',
'Hexagonal',
'2.989 g/cm3',
'silvery',
{'Year':'1879','Discoverer':'Lars Nilson','NameOrigin':'From Scandinavia'},
'No uses known',
'minerals (thortveitile, wiikite)'
)


titanium=Elements(
'Titanium',
'Ti',
'22',
'47.867 amu',
{'Celsius':1660.0,'Farenheit':3020.0,'Kelvin':1933.15},
{'Celsius':3287.0,'Farenheit':5948.6,'Kelvin':3560.15},
'22',
'26',
'Transition Metal',
'Hexagonal',
'4.54 g/cm3',
'silverish',
{'Year':'1791','Discoverer':'William Gregor','NameOrigin':'From the Greek word titanos (Titans)'},
'paint, rubber, paper',
'minerals (ilmenite, rutile)'
)


vanadium=Elements(
'Vanadium',
'V',
'23',
'50.9415 amu',
{'Celsius':1890.0,'Farenheit':3434.0,'Kelvin':2163.15},
{'Celsius':3380.0,'Farenheit':6116.0,'Kelvin':3653.15},
'23',
'28',
'Transition Metal',
'Cubic',
'5.8 g/cm3',
'Silverish',
{'Year':'1830','Discoverer':'Nils Sefstrom','NameOrigin':'After Vanadis (Scandinavian goddess)'},
'catalyst, dye, color-fixer',
'minerals (patronite, vanadinite)'
)


chromium=Elements(
'Chromium',
'Cr',
'24',
'51.9961 amu',
{'Celsius':1857.0,'Farenheit':3374.6,'Kelvin':2130.15},
{'Celsius':2672.0,'Farenheit':4841.6,'Kelvin':2945.15},
'24',
'28',
'Transition Metal',
'Cubic',
'7.19 g/cm3',
'gray',
{'Year':'1797','Discoverer':'Louis Vauquelin','NameOrigin':'From the Greek word chrma (color)'},
'Stainless steel',
'Chromite'
)


manganese=Elements(
'Manganese',
'Mn',
'25',
'54.93805 amu',
{'Celsius':1245.0,'Farenheit':2273.0,'Kelvin':1518.15},
{'Celsius':1962.0,'Farenheit':3563.6,'Kelvin':2235.15},
'25',
'30',
'Transition Metal',
'Cubic',
'7.43 g/cm3',
'silverish/grayish',
{'Year':'1774','Discoverer':'Johann Gahn','NameOrigin':'From the Latin word mangnes (magnet)'},
'steel, batteries, ceramics',
'pyrolusite, psilomelane, rhodochrosite'
)


iron=Elements(
'Iron',
'Fe',
'26',
'55.845 amu',
{'Celsius':1535.0,'Farenheit':2795.0,'Kelvin':1808.15},
{'Celsius':2750.0,'Farenheit':4982.0,'Kelvin':3023.15},
'26',
'30',
'Transition Metal',
'Cubic',
'7.86 g/cm3',
'Silvery',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'Latin'},
'steel, hemoglobin (carries oxygen in blood)',
'iron ores'
)


cobalt=Elements(
'Cobalt',
'Co',
'27',
'58.9332 amu',
{'Celsius':1495.0,'Farenheit':2723.0,'Kelvin':1768.15},
{'Celsius':2870.0,'Farenheit':5198.0,'Kelvin':3143.15},
'27',
'32',
'Transition Metal',
'Hexagonal',
'8.9 g/cm3',
'silver',
{'Year':'1737','Discoverer':'George Brandt','NameOrigin':'From the German word kobalt or kobold (evil spirit)'},
'magnets, ceramics, special glasses',
'arsenic, oxygen, sulfur, cobaltine'
)


nickel=Elements(
'Nickel',
'Ni',
'28',
'58.6934 amu',
{'Celsius':1453.0,'Farenheit':2647.4,'Kelvin':1726.15},
{'Celsius':2732.0,'Farenheit':4949.6,'Kelvin':3005.15},
'28',
'31',
'Transition Metal',
'Cubic',
'8.902 g/cm3',
'white',
{'Year':'1751','Discoverer':'Alex Cronstedt','NameOrigin':'From the German word kupfernickel (false copper)'},
'electroplating metal alloys, nickel-cadmium batteries',
'pentlandite'
)


copper=Elements(
'Copper',
'Cu',
'29',
'63.546 amu',
{'Celsius':1083.0,'Farenheit':1981.4,'Kelvin':1356.15},
{'Celsius':2567.0,'Farenheit':4652.6,'Kelvin':2840.15},
'29',
'35',
'Transition Metal',
'Cubic',
'8.96 g/cm3',
'red/orange',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Latin word cyprium, after the island of Cyprus'},
'electrical conductor, jewelry, coins, plumbing',
'chalcopyrite, coveline, chalcosine'
)


zinc=Elements(
'Zinc',
'Zn',
'30',
'65.39 amu',
{'Celsius':419.58,'Farenheit':787.24396,'Kelvin':692.73},
{'Celsius':907.0,'Farenheit':1664.6,'Kelvin':1180.15},
'30',
'35',
'Transition Metal',
'Hexagonal',
'7.133 g/cm3',
'bluish',
{'Year':'1746','Discoverer':'Andreas Marggraf','NameOrigin':'From the German word zin (meaning tin)'},
'metal coating, rust protection, brass, bronze, nickel',
'zinc blende, calamine'
)


gallium=Elements(
'Gallium',
'Ga',
'31',
'69.723 amu',
{'Celsius':29.78,'Farenheit':85.604004,'Kelvin':302.93},
{'Celsius':2403.0,'Farenheit':4357.4,'Kelvin':2676.15},
'31',
'39',
'Other Metals',
'Orthorhombic',
'5.907 g/cm3',
'White/Silver',
{'Year':'1875','Discoverer':'Paul Emile Lecoq de Boisbaudran','NameOrigin':'From the Latin word Gallia, the old name of France'},
'semiconductor production',
'bauxite, germanite, coal'
)


germanium=Elements(
'Germanium',
'Ge',
'32',
'72.61 amu',
{'Celsius':937.4,'Farenheit':1719.3201,'Kelvin':1210.55},
{'Celsius':2830.0,'Farenheit':5126.0,'Kelvin':3103.15},
'32',
'41',
'Metalloid',
'Cubic',
'5.323 g/cm3',
'grayish',
{'Year':'1886','Discoverer':'Clemens Winkler','NameOrigin':'From the Latin word Germania, meaning Germany'},
'semiconductors',
'refining of copper, zinc, lead'
)


arsenic=Elements(
'Arsenic',
'As',
'33',
'74.9216 amu',
{'Celsius':817.0,'Farenheit':1502.6,'Kelvin':1090.15},
{'Celsius':613.0,'Farenheit':1135.4,'Kelvin':886.15},
'33',
'42',
'Metalloid',
'Rhombohedral',
'5.72 g/cm3',
'Gray',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Greek word arsenikos and the Latin word arsenicum'},
'Poison, conducts electricity, semiconductors',
'mispickel'
)


selenium=Elements(
'Selenium',
'Se',
'34',
'78.96 amu',
{'Celsius':217.0,'Farenheit':422.6,'Kelvin':490.15},
{'Celsius':684.9,'Farenheit':1264.8201,'Kelvin':958.05005},
'34',
'45',
'Non-metal',
'Hexagonal',
'4.79 g/cm3',
'gray',
{'Year':'1817','Discoverer':'Jons Berzelius','NameOrigin':'From the Greek word Seln (Moon)'},
'photoelectric cells, TV cameras',
'refining of lead, copper, nickel'
)


bromine=Elements(
'Bromine',
'Br',
'35',
'79.904 amu',
{'Celsius':-7.2,'Farenheit':19.04,'Kelvin':265.95},
{'Celsius':58.78,'Farenheit':137.804,'Kelvin':331.93},
'35',
'45',
'Halogen',
'Orthorhombic',
'3.119 g/cm3',
'Red',
{'Year':'1826','Discoverer':'Antoine J. Balard','NameOrigin':'From the Greek word brmos (stench)'},
'Poisonous',
'Sea Water'
)


krypton=Elements(
'Krypton',
'Kr',
'36',
'83.8 amu',
{'Celsius':-157.2,'Farenheit':-250.95999,'Kelvin':115.950005},
{'Celsius':-153.4,'Farenheit':-244.12,'Kelvin':119.75001},
'36',
'48',
'Noble Gas',
'Cubic',
'3.74 g/cm3',
'colorless gas',
{'Year':'1898','Discoverer':'Sir William Ramsay','NameOrigin':'From the Greek word kryptos (hidden)'},
'Lighting',
'production of liquid air'
)


rubidium=Elements(
'Rubidium',
'Rb',
'37',
'85.4678 amu',
{'Celsius':38.89,'Farenheit':102.002,'Kelvin':312.04},
{'Celsius':688.0,'Farenheit':1270.4,'Kelvin':961.15},
'37',
'48',
'Alkali Metal',
'Cubic',
'1.532 g/cm3',
'silver',
{'Year':'1861','Discoverer':'R. Bunsen','NameOrigin':'From the Latin word rubidus (red)'},
'catalyst, photocells',
'lithium production'
)


strontium=Elements(
'Strontium',
'Sr',
'38',
'87.62 amu',
{'Celsius':769.0,'Farenheit':1416.2,'Kelvin':1042.15},
{'Celsius':1384.0,'Farenheit':2523.2,'Kelvin':1657.15},
'38',
'50',
'Alkaline Earth',
'Cubic',
'2.54 g/cm3',
'yellowish',
{'Year':'1790','Discoverer':'A. Crawford','NameOrigin':'After Strotian (a Scottish town)'},
'flares, fireworks, crimson color',
'celestite, strontianite'
)


yttrium=Elements(
'Yttrium',
'Y',
'39',
'88.90585 amu',
{'Celsius':1523.0,'Farenheit':2773.4,'Kelvin':1796.15},
{'Celsius':3337.0,'Farenheit':6038.6,'Kelvin':3610.15},
'39',
'50',
'Transition Metal',
'Hexagonal',
'4.469 g/cm3',
'silvery',
{'Year':'1794','Discoverer':'Johann Gadolin','NameOrigin':'After Ytterby (a town in Sweden)'},
"color TV's, radars",
'monazite, xenotime, yettriac'
)


zirconium=Elements(
'Zirconium',
'Zr',
'40',
'91.224 amu',
{'Celsius':1852.0,'Farenheit':3365.6,'Kelvin':2125.15},
{'Celsius':4377.0,'Farenheit':7910.6,'Kelvin':4650.15},
'40',
'51',
'Transition Metal',
'Hexagonal',
'6.49 g/cm3',
'Grayish',
{'Year':'1789','Discoverer':'Martin Klaproth','NameOrigin':'zircon (mineral)'},
'nuclear applications',
'zircon, baddeleyite'
)


niobium=Elements(
'Niobium',
'Nb',
'41',
'92.90638 amu',
{'Celsius':2468.0,'Farenheit':4474.4,'Kelvin':2741.15},
{'Celsius':4927.0,'Farenheit':8900.6,'Kelvin':5200.15},
'41',
'52',
'Transition Metal',
'Cubic',
'8.57 g/cm3',
'white',
{'Year':'1801','Discoverer':'Charles Hatchet','NameOrigin':'After Niobe, daughter of mythical king (Tantalus)'},
'No uses known',
'columbite'
)


molybdenum=Elements(
'Molybdenum',
'Mo',
'42',
'95.94 amu',
{'Celsius':2617.0,'Farenheit':4742.6,'Kelvin':2890.15},
{'Celsius':4612.0,'Farenheit':8333.6,'Kelvin':4885.15},
'42',
'54',
'Transition Metal',
'Cubic',
'10.22 g/cm3',
'silverish',
{'Year':'1778','Discoverer':'Carl Wilhelm Scheele','NameOrigin':'From the Greek word molubdos (lead)'},
'aircraft, missiles',
'molybdenite, wulfenite'
)


technetium=Elements(
'Technetium',
'Tc',
'43',
'(98.0) amu',
{'Celsius':2200.0,'Farenheit':3992.0,'Kelvin':2473.15},
{'Celsius':4877.0,'Farenheit':8810.6,'Kelvin':5150.15},
'43',
'55',
'Transition Metal',
'Hexagonal',
'11.5 g/cm3',
'Unknown',
{'Year':'1937','Discoverer':'Carlo Perrier','NameOrigin':'From the Greek word techntos (artificial)'},
'Tc-99m is used for radioactive tracing in medicine',
'Man-made'
)


ruthenium=Elements(
'Ruthenium',
'Ru',
'44',
'101.07 amu',
{'Celsius':2250.0,'Farenheit':4082.0,'Kelvin':2523.15},
{'Celsius':3900.0,'Farenheit':7052.0,'Kelvin':4173.15},
'44',
'57',
'Transition Metal',
'Hexagonal',
'12.2 g/cm3',
'silvery',
{'Year':'1844','Discoverer':'Karl Klaus','NameOrigin':'From the Latin word Ruthenia (Russia)'},
'platinum alloys',
'pentlandite, pyroxinite'
)


rhodium=Elements(
'Rhodium',
'Rh',
'45',
'102.9055 amu',
{'Celsius':1966.0,'Farenheit':3570.8,'Kelvin':2239.15},
{'Celsius':3727.0,'Farenheit':6740.6,'Kelvin':4000.15},
'45',
'58',
'Transition Metal',
'Cubic',
'12.41 g/cm3',
'silverish',
{'Year':'1803','Discoverer':'William Wollaston','NameOrigin':'From the Greek word rhodon (rose)'},
'coatings',
'by-product of nickel production'
)


palladium=Elements(
'Palladium',
'Pd',
'46',
'106.42 amu',
{'Celsius':1552.0,'Farenheit':2825.6,'Kelvin':1825.15},
{'Celsius':2927.0,'Farenheit':5300.6,'Kelvin':3200.15},
'46',
'60',
'Transition Metal',
'Cubic',
'12.02 g/cm3',
'white',
{'Year':'1803','Discoverer':'William Wollaston','NameOrigin':'From the Greek goddess of wisdom (Pallas) and after an asteroid'},
'jewelry, medical instruments',
'platinum, nickel, copper, mercury ores'
)


silver=Elements(
'Silver',
'Ag',
'47',
'107.8682 amu',
{'Celsius':961.93,'Farenheit':1763.474,'Kelvin':1235.08},
{'Celsius':2212.0,'Farenheit':4013.6,'Kelvin':2485.15},
'47',
'61',
'Transition Metal',
'Cubic',
'10.5 g/cm3',
'silver',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Old English word seolfor (silver)'},
'jewelry, photography, electrical conductor',
'ores (argentite, light ruby silver, dark ruby silver, brittle silver)'
)


cadmium=Elements(
'Cadmium',
'Cd',
'48',
'112.411 amu',
{'Celsius':320.9,'Farenheit':609.62,'Kelvin':594.05},
{'Celsius':765.0,'Farenheit':1409.0,'Kelvin':1038.15},
'48',
'64',
'Transition Metal',
'Hexagonal',
'8.65 g/cm3',
'Silvery',
{'Year':'1817','Discoverer':'Fredrich Stromeyer','NameOrigin':'From the Greek word kadmeia (ancient name for calamine) and from the Latin word cadmia'},
'poisonous, nickel-cadmium batteries',
'by-product of zinc refining'
)


indium=Elements(
'Indium',
'In',
'49',
'114.818 amu',
{'Celsius':156.61,'Farenheit':313.898,'Kelvin':429.76},
{'Celsius':2000.0,'Farenheit':3632.0,'Kelvin':2273.15},
'49',
'66',
'Other Metals',
'Tetragonal',
'7.31 g/cm3',
'Silverish',
{'Year':'1863','Discoverer':'Ferdinand Reich','NameOrigin':'From the Indigo color seen in its spectrum'},
'coating of high-speed bearings',
'by-product of zinc refining'
)


tin=Elements(
'Tin',
'Sn',
'50',
'118.71 amu',
{'Celsius':231.9,'Farenheit':449.41998,'Kelvin':505.05},
{'Celsius':2270.0,'Farenheit':4118.0,'Kelvin':2543.15},
'50',
'69',
'Other Metals',
'Tetragonal',
'7.31 g/cm3',
'white',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'Latin'},
'coating for steel cans',
'ore cassiterite'
)


antimony=Elements(
'Antimony',
'Sb',
'51',
'121.76 amu',
{'Celsius':630.0,'Farenheit':1166.0,'Kelvin':903.15},
{'Celsius':1750.0,'Farenheit':3182.0,'Kelvin':2023.15},
'51',
'71',
'Metalloid',
'Rhombohedral',
'6.684 g/cm3',
'bluish',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Greek words anti (opposed) and monos (solitude), hence "not alone"'},
'hardens lead, plastics, chemicals',
'stibnite, valentinite'
)


tellurium=Elements(
'Tellurium',
'Te',
'52',
'127.6 amu',
{'Celsius':449.5,'Farenheit':841.1,'Kelvin':722.65},
{'Celsius':989.8,'Farenheit':1813.64,'Kelvin':1262.95},
'52',
'76',
'Metalloid',
'Hexagonal',
'6.24 g/cm3',
'silverish',
{'Year':'1782','Discoverer':'Franz Muller von Reichenstein','NameOrigin':'From the Greek word tellus (Earth)'},
'coloring of glass and ceramics, thermoelectric devices',
'by-product of refining of lead and copper'
)


iodine=Elements(
'Iodine',
'I',
'53',
'126.90447 amu',
{'Celsius':113.5,'Farenheit':236.3,'Kelvin':386.65},
{'Celsius':184.0,'Farenheit':363.2,'Kelvin':457.15},
'53',
'74',
'Halogen',
'Orthorhombic',
'4.93 g/cm3',
'blackish',
{'Year':'1811','Discoverer':'Bernard Courtois','NameOrigin':'From the Greek word ides (violet)'},
'required in humans',
'sodium and potassium compounds'
)


xenon=Elements(
'Xenon',
'Xe',
'54',
'131.29 amu',
{'Celsius':-111.9,'Farenheit':-169.42,'Kelvin':161.25},
{'Celsius':-108.1,'Farenheit':-162.58,'Kelvin':165.05},
'54',
'77',
'Noble Gas',
'Cubic',
'5.8971 g/cm3',
'Colorless Gas',
{'Year':'1898','Discoverer':'Sir William Ramsay','NameOrigin':'From the Greek word xenon (stranger)'},
'powerful lamps, bubble chambers',
'liquid air'
)


cesium=Elements(
'Cesium',
'Cs',
'55',
'132.90546 amu',
{'Celsius':28.5,'Farenheit':83.3,'Kelvin':301.65},
{'Celsius':678.4,'Farenheit':1253.12,'Kelvin':951.55005},
'55',
'78',
'Alkali Metal',
'Cubic',
'1.873 g/cm3',
'silver',
{'Year':'1860','Discoverer':'Fustov Kirchoff','NameOrigin':'From the Latin word caesius (sky blue)'},
'removes air traces in vacuum tubes',
'pollucite, lepidolite'
)


barium=Elements(
'Barium',
'Ba',
'56',
'137.327 amu',
{'Celsius':725.0,'Farenheit':1337.0,'Kelvin':998.15},
{'Celsius':1140.0,'Farenheit':2084.0,'Kelvin':1413.15},
'56',
'81',
'Alkaline Earth',
'Cubic',
'3.51 g/cm3',
'Silver',
{'Year':'1808','Discoverer':'Sir Humphrey Davy','NameOrigin':'From the Greek word barys (heavy)'},
'Medical applications, among others ',
'barytine, whiterite'
)


hafnium=Elements(
'Hafnium',
'Hf',
'72',
'178.49 amu',
{'Celsius':2150.0,'Farenheit':3902.0,'Kelvin':2423.15},
{'Celsius':5400.0,'Farenheit':9752.0,'Kelvin':5673.15},
'72',
'106',
'Transition Metal',
'Hexagonal',
'13.2 g/cm3',
'Silver',
{'Year':'1923','Discoverer':'Dirk Coster','NameOrigin':'From the Latin word Hafnia (Copenhagen)'},
'nuclear reactors',
'zircon'
)


tantalum=Elements(
'Tantalum',
'Ta',
'73',
'180.9479 amu',
{'Celsius':2996.0,'Farenheit':5424.8,'Kelvin':3269.15},
{'Celsius':5425.0,'Farenheit':9797.0,'Kelvin':5698.15},
'73',
'108',
'Transition Metal',
'Cubic',
'16.654 g/cm3',
'gray',
{'Year':'1802','Discoverer':'Anders Ekeberg','NameOrigin':'After king Tantalus (Greek mythology)'},
'capacitors, camera lenses',
'tantalite'
)


tungsten=Elements(
'Tungsten',
'W',
'74',
'183.84 amu',
{'Celsius':3410.0,'Farenheit':6170.0,'Kelvin':3683.15},
{'Celsius':5660.0,'Farenheit':10220.0,'Kelvin':5933.15},
'74',
'110',
'Transition Metal',
'Cubic',
'19.3 g/cm3',
'Silver',
{'Year':'1783','Discoverer':'Fausto and Juan Jose de Elhuyar','NameOrigin':'From the Swedish words tung sten (heavy stone)'},
'used widely in electronics industry',
'scheelite, wolframite'
)


rhenium=Elements(
'Rhenium',
'Re',
'75',
'186.207 amu',
{'Celsius':3180.0,'Farenheit':5756.0,'Kelvin':3453.15},
{'Celsius':5627.0,'Farenheit':10160.6,'Kelvin':5900.15},
'75',
'111',
'Transition Metal',
'Hexagonal',
'21.02 g/cm3',
'silverish',
{'Year':'1925','Discoverer':'Walter Noddack','NameOrigin':'From Rhines provinces of Germany'},
'filaments for mass spectrographs',
'gadolinite, molybdenite'
)


osmium=Elements(
'Osmium',
'Os',
'76',
'190.23 amu',
{'Celsius':3045.0,'Farenheit':5513.0,'Kelvin':3318.15},
{'Celsius':5027.0,'Farenheit':9080.6,'Kelvin':5300.15},
'76',
'114',
'Transition Metal',
'Hexagonal',
'22.4 g/cm3',
'silvery',
{'Year':'1803','Discoverer':'Smithson Tenant','NameOrigin':'From the Greek word osm (odor)'},
'tip gold pen points, instrument pivots, electrical light filaments',
'ores that contain platinum'
)


iridium=Elements(
'Iridium',
'Ir',
'77',
'192.217 amu',
{'Celsius':2410.0,'Farenheit':4370.0,'Kelvin':2683.15},
{'Celsius':4527.0,'Farenheit':8180.6,'Kelvin':4800.15},
'77',
'115',
'Transition Metal',
'Cubic',
'22.5 g/cm3',
'white',
{'Year':'1804','Discoverer':'S. Tenant','NameOrigin':'From the Latin word iridis (rainbow)'},
'tip gold pens, crucible and special containers',
'gravel deposits with platinum'
)


platinum=Elements(
'Platinum',
'Pt',
'78',
'195.078 amu',
{'Celsius':1772.0,'Farenheit':3221.6,'Kelvin':2045.15},
{'Celsius':3827.0,'Farenheit':6920.6,'Kelvin':4100.15},
'78',
'117',
'Transition Metal',
'Cubic',
'21.45 g/cm3',
'silverish',
{'Year':'1735','Discoverer':'Julius Scaliger','NameOrigin':'From the Spanish word platina (little silver)'},
'jewelry, containers, catalyst',
'platinum ores'
)


gold=Elements(
'Gold',
'Au',
'79',
'196.96655 amu',
{'Celsius':1064.43,'Farenheit':1947.9741,'Kelvin':1337.5801},
{'Celsius':2807.0,'Farenheit':5084.6,'Kelvin':3080.15},
'79',
'118',
'Transition Metal',
'Cubic',
'19.32 g/cm3',
'Gold',
{'Year':'circa3000BC','Discoverer':'Unknown','NameOrigin':'From the Old English word geolo (yellow)'},
'electronics, jewelry, coins',
'crust of the earth, copper ores'
)


mercury=Elements(
'Mercury',
'Hg',
'80',
'200.59 amu',
{'Celsius':-38.87,'Farenheit':-37.966,'Kelvin':234.28},
{'Celsius':356.58,'Farenheit':673.844,'Kelvin':629.73},
'80',
'121',
'Transition Metal',
'Rhombohedral',
'13.456 g/cm3',
'Silver',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'After the planet Mercury'},
'thermometers, barometers, fluorescent lamps, batteries',
'cinnabar ore'
)


thallium=Elements(
'Thallium',
'Tl',
'81',
'204.3833 amu',
{'Celsius':303.5,'Farenheit':578.3,'Kelvin':576.65},
{'Celsius':1457.0,'Farenheit':2654.6,'Kelvin':1730.15},
'81',
'123',
'Other Metals',
'Hexagonal',
'11.85 g/cm3',
'bluish',
{'Year':'1861','Discoverer':'Sir William Crookes','NameOrigin':'From the Greek word thallos (young shoot)'},
'rat and ant poisons, detecting infrared radiation',
'crookesite, hutchinsonite, lorandite'
)


lead=Elements(
'Lead',
'Pb',
'82',
'207.2 amu',
{'Celsius':327.5,'Farenheit':621.5,'Kelvin':600.65},
{'Celsius':1740.0,'Farenheit':3164.0,'Kelvin':2013.15},
'82',
'125',
'Other Metals',
'Cubic',
'11.34 g/cm3',
'bluish',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the Greek word protos (first)'},
'solder and shielding against radiation, batteries',
'galena'
)


bismuth=Elements(
'Bismuth',
'Bi',
'83',
'208.98038 amu',
{'Celsius':271.3,'Farenheit':520.33997,'Kelvin':544.45},
{'Celsius':1560.0,'Farenheit':2840.0,'Kelvin':1833.15},
'83',
'126',
'Other Metals',
'Rhombohedral',
'9.8 g/cm3',
'white',
{'Year':'Known to the ancients','Discoverer':'Unknown','NameOrigin':'From the German word wissmuth (white mass)'},
'pharmaceuticals, fuses',
'bismuthine'
)


polonium=Elements(
'Polonium',
'Po',
'84',
'(209.0) amu',
{'Celsius':254.0,'Farenheit':489.2,'Kelvin':527.15},
{'Celsius':962.0,'Farenheit':1763.6,'Kelvin':1235.15},
'84',
'125',
'Metalloid',
'Monoclinic',
'9.4 g/cm3',
'Unknown',
{'Year':'1898','Discoverer':'Pierre and Marie Curie','NameOrigin':'After Poland'},
'No uses known',
'pitchblende, decay of radium'
)


astatine=Elements(
'Astatine',
'At',
'85',
'(210.0) amu',
{'Celsius':302.0,'Farenheit':575.6,'Kelvin':575.15},
{'Celsius':337.0,'Farenheit':638.6,'Kelvin':610.15},
'85',
'125',
'Halogen',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1940','Discoverer':'D.R. Corson','NameOrigin':'From the Greek word astatos (unstable)'},
'No uses known',
'Man-made'
)


radon=Elements(
'Radon',
'Rn',
'86',
'(222.0) amu',
{'Celsius':-71.0,'Farenheit':-95.8,'Kelvin':202.15},
{'Celsius':-61.8,'Farenheit':-79.24,'Kelvin':211.35},
'86',
'136',
'Noble Gas',
'Cubic',
'9.73 g/cm3',
'colorless',
{'Year':'1898','Discoverer':'Fredrich Ernst Dorn','NameOrigin':'From radium'},
'treatment of cancer',
'decay of radium'
)


francium=Elements(
'Francium',
'Fr',
'87',
'(223.0) amu',
{'Celsius':27.0,'Farenheit':80.6,'Kelvin':300.15},
{'Celsius':677.0,'Farenheit':1250.6,'Kelvin':950.15},
'87',
'136',
'Alkali Metal',
'Cubic',
'Unknown',
'Unknown',
{'Year':'1939','Discoverer':'Marguerite Perey','NameOrigin':'After France'},
'No uses known',
'decay of actinium'
)


radium=Elements(
'Radium',
'Ra',
'88',
'(226.0) amu',
{'Celsius':700.0,'Farenheit':1292.0,'Kelvin':973.15},
{'Celsius':1737.0,'Farenheit':3158.6,'Kelvin':2010.15},
'88',
'138',
'Alkaline Earth',
'Cubic',
'5.0 g/cm3',
'silverish',
{'Year':'1898','Discoverer':'Pierre and Marie Curie','NameOrigin':'From the Latin word radius (ray)'},
'treating cancer',
'uranium ores'
)


praseodymium=Elements(
'Praseodymium',
'Pr',
'59',
'140.90765 amu',
{'Celsius':935.0,'Farenheit':1715.0,'Kelvin':1208.15},
{'Celsius':3127.0,'Farenheit':5660.6,'Kelvin':3400.15},
'59',
'82',
'Rare Earth',
'Hexagonal',
'6.77 g/cm3',
'Unknown',
{'Year':'1885','Discoverer':'C.F. Aver von Welsbach','NameOrigin':'From the Greek words prasios (green) and didymos (twin)'},
'coloring glass and ceramics',
'salts'
)


neodymium=Elements(
'Neodymium',
'Nd',
'60',
'144.24 amu',
{'Celsius':1010.0,'Farenheit':1850.0,'Kelvin':1283.15},
{'Celsius':3127.0,'Farenheit':5660.6,'Kelvin':3400.15},
'60',
'84',
'Rare Earth',
'Hexagonal',
'7.007 g/cm3',
'silvery',
{'Year':'1925','Discoverer':'C.F. Aver von Welsbach','NameOrigin':'From the Greek words neos (new) and didymos (twin)'},
'coloring glass and ceramics, infrared radiation filtering',
'electrolysis of salts'
)


dysprosium=Elements(
'Dysprosium',
'Dy',
'66',
'162.5 amu',
{'Celsius':1412.0,'Farenheit':2573.6,'Kelvin':1685.15},
{'Celsius':2562.0,'Farenheit':4643.6,'Kelvin':2835.15},
'66',
'97',
'Rare Earth',
'Hexagonal',
'8.536 g/cm3',
'Unknown',
{'Year':'1886','Discoverer':'Paul Emile Lecoq de Boisbaudran','NameOrigin':'From the Greek word dysprositos (hard to get at)'},
'nuclear reactors',
'erbium, holmium'
)


holmium=Elements(
'Holmium',
'Ho',
'67',
'164.93031 amu',
{'Celsius':1470.0,'Farenheit':2678.0,'Kelvin':1743.15},
{'Celsius':2720.0,'Farenheit':4928.0,'Kelvin':2993.15},
'67',
'98',
'Rare Earth',
'Hexagonal',
'8.54 g/cm3',
'Silver',
{'Year':'1878','Discoverer':'J.L. Soret','NameOrigin':'Form the Latin word Holmia (Stockholm)'},
'nuclear reactors',
'gadolinite'
)


erbium=Elements(
'Erbium',
'Er',
'68',
'167.26 amu',
{'Celsius':1522.0,'Farenheit':2771.6,'Kelvin':1795.15},
{'Celsius':2510.0,'Farenheit':4550.0,'Kelvin':2783.15},
'68',
'99',
'Rare Earth',
'Hexagonal',
'8.795 g/cm3',
'grayish',
{'Year':'1843','Discoverer':'Carl Mosander','NameOrigin':'Ytterby (a town in Sweden)'},
'ceramics',
'heavier rare earth minerals'
)


thulium=Elements(
'Thulium',
'Tm',
'69',
'168.9342 amu',
{'Celsius':1545.0,'Farenheit':2813.0,'Kelvin':1818.15},
{'Celsius':1727.0,'Farenheit':3140.6,'Kelvin':2000.15},
'69',
'100',
'Rare Earth',
'Hexagonal',
'9.321 g/cm3',
'silverish',
{'Year':'1879','Discoverer':'Per Theodor Cleve','NameOrigin':'From Thule (ancient name of Scandinavia)'},
'power for portable x-ray machines',
'gadolinite, euxenite, xenotime'
)


ytterbium=Elements(
'Ytterbium',
'Yb',
'70',
'173.04 amu',
{'Celsius':824.0,'Farenheit':1515.2,'Kelvin':1097.15},
{'Celsius':1466.0,'Farenheit':2670.8,'Kelvin':1739.15},
'70',
'103',
'Rare Earth',
'Cubic',
'6.98 g/cm3',
'Silvery',
{'Year':'1878','Discoverer':'Jean de Marignac','NameOrigin':'Ytterby (a town in Sweden)'},
'metallurgical and chemical experiments',
'yttria, monazite, gadolinite, xenotime'
)


lutetium=Elements(
'Lutetium',
'Lu',
'71',
'174.967 amu',
{'Celsius':1656.0,'Farenheit':3012.8,'Kelvin':1929.15},
{'Celsius':3315.0,'Farenheit':5999.0,'Kelvin':3588.15},
'71',
'104',
'Rare Earth',
'Hexagonal',
'9.85 g/cm3',
'silvery',
{'Year':'1907','Discoverer':'Georges Urbain','NameOrigin':'From Lutetia (ancient name of Paris)'},
'No uses known',
'gadolinite, xenotime'
)


actinium=Elements(
'Actinium',
'Ac',
'89',
'(227.0) amu',
{'Celsius':1050.0,'Farenheit':1922.0,'Kelvin':1323.15},
{'Celsius':3200.0,'Farenheit':5792.0,'Kelvin':3473.15},
'89',
'138',
'Rare Earth',
'Cubic',
'10.07 g/cm3',
'Silvery',
{'Year':'1899','Discoverer':'Andre Debierne','NameOrigin':'From the Greek word aktinos (ray)'},
'No uses known',
'extremely rare'
)


thorium=Elements(
'Thorium',
'Th',
'90',
'232.0381 amu',
{'Celsius':1750.0,'Farenheit':3182.0,'Kelvin':2023.15},
{'Celsius':4790.0,'Farenheit':8654.0,'Kelvin':5063.15},
'90',
'142',
'Rare Earth',
'Cubic',
'11.72 g/cm3',
'silvery',
{'Year':'1828','Discoverer':'Jons Berzelius','NameOrigin':'Thor (Scandinavian god)'},
'strong alloys, ultraviolet photoelectric cells',
'monazite, thorite'
)


uranium=Elements(
'Uranium',
'U',
'92',
'238.0289 amu',
{'Celsius':1132.0,'Farenheit':2069.6,'Kelvin':1405.15},
{'Celsius':3818.0,'Farenheit':6904.4,'Kelvin':4091.15},
'92',
'146',
'Rare Earth',
'Orthorhombic',
'18.95 g/cm3',
'silverish',
{'Year':'1789','Discoverer':'Martin Klaproth','NameOrigin':'After the planet Uranus'},
'fuel for nuclear reactors',
'many rocks, large amounts in pitchblende and carnotite'
)


neptunium=Elements(
'Neptunium',
'Np',
'93',
'(237.0) amu',
{'Celsius':640.0,'Farenheit':1184.0,'Kelvin':913.15},
{'Celsius':3902.0,'Farenheit':7055.6,'Kelvin':4175.15},
'93',
'144',
'Rare Earth',
'Orthorhombic',
'20.45 g/cm3',
'Unknown',
{'Year':'1940','Discoverer':'E.M. McMillan','NameOrigin':'After the planet Neptune'},
'No uses known',
'Man-made'
)


plutonium=Elements(
'Plutonium',
'Pu',
'94',
'(244.0) amu',
{'Celsius':639.5,'Farenheit':1183.1,'Kelvin':912.65},
{'Celsius':3235.0,'Farenheit':5855.0,'Kelvin':3508.15},
'94',
'150',
'Rare Earth',
'Monoclinic',
'19.84 g/cm3',
'Unknown',
{'Year':'1940','Discoverer':'G.T. Seaborg','NameOrigin':'After the planet Pluto'},
'bombs, nuclear reactors',
'some uranium ores, man-made'
)


americium=Elements(
'Americium',
'Am',
'95',
'(243.0) amu',
{'Celsius':994.0,'Farenheit':1821.2,'Kelvin':1267.15},
{'Celsius':2607.0,'Farenheit':4724.6,'Kelvin':2880.15},
'95',
'148',
'Rare Earth',
'Hexagonal',
'13.6 g/cm3',
'Unknown',
{'Year':'1945','Discoverer':'G.T. Seaborg','NameOrigin':'After America'},
'Smoke Detectors',
'Man-made'
)


thorium=Elements(
'Thorium',
'Th',
'90',
'232.0381 amu',
{'Celsius':1750.0,'Farenheit':3182.0,'Kelvin':2023.15},
{'Celsius':4790.0,'Farenheit':8654.0,'Kelvin':5063.15},
'90',
'142',
'Rare Earth',
'Cubic',
'11.72 g/cm3',
'silvery',
{'Year':'1828','Discoverer':'Jons Berzelius','NameOrigin':'Thor (Scandinavian god)'},
'strong alloys, ultraviolet photoelectric cells',
'monazite, thorite'
)

uranium=Elements(
'Uranium',
'U',
'92',
'238.0289 amu',
{'Celsius':1132.0,'Farenheit':2069.6,'Kelvin':1405.15},
{'Celsius':3818.0,'Farenheit':6904.4,'Kelvin':4091.15},
'92',
'146',
'Rare Earth',
'Orthorhombic',
'18.95 g/cm3',
'silverish',
{'Year':'1789','Discoverer':'Martin Klaproth','NameOrigin':'After the planet Uranus'},
'fuel for nuclear reactors',
'many rocks, large amounts in pitchblende and carnotite'
)


neptunium=Elements(
'Neptunium',
'Np',
'93',
'(237.0) amu',
{'Celsius':640.0,'Farenheit':1184.0,'Kelvin':913.15},
{'Celsius':3902.0,'Farenheit':7055.6,'Kelvin':4175.15},
'93',
'144',
'Rare Earth',
'Orthorhombic',
'20.45 g/cm3',
'Unknown',
{'Year':'1940','Discoverer':'E.M. McMillan','NameOrigin':'After the planet Neptune'},
'No uses known',
'Man-made'
)


plutonium=Elements(
'Plutonium',
'Pu',
'94',
'(244.0) amu',
{'Celsius':639.5,'Farenheit':1183.1,'Kelvin':912.65},
{'Celsius':3235.0,'Farenheit':5855.0,'Kelvin':3508.15},
'94',
'150',
'Rare Earth',
'Monoclinic',
'19.84 g/cm3',
'Unknown',
{'Year':'1940','Discoverer':'G.T. Seaborg','NameOrigin':'After the planet Pluto'},
'bombs, nuclear reactors',
'some uranium ores, man-made'
)


americium=Elements(
'Americium',
'Am',
'95',
'(243.0) amu',
{'Celsius':994.0,'Farenheit':1821.2,'Kelvin':1267.15},
{'Celsius':2607.0,'Farenheit':4724.6,'Kelvin':2880.15},
'95',
'148',
'Rare Earth',
'Hexagonal',
'13.6 g/cm3',
'Unknown',
{'Year':'1945','Discoverer':'G.T. Seaborg','NameOrigin':'After America'},
'Smoke Detectors',
'Man-made'
)


mendelevium=Elements(
'Mendelevium',
'Md',
'101',
'(258.0) amu',
'Unknown',
'Unknown',
'101',
'157',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1955','Discoverer':'G.T. Seaborg','NameOrigin':'After Dmitri Ivanovitch Mendeleyev'},
'No uses known',
'Man-made'
)


nobelium=Elements(
'Nobelium',
'No',
'102',
'(259.0) amu',
'Unknown',
'Unknown',
'102',
'157',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1957','Discoverer':'Nobel Institute for Physics','NameOrigin':'After Alfred Nobel'},
'No uses known',
'Man-made'
)


lawrencium=Elements(
'Lawrencium',
'Lr',
'103',
'(262.0) amu',
'Unknown',
'Unknown',
'103',
'159',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1961','Discoverer':'Albert Ghiorso','NameOrigin':'After Ernest Lawrence'},
'No uses known',
'Man-made'
)


lanthanum=Elements(
'Lanthanum',
'La',
'57',
'138.9055 amu',
{'Celsius':920.0,'Farenheit':1688.0,'Kelvin':1193.15},
{'Celsius':3469.0,'Farenheit':6276.2,'Kelvin':3742.15},
'57',
'82',
'Rare Earth',
'Hexagonal',
'6.7 g/cm3',
'white',
{'Year':'1839','Discoverer':'Carl Mosander','NameOrigin':'From the Greek word lanthaneis (to lie hidden)'},
'expensive camera lenses',
'monazite, bastnasite'
)


cerium=Elements(
'Cerium',
'Ce',
'58',
'140.116 amu',
{'Celsius':795.0,'Farenheit':1463.0,'Kelvin':1068.15},
{'Celsius':3257.0,'Farenheit':5894.6,'Kelvin':3530.15},
'58',
'82',
'Rare Earth',
'Cubic',
'6.773 g/cm3',
'gray',
{'Year':'1803','Discoverer':'W. von Hisinger','NameOrigin':'Ceres (asteroid)'},
'heat-resistant alloys',
'monazite'
)


samarium=Elements(
'Samarium',
'Sm',
'62',
'150.36 amu',
{'Celsius':1072.0,'Farenheit':1961.6,'Kelvin':1345.15},
{'Celsius':1900.0,'Farenheit':3452.0,'Kelvin':2173.15},
'62',
'88',
'Rare Earth',
'Rhombohedral',
'7.54 g/cm3',
'silver',
{'Year':'1879','Discoverer':'Paul Emile Lecoq de Boisbaudran','NameOrigin':'smarskite (mineral)'},
'used in magnets, in alloys with cobalt, and nuclear reactors',
'found with other rare earths'
)


europium=Elements(
'Europium',
'Eu',
'63',
'151.964 amu',
{'Celsius':822.0,'Farenheit':1511.6,'Kelvin':1095.15},
{'Celsius':1597.0,'Farenheit':2906.6,'Kelvin':1870.15},
'63',
'89',
'Rare Earth',
'Cubic',
'5.259 g/cm3',
'silver',
{'Year':'1901','Discoverer':'Eugene Demarcay','NameOrigin':'Europe'},
'color televisions',
'Man-made'
)


gadolinium=Elements(
'Gadolinium',
'Gd',
'64',
'157.25 amu',
{'Celsius':1311.0,'Farenheit':2391.8,'Kelvin':1584.15},
{'Celsius':3233.0,'Farenheit':5851.4,'Kelvin':3506.15},
'64',
'93',
'Rare Earth',
'Hexagonal',
'7.895 g/cm3',
'Silverish',
{'Year':'1880','Discoverer':'Jean de Marignac','NameOrigin':'gadolinite (mineral)'},
'magnetic',
'gadolinite'
)


terbium=Elements(
'Terbium',
'Tb',
'65',
'158.92534 amu',
{'Celsius':1360.0,'Farenheit':2480.0,'Kelvin':1633.15},
{'Celsius':3041.0,'Farenheit':5505.8,'Kelvin':3314.15},
'65',
'94',
'Rare Earth',
'Hexagonal',
'8.27 g/cm3',
'silverish',
{'Year':'1843','Discoverer':'Carl Mosander','NameOrigin':'Ytterby (a town in Sweden)'},
"in color TV's",
'with other rare earths'
)


samarium=Elements(
'Samarium',
'Sm',
'62',
'150.36 amu',
{'Celsius':1072.0,'Farenheit':1961.6,'Kelvin':1345.15},
{'Celsius':1900.0,'Farenheit':3452.0,'Kelvin':2173.15},
'62',
'88',
'Rare Earth',
'Rhombohedral',
'7.54 g/cm3',
'silver',
{'Year':'1879','Discoverer':'Paul Emile Lecoq de Boisbaudran','NameOrigin':'smarskite (mineral)'},
'used in magnets, in alloys with cobalt, and nuclear reactors',
'found with other rare earths'
)


europium=Elements(
'Europium',
'Eu',
'63',
'151.964 amu',
{'Celsius':822.0,'Farenheit':1511.6,'Kelvin':1095.15},
{'Celsius':1597.0,'Farenheit':2906.6,'Kelvin':1870.15},
'63',
'89',
'Rare Earth',
'Cubic',
'5.259 g/cm3',
'silver',
{'Year':'1901','Discoverer':'Eugene Demarcay','NameOrigin':'Europe'},
'color televisions',
'Man-made'
)


gadolinium=Elements(
'Gadolinium',
'Gd',
'64',
'157.25 amu',
{'Celsius':1311.0,'Farenheit':2391.8,'Kelvin':1584.15},
{'Celsius':3233.0,'Farenheit':5851.4,'Kelvin':3506.15},
'64',
'93',
'Rare Earth',
'Hexagonal',
'7.895 g/cm3',
'Silverish',
{'Year':'1880','Discoverer':'Jean de Marignac','NameOrigin':'gadolinite (mineral)'},
'magnetic',
'gadolinite'
)


terbium=Elements(
'Terbium',
'Tb',
'65',
'158.92534 amu',
{'Celsius':1360.0,'Farenheit':2480.0,'Kelvin':1633.15},
{'Celsius':3041.0,'Farenheit':5505.8,'Kelvin':3314.15},
'65',
'94',
'Rare Earth',
'Hexagonal',
'8.27 g/cm3',
'silverish',
{'Year':'1843','Discoverer':'Carl Mosander','NameOrigin':'Ytterby (a town in Sweden)'},
"in color TV's",
'with other rare earths'
)


dubnium=Elements(
'Dubnium',
'Db',
'105',
'(262.0) amu',
'Unknown',
'Unknown',
'105',
'157',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1970','Discoverer':'Albert Ghiorso','NameOrigin':'After Dubna, Russia'},
'No uses known',
'Man-made'
)


rutherfordium=Elements(
'Rutherfordium',
'Rf',
'104',
'(261.0) amu',
'Unknown',
'Unknown',
'104',
'157',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1969','Discoverer':'Albert Ghiorso','NameOrigin':'After Lord Rutherford, a New Zealand chemist and physicist'},
'No uses known',
'Man-made'
)


seaborgium=Elements(
'Seaborgium',
'Sg',
'106',
'(263.0) amu',
'Unknown',
'Unknown',
'106',
'157',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1974','Discoverer':'Albert Ghiorso','NameOrigin':'After Glenn T. Seaborg, who discovered many of the transuranium elements'},
'No uses known',
'Man-made'
)


bohrium=Elements(
'Bohrium',
'Bh',
'107',
'(262.0) amu',
'Unknown',
'Unknown',
'107',
'155',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1976','Discoverer':'Peter Armbruster, Gottfried Munzenber and others','NameOrigin':'After Niels Bohr (Danish physicist)'},
'No uses known',
'Man-made'
)


hassium=Elements(
'Hassium',
'Hs',
'108',
'(265.0) amu',
'Unknown',
'Unknown',
'108',
'157',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1984','Discoverer':'Peter Armbruster, Gottfried Munzenber and others','NameOrigin':'from the Latin word Hassias, a German state.'},
'No uses known',
'Man-made'
)


meitnerium=Elements(
'Meitnerium',
'Mt',
'109',
'(266.0) amu',
'Unknown',
'Unknown',
'109',
'157',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1982','Discoverer':'Heavy Ion Research Laboratory','NameOrigin':'After Lise Meitner (Austrian physicist)'},
'No uses known',
'Man-made'
)


promethium=Elements(
'Promethium',
'Pm',
'61',
'(145.0) amu',
'Unknown',
'Unknown',
'61',
'84',
'Rare Earth',
'Hexagonal',
'6.475 g/cm3',
'Unknown',
{'Year':'1945','Discoverer':'J.A. Marinsky','NameOrigin':'From the god Prometheus (who stole fire of the sky and gave it to man)'},
'No uses known',
'fission products of uranium, thorium, plutonium'
)


protactinium=Elements(
'Protactinium',
'Pa',
'91',
'231.03587 amu',
{'Celsius':1600.0,'Farenheit':2912.0,'Kelvin':1873.15},
'Unknown',
'91',
'140',
'Rare Earth',
'Orthorhombic',
'15.4 g/cm3',
'Unknown',
{'Year':'1917','Discoverer':'Fredrich Soddy','NameOrigin':'From the Greek word protos (first)'},
'No uses known',
'fission product of uranium, thorium, plutonium'
)


curium=Elements(
'Curium',
'Cm',
'96',
'(247.0) amu',
{'Celsius':1340.0,'Farenheit':2444.0,'Kelvin':1613.15},
'Unknown',
'96',
'151',
'Rare Earth',
'Unknown',
'13.511 g/cm3',
'Unknown',
{'Year':'1944','Discoverer':'G.T. Seaborg','NameOrigin':'After Pierre and Marie Curie'},
'No uses known',
'Man-made'
)


berkelium=Elements(
'Berkelium',
'Bk',
'97',
'(247.0) amu',
'Unknown',
'Unknown',
'97',
'150',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1949','Discoverer':'G.T. Seaborg','NameOrigin':'After Berkeley, California'},
'No uses known',
'Man-made'
)


californium=Elements(
'Californium',
'Cf',
'98',
'(251.0) amu',
'Unknown',
'Unknown',
'98',
'153',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1950','Discoverer':'G.T. Seaborg','NameOrigin':'California (State and University)'},
'No uses known',
'Man-made'
)


einsteinium=Elements(
'Einsteinium',
'Es',
'99',
'(252.0) amu',
'Unknown',
'Unknown',
'99',
'153',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1952','Discoverer':'Argonne, Los Alamos, University of California','NameOrigin':'After Albert Einstein'},
'No uses known',
'Man-made'
)


fermium=Elements(
'Fermium',
'Fm',
'100',
'(257.0) amu',
'Unknown',
'Unknown',
'100',
'157',
'Rare Earth',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1953','Discoverer':'Argonne, Los Alamos, University of California','NameOrigin':'After Enrico Fermi'},
'No uses known',
'Man-made'
)


ununbium=Elements(
'Ununbium',
'Uub',
'112',
'(277.0) amu',
'Unknown',
'Unknown',
'112',
'165',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1996','Discoverer':'S. Hofmann, V. Ninov, F. P. Hessbuger','NameOrigin':'Un (one) un (one) bi (two) um'},
'No uses known',
'Fusion of zinc and lead'
)


ununnilium=Elements(
'Ununnilium',
'Uun',
'110',
'(269.0) amu',
'Unknown',
'Unknown',
'110',
'159',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1987','Discoverer':'Organessian, et al. ','NameOrigin':'Un (one) un (one) nil (zero) ium'},
'No uses known',
'Man-made'
)


unununium=Elements(
'Unununium',
'Uuu',
'111',
'(272.0) amu',
'Unknown',
'Unknown',
'111',
'161',
'Transition Metal',
'Unknown',
'Unknown',
'Unknown',
{'Year':'1994','Discoverer':'S. Hofmann','NameOrigin':'Un (one) un (one) un (one) ium'},
'No uses known',
'Man-made'
)

Elements=[actinium, aluminum, americium, antimony, argon, arsenic, astatine, barium, berkelium, beryllium, bismuth, bohrium, boron, bromine, cadmium, calcium, californium, carbon, cerium, cesium, chlorine, chromium, cobalt, copper, curium, dubnium, dysprosium, einsteinium, erbium, europium, fermium, fluorine, francium, gadolinium, gallium, germanium, gold, hafnium, hassium, helium, holmium, hydrogen, indium, iodine, iridium, iron, krypton, lanthanum, lawrencium, lead, lithium, lutetium, magnesium, manganese, meitnerium, mendelevium, mercury, molybdenum, neodymium, neon, neptunium, nickel, niobium, nitrogen, nobelium, osmium, oxygen, palladium, phosphorus, platinum, plutonium, polonium, potassium, praseodymium, promethium, protactinium, radium, radon, rhenium, rhodium, rubidium, ruthenium, rutherfordium, samarium, scandium, seaborgium, selenium, silicon, silver, sodium, strontium, sulfur, tantalum, technetium, tellurium, terbium, thallium, thorium, thulium, tin, titanium, tungsten, ununbium, ununnilium, unununium, uranium, vanadium, xenon, ytterbium, yttrium, zinc, zirconium]


Rare_Earth_Elements=[actinium, americium, berkelium, californium, cerium, curium, dysprosium, einsteinium, erbium, europium, fermium, gadolinium, holmium, lanthanum, lawrencium, lutetium, mendelevium, neodymium, neptunium, nobelium, plutonium, praseodymium, promethium, protactinium, samarium, terbium, thorium, thulium, uranium, ytterbium]
Noble_Gases=[argon, helium, krypton, neon, radon, xenon]
Rare_Gases=Noble_Gases
Alkali_Metals=[cesium, francium, lithium, potassium, rubidium, sodium]
Alkaline_Earth_Metals=[barium, beryllium, calcium, magnesium, radium, strontium]
Non_Metals=[carbon, nitrogen, oxygen, phosphorus, selenium, sulfur]
Halogens=[astatine, bromine, chlorine, fluorine, iodine]
Others=[aluminum, bismuth, gallium, indium, lead, thallium, tin]
Metalloids=[antimony, arsenic, boron, germanium, polonium, silicon, tellurium]
Transition_Metals=[bohrium, cadmium, chromium, cobalt, copper, dubnium, gold, hafnium, hassium, iridium, iron, manganese, meitnerium, mercury, molybdenum, nickel, niobium, osmium, palladium, platinum, rhenium, rhodium, ruthenium, rutherfordium, scandium, seaborgium, silver, tantalum, technetium, titanium, tungsten, ununbium, ununnilium, unununium, vanadium, yttrium, zinc, zirconium]

#Assigning Object Properties for their Symbols
Ac=actinium; Al=aluminum; Am=americium; Sb=antimony; Ar=argon; As=arsenic; At=astatine; Ba=barium; Bk=berkelium; Be=beryllium; Bi=bismuth; Bh=bohrium; B=boron; Br=bromine; Cd=cadmium; Ca=calcium; Cf=californium; C=carbon; Ce=cerium; Cs=cesium; Cl=chlorine; Cr=chromium; Co=cobalt; Cu=copper; Cm=curium; Db=dubnium; Dy=dysprosium; Es=einsteinium; Er=erbium; Eu=europium; Fm=fermium; F=fluorine; Fr=francium; Gd=gadolinium; Ga=gallium; Ge=germanium; Au=gold; Hf=hafnium; Hs=hassium; He=helium; Ho=holmium; H=hydrogen; In=indium; I=iodine; Ir=iridium; Fe=iron; Kr=krypton; La=lanthanum; Lr=lawrencium; Pb=lead; Li=lithium; Lu=lutetium; Mg=magnesium; Mn=manganese; Mt=meitnerium; Md=mendelevium; Hg=mercury; Mo=molybdenum; Nd=neodymium; Ne=neon; Np=neptunium; Ni=nickel; Nb=niobium; N=nitrogen; No=nobelium; Os=osmium; O=oxygen; Pd=palladium; P=phosphorus; Pt=platinum; Pu=plutonium; Po=polonium; K=potassium; Pr=praseodymium; Pm=promethium; Pa=protactinium; Ra=radium; Rn=radon; Re=rhenium; Rh=rhodium; Rb=rubidium; Ru=ruthenium; Rf=rutherfordium; Sm=samarium; Sc=scandium; Sg=seaborgium; Se=selenium; Si=silicon; Ag=silver; Na=sodium; Sr=strontium; S=sulfur; Ta=tantalum; Tc=technetium; Te=tellurium; Tb=terbium; Tl=thallium; Th=thorium; Tm=thulium; Sn=tin; Ti=titanium; W=tungsten; Uub=ununbium; Uun=ununnilium; Uuu=unununium; U=uranium; V=vanadium; Xe=xenon; Yb=ytterbium; Y=yttrium; Zn=zinc; Zr=zirconium;



def compare(elem1,elem2):
    
    try:
        
        i,j=elem1,elem2
        size=len(max(["AtomicNumber","Classification","CrystalStructure"],key=len))
    
        size1=len(max([i.Classification,i.CrystalStructure,i.Density],key=len))
        print("="*(len(i.Name)+len(j.Name)+size+size1+len("Property")+3))
        print("Property",end=' '*(size-len("Property")+2));print("| ",end='');print(i.Name,j.Name,sep=' '*(size1-len(elem1.Name)+4))
        print("#"*(len(i.Name)+len(j.Name)+size+size1+len("Property")+3))
        print("Symbol",end=' '*(size-len("Symbol")+2));print("| ",end='');print(i.Symbol,j.Symbol,sep=' '*(size1-len(elem1.Symbol)+4))
        print("AtomicNumber",end=' '*(size-len("AtomicNumber")+2));print("| ",end='');print(i.AtomicNumber,j.AtomicNumber,sep=' '*(size1-len(str(elem1.AtomicNumber))+4))
        print("AtomicMass",end=' '*(size-len("AtomicMass")+2));print("| ",end='');print(i.AtomicMass,j.AtomicMass,sep=' '*(size1-len(elem1.AtomicMass)+4))
        print("Classification",end=' '*(size-len("Classification")+2));print("| ",end='');print(i.Classification,j.Classification,sep=' '*(size1-len(elem1.Classification)+4))
        print("CrystalStructure",end=' '*(size-len("CrystalStructure")+2));print("| ",end='');print(i.CrystalStructure,j.CrystalStructure,sep=' '*(size1-len(elem1.CrystalStructure)+4))
        print("Density",end=' '*(size-len("Density")+2));print("| ",end='');print(i.Density,j.Density,sep=' '*(size1-len(elem1.Density)+4))
        print("Color",end=' '*(size-len("Color")+2));print("| ",end='');print(i.Color,j.Color,sep=' '*(size1-len(elem1.Color)+4))
        print("="*(len(i.Name)+len(j.Name)+size+size1+len("Property")+3))
        
    except:
        
        raise AssertionError("Got String.Expected Element Type")
    

    
#  Got from the Package "https://pypi.python.org/pypi/periodic" Thanks to that Guy

Table = '''      -----                                                               -----
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
              -------------------------------------------------------------'''    



# End Of Module