heros = ['spider man','thor','hulk','iron man','captain america']
print(len(heros))

heros.append('black panther')
print(heros)

heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

heros.remove('thor')
heros.remove('hulk')
heros.insert(1,'doctor strange')
print(heros)

heros.sort()
print(heros)
