from itertools import izip, islice
from time import sleep
def satinfo():
    search_string = raw_input("Load : ")
    with open('visual.txt', 'r') as infile, open('visual.tmp', 'w') as outfile:
        for line in infile:
            if search_string in line:
                outfile.writelines([line, next(infile), next(infile)])

    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                return name, one, two    
                         
def prntlist():            
    from time import sleep
    with open('visual.txt', 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            if not next_n_lines:
                break
            sleep(.5)
            print next_n_lines[0],
        
def reuse():
    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                #print name, one, two    
                f.close()
                return name, one, two  
            
            