import re
import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()

class Preprocess:

    def __init__(self, docs):
        self.docs = docs

    def preprocessing(self):
        # case folding & cleaning
        for dokumen in self.docs:
            casefolding = dokumen[1].lower()
            linkRegex = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|" \
              "www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|" \
              "https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})"
            nolink = re.sub(linkRegex, '', casefolding)
            dokumen[1] = nolink
            #print dokumen[1]

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
        for kata in self.docs:
            no_punct = ""
            for char in kata[1]:
                if char not in punctuations:
                    no_punct = no_punct + char
                elif char in punctuations:
                    no_punct = no_punct + ' '
            kata[1] = no_punct

        # stemming
        stemmer = factory.create_stemmer()
        for word in self.docs:
            word[1] = stemmer.stem(str(word[1].lower()))
            #print word[1]

        # stopword
        stopword = open('C:\Users\ACER\PycharmProjects\Skripsimaster\kamus\modifikasi_stopword.txt', 'r').read()
        stopwordlist = re.split(r'\n', stopword)
        for kolom in self.docs:
            wordstop = re.split(r'\s', kolom[1])
            fil = ''
            for b in wordstop:
                if b not in stopwordlist:
                    fil += ' ' + b
            kolom[1] = fil
            #print kolom[1]

        # tokenize
        for value in self.docs:
            baris = re.split(r'\s', value[1])
            value[1] = baris

        for dat in self.docs:
            for a in dat[1]:
                if a == '':
                    dat[1].remove(a)
            #print dat

        # cek kata unik as fitur
        unik = []
        for term in self.docs:
            for unique in term[1]:
                if unique not in unik:
                    unik.append(unique)
            termfeature = sorted(unik)
        # print termfeature

        doc_counts = []
        for terms in termfeature:  # takes each term in the set
            doc_counts.append(0)
            rawterm = []
            # praproses = []
            rawterm.append(terms)
            for fdoc in self.docs:  # counts the no of times "term" is encountered in each doc
                ct = fdoc[1].count(str(terms))  # counts the no. of times "term" is present in the file
                rawterm.append(ct)
            print rawterm

            with open("C:\Users\ACER\PycharmProjects\Skripsimaster\output\Manualisasi\ekstrakfitur.csv", "ab") as fp:
                wr = csv.writer(fp)
                wr.writerow(rawterm)
docs = []
with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\DataManual\dataset.csv","r") as data:
    x = csv.reader(data)
    docs = []
    for i in x:
        docs.append(i)
    x = Preprocess(docs)
    x.preprocessing()

