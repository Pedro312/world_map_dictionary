###m #
#World Map Project
#
#Author: Pedro
####

import sys
world_map = {
#Room1
    'mentr':{
        'NAME': 'Mall Entrance',
        'DESCRIPTION': ' You are in the front mall entrance. Behind you are the \
mall front doors, but they are nailed shut.',
        'PATHS':{
            'west':'food',
            'east':'elev',
            'north':'hw'
        }
    },
    #Room2
    'food':{
        'NAME':'Food Court',
        'DESCRIPTION': ' There are tons of empty tables. The light is flickering.',
        'PATHS':{
            'east':'mentr',
            'west':'wfr',
            'south':'bath'
        }
    },
    #Room3
    'elev':{
        'NAME':'Elevator',
        'DESCRIPTION': ' It\'s an elevator. The power is down.',
        'PATHS':{
            'west':'mentr'
        }
    },
    #Room4
    'hw':{
        'NAME':'Hallway',
        'DESCRIPTION':' It\'s a long hallway.',
        'PATHS':{
            'south':'mentr',
            'east':'hw2',
            'north':'ftl',
            'west':'jail'
            }
    },
    #Room5
    'wfr':{
        'NAME':'Wet Floor',
        'DESCRIPTION':' The floor is significantly moist.',
        'PATHS':{
            'east':'food'
        }
    },
    #Room6
    'hw2':{
        'NAME':'Hallway',
        'DESCRIPTION':' It\'s a long hallway.',
        'PATHS':{
            'west':'hw',
            'north':'pp',
            'south':'hg',
            'east':'pa'
        }
    },
    #Room7
    'ftl':{
        'NAME':'Footlocker',
        'DESCRIPTION':' It\'s a store. There are shoes thrown all over the ground \
and fairly large footprints,',
        'PATHS':{
            'south':'hw'
        }
    },
    #Room8
    'bath':{
        'NAME':'Bathroom',
        'DESCRIPTION':' It\'s a bathroom. The stalls are locked and the mirror is shattered.',
        'PATHS':{
            'north':'food'
        }
    },
    #Room9
    'jail':{
        'NAME':'Mall Jail',
        'DESCRIPTION':' This is the mall jail. It is extremely cold, and a\
badge is gleaming on the desk.',
        'PATHS':{
            'east':'hw'
        }
    },
    #Room10
    'pp':{
        'NAME':"Pretzel Palace",
        'DESCRIPTION':'There is a cold\
 pretzel on the counter, and the cash register is empty.',
        'PATHS':{
            'south': 'hw2',
            'north':'kc'
            }
    },
    #Room11
    'kc':{
        'NAME':'Kitchen',
        'DESCRIPTION':"It's a kitchen. There\
 is a freezer towards the back and pans on the ground.",
        'PATHS':{
            'north' : 'frz',
            'south' : 'pp'
            }
    },
    #Room12
    'frz':{
        'NAME':'Freezer',
        'DESCRIPTION': "It is extremely\
 cold (obviously, it's a freezer) and to your right there are frozen\
 water bottles.",
        'PATHS':{
            'south' : 'kc'
        }
    },
    #Room13
    'hg':{
        'NAME': 'Hunting Goods',
        'DESCRIPTION':"It's a hunting shop. There are\
 firearms hung on the walls and on the counters.",
        'PATHS':{
            'north' : 'hw2'
        }
    },
    #Room14
    'hw3':{
        'NAME':'Hallway',
        'DESCRIPTION':'It\'s a long hallway.',
        'PATHS':{
            'west':'pa',
            'north':'fa',
            'south':'co',
            'east':'hbp'
        }
    },
    #Room15
    'pa':{
        'NAME':'Play Area',
        'DESCRIPTION':"There are\
 multiple obstacle courses for children, but a few are broken in half\
 and most have spider webs.",
        'PATHS':{
            'north': 'ts',
            'south' : 'jwr',
            'west':'hw2',
            'east':'hw3'
        }
    },
    #Room16
    'jwr':{
        'NAME':'Jewelry Store',
        'DESCRIPTION':"There are\
 diamond rings in the glass cases, and a sparkling diamond necklace\
 sitting alone on a counter top.",
        'PATHS':{
            'north':'pa'
        }
    },
    #Room17
    'ts':{
        'NAME':'Toy Store',
        'DESCRIPTION':"This room seems to\
 be oddly clean, compared to the rest. Although some\
 shelves are still snapped.",
        'PATHS':{
            'south':'pa'
        }
    },
    #Room18
    'ws':{
        'NAME':'Weapon Storage',
        'DESCRIPTION':"There are\
 racks of weapons on the walls and alligned on shelves, and stacks of\
 ammunition in the corner of the room.",
        'PATHS':{
            'north':'hg'
        }
    },
    #Room19
    'co':{
        'NAME':'Clothing Outlet',
        'DESCRIPTION':"There is \
tons of clothes thrown on the ground, and all the metal racks\
are flipped over.",
        'PATHS':{
            'north':'hw3'
        }
    },
    #Room20
    'hbp':{
        'NAME':'Hli\'s Beauty Products',
        'DESCRIPTION':"A\
 very neat beauty store, with makeup products on  the shelves,\
 and clothing hanging on racks organized by color. A nametag reading 'Hli'\
 is lying on the counter.",
        'PATHS':{
            'west':'hw3'
        }
    }
}

#static variables
node = world_map['mentr']
is_alive = True
directions = ['north','south','east','west','up','down']
short_directions = ['n','s','e','w','u','d']

#Controller
while is_alive:
    #print room name and description
    print node['NAME']
    print node['DESCRIPTION']
    
    #Ask for input
    command = raw_input('> ')
    if command in ['q','quit','exit']:
        sys.exit(0)
    
        #Allows us to change nodes
    if command in short_directions:
        command = directions[short_directions.index(command)]
    try:
        node = world_map[node['PATHS'][command]]
    except:
        print 'You can\'t'