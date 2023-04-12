import random
import requests

vowels = ["a", "e", "i", "o", "u"]
esVerbs = ["ch", "ss", "sh", "zz"]
constonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


def noun():
    url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/words/nouns.json"
    response = requests.get(url)
    nouns = response.json()["nouns"]
    random_noun = random.sample(nouns, 1)
    return random_noun[0]

def verb():
    url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/words/verbs.json"
    response = requests.get(url)
    verbs = response.json()["verbs"]
    random_verb = random.sample(verbs, 1)
    rv = random_verb[0].get('present')
    if rv == "have":
        return "has"
    elif rv == "go":
        return "goes"
    elif rv[-2:] in esVerbs or rv[-1] == "x":
        return rv + "es"
    elif rv[-2] not in "aeiou" and rv[-1] == "y":
        length = len(rv)
        return rv[1:length-1] + "ies"
    else:
        return rv + "s"

def adjective():
    url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/words/adjs.json"
    response = requests.get(url)
    adjs = response.json()["adjs"]
    random_adj = random.sample(adjs, 1)
    return random_adj[0]

def adverb():
    url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/words/adverbs.json"
    response = requests.get(url)
    adverbs = response.json()["adverbs"]
    random_adverb = random.sample(adverbs, 1)
    return random_adverb[0]

def SentenceType():
    string = "The " + noun() + " " + verb() + " " + adverb() + " over the " + adjective() + " " + noun()
    return string


sentenceList = []
for i in range(10):
    sentenceList.append(SentenceType())

print(sentenceList)
