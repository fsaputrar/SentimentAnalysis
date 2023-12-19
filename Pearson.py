from __future__ import division
import csv
import math

class Pearsons:

    def __init__(self,fiturs,docs):
        self.fiturs = fiturs
        self.docs = docs

    def x_value(self):
        sumx = []
        for fitur in self.fiturs:
            x = sum([float(x) for x in fitur[1:401]])
            sumx.append(x)
        print sumx
        return sumx

    def x_pow(self):
        sumxp = []
        for fitur in self.fiturs:
            xval_pow = sum([float(x)**2 for x in fitur[1:401]])
            sumxp.append(xval_pow)
        print sumxp
        return sumxp

    def y_value(self):
        sumy = []
        for dokumen in self.docs:
            if dokumen[2].lower() == "positif":
                sumy.append(1)
            else:
                sumy.append(0)
        print sumy
        sigma_y = sum(sumy)
        print sigma_y
        return sigma_y

    def y_pow(self):
        sumy = []
        for dokumen in self.docs:
            if dokumen[2].lower() == "positif":
                sumy.append(1)
            else:
                sumy.append(0)
        ypow = []
        for x in sumy:
            ypow.append(x ** 2)
        sigmapow = sum(ypow)
        print sigmapow
        return sigmapow

    def xy_val(self):
        list_y = []
        for dokumen in self.docs:
            if dokumen[2].lower() == "positif":
                list_y.append(1)
            else:
                list_y.append(0)
        # print list_y
        sigmaxy = []
        for xyfitur in self.fiturs:
            xy = []
            for i, x in enumerate(list_y):
                xy.append(float(xyfitur[1:][i]) * list_y[i])
            sigmaxy.append(sum(xy))
        print sigmaxy
        return sigmaxy

    def pearson (self):
        list_y = []
        for dokumen in self.docs:
            if dokumen[2].lower() == "positif":
                list_y.append(1)
            else:
                list_y.append(0)
        # Assume len(x) == len(y)
        n = len(list_y)
        print n
        sigmax = self.x_value()
        sigmay = self.y_value()
        sigmaxpow = self.x_pow()
        sigmaypow = self.y_pow()
        sigmaxy = self.xy_val()
        rpxy_list = []
        for i, v in enumerate(sigmax):
            rpxy_top = (n * sigmaxy[i]) - (sigmax[i] * sigmay)
            rpxy_bot = math.sqrt((n * sigmaxpow[i]) - (sigmax[i] ** 2)) * math.sqrt((n * sigmaypow) - (sigmay ** 2))
            if rpxy_bot == 0:
                rpxy_list.append(0)
            else:
                rpxy_list.append(abs(rpxy_top / rpxy_bot))
        print rpxy_list

        x = []
        for fitur in self.fiturs:
            x.append(fitur[0])
            a = [x ,rpxy_list]
            pairs = zip(*a)

            pearson = []
            for set in pairs:
                a = list(set)
                pearson.append(a)
        return pearson

fiturs = []
docs = []
with open("C:\Users\ACER\PycharmProjects\Skripsimaster\output\sfiturrdb\ekstrakfiturbaku.csv", "rb") as f:
    fiturcsv = csv.reader(f)
    fiturs = [x for x in fiturcsv]
    fiturs.insert(0, fiturs[0])

with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\datasetbakulatih.csv", "rb") as f:
    docscsv = csv.reader(f)
    docs = [x for x in docscsv]

p = Pearsons(fiturs, docs)
p.xy_val()

with open('C:\Users\ACER\PycharmProjects\Skripsimaster\output\NilaiPearsons1.csv','wb') as selection:
    selections = csv.writer(selection)
    seleksi = p.pearson()
    #seleksi.pop(0)
    for x in seleksi:
        selections.writerow(x)