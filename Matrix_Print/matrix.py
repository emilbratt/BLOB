import random

def matrix(List,col):
    w = 5 # column width
    for item in List:
        if len(str(item)) >= w:
            w = len(str(item))+2

    # add dummy values to match grid
    while (len(List)%col) != 0 :
        List.append('')

    print() # force \n
    if col == 6:
        for i in range(0,len(List),col):
            print('\t+'+'-'*((w*6)+5)+'+')
            print(f'\t|{str(List[i]).center(w)}|{str(List[i+1]).center(w)}'
            + f'|{str(List[i+2]).center(w)}|{str(List[i+3]).center(w)}'
            +f'|{str(List[i+4]).center(w)}|{str(List[i+5]).center(w)}|')
        print('\t+'+'-'*((w*6)+5)+'+')
    elif col == 5:
        for i in range(0,len(List),col):
            print('\t+'+'-'*((w*5)+4)+'+')
            print(f'\t|{str(List[i]).center(w)}|{str(List[i+1]).center(w)}'
            + f'|{str(List[i+2]).center(w)}|{str(List[i+3]).center(w)}'
            +f'|{str(List[i+4]).center(w)}|')
        print('\t+'+'-'*((w*5)+4)+'+')
    elif col == 4:
        for i in range(0,len(List),col):
            print('\t+'+'-'*((w*4)+3)+'+')
            print(f'\t|{str(List[i]).center(w)}|{str(List[i+1]).center(w)}'
            + f'|{str(List[i+2]).center(w)}|{str(List[i+3]).center(w)}|')
        print('\t+'+'-'*((w*4)+3)+'+')
    elif col == 3:
        for i in range(0,len(List),col):
            print('\t+'+'-'*((w*3)+2)+'+')
            print(f'\t|{str(List[i]).center(w)}|{str(List[i+1]).center(w)}'
            + f'|{str(List[i+2]).center(w)}|')
        print('\t+'+'-'*((w*3)+2)+'+')
    elif col == 2:
        for i in range(0,len(List),col):
            print('\t+'+'-'*((w*2)+1)+'+')
            print(f'\t|{str(List[i]).center(w)}|{str(List[i+1]).center(w)}'
            + f'|')
        print('\t+'+'-'*((w*2)+1)+'+')
    elif col == 1:
        for i in range(0,len(List),col):
            print('\t+'+'-'*(w)+'+')
            print(f'\t|{str(List[i]).center(w)}|')
        print('\t+'+'-'*(w)+'+')

    # remove dummy values
    while List[-1] == '':
        del List[-1]
    print() # force \n


# example usage
if __name__ == '__main__':

    # create a list with random values
    list = []
    for i in range(random.randint(14,27)):
        list.append(random.randint(1000,50000))

    # send the list through the matrix function
    # argument 1 is the list, argument 2 is a number between 1 and 6
    matrix(list,random.randint(1,6))
