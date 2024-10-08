import spacy
def extract(nlp,text):
    location_words=text
    doc=nlp(location_words)
    test=[]
    locations=[]
    for token in doc:
        test.append(token.ent_type_)
        if token.ent_type_ =="GPE":
            locations.append(1)
        else:
            locations.append(0)
            
    result=[]
    temp_start = -1
    for i in range(len(locations)):
        if locations[i]==1:
            if temp_start==-1:
                temp_start=i
        elif temp_start!=-1:
            result.append(doc[temp_start:i])
        
            temp_start=-1
        else:
            continue
    return result