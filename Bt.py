def badtext(essays):
    badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    essay = essay.translate(badtext)
    return essay