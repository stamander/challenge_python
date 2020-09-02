e2f = {'dog':'chien','cat':'chat','walrus':'mouse'}
print(e2f)

f2e= {}

for english , french in e2f.items():
  f2e[french]= english

print(f2e['chien'])


