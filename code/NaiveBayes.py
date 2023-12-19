from __future__ import division
import csv
import re
import math
from operator import mul

class Naive_Bayes:

    def __init__(self,fiturs,fituruji,docs):
        self.fiturs = fiturs
        self.docs = docs
        self.fituruji = fituruji

    def Prior(self):
        dokumen_pos = 0
        dokumen_neg = 0
        for dokumen in self.docs:
            if dokumen[2].lower() == 'positif':
                dokumen_pos += 1
            else:
                dokumen_neg += 1
        prior_pos = float(dokumen_pos) / len(self.docs)
        prior_neg = float(dokumen_neg) / len(self.docs)
        self.prior_pos = prior_pos
        self.prior_neg = prior_neg
        # print prior_pos
        # print prior_neg

    def BernoulliTrain(self):
        doc_pos = 0
        doc_neg = 0
        for doc in self.docs:
            if doc[2].lower() == 'positif':
                doc_pos += 1
            else:
                doc_neg += 1
        tot_neg = []
        tot_pos = []
        print "Fitur Bernoulli"
        for fitur in self.fiturs:
            if (fitur[0] == 'F1') or (fitur[0] == 'F2') or (fitur[0] == 'F3') or (
                    fitur[0] == 'F4') or (fitur[0] == 'F11') or (fitur[0] == 'F12'):
                print fitur[0]
                counter = 0
                pos = 0
                neg = 0
                for doc in self.docs:
                    if doc[2].lower() == 'positif':
                        pos += float(fitur[1:][counter])
                    else:
                        neg += float(fitur[1:][counter])
                    counter +=1
                tot_pos.append(pos)
                tot_neg.append(neg)
            
            pf_neg = []
            for neg in tot_neg:
                pf_neg.append((neg+1)/(doc_neg+2))

            pf_pos = []
            for pos in tot_pos:
                pf_pos.append((pos+1)/(doc_pos+2))

        # print pf_pos
        # print pf_neg
        self.bpf_pos = pf_pos
        self.bpf_neg = pf_neg

    def BernoulliTest(self):
        btrain = self.BernoulliTrain()
        a = []
        bpf_pos = []
        for c in self.bpf_pos:
            bpf_pos.append(c)

        bpf_neg = []
        for d in self.bpf_neg:
            bpf_neg.append(d)

        ab = []
        for fitur in self.fituruji:
            if (fitur[0] == 'F1') or (fitur[0] == 'F2') or (fitur[0] == 'F3') or (
                    fitur[0] == 'F4') or (fitur[0] == 'F11') or (fitur[0] == 'F12'):
                ab.append(fitur)

        d_neg = []
        d_pos = []
        for i, uji in enumerate(ab):
            f_pd_neg = []
            f_pd_pos = []
            for x in uji[1:]:
                f_pd_neg.append(round((bpf_neg[i] ** float(x)) * ((1 - bpf_neg[i]) ** (1 - float(x))), 5))
                f_pd_pos.append(round((bpf_pos[i] ** float(x)) * ((1 - bpf_pos[i]) ** (1 - float(x))), 5))
            d_neg.append(f_pd_neg)
            d_pos.append(f_pd_pos)
        # print d_neg
        # print d_pos

        positif = []
        for i, pos in enumerate(d_pos):
            positif.append(pos)

        blikelihood_pos = [reduce(mul, i) for i in zip(*positif)]
        # print blikelihood_pos
        self.blikelihood_pos = blikelihood_pos

        negatif = []
        for i, neg in enumerate(d_neg):
            negatif.append(neg)

        blikelihood_neg = [reduce(mul, i) for i in zip(*negatif)]
        # print blikelihood_neg
        self.blikelihood_neg = blikelihood_neg

    def Gaussian(self):
        doc_pos = 0
        doc_neg = 0
        for doc in self.docs:
            if doc[2].lower() == 'positif':
                doc_pos += 1
            else:
                doc_neg += 1

        average_neg = []
        average_pos = []
        print "Fitur Gaussian"
        for fitur in self.fiturs:
            if (fitur[0] == 'F5') or (fitur[0] == 'F6') or (fitur[0] == 'F18') or (fitur[0] == 'F19') or (
                    fitur[0] == 'F20') or (fitur[0] == 'F21') or (fitur[0] == 'F22') or (fitur[0] == 'F31') or (
                    fitur[0] == 'F32') or (fitur[0] == 'F33') or (fitur[0] == 'F34') or (fitur[0] == 'F35') or (fitur[0] == 'F36'):
                print fitur[0]
                counter = 0
                pos = 0
                neg = 0
                for doc in self.docs:
                    if doc[2].lower() == 'positif':
                        pos += float(
                            fitur[1:][counter])  # agar tahu indeks dokumen, maka doc dihubungkan dengan fitur fungsi counter
                    else:
                        neg += float(fitur[1:][counter])
                    counter += 1
                average_pos.append(pos / doc_pos)
                average_neg.append(neg / doc_neg)
        self.rata2_pos = average_pos
        self.rata2_neg = average_neg

        gfiturtrain = []
        for fitur in self.fiturs:
            if (fitur[0] == 'F5') or (fitur[0] == 'F6') or (fitur[0] == 'F18') or (fitur[0] == 'F19') or (
                    fitur[0] == 'F20') or (fitur[0] == 'F21') or (fitur[0] == 'F22') or (fitur[0] == 'F31') or (
                    fitur[0] == 'F32') or (fitur[0] == 'F33') or (fitur[0] == 'F34') or (fitur[0] == 'F35') or (
                    fitur[0] == 'F36'):
                gfiturtrain.append(fitur)

        var_pos = []
        var_neg = []
        for i, gauss in enumerate(gfiturtrain):
            varianpos = 0
            varianneg = 0
            for j,dokumen in enumerate(self.docs):
                if dokumen[2].lower() == "positif":
                    varianpos += (float(gauss[1:][j]) - average_pos[i]) ** 2
                else:
                    varianneg += (float(gauss[1:][j]) - average_neg[i]) ** 2
            var_pos.append(varianpos / doc_pos)
            var_neg.append(varianneg / doc_neg)

        self.v_pos = var_pos
        self.v_neg = var_neg

    def GaussianTesting(self):
        gauss = self.Gaussian()

        rt_pos = []
        for rtp in self.rata2_pos:
            rt_pos.append(rtp)

        rt_neg = []
        for rtn in self.rata2_neg:
            rt_neg.append(rtn)
        #print rt_neg

        v_pos = []
        for vp in self.v_pos:
            v_pos.append(vp)
        #print self.v_pos

        v_neg = []
        for vn in self.v_neg:
            v_neg.append(vn)
        #print v_neg

        gfiturtest = []
        for fitur in self.fituruji:
            if (fitur[0] == 'F5') or (fitur[0] == 'F6') or (fitur[0] == 'F18') or (fitur[0] == 'F19') or (
                    fitur[0] == 'F20') or (fitur[0] == 'F21') or (fitur[0] == 'F22') or (fitur[0] == 'F31') or (
                    fitur[0] == 'F32') or (fitur[0] == 'F33') or (fitur[0] == 'F34') or (fitur[0] == 'F35') or (
                    fitur[0] == 'F36'):
                #print fitur[0]
                gfiturtest.append(fitur)

        d_pos = []
        d_neg = []
        for i, fitur in enumerate(gfiturtest):
            f_pd_pos = []
            f_pd_neg = []
            for x in fitur[1:]:
                try:
                    exponent_pos = math.exp (- (math.pow (float(x) - rt_pos[i],2) / (2*v_pos[i])))
                    gauss_pos = (1/ (math.sqrt(2*math.pi * v_pos[i]))) * exponent_pos
                except ZeroDivisionError:
                    gauss_pos = 1

                try:
                    exponent_neg = math.exp(- (math.pow(float(x) - rt_neg[i], 2) / (2 * v_neg[i])))
                    gauss_neg = (1 / (math.sqrt(2 * math.pi * v_neg[i]))) * exponent_neg
                except ZeroDivisionError:
                    gauss_neg = 1
                f_pd_pos.append(gauss_pos)
                f_pd_neg.append(gauss_neg)
            d_pos.append(f_pd_pos)
            d_neg.append(f_pd_neg)

        # print d_pos
        # print d_neg

        positif = []
        for i, pos in enumerate(d_pos):
            positif.append(pos)
        # print positif

        gausslikelihood_pos = [reduce(mul, i) for i in zip(*positif)]
        #print gausslikelihood_pos
        self.gausslikelihood_pos = gausslikelihood_pos

        negatif = []
        for i, neg in enumerate(d_neg):
            negatif.append(neg)
        # print positif

        gausslikelihood_neg = [reduce(mul, i) for i in zip(*negatif)]
        #print gausslikelihood_neg
        self.gausslikelihood_neg = gausslikelihood_neg

    def MultinomialTrain(self):
        # doc_pos = 0
        # doc_neg = 0
        # for doc in self.docs:
        #     if doc[2].lower() == 'positif':
        #         doc_pos += 1
        #     else:
        #         doc_neg += 1
        #     print doc_pos
        tot_neg = []
        tot_pos = []

        with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\dtdkbaku\sf20%\DataLatihBaru20%.csv", "r") as infile:
            print  "Fitur Multinomial"
            for fitur in infile.readlines():
                fitur = fitur.split(',')
                if (fitur[0] == 'F7') or (fitur[0] == 'F8') or (fitur[0] == 'F9') or (fitur[0] == 'F10') or (
                        fitur[0] == 'F13') or (fitur[0] == 'F14') or (fitur[0] == 'F15') or (fitur[0] == 'F16') or (
                        fitur[0] == 'F17') or (fitur[0] == 'F23') or (fitur[0] == 'F24') or (fitur[0] == 'F25') or (
                        fitur[0] == 'F26') or (fitur[0] == 'F27') or (fitur[0] == 'F28') or (fitur[0] == 'F29') or (
                        fitur[0] == 'F30') or (fitur[0] == 'F37') or (fitur[0] == re.findall('[A-Za-z]+', fitur[0])[0]):
                    print fitur[0]
                    counter = 0
                    pos = 0
                    neg = 0
                    for doc in self.docs:
                        if doc[2].lower() == 'positif':
                            pos += float(fitur[1:][
                                     counter])  # agar tahu indeks dokumen, maka doc dihubungkan dengan fitur fungsi counter
                        else:
                            neg += float(fitur[1:][counter])
                        counter += 1
                    tot_pos.append(pos)
                    tot_neg.append(neg)

        pf_pos = []
        for pos in tot_pos:
            pf_pos.append(round((pos + 1) / (sum(tot_pos) + len(tot_pos)), 4))
        self.m_pf_pos = pf_pos

        pf_neg = []
        for neg in tot_neg:
            pf_neg.append(round((neg + 1) / (sum(tot_neg) + len(tot_neg)), 4))
        self.m_pf_neg = pf_neg

    def MultinomialTesting(self):
        mtrain = self.MultinomialTrain()

        mpf_pos = []
        for pos in self.m_pf_pos:
            mpf_pos.append(pos)
        #print mpf_pos

        mpf_neg = []
        for neg in self.m_pf_neg:
            mpf_neg.append(neg)
        #print mpf_neg

        mfitur = []
        with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\dtdkbaku\sf20%\DataUjiBaru20%.csv", "r") as infile:
            for fitur in infile.readlines():
                fitur = fitur.split(',')
                if (fitur[0] == 'F7') or (fitur[0] == 'F8') or (fitur[0] == 'F9') or (fitur[0] == 'F10') or (
                        fitur[0] == 'F13') or (fitur[0] == 'F14') or (fitur[0] == 'F15') or (fitur[0] == 'F16') or (
                        fitur[0] == 'F17') or (fitur[0] == 'F23') or (fitur[0] == 'F24') or (fitur[0] == 'F25') or (
                        fitur[0] == 'F26') or (fitur[0] == 'F27') or (fitur[0] == 'F28') or (fitur[0] == 'F29') or (
                        fitur[0] == 'F30') or (fitur[0] == 'F37') or (fitur[0] == re.findall('[A-Za-z]+', fitur[0])[0]):
                  #print fitur
                  mfitur.append(fitur)
            #print mfitur

        d_pos = []
        d_neg = []
        for i, uji in enumerate(mfitur):
            #print uji
            f_pd_neg = []
            f_pd_pos = []
            for x in uji[1:]:
                f_pd_pos.append(mpf_pos[i] ** float(x))
                f_pd_neg.append(mpf_neg[i] ** float(x))
            d_pos.append(f_pd_pos)
            d_neg.append(f_pd_neg)
        #print d_pos

        positif = []
        for i, pos in enumerate(d_pos):
            positif.append(pos)
        #print positif

        mlikelihood_pos = [reduce(mul, i) for i in zip(*positif)]
        #print mlikelihood_pos
        self.mlikelihood_pos = mlikelihood_pos

        negatif = []
        for i, neg in enumerate(d_neg):
            negatif.append(neg)

        mlikelihood_neg = [reduce(mul, i) for i in zip(*negatif)]
        #print mlikelihood_neg
        self.mlikelihood_neg = mlikelihood_neg

    def Posterior(self):
        prior = self.Prior()
        bernoulli = self.BernoulliTest()
        gaussian = self.GaussianTesting()
        multinomial = self.MultinomialTesting()

        bernoulli_pos = self.blikelihood_pos
        bernoulli_neg = self.blikelihood_neg

        gauss_pos = self.gausslikelihood_pos
        gauss_neg = self.gausslikelihood_neg

        multinomial_pos = self.mlikelihood_pos
        multinomial_neg = self.mlikelihood_neg

        posterior_pos = []
        for i, posteriorpos in enumerate(gauss_pos):
            posteriorpos = self.prior_pos  * bernoulli_pos[i] * gauss_pos[i] * multinomial_pos[i]
            posterior_pos.append(posteriorpos)

        posterior_neg = []
        for j, posteriorneg in enumerate(gauss_neg):
            posteriorneg = self.prior_neg * bernoulli_neg[j] *gauss_neg[j] * multinomial_neg[j]
            posterior_neg.append(posteriorneg)

        klasifikasi = []
        for k,kelas in enumerate(posterior_pos):
            if posterior_pos[k] >= posterior_neg[k]:
                klasifikasi.append("Positif")
            else:
                klasifikasi.append("Negatif")

        with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\datasettdkbakuuji.csv" , "r") as f:
            with open('C:\Users\ACER\PycharmProjects\Skripsimaster\data\dtdkbaku\sf20%\datauji20%.csv', 'wb') as f1:
                data = list(csv.reader(f))
                write = csv.writer(f1)
                write.writerows([a + [b] for a, b in zip(data, klasifikasi)])

        print "======================================================================================="
        print "Analisis Sentimen Opini Film dengan menggunakan Ensemble Fitur dan Seleksi Fitur PCC"
        print "======================================================================================="
        print "Positif Category"
        print "Bernoulli Naive Bayes Positif","\n",bernoulli_pos
        print "Gaussian Naive Bayes Positif", "\n", gauss_pos
        print "Multinomial Naive Bayes Positif", "\n", multinomial_pos
        print "----------------------------------------------------------------------------------------"

        print "Negative Category"
        print "Bernoulli Naive Bayes Negative", "\n", bernoulli_neg
        print "Gaussian Naive Bayes Negative", "\n", gauss_neg
        print "Multinomial Naive Bayes Negative", "\n", multinomial_neg
        print "----------------------------------------------------------------------------------------"

        print "Posterior Positif","\n",posterior_pos
        print "----------------------------------------------------------------------------------------"
        print "Posterior Negatif","\n",posterior_neg
        print "----------------------------------------------------------------------------------------"
        print "Kelas dari Sistem", klasifikasi

fiturs = []
docs = []
with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\dtdkbaku\sf20%\DataLatihBaru20%.csv","rb") as f:
    fiturcsv = csv.reader(f)
    fiturs = [x for x in fiturcsv]
    fiturs.insert(0, fiturs[0])
    #fiturs.pop(0)

with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\dtdkbaku\sf20%\DataUjiBaru20%.csv", "rb") as fu:
    fiturujicsv = csv.reader(fu)
    fitursuji = [x for x in fiturujicsv]
    fitursuji.insert(0, fitursuji[0])
    #fitursuji.pop(0)

with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\datasettdkbakulatih.csv", "rb") as f:
    docscsv = csv.reader(f)
    docs = [x for x in docscsv]


nb = Naive_Bayes(fiturs,fitursuji, docs)
#nb.Prior()
nb.Posterior()
#nb.BernoulliTrain()
#nb.BernoulliTest()