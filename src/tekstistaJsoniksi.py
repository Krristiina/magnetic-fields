#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import json

# http://www.gingersoftware.com/content/grammar-rules/adjectives/lists-of-adjectives/
#This function is used to write input to a file (input to be given in JSON format)
def writeToFile(input):
    file = open('../resources/tagatytSanat.json', 'w')
    file.write(input)
    file.close()


#This function gathers the data from a file and return them in categorized arrays
def dataToCategorizedArrays():
    with open('../resources/sanoja.txt') as words:
        all = [line.strip() for line in words]

    adjIndeksi = all.index("ADJEKTIIVI")
    subIndeksi = all.index("SUBSTANTIIVI")
    verbIndeksi = all.index("VERBI")
    pronIndeksi = all.index("PRONOMINI")
    paateIndeksi = all.index("PÄÄTE")
    partIndeksi = all.index("PARTIKKELI")
    merkkiIndeksi = all.index("VÄLIMERKKI")


    adjektiivit = all[adjIndeksi:subIndeksi]
    substantiivit = all[subIndeksi:verbIndeksi]
    verbit = all[verbIndeksi:pronIndeksi]
    pronominit = all[pronIndeksi:paateIndeksi]
    paatteet = all[paateIndeksi:partIndeksi]
    partitiivit = all[partIndeksi:merkkiIndeksi]
    valimerkit = all[merkkiIndeksi:]

    categorizedAll = adjektiivit, substantiivit, verbit, pronominit, paatteet, partitiivit, valimerkit
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
                data.append({'item': text, 'tag': tag})

    json_data = json.dumps(data, indent=4, sort_keys=True)
    writeToFile(json_data)


arrayToJson(dataToCategorizedArrays())