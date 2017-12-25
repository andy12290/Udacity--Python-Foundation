import urllib.request as ur

# Reading file.
def read_txt():
    ''' Reading the text file. '''
    quotes = open('/Users/Aniket/PycharmProjects/Udacity/movie_quotes.txt')
    file = quotes.read()
    #print(file)
    quotes.close()
    profanity_chk(file)

# Another function to check the profanity

def profanity_chk(file):
    connection = ur.urlopen('http://www.wdylike.appspot.com/?q='.format(file))
    output = connection.read()
    print(" This is output of file: {}".format(output))
    connection.close()

    if output == b"false":
        print('Profinity checked ok!!!')

read_txt()


