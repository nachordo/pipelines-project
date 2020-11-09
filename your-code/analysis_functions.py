import pandas as pd

#Function to return the word frequency of a column 
#whose elements are lists of arrays
def word_count(df):
    counts = dict()
    for row in df:
        for word in row:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
            
    return  pd.Series(counts).sort_values(ascending=False)
