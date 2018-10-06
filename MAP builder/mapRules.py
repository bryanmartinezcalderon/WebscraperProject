from __future__ import print_function
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
            
    def place_weapon(self,x,y):
        freebool=self.Mymap[x][y]#+self.Mymap[x+1][y]+self.Mymap[x+2][y]+self.Mymap[x][y+1]+self.Mymap[x][y+2]+self.Mymap[x+1][y+1]+self.Mymap[x+1][y+2]+self.Mymap[x+2][y+1]+self.Mymap[x+2][y+2]
        if freebool >0:
            MSG=FALSE
        else:
            #weapon.__init__(self,x, y,item_damage_per_second,item_hitpoints,item_range,item_damage_type,item_targets,item_favorite_target)
            self.Mymap[x][y]=1
            self.Mymap[x+1][y]=1
            self.Mymap[x+2][y]=1
            self.Mymap[x][y+1]=1
            self.Mymap[x][y+2]=1
            self.Mymap[x+1][y+1]=1
            self.Mymap[x+1][y+2]=1
            self.Mymap[x+2][y+1]=1
            self.Mymap[x+2][y+2]=1
            self.amount_of_components+=1
            MSG='TRUE'
        return MSG

    def place_other(x,y,item_size,item_hitpoints):
        freebool=0
        for i in range(item_size):
            for j in range (item_size):
                freebool=freebool+self.Mymap[x+i,y+j]
        if freebool >0:
            MSG='FALSE'
        else:
            for i in range(item_size):
                for j in range (item_size):
                    self.Mymap[x+i][y+j]=9
            self.amount_of_components+=1
            MSG='TRUE'
        return MSG

class weapon:
    item_damage_per_second=0
    item_hitpoints=0
    item_range=0
    item_damage_type=0
    item_targets=0
    item_favorite_target=0
    def __init__(self, item_damage_per_second,item_hitpoints,item_range,item_damage_type,item_targets,item_favorite_target):
        """Initializes the weapon."""
        self.item_damage_per_second=item_damage_per_second
        self.item_hitpoints=item_hitpoints
        self.item_range=item_range
        self.item_damage_type=item_damage_type
        self.item_targets=item_targets
        self.item_favorite_target=item_favorite_target
        print("(Initializing weapon)")
    def setitemattributes(self,item_damage_per_second,item_hitpoints,item_range,item_damage_type,item_targets,item_favorite_target):
        self.item_damage_per_second=item_damage_per_second
        self.item_hitpoints=item_hitpoints
        self.item_range=item_range
        self.item_damage_type=item_damage_type
        self.item_targets=item_targets
        self.item_favorite_target=item_favorite_target

class building:
    item_hitpoints=0
    item_size=0
    def __init__(self,item_size,item_hitpoints):
        """Initializes the weapon."""
        self.item_hitpoints=item_hitpoints
        self.item_size=item_size
        print("(Initializing building)")
    def setitemattributes(self,item_hitpoints):
        self.item_hitpoints=item_hitpoints

mymap=MAP("mymap")
mymap.printmap()
canon1=weapon(5,1,1,1,1,1)
mymap.place_weapon(1,1)
mymap.printmap()
mymap.resetmap()
mymap.printmap()

