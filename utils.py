def ToList(filename):
    '''
    Takes filename as argument and returns list of lines in that file.
    '''
    lines = open(filename, 'r', encoding='utf-8').readlines()
    return lines


if __name__ =='__main__':
    print('Running Utils function')
    
    
