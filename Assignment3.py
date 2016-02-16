# @author Ashish Tamrakar
# @Date 2016-02-14
# Program to find the document id, unique terms and terms and its term frequency.
# Python v2.7.10
import re
from stemmer import PorterStemmer
from collections import OrderedDict
import sys

def addToDict(listWords, stemWord):
    if (stemWord in listWords):
        listWords[stemWord] += 1
    else:
        listWords[stemWord] = 1

    return listWords

def main():
    # Reading the document from the file
    file = open("cran.all.1400", "r")
    # file = open("cran.txt", "r")
    documents = file.read()

    # Reading stop words from the file
    fileStopwords = open('stopwords.txt', 'r')
    stopwordsList = fileStopwords.read()
    stopwords = stopwordsList.split()

    # List that maintains the document id number, number of unique terms in document, for each term in the document, its term and it's term frequency.
    documentList = []
    docId = 1

    # Splits the multiple documents of the same file into list
    document = re.split(".I | \n.I", documents)

    for doc in enumerate(document):
        words = re.findall(r'\w+', doc[1])

        pObj = PorterStemmer()
        listWords = {}
        for word in words:
            flagStopwords = word.lower() in stopwords

            if (not flagStopwords and word.isalpha()):
                stemWord = pObj.stem(word, 0, len(word) - 1)

                listWords = addToDict(listWords, stemWord)


        sortedList = sorted(listWords.items(), key=lambda t: t[0])
        if (sortedList):
            temp = {'id': docId, 'unique': len(sortedList), 'terms': sortedList}
            docId += 1
            documentList.append(temp)

    for i in range(0, len(documentList)):
        print "Document:", documentList[i]['id'], "Unique Terms:", documentList[i]['unique'], "Terms:", documentList[i]['terms']

main()