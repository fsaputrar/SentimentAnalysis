import csv
import math

class FeatureSelection:

    def __init__(self,selection):
        self.selection = selection

    def seleksifitur(self):
        sortedx = sorted(self.selection, key=lambda x: x[1], reverse=True)
        #print sortedx
        panjangfitur = len(sortedx)
        sample = math.ceil(panjangfitur * 0.85)
        pearsonsample = sortedx[:int(sample)]
        return pearsonsample

    def fitur(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\output\ekstrakfiturbaku.csv", "rb") as f:
            fiturReader = csv.reader(f)
            fiturs = [fitur for fitur in fiturReader]
            list_fitur = []
            sorting = self.seleksifitur()
            for urut in sorting:
                found = False
                for fitur in fiturs:
                    if fitur[0] == urut[0]:
                        list_fitur.append(fitur)
                        found = True
                        break
                if not found:
                    list_fitur.append(0)
            sortedx = sorted(list_fitur, key=lambda x: x[0][0], reverse=False)
        return sortedx

with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\output\NilaiPearsons.csv", "rb") as f:
    pearsoncsv = csv.reader(f)
    pearson = [x for x in pearsoncsv]
    pearson.insert(0, pearson[0])

fs = FeatureSelection(pearson)
fs.seleksifitur()

with open('C:\Users\ACER\PycharmProjects\ProgramBismillah\output\SelectionData85%.csv','wb') as selectionlatih:
    selectionslatih = csv.writer(selectionlatih)
    seleksilatih = fs.fitur()
    for x in seleksilatih:
        selectionslatih.writerow(x)