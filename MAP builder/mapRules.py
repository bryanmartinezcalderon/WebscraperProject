from __future__ import print_function


class building:
    MSG='TRUE'
#object attributes
    x=0
    y=0
    item_size=0
    item_hitpoints=0

    item_damage_per_second=0
    item_range=0
    item_damage_type='N/A'
    item_targets='N/A'
    item_favorite_target='any'
    building_type='normal'
    ALL_damage_type=[
        'single',
        'N/A'
        ]

    ALL_targets=[
        'ground',
        'air',
        'N/A'
        ]
    ALL_favorite_target=[
        'any',
        'N/A'
        ]
    ALL_building_type=[
        'normal',
        'weapon'
        ]

#CREATOR
#   Compulsory attributes 
#       x
#       y
#       item_size 
#       item_hitpoints
#       building_type
#   Additional weapon attributes
#       item_damage_per_second
#       item_range
#       item_damage_type
#       item_targets
#       item_favorite_target

    def __init__(self,item_hitpoints,building_type,item_size,[x,y]=[-1,-1],item_damage_per_second=0,item_range=0,item_damage_type='N/A',item_targets='N/A',item_favorite_target='N/A'):
        """Initializes the weapon."""
        self.x=x
        self.y=y
        self.item_size=item_size
        self.item_hitpoints=item_hitpoints
        self.building_type=building_type
        #Weapon attributes
        print(building_type)
        if building_type == 'weapon':
            self.item_damage_per_second=item_damage_per_second
            self.item_range=item_range
            self.item_damage_type=item_damage_type
            self.item_targets=item_targets
            self.item_favorite_target=item_favorite_target
        print("(Building Initialized)")

    def setHitpoints(self,item_hitpoints):
        self.item_hitpoints=item_hitpoints

    def getHitpoints(self,item_hitpoints):
        return self.item_hitpoints

    def getlocation(self):
        return [x,y]
    def setlocation(self,[x,y]):
        self.x=x
        self.y=y

    def setitemattributes(self,item_hitpoints,item_damage_per_second,item_range,item_damage_type,item_targets,item_favorite_target):
        if idigit(item_damage_per_second) and isdigit(item_hitpoints) and isdigit(item_range):   
            self.item_damage_per_second=item_damage_per_second
            self.item_hitpoints=item_hitpoints
            self.item_range=item_range
        else:
            self.MSG='FALSE'
        if isascii(item_damage_type) and isascii(item_targets) and isascii(item_favorite_target):
            if item_damage_type in ALL_damage_type:
                self.item_damage_type=item_damage_type
            else: 
                print("ERR:(invalid damage_type)")
                self.MSG='FALSE'
            if item_targets in ALL_targets:
                self.item_targets=item_targets
            else: 
                print("ERR:(invalid targets)")
                self.MSG='FALSE'
            if item_favorite_target in ALL_favorite_target:
                self.item_favorite_target=item_favorite_target
            else: 
                print("ERR:(invalid favorite_target)")
                self.MSG='FALSE'
    def getMSG(self):
        return self.MSG
    def setMSG(self,MSG):
        self.MSG=MSG

class MAP:

#MAP attributes:
    amount_of_components=0
    name=''
    Map_width=43
    Map_height=43
    Mymap = [0] * Map_width
    for i in range(Map_height):
        Mymap[i] = [0] * Map_width
    
#Creator
    def __init__(self, name):
        """Initializes the Map."""
        self.name = name
        print("(Initializing {})".format(self.name))
       
            
    def printmap(self):
        print("(Printing {})".format(self.name))
        for i in range(self.Map_height):
            print("|", end="")
            for j in range(self.Map_width):
                print(self.Mymap[i][j], end="")
            print("|")

    def resetmap(self):
        print("(Reseting {})".format(self.name))
        for i in range(self.Map_height):
            self.Mymap[i] = [0] * self.Map_width

    def place_building(self,building):
        freebool=0
        print("item size",building.item_size)
        for i in range(building.item_size):
            for j in range (building.item_size):
                freebool=freebool+self.Mymap[building.x+i][building.y+j]
        if freebool >0:
            building.setMSG('FALSE')
        elif building.building_type=='weapon':
            for i in range(building.item_size):
                for j in range (building.item_size):
                    self.Mymap[building.x+i][building.y+j]=1
            self.Mymap[building.x+1][building.y+1]=2
            self.amount_of_components+=1
        else:
            print("building.building_type",building.building_type)
            for i in range(building.item_size):
                for j in range (building.item_size):
                    self.Mymap[building.x+i][building.y+j]=9
            self.amount_of_components+=1         


