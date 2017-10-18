# Ask to enter string to search
# this will search all *.txt files in the current directory
# input window will ask "Search Phrase" 
"""
import Txsearch
Txsearch.txsearch()
"""
import os
import timeit
def txsearch():
    Sstring = raw_input("Search Phrase")
    for fname in os.listdir('./'):
       # Apply file type filter   
       if fname.endswith(".txt"):
            # Open file for reading
            fo = open(fname)
            # Read the first line from the file
            line = fo.readline()
            # Initialize counter for line number
            line_no = 1
            # Loop until EOF
            while line != '' :
                    index = line.find(Sstring)
                    if ( index != -1) :
                        # Set some parameters no lines longer than 240 characters 
                        # or less than search phrase +30 characters 
                        if len(line)< 240 and len(line)> len(Sstring)+20 :
                            #print(fname, "[", line_no, ",", index, "] ", line)
                            #print fname,line[1:-8],"  "
                            print fname,line_no,line
                    # Read next line
                    line = fo.readline()  
                    # Increment line counter
                    line_no += 1
            # Close the files
            fo.close()
            