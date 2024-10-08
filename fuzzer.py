from fuzzywuzzy import fuzz
import csv
def data_extract(filename):
    names=[]
    dict={}
    with open(filename,'r')as fh:
        reader= csv.reader(fh)
        for i in reader:
            names.append(i[0])
            dict[i[0]]= i[2]
    return names,dict

def find_closest_match(input_word,location_list):
    max_similarity = 0
    closest_match = None
    for location in location_list:
        similarity = fuzz.ratio(input_word, location)
        if similarity > max_similarity:
            max_similarity= similarity
            closest_match=location
    return closest_match,location_list.index(closest_match)

def fuzzy_search(file,word):
    data,dict=data_extract(file)
    fuzzy ,ind =find_closest_match(word,data)
    return fuzzy, ind,dict[fuzzy]