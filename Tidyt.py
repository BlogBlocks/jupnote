def tidyt(in_string):    
    texout = in_string.replace("', u'", "  ");texout = texout.replace("\u2018", "")
    texout = texout.replace("\u2019 ", "");texout = texout.replace("%", "")
    texout = texout.replace("[u'", "");texout = texout.replace(" u'", "")
    texout = texout.replace(', u"', ' ');texout = texout.replace('",', ' ')
    texout = texout.replace("'", '');texout = texout.replace("Mr.  ", 'Mr. ')
    texout = texout.replace(",", '');texout = texout.replace(".", '')
    ftexout =texout.replace("']", "")
    return ftexout