from __future__ import division

import codecs
import csv
from prettytable import PrettyTable
from prettytable import from_csv

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

        precission = (((tp) / (tp+fp)) *100)
        self.precission = precission
        print "Precision :", precission,'%'

    def Recall(self):
        cm = self.confussionmatrix()
        tp = self.tp
        fn = self.fn

        recall = ((tp) / (tp+fn))*100
        self.recall =recall
        print "Recall :", recall,"%"

    def FMeasure(self):
        cm = self.confussionmatrix()

        p = self.precission
        r = self.recall

        fm = ((2*p*r) / (p+r))
        print "F-Measure :", fm,"%"

    def accuracy(self):
        cm = self.confussionmatrix()
        tp = self.tp
        fp = self.fp
        fn = self.fn
        tn = self.tn
        print "True Positif :",tp
        print "True Negatif :", tn
        print "False Positif :", fp
        print "False Negatif :", fn
        print "-------------------------------------------------------------"
        accuracy = ((tp+tn)/(tp+fp+fn+tn)) * 100
        print "Accuracy :" , accuracy,"%"

    def home(self):
        print "-------------------------------------------------------------------------"
        print "Analisis Sentimen Opini Film Ensemble Features + BoW dan Seleksi Fitur PCC"
        print "-------------------------------------------------------------------------"

        file_path = "C:\Users\ACER\PycharmProjects\Skripsimaster\data\dbaku\sf85%\datauji85%.csv"
        table = PrettyTable
        csv_file = open(file_path)
        x = from_csv(csv_file)
        print x
        #table.field_names = ['ID','Tweet','Prediksi','Sistem (GT)']
            # docs = []
            # for i in x:
            #     docs.append(i)
            #     print tabulate([i], headers=['ID', 'Tweet', 'Prediksi', 'Sistem'])
        print "-------------------------------------------------------------"

with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\dbaku\sf85%\datauji85%.csv",
          "rb") as data:
    x = csv.reader(data)
    docs = []
    for i in x:
        docs.append(i)

    k = Pengujian(docs)
    k.home()
    k.accuracy()
    k.Precission()
    k.Recall()
    k.FMeasure()