from os import listdir
from os.path import isfile, join

path = 'collection'
collection = []
teacher = []

for flist in listdir(path):
    if isfile(join(path, flist)):
        with open(path + '/' + flist) as f:
            content = [x.strip('\n') for x in f.readlines()]
            data = [x.split() for x in content]
            teacher.extend([data.pop(0)])
            item = []
            for x in data:
                item.extend(x)
            collection.extend([item])

# print teacher
# print collection
