from __future__ import division
import csv
import math


class Pengujian:

    def __init__(self,docs):
        self.docs = docs

    def confussionmatrix(self):
        tp = tn = fp = fn = 0
        for dok in self.docs:
            if dok[2].lower() == 'positif' and dok[3].lower() == "positif":
                tp += 1
            elif dok[2].lower() == 'positif' and dok[3].lower() == "negatif":
                fp += 1
            elif dok[2].lower() == 'negatif' and dok[3].lower() == "positif":
                fn += 1
            elif dok[2].lower() == 'negatif' and dok[3].lower() == "negatif":
                tn += 1

        self.tp = tp
        self.fp = fp
        self.fn = fn
        self.tn = tn

    def Precission(self):
        cm = self.confussionmatrix()
        tp = self.tp
        fp = self.fp
        fn = self.fn
        tn = self.tn

        precissionpos = ((tp) / (tp+fp))
        precissionneg = (tn / (tn+fn))
        self.precission = precissionpos
        print precissionpos
        return

    def Recall(self):
        cm = self.confussionmatrix()
        tp = self.tp
        fp = self.fp
        fn = self.fn
        tn = self.tn

        recall = ((tp) / (tp+fn))
        print recall
        self.recall =recall

    def FMeasure(self):
        cm = self.confussionmatrix()
        tp = self.tp
        fp = self.fp
        fn = self.fn
        tn = self.tn

        pr = self.Precission()
        rc = self.Recall()

        p = self.precission
        r = self.recall

        fm = ((2*p*r) / (p+r))
        print fm
        return fm

    def accuracy(self):
        cm = self.confussionmatrix()
        tp = self.tp
        fp = self.fp
        fn = self.fn
        tn = self.tn
        print tp,tn,fn,fp

        accuracy = ((tp+tn)/(tp+fp+fn+tn)) * 100
        print "akurasi :" , accuracy,"%"


with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\data\datauji85%.csv",
          "rb") as data:
    x = csv.reader(data)
    docs = []
    for i in x:
        docs.append(i)

    k = Pengujian(docs)
    #k.confussionmatrix()
    k.accuracy()
    k.Precission()
    k.Recall()
    k.FMeasure()