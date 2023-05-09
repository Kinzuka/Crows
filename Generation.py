level_width = 40
level_length = 60


import random


def create_level():
  level = {}
  for i in range(level_width):
    row = []
    for j in range(level_length):
      row.append(0)
    level['row_'+str(i)] = row
  return level

def create_room():
  k = 1
  room = []
  room_width = random.choice(range(3,20))
  room_length = random.choice(range(3,13))
  for i in range(room_width):
    row = []
    for j in range(room_length):
      if k == 1:
        row.append(-1)
        k-=1
      row.append(1)
    room.append(row)
  row = room[len(room)//2]
  centre_tile = row[len(row)//2]
  for i in range(random.choice([1,2,3])):
    room_width = random.choice(range(3,7))
    room_length = random.choice(range(3,7))
    for b in range(len(room)//2,room_width):
      try: 
        row = room[b]
        for a in range(len(row)//2,room_length):
          try: row[a] = 1
          except IndexError:
            row.append(1)
      except IndexError:
        room.append([])
        row = room[b]
        for a in range(len(row)//2,room_length):
          try: row[a] = 1
          except IndexError:
            row.append(1)
  return room

  





def floor_map():
  room_no = random.choice([1,2,3,4,5])
  level = create_level()
  for i in range(room_no):
    room = create_room()
    x = random.choice(range(len(list(level.keys()))))
    row = level['row_'+str(x)]
    start_tile = random.choice(row)
    start_tile_index = row.index(start_tile)
    for a in range(len(room)):
      try: row = level['row_'+str(a+x)]
      except KeyError:
        x = -(a-1)
      room_row = room[a]
      for b in range(len(room_row)):
        try: row[b+start_tile_index] = room_row[b]
        except IndexError:
          pass  

  return level





###STEP 2
# for walls

def dir_check(tile):
  pass