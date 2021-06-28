import random
import numpy
import imdbscraper

def info(id: int):
    actor = imdbscraper.Name(id)
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("ID: " + str(actor.id))
    print("URL: " + str(actor.url))
    print("Name: " + str(actor.name))
    print("Birthday: " + str(actor.birthday))
    print("Birthplace: " + str(actor.birthplace))
    print("Birthname: " + str(actor.birth_name))
    print("Height: " + str(actor.height))


id_list = numpy.zeros(5, int)

random.seed()
for x in range(len(id_list)):
    id_list[x] = random.randrange(1, 1000)


for id in id_list:
    info(id)
