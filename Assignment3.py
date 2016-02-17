# @author Ashish Tamrakar
# @Date 2016-02-14
# Program to find the document id, unique terms and terms and its term frequency.
# Python v2.7.10
import re
from stemmer import PorterStemmer
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
    documents = file.read()
    # Reading stop words from the file
    fileStopwords = open('stopwords.txt', 'r')
    stopwordsList = fileStopwords.read()
    stopwords = stopwordsList.split()
    # List that maintains the document id number, number of unique terms in document, for each term in the document, its term and it's term frequency.
    documentList = []
    docId = 1
    # Splits the multiple documents of the same file into list
    document = re.split(".I | \n.I", documents)[1:]

    for doc in enumerate(document):
        startIndex = doc[1].index('.W\n')
        text = doc[1][startIndex + 3:]
        words = re.findall(r'\w+', text)

        pObj = PorterStemmer()
        listWords = {}
        for word in words:
            flagStopwords = word.lower() in stopwords
            if (not flagStopwords and word.isalpha()):
                stemWord = pObj.stem(word, 0, len(word) - 1)
                listWords = addToDict(listWords, stemWord)

        sortedList = sorted(listWords.items(), key=lambda t: t[0])
        output = {'id': docId, 'unique': len(sortedList), 'terms': sortedList}
        docId += 1
        documentList.append(output)

    for i in range(0, len(documentList)):
        print "Document:", documentList[i]['id'], "\nUnique Terms:", documentList[i]['unique'], "\nTerms:\n", documentList[i]['terms']

main()