import xml.etree.ElementTree as ET

class NEIGHBOR():
    def __init__(self):
        self.name=''
        self.direction=''

class COUNTRY():
    def __init__(self):
        self.rank = []
        self.name=''
        self.neighbor=[]

class GSV():
    def __init__(self):
        self.country = []
        
    def xmlparse(self,path):
        tree = ET.parse(path)
        root = tree.getroot()
        
        for c in root.findall('country'):
            country = COUNTRY()
            
            # name
            country.name = c.get('name')
            
            # rank
            country.rank.append(c.find('rank').text)
            
            # get all neighbor in country
            for n in c.findall('neighbor'):
                neighbor = NEIGHBOR()
                neighbor.name = n.get('name')
                neighbor.direction = n.get('direction')
                country.neighbor.append(neighbor)
                
            self.country.append(country)


# start
gsv=GSV()
gsv.xmlparse('country_data.xml')

#print(repr(root))
print(dir(gsv))

print("")
for country in gsv.country:
    print("country: {:s}".format(country.name))
    for rank in country.rank:
        print("rank: {:s}".format(rank))
        
    for neighbor in country.neighbor:
        print("neighbor: {:s}, direction: {:s}".format(neighbor.name, neighbor.direction))
    print("")

#for child in root:
    #print child.tag, child.attrib
