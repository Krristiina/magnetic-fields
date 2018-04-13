import json

#This function is used to write input to a file (input to be given in JSON format)
def writeToFile(input):
    file = open('../resources/wordsTagged.json', 'w')
    file.write(input)
    file.close()


#This function gathers the data from a file and return them in categorized arrays
def dataToCategorizedArrays():
    with open('../resources/words.txt') as words:
        all = [line.strip() for line in words]

    adjectiveindex = all.index("ADJECTIVES")
    nounindex = all.index("NOUNS")
    verbindex = all.index("VERBS")
    affixindex = all.index("AFFIXES")
    adpositionindex = all.index("ADPOSITIONS")

    adjectives = all[adjectiveindex:nounindex]
    nouns = all[nounindex:verbindex]
    verbs = all[verbindex:affixindex]
    affixes = all[affixindex:adpositionindex]
    adpositions = all[adpositionindex:]

    categorizedAll = adjectives, nouns, verbs, affixes, adpositions
    return categorizedAll



#This function converts categorized arrays into JSON data and writes it to a file
def arrayToJson(arrays):
    """
    :param :arrays: a collection of categorized arrays
    """
    data = []

    for array in arrays:
        for item in array:
            if array[0] not in array[array.index(item)]:
                text = array[array.index(item)]
                tag = array[0].lower()
                data.append({'name': text, 'tag': tag})

    json_data = json.dumps(data)
    writeToFile(json_data)


arrayToJson(dataToCategorizedArrays())