import pickle

def make_text(x):
    if len(x) == 5:
        my_list = []
        for i in x:
            a = len(i)
            my_list.append(a)

        my_list.sort(reverse=True)
        main_list = my_list[:2]
        main_text = []
        for i in x:
            if main_list[0] == len(i):
                main_text.append(i)
            elif main_list[1] == len(i):
                main_text.append(i)

        return str(my_list)
    elif len(x) == 6:
        return ' '.join(x[2:])
    elif len(x)==4:
        return x[0]
    elif len(x)==3:
        return x[0]
    elif len(x)==2:
        return ' '.join(x)
    elif len(x)==2:
        return x[0]
    elif len(x)==1:
        return ' '.join(x)
    else:
        return "nothing"


def take_main_fail(text):
    try:
        if text[0:4] == 'test':
            end_text = text.split(":")[2:]
        else:
            end_text = text.split(":")[1:]
    except:
        end_text = text

    return end_text





with open("my_words.pkl","rb") as d:
    vectorizer =pickle.load(d)

with open("cluster.pkl","rb") as t:
    model =pickle.load(t)


def my_group(text):
    input1 = vectorizer.transform([text]).toarray()
    find_group = model.predict(input1)
    return find_group






