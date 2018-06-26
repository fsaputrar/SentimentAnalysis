import csv
import requests
import json
import time
from nltk import word_tokenize

class Kateglo:

    def __init__(self,docs):
        self.docs = docs

    def noun(self):
        list_noun = []
        for dokumen in self.docs:
            kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
            for w in kata:
                response = requests.get("http://kateglo.com/api.php?format=json&phrase=" + w)
                try:
                    json_object = json.loads(response.text)
                    kelas = json_object["kateglo"]["lex_class"]
                    if w and kelas == 'n':
                        list_noun.append(w)
                except ValueError,e:
                    pass
                time.sleep(1)
            print list_noun

        with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\Noun10.csv", 'wb') as n:
            noun = csv.writer(n)
            #noun.writerow(list_noun)
            noun.writerows([[i] for i in list_noun])

    def adj(self):
        list_adj = []
        for dokumen in self.docs:
            kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
            for w in kata:
                response = requests.get("http://kateglo.com/api.php?format=json&phrase=" + w)
                try:
                    json_object = json.loads(response.text)
                    kelas = json_object["kateglo"]["lex_class"]
                    if w and kelas == 'adj':
                        list_adj.append(w)
                except ValueError,e:
                    pass
                time.sleep(1)
            print list_adj

        with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\Adjective10.csv",
                  'wb') as adj:
            adjective = csv.writer(adj)
            #noun.writerow(list_noun)
            adjective.writerows([[i] for i in list_adj])

    def verb(self):
        list_verb = []
        for dokumen in self.docs:
            kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
            for w in kata:
                response = requests.get("http://kateglo.com/api.php?format=json&phrase=" + w)
                try:
                    json_object = json.loads(response.text)
                    kelas = json_object["kateglo"]["lex_class"]
                    if w and kelas == 'v':
                        list_verb.append(w)
                except ValueError,e:
                    pass
                time.sleep(1)
            print list_verb

        with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\Verb10.csv", 'wb') as v:
            verb = csv.writer(v)
            #noun.writerow(list_noun)
            verb.writerows([[i] for i in list_verb])

    def adverb(self):
        list_adverb = []
        for dokumen in self.docs:
            kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
            for w in kata:
                response = requests.get("http://kateglo.com/api.php?format=json&phrase=" + w)
                try:
                    json_object = json.loads(response.text)
                    kelas = json_object["kateglo"]["lex_class"]
                    if w and kelas == 'adv':
                        list_adverb.append(w)
                except ValueError, e:
                    pass
                time.sleep(1)
            print list_adverb

        with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\Adverb10.csv", 'wb') as adv:
            adverb = csv.writer(adv)
            # noun.writerow(list_noun)
            adverb.writerows([[i] for i in list_adverb])

    def interjection(self):
        list_i = []
        for dokumen in self.docs:
            kata = word_tokenize(dokumen[1].lower().decode('utf-8', 'ignore'))
            for w in kata:
                response = requests.get("http://kateglo.com/api.php?format=json&phrase=" + w)
                try:
                    json_object = json.loads(response.text)
                    kelas = json_object["kateglo"]["lex_class"]
                    if w and kelas == 'i':
                        list_i.append(w)
                except ValueError, e:
                    pass
                time.sleep(1)
            print list_i

        with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\Interjection.csv", 'wb') as inter:
            interjection = csv.writer(inter)
            # noun.writerow(list_noun)
            interjection.writerows([[i] for i in list_i])

with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\data\kesepuluh.csv",
          "rb") as data:
    x = csv.reader(data)
    docs = []
    for i in x:
        docs.append(i)

    k = Kateglo(docs)
    #k.noun()
    #k.adj()
    #k.verb()
    k.adverb()
    #k.interjection()