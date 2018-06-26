import csv

class duplikat:

    def __init__(self, docs):
        self.docs = docs

    def Adjectivepostag(self):
        # cek kata unik as fitur
        unik = []
        for term in self.docs:
            for unique in term:
                if unique not in unik:
                    unik.append(unique)
        termfeature = sorted(unik)
        print termfeature
        # print termfeature

        with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\unikVerb.csv", 'wb') as n:
            noun = csv.writer(n)
            # noun.writerow(list_noun)
            noun.writerows([[i] for i in termfeature])


docs = []
with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\Postag\Verb1new.csv",
          "rb") as data:
    x = csv.reader(data)
    docs = []
    for i in x:
        docs.append(i)
    x = duplikat(docs)
    x.Adjectivepostag()

