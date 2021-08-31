import enum

class countrys(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 244
    Angola = 244
    Antacitia = 672


for country in (countrys):
    print(country)

print(countrys(244))