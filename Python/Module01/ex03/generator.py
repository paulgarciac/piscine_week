import random

def generator(txt, sep = " ", option = None):
    try:
        check_text = isinstance(txt, str)
        splitted_txt = txt.split(sep)
        if option != None:
            if option == "unique":
                splitted_txt = list(dict.fromkeys(splitted_txt))
                for i in splitted_txt:
                    yield i
        else:
            for i in splitted_txt:
                yield i
    except:
        print("ERROR")
        

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
# 
# for i in infinite_sequence():
#     print(i, end=" ")    

txt = "Le Lorem Lorem Ipsum est Lorem simplement du faux texte."

for word in generator(txt, option="unique"):
    print(word)
