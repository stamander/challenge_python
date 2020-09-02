
pythons = {
  'Champman':'Graham',
  'Cleese':'John',
  'Idle':'Eric',
  'Jones':'Terry',
  'Palin':'Michael'
}


others = {'Marx':'Grousho','Howard':'Moe'}


pythons.update(others)

print(pythons)


del pythons['Marx']
del pythons['Howard']


pythons = {}
print(pythons)