from __future__ import division
import csv
import re
from nltk import word_tokenize

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()

class EnsemblesFeatures:

    def __init__(self, docs):
        self.docs = docs

    def F1(self):
        list = []  # data disimpan sementara
        list.append("F1")
        for dokumen in self.docs:
            if '#' in dokumen[1]:
                list.append(1)
            else:
                list.append(0)
        return list

    def F2(self):
        list = []
        list.append("F2")
        for dokumen in self.docs:
            if 'RT' in dokumen[1]:
                list.append(1)
            else:
                list.append(0)
        return list

    def F3(self):
        list = []
        list.append("F3")
        username = "(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([\w+[\w0-9-_]+)"
        for dokumen in self.docs:
            if re.findall(username, dokumen[1]):
                list.append(1)
            else:
                list.append(0)
        return list

    def F4(self):
        list = []
        list.append("F4")
        rgx = "((http|https|ftp)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
        for dokumen in self.docs:
            if re.findall(rgx, dokumen[1]):
                list.append(1)
            else:
                list.append(0)
        return list

    def F5(self):
        list = []
        list.append("F5")
        for dokumen in self.docs:
            rgxurl = "((http|https|ftp)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
            nolink = re.sub(rgxurl, '', dokumen[1])
            stripped = re.sub(r'[^A-Za-z\s]', '', nolink)
            wordcount = stripped.split()
            wordlength = len(wordcount)
            list.append(wordlength)
        return list

    def F6(self):
        list = []
        list.append("F6")
        for dokumen in self.docs:
            # return dokumen[0]
            wordcount = dokumen[1].split()
            wordlength = int(len(wordcount))
            karakter = int(len(dokumen[1]))
            try:
                averageword = float(karakter) / float(wordlength)
            except ZeroDivisionError:
                averageword = 0
            list.append(round(averageword, 4))
        return list

    def F7(self):
        list = []
        list.append("F7")
        for dokumen in self.docs:
            list.append(dokumen[1].count("?"))
        return list

    def F8(self):
        list = []
        list.append("F8")
        for dokumen in self.docs:
            list.append(dokumen[1].count("!"))
        return list

    def F9(self):
        list = []
        list.append("F9")
        rgx = '"([^"]*)"'
        for dokumen in self.docs:
            a = len(re.findall(rgx, dokumen[1]))
            list.append(a)
        return list

    def F10(self):
        list = []
        list.append("F10")
        startwithUppercase = "\\b([A-Z][A-Z]+|[A-Z][a-z]+|[A-Z][0-9]+|[A-Z][a-z0-9]+){1,}\\b"
        for dokumen in self.docs:
            a = len(re.findall(startwithUppercase, dokumen[1]))
            list.append(a)
        return list

    def F11(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\emoticon_id.txt", "rb") as f:
            emotsReader = csv.reader(f, delimiter='|')
            emots = [emot for emot in emotsReader]
            list = []
            list.append("F11")
            for dokumen in self.docs:
                found = False
                for emot in emots:
                    if emot[1] is not '' and emot[0] in dokumen[1].lower() and int(emot[1]) > 0:
                        list.append(1)
                        found = True
                        break
                if not found:
                    list.append(0)
            return list

    def F12(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\emoticon_id.txt", "rb") as f:
            emotsReader = csv.reader(f, delimiter='|')
            emots = [emot for emot in emotsReader]
            list = []
            list.append("F12")
            for dokumen in self.docs:
                found = False
                for emot in emots:
                    if emot[1] is not '' and emot[0] in dokumen[1].lower() and int(emot[1]) < 0:
                        list.append(1)
                        found = True
                        break
                if not found:
                    list.append(0)
            return list

    def F13(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Noun.csv",
                  "rb") as n:
            nounReader = csv.reader(n)
            noun = []
            for word in nounReader:
                noun.append(word)
            list_noun = []
            list_noun.append("F13")
            for dokumen in self.docs:
                jumlah_noun = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    ktbenda = True
                    for word in noun:
                        if k == word[0]:
                            ktbenda = False
                            break
                    if not ktbenda:
                        jumlah_noun += 1
                list_noun.append(jumlah_noun)
            #print list_noun
            return list_noun

    def F14(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Adjective.csv",
                  "rb") as adjv:
            adjReader = csv.reader(adjv)
            adj = []
            for word in adjReader:
                adj.append(word)
            list_adj = []
            list_adj.append("F14")
            for dokumen in self.docs:
                jumlah_adj = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    ktsifat = True
                    for word in adj:
                        if k == word[0]:
                            ktsifat = False
                            break
                    if not ktsifat:
                        jumlah_adj += 1
                list_adj.append(jumlah_adj)
            #print list_adj
            return list_adj

    def F15(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Verb.csv",
                  "rb") as v:
            verbReader = csv.reader(v)
            verb = []
            for word in verbReader:
                verb.append(word)
            list_verb = []
            list_verb.append("F15")
            for dokumen in self.docs:
                jumlah_verb = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    ktkerja = True
                    for word in verb:
                        if k == word[0]:
                            ktkerja = False
                            break
                    if not ktkerja:
                        jumlah_verb += 1
                list_verb.append(jumlah_verb)
            #print list_verb
            return list_verb

    def F16(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Adverb.csv",
                  "rb") as adv:
            adverbReader = csv.reader(adv)
            adverb = []
            for word in adverbReader:
                adverb.append(word)
            list_adverb = []
            list_adverb.append("F16")
            for dokumen in self.docs:
                jumlah_adverb = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    ktktg = True
                    for word in adverb:
                        if k == word[0]:
                            ktktg = False
                            break
                    if not ktktg:
                        jumlah_adverb += 1
                list_adverb.append(jumlah_adverb)
            #print list_adverb
            return list_adverb

    def F17(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Interjection.csv",
                  "rb") as i:
            interReader = csv.reader(i)
            inter = []
            for word in interReader:
                inter.append(word)
            list_i = []
            list_i.append("F17")
            for dokumen in self.docs:
                jumlah_inter = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    ktinter = True
                    for word in inter:
                        if k == word[0]:
                            ktinter = False
                            break
                    if not ktinter:
                        jumlah_inter += 1
                list_i.append(jumlah_inter)
            #print list_i
            return list_i

    def F18(self):
        list = []
        noun = self.F13()
        F5 = self.F5()
        list.append("F18")
        for i in range(len(noun[1:])):
            try:
                percentage = float(((noun[1:][i]) / F5[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        #print list

    def F19(self):
        list = []
        adj = self.F14()  # mengambil atribut
        F5 = self.F5()
        list.append("F19")
        for i in range(len(adj[1:])):
            try:
                percentage = float(((adj[1:][i]) / F5[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        #print list
        return list

    def F20(self):
        list = []
        verb = self.F15()
        F5 = self.F5()
        list.append("F20")
        for i in range(len(verb[1:])):
            try:
                percentage = float(((verb[1:][i]) / F5[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        #print list
        return list

    def F21(self):
        list = []
        adv = self.F16()
        F5 = self.F5()
        list.append("F21")
        for i in range(len(adv[1:])):
            try:
                percentage = float(((adv[1:][i]) / F5[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        #print list
        return list

    def F22(self):
        list = []
        interjection = self.F17()
        F5 = self.F5()
        list.append("F22")
        for i in range(len(interjection[1:])):
            try:
                percentage = float(((interjection[1:][i]) / F5[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        #print list
        return list

    def F23(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt", "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)
            list = []
            list.append("F23")
            for dokumen in self.docs:
                jumlah_kata_positif = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    positif = True
                    for word in words:
                        if k == word[0] and word[1] is not '' and int(word[1]) > 0:
                            positif = False
                            break
                    if not positif:
                        jumlah_kata_positif += 1
                list.append(jumlah_kata_positif)
            # return list
            return list

    def F24(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)
            list = []
            list.append("F24")
            for dokumen in self.docs:
                jumlah_kata_negatif = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    negatif = True
                    for word in words:
                        if k == word[0] and word[1] is not '' and int(word[1]) < 0:
                            negatif = False
                            break
                    if not negatif:
                        jumlah_kata_negatif += 1
                list.append(jumlah_kata_negatif)
            return list

    def F25(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)

        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Adjective.csv",
                  "rb") as adj:
            adjReader = csv.reader(adj)
            adj = []
            for a in adjReader:
                adj.append(a)

            # print adj
            list_adj = []
            list_adj.append("F25")
            for dokumen in self.docs:
                jumlah_adj = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    for sifat in adj:
                        if k == sifat[0]:
                            pos = True
                            for word in words:
                                if k == word[0] and word[1] is not '' and int(word[1]) > 0:
                                    pos = False
                                    break
                            if not pos:
                                jumlah_adj += 1
                list_adj.append(jumlah_adj)
            return list_adj

    def F26(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)

        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Adjective.csv",
                  "rb") as adj:
            adjReader = csv.reader(adj)
            adj = []
            for a in adjReader:
                adj.append(a)

            # print adj
            list_adj = []
            list_adj.append("F26")
            for dokumen in self.docs:
                jumlah_adj = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    for sifat in adj:
                        if k == sifat[0]:
                            neg = True
                            for word in words:
                                if k == word[0] and word[1] is not '' and int(word[1]) < 0:
                                    neg = False
                                    break
                            if not neg:
                                jumlah_adj += 1
                list_adj.append(jumlah_adj)
            return list_adj

    def F27(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)

        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Verb.csv",
                  "rb") as v:
            verbReader = csv.reader(v)
            verb = []
            for a in verbReader:
                verb.append(a)

            # print adj
            list_verb = []
            list_verb.append("F27")
            for dokumen in self.docs:
                jumlah_verb = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    for kerja in verb:
                        if k == kerja[0]:
                            pos = True
                            for word in words:
                                if k == word[0] and word[1] is not '' and int(word[1]) > 0:
                                    pos = False
                                    break
                            if not pos:
                                jumlah_verb += 1
                list_verb.append(jumlah_verb)
            return list_verb

    def F28(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)

        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Verb.csv",
                  "rb") as v:
            verbReader = csv.reader(v)
            verb = []
            for a in verbReader:
                verb.append(a)

            # print adj
            list_verb = []
            list_verb.append("F28")
            for dokumen in self.docs:
                jumlah_verb = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    for kerja in verb:
                        if k == kerja[0]:
                            neg = True
                            for word in words:
                                if k == word[0] and word[1] is not '' and int(word[1]) < 0:
                                    neg = False
                                    break
                            if not neg:
                                jumlah_verb += 1
                list_verb.append(jumlah_verb)
            return list_verb

    def F29(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)

        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Adverb.csv",
                  "rb") as adv:
            adverbReader = csv.reader(adv)
            adverb = []
            for a in adverbReader:
                adverb.append(a)

            # print adj
            list_adverb = []
            list_adverb.append("F29")
            for dokumen in self.docs:
                jumlah_adverb = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    for keterangan in adverb:
                        if k == keterangan[0]:
                            pos = True
                            for word in words:
                                if k == word[0] and word[1] is not '' and int(word[1]) > 0:
                                    pos = False
                                    break
                            if not pos:
                                jumlah_adverb += 1
                list_adverb.append(jumlah_adverb)
            return list_adverb

    def F30(self):
        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\sentiwords_id.txt",
                  "rb") as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)

        with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\Postag\Adverb.csv",
                  "rb") as adv:
            adverbReader = csv.reader(adv)
            adverb = []
            for a in adverbReader:
                adverb.append(a)

            # print adj
            list_adverb = []
            list_adverb.append("F30")
            for dokumen in self.docs:
                jumlah_adverb = 0
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                for k in kata:
                    for keterangan in adverb:
                        if k == keterangan[0]:
                            neg = True
                            for word in words:
                                if k == word[0] and word[1] is not '' and int(word[1]) < 0:
                                    neg = False
                                    break
                            if not neg:
                                jumlah_adverb += 1
                list_adverb.append(jumlah_adverb)
            return list_adverb

    def F31(self):
        list = []
        tagadj_pos = self.F25()
        F23 = self.F23()
        list.append("F31")
        for i in range(len(tagadj_pos[1:])):
            try:
                percentage = float(((tagadj_pos[1:][i]) / F23[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        # return list

    def F32(self):
        list = []
        tagadj_neg = self.F26()
        F24 = self.F24()
        list.append("F32")
        for i in range(len(tagadj_neg[1:])):
            try:
                percentage = float(((tagadj_neg[1:][i]) / F24[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        # return list

    def F33(self):
        list = []
        tagverb_pos = self.F27()
        F23 = self.F23()
        list.append("F33")
        for i in range(len(tagverb_pos[1:])):
            try:
                percentage = float(((tagverb_pos[1:][i]) / F23[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        # return list

    def F34(self):
        list = []
        tagverb_neg = self.F28()
        F24 = self.F24()
        list.append("F34")
        for i in range(len(tagverb_neg[1:])):
            try:
                percentage = float(((tagverb_neg[1:][i]) / F24[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        # return list

    def F35(self):
        list = []
        tagadv_pos = self.F29()
        F23 = self.F23()
        list.append("F35")
        for i in range(len(tagadv_pos[1:])):
            try:
                percentage = float(((tagadv_pos[1:][i]) / F23[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        # return list

    def F36(self):
        list = []
        tagadv_neg = self.F30()
        F24 = self.F24()
        list.append("F36")
        for i in range(len(tagadv_neg[1:])):
            try:
                percentage = float(((tagadv_neg[1:][i]) / F24[1:][i]) * 1)
            except ZeroDivisionError:
                percentage = 0
            list.append(round(percentage, 4))
        return list
        # return list

    def F37(self):
        with open('C:\Users\ACER\PycharmProjects\ProgramBismillah\kamus\penegasan_boosterwords_id.txt',
                  'rb') as f:
            wordsReader = csv.reader(f, delimiter=":")
            words = []
            for word in wordsReader:
                words.append(word)
            list = []
            list.append("F37")
            for dokumen in self.docs:
                kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
                jumlah_kata_intensifier = 0
                for k in kata:
                    for word in words:
                        if k == word[0]:
                            jumlah_kata_intensifier += 1
                            break
                list.append(jumlah_kata_intensifier)
            return list

features = []
docs = []
with open("C:\Users\ACER\PycharmProjects\ProgramBismillah\data\datasetbaku.csv","rb") as data:
    x = csv.reader(data)
    docs = []
    for i in x:
        docs.append(i)
    x = EnsemblesFeatures(docs)

    fitur = [0] * len(docs)
    features = [fitur] * 38

    features[1] = x.F1()
    features[2] = x.F2()
    features[3] = x.F3()
    features[4] = x.F4()
    features[5] = x.F5()
    features[6] = x.F6()
    features[7] = x.F7()
    features[8] = x.F8()
    features[9] = x.F9()
    features[10] = x.F10()
    features[11] = x.F11()
    features[12] = x.F12()
    features[13] = x.F13()
    features[14] = x.F14()
    features[15] = x.F15()
    features[16] = x.F16()
    features[17] = x.F17()
    features[18] = x.F18()
    features[19] = x.F19()
    features[20] = x.F20()
    features[21] = x.F21()
    features[22] = x.F22()
    features[23] = x.F23()
    features[24] = x.F24()
    features[25] = x.F25()
    features[26] = x.F26()
    features[27] = x.F27()
    features[28] = x.F28()
    features[29] = x.F29()
    features[30] = x.F30()
    features[31] = x.F31()
    features[32] = x.F32()
    features[33] = x.F33()
    features[34] = x.F34()
    features[35] = x.F35()
    features[36] = x.F36()
    features[37] = x.F37()


with open('C:\Users\ACER\PycharmProjects\ProgramBismillah\output\ekstrakfiturbaku.csv', 'wb') \
        as saveinfile:
    writer = csv.writer(saveinfile)
    for feature in features:
        writer.writerow(feature)