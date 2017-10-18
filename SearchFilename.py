'''
Search a filename for a phrase and how many following lines to display
USAGE:
import SearchFilename
filename = "hek.txt"
length = 4
SearchFilename.searchfilename(filename, length)
'''
def searchfilename(filename, length):
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    search = str(raw_input("Search Phrase : "))
    for i, line in enumerate(searchlines):
        if search in line: 
            for l in searchlines[i:i+length]: print l,
            print