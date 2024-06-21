import cv2
import json 
import os
import verify

# to search the file in the given  path  and retrieve the  pair value of a give  as output 
def searchData(path, word ):
    file_type = get_file_type(path) 
    data = " "
    if file_type == " json file ":
        data = open_json(path)   
    elif file_type == "PNG image" or " JPEG image":
        data =  open_png(path , file_type )   
# functipon to open json files
def open_json(path):
    with open( path , 'rb') as json_file:
        data = json.load(json_file)
    return data

# function to open images 
def open_png(path, file_type):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow(image, "image")
    cv2.waitKey(0)
     

 # get the type for the file given    
def get_file_type(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(4)  # Read the first 4 bytes
        if header.startswith(b'\x89PNG'):
            return 'PNG image'
        elif header.startswith(b'\xFF\xD8'):
            return 'JPEG image' # Add more checks for other file types
        
# the meaning of the input word from the provided data 
def get_meaning(word):
    data = open_json("dictionary.json ")
    key = data[word]
    print(key)
    
# get the order of the sentence kind and find what order it belongs to 
def getOrder(list, path, path2):
    kindlist= []
    data = open_json(path)
    foundtype = False
    searchfound = False
    for i in range(list):
        item = list.get(i)
        word_type = data[item]
        if word_type is not None:
            kindlist.append(word_type)
        else:
            kindlist.append("Null")
    while foundtype == False:
        data2 = open_json(path2)
# get the word type         
def get_type(word):
    pass
#finding the subject verb and object
def FindSVO(question):
    pass

# make the path by conjoining the base_path and the foundpath
def MakePath(base_path,foundpath):
    full_path = os.path.join(base_path, foundpath)
    return full_path

#get the list of all items in the folder
def get_list_dir(path):
    listitm = os.listdir(path)
    return listitm

#get the path to a file 
def find_file(word):
    file_path = ""
    wordpath = word+".json"
    base_path = "../data/"
    datalist = get_list_dir(base_path)
    def get(datalist):
        for itm in datalist:
            if itm == wordpath:
                file_path = MakePath(base_path, wordpath)
                return file_path
            else:
                path=  MakePath(base_path, itm)
                datalist2 = get_list_dir(path)
        return datalist2
    itm = get(datalist) 
    lenght = len(itm)
    while lenght > 1:
        get(itm)
    return itm            
                   
# get reply from the last time the sentence was asked 
def Question_history(sentence_type , sentence ):
    path = ""
    path2 = ""
    data = open_json(path)
    try:
        for itm in data:
            if itm == sentence:
                response = data.get(itm)
                reply = verify.verify.isResponseStillValid(response, sentence)
                reply2 = verify.verify.isResponseGood(response, sentence)
                if reply is True and reply2 is True:
                    return reply
    except :
        data2 = open_json(path2)
        for itm in data2:
            if itm == sentence_type:
                response = data.get(itm)
                return response            
            
            


    