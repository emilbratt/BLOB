

def prettysql(records): # input = sql query result or list with tuples
    '''
        this function takes a list with tuple values

        the format should be like this:
        [('val','val','val'),('val','val','val'),]

        if the last values in a row is not present, the function
        will generate whitespace values so that the integrity of
        the matrix remains untouched

        this can be used as a pretty print of pythons sqlite3 queries

        feed the query-result of sqlite into this function
        and loop through the returned list

        each list-object holds one row making it easy
        to iterate through the results in a for loop

        an example usage:
        for row in prettysql(sqlResult):
            print(row)

    '''

    numColumns = len(records[0]) # get number of columns

    # loop through each value and set a column width based
    # on the length of the longest string in that column
    colWith = [] # column widths
    for col in records:
        for i,val in enumerate(col):
            try:
                if len(str(val)) >= colWith[i]-1:
                    colWith[i] = len(str(val))+2
            except IndexError:
                    colWith.insert(i, len(str(val))+2)

    breakLine = '+'

    # create the line that is between each printed record
    for i in range(numColumns):
        breakLine += '-'*(colWith[i])+'+'

    # append the formated strings to the print list
    printFormat = []
    for line,row in enumerate(records):
        addDummy = 0
        string = '|'

        for i in range(numColumns):
            try:
                string += row[i].center(colWith[i])+'|'
            except IndexError:
                # add dummy values if the row has less
                # than values than columns
                string += ''.center(colWith[i])+'|'

        printFormat.append(breakLine)
        printFormat.append(string)

    printFormat.append(breakLine)

    return printFormat


# example usage
if __name__ == '__main__':
    import random
    # random is for use with the example generating
    # a random record of numbers with a random number of columns

    # example with a list with a missing value
    myRecords = [
    ('name','age','city'),
    ('bob','30','new york'),
    ('bob','30','new york'),
    ('ross','30','london'),
    ('alice','40','rome'),
    ('jon','26','berlin'),
    ('jane','20'),
    ]

    for row in prettysql(myRecords):
        print(row)

    # example with a list wih a random amount of rows and values
    genTuple = []
    genList = []
    rangeNum = random.randint(16,28)
    for i in range(rangeNum):

        if i % 5 == 0:
            if genList == []:
                continue
            else:
                genTuple.append(tuple(genList))
                genList = []
        num = str(random.randint(1000,50000))
        genList.append(num)
    if i == rangeNum-1:
        genTuple.append(tuple(genList))

    for row in prettysql(genTuple):
        print(row)
