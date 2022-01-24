"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    book = open(filename,"r")
    corpus_text = []
    for text in book:
        line = text.split()
        if line != []:
            corpus_text.append(line)
    return corpus_text
'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    corpuslength = 0
    for word in range(len(corpus)):
        corpuslength = corpuslength + len(corpus[word])
    return corpuslength

'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    uniqwords = []
    for list in corpus:
        for eachword in list:
            if eachword not in uniqwords:
                uniqwords.append(eachword)
    return uniqwords

'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    unigramcounts = {}
    for list in corpus:
        for eachword in list:
            if eachword not in unigramcounts:
                unigramcounts[eachword] = 0
            unigramcounts[eachword] += 1      
    return unigramcounts


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    startwordlst = []
    for word in corpus:
        if word[0] not in startwordlst:
            startwordlst.append(word[0])
    return startwordlst

'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    startworddic = {}
    for fstword in corpus:
        if fstword[0] not in startworddic:
            startworddic[fstword[0]] = 0
        startworddic[fstword[0]] += 1
    return startworddic


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    bigramdic = {}
    for line in range(len(corpus)):
        for word in range(len(corpus[line])-1):
            fstkeyword = corpus[line][word]
            seckeyword = corpus[line][word+1]
            if fstkeyword not in bigramdic:
                bigramdic[fstkeyword] = {}
            if seckeyword not in bigramdic[fstkeyword]:
                bigramdic[fstkeyword][seckeyword] = 1
            else:
                bigramdic[fstkeyword][seckeyword] += 1
    return bigramdic

### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    unilen = len(unigrams)
    probabilitylst = []
    for word in unigrams:
        word= probabilitylst.append(1/unilen)
    return probabilitylst


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    unigrmprblst = []
    for index in range(len(unigrams)):
        for wordval in unigramCounts:
            if unigrams[index] == wordval:
                unigrmprblst.append(unigramCounts[wordval]/totalCount)
    return unigrmprblst

'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    newdic = {}
    for word in bigramCounts:
        wordcnt = unigramCounts[word]
        nxtword = []
        prob = []
        for keyword in bigramCounts[word]:
            nxtword.append(keyword)
            prob.append(bigramCounts[word][keyword]/wordcnt)
        tempdic ={}
        tempdic["words"] = nxtword
        tempdic["probs"] = prob
        newdic[word]=tempdic
    return newdic

'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    empdic = dict(zip(words,probs))
    orderdic = dict(sorted(empdic.items(), key = lambda x:x[1], reverse = True))
    newdic={}
    for keys, values in orderdic.items():
        if keys not in ignoreList and len(newdic)<count:
            newdic[keys] = values
    return newdic

'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices, random
def generateTextFromUnigrams(count, words, probs):
    randomlst = []
    randomstr = ""
    while len(randomlst) < count:
        randomlst += choices(words,probs)
    for word in randomlst:
        randomstr = randomstr + " "+ word
    return randomstr

'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    randomlst = []
    textstr =""
    while len(randomlst)<count:
        if len(randomlst) == 0 or randomlst[-1] == ".":
            randomlst += choices(startWords,startWordProbs)    
        else:
            last = randomlst[-1]
            randomlst += choices(bigramProbs[last]["words"],bigramProbs[last]["probs"])
    for wd in randomlst:
        textstr = textstr + " " + wd
    return textstr

### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    import matplotlib.pyplot as plt
    word = buildVocabulary(corpus)
    prob = countUnigrams(corpus)
    probab =  buildUnigramProbs(word, prob, getCorpusLength(corpus))
    topwords = getTopWords(50, word, probab, ignore)
    # barPlot(topwords, "TOP 50 Words")
    return 


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    strtwrd = getStartWords(corpus)
    strtprob =countStartWords(corpus)
    prob =  buildUnigramProbs(strtwrd, strtprob, getCorpusLength(corpus))
    topstrtwords = getTopWords(50, strtwrd, prob, ignore)
    # print(topstrtwords)
    # barPlot(topstrtwords, "TOP 50 Start Words")
    return

'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    wrd = countUnigrams(corpus)
    prb = countBigrams(corpus)
    prob = buildBigramProbs(wrd,prb)
    topnxtwrds = getTopWords(10,prob[word]["words"],prob[word]["probs"],ignore)
    # barPlot(topnxtwrds,"TOP NEXT WORDS")
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    word = buildVocabulary(corpus1)
    prob = countUnigrams(corpus1)
    probab =  buildUnigramProbs(word, prob, getCorpusLength(corpus1))
    topwordscorp1 = getTopWords(topWordCount, word, probab, ignore)
    corp1lst = [] #1
    for corp1word in topwordscorp1:
        corp1lst.append(corp1word)
    word1 = buildVocabulary(corpus2)
    prob1 = countUnigrams(corpus2)
    probab1 =  buildUnigramProbs(word1, prob1, getCorpusLength(corpus2))
    topwordscorp2 = getTopWords(topWordCount, word1, probab1, ignore)
    for corp2word in topwordscorp2:
        if corp2word not in corp1lst:
            corp1lst.append(corp2word)
    problst1 = []
    problst2 = []
    for keyword in corp1lst:
        if keyword in word:
            ind = word.index(keyword)
            problst1.append(probab[ind])
        else:
            problst1.append(0)
        if keyword in word1:
            ind1 = word1.index(keyword)
            problst2.append(probab1[ind1])
        else:
            problst2.append(0)
    dic ={}
    dic["topWords"] = corp1lst
    dic["corpus1Probs"] = problst1
    dic["corpus2Probs"] = problst2
    return dic


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek1()
    # test.testLoadBook()
    # test.testGetCorpusLength()
    # test.testBuildVocabulary()
    # test.testCountUnigrams()
    # test.testGetStartWords()
    # test.testCountStartWords()
    # test.testCountBigrams()

    ## Uncomment these for Week 2 ##

    # print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    # test.week2Tests()
    # print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek2()
    # test.testBuildUniformProbs()
    # test.testBuildUnigramProbs()
    # test.testBuildBigramProbs()
    # test.testGetTopWords()
    # test.testGenerateTextFromUnigrams()
    # test.testGenerateTextFromBigrams()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek3()
    test.testSetupChartData()
