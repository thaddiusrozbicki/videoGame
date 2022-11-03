def monkey_troubke(a_smile,b_smile):
    if a_smile==True and b_smile==True:
        return('True')
    elif a_smile==False and b_smile==False:
        return('True')
    elif a_smile==True and b_smile==False:
        return('False')
    else:
        return('False')

def monkey_trouble_butbetter(a_smile,b_smile):
    if a_smile==b_smile:
        return(True)
    else:
        return(False)