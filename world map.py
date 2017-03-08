
####
#World Map Project
#
#Author: Pedro
####

import sys
world_map = {
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
    'food':{
        'NAME':'Food Court',
        'DESCRIPTION': ' There are tons of empty tables. The light is flickering.',
        'PATHS':{
            'east':'mentr',
            'west':'wfr',
            'south':'bath'
        }
    },
    'elev':{
        'NAME':'Elevator',
        'DESCRIPTION': ' It\'s an elevator. The power is down.',
        'PATHS':{
            'west':'mentr'
        }
    },
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
    'wfr':{
        'NAME':'Wet Floor',
        'DESCRIPTION':' The floor is significantly moist.',
        'PATHS':{
            'east':'food'
        }
    },
    'hw2':{
        'NAME':'Hallway',
        'DESCRIPTION':' It\'s a long hallway.',
        'PATHS':{
            'west':'hw'
        }
    },
    'ftl':{
        'NAME':'Footlocker',
        'DESCRIPTION':' It\'s a store. There are shoes thrown all over the ground \
and fairly large footprints,',
        'PATHS':{
            'south':'hw'
        }
    },
    'bath':{
        'NAME':'Bathroom',
        'DESCRIPTION':' It\'s a bathroom. The stalls are locked and the mirror is shattered.',
        'PATHS':{
            'north':'food'
        }
    },
    'jail':{
        'NAME':'Mall Jail',
        'DESCRIPTION':' This is the mall jail. It is extremely cold, and a\
badge is gleaming on the desk.',
        'PATHS':{
            'east':'hw'
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
