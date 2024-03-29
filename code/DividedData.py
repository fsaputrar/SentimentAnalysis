import csv

class DividedData:

    def __init__(self, fiturs):
        self.fiturs = fiturs

    def datalatih(self):
        latih = []
        for x in self.fiturs:
            latih.append(x[0:401])
        return latih

    def datauji(self):
        uji = []
        for x in self.fiturs:
            a = x[:1] + x[-100:]
            #a = x[:1] + x[-5:-4] + x[-4:-3]
            #a = [x[0], x[-90]] #1 data uji
            uji.append(a)
        return uji

with open("C:\Users\ACER\PycharmProjects\Skripsimaster\output\sfiturrdb\SelectionData85%.csv", "rb") as f:
    dividedatacsv = csv.reader(f)
    data = [x for x in dividedatacsv]
    data.insert(0, data[0])

d = DividedData(data)
d.datauji()

with open('C:\Users\ACER\PycharmProjects\Skripsimaster\data\DataLatihBaru85%.csv','wb') as dtb:
    training = csv.writer(dtb)
    datalat = d.datalatih()
    datalat.pop(0)
    for x in datalat:
        training.writerow(x)

with open('C:\Users\ACER\PycharmProjects\Skripsimaster\data\DataUjiBaru85%.csv','wb') as dub:
    testing = csv.writer(dub)
    datatest = d.datauji()
    datatest.pop(0)
    for x in datatest:
        testing.writerow(x)