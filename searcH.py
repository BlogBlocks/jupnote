# Simple File Search
#import searcH
#searcH.search()
def search(filename, term):
    datafile = open(filename, "r")
    data = datafile.readlines()
    for line in data:
        if term in line:
            print line,

if __name__ == "__main__":
    search(filename, term)            