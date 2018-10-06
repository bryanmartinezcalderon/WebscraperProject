class Townhall_l3:
	size=4
	hitpoints=1850
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)

class Canon_l4:
	size=3
	hitpoints=570
	def __init__(self):
        Building.__init__(self.hitpoints,'weapon',self.size)

class Tower_l3:
	size=3
	hitpoints=460
	def __init__(self):
        Building.__init__(self.hitpoints,'weapon',self.size)

class Hut:
	size=2
	hitpoints=250
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)


class Resource_l5:
	size=3
	hitpoints=560
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)

class Storage_l5:
	size=3
	hitpoints=1200
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)

class Camp_l2:
	size=3
	hitpoints=270
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)

class Baracks_l3:
	size=1
	hitpoints=300
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)

class Wall_l1:
	size=1
	hitpoints=300
	def __init__(self):
        Building.__init__(self.hitpoints,'normal',self.size)



mymap=MAP("mymap")



townhall=building(,12,2,300,'normal')


canon1=building(12,12,3,300,'weapon')
hut1=building(12,12,2,300,'normal')
mymap.place_building(canon1)
mymap.printmap()
mymap.place_building(hut1)
mymap.printmap()
print(hut1.getMSG())
print(1.getMSG())


	hut1,
	hut2,
	elixir1,
	elixir2,
	mine1,
	mine2,
	baracks1,
	baracks2,
	camp1,
	camp2
	wall1,
	wall2,
	wall3,
	wall4,
	wall5,
	wall6,
	wall7,
	wall8,
	wall9,
	wall10,
	wall11,
	wall12,
	wall13,
	wall14,
	wall15,
	wall16,
	wall17,
	wall18,
	wall19,
	wall20,
	wall21,
	wall22,
	wall23,
	wall24,
	wall25