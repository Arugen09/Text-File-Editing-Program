filename1 = None
filename2 = None
text=None
def dothing(thing):
    if thing == 1:
        filename1 = input('What is the file name? ')
        text = input('What is the text you are writing? ')
        print('Got it!')
        with open(filename1, 'w') as doc:
            doc.write(text)
        print('Check the File!')
    elif thing == 2:
        filename1 = input('What is the file name?')
        print('Got It!')
        with open(filename1, 'r') as doc:
            text = doc.read()
        print('The text in this document is ' + text)
    elif thing == 3:
        filename1 = input('What is the first file name?')
        filename2 = input('What is the second file name? ')
        with open(filename1, 'r') as a:
            adata = a.read()
        with open(filename2, 'r') as b:
            bdata = b.read()
        with open(filename1, 'w') as a:
            a.write(bdata)
        with open(filename2, 'w') as b:
            b.write(adata)
        print('It is done!')
    elif thing == 4:
        filename1 = input('What is the file name?')
        with open(filename1, 'r') as doc:
            charamount = str(int(str(doc.read).count(' ')) + 1)
        print('There are ' + charamount + ' words in this document')
    else:
        print('what?')
x='y'
while x == 'y':
    action = int(input('What is the action you would like to do? [1=edit, 2=read, 3=swap, 4=count words] '))
    dothing(action)
    x = input('Do you want to do something again? [y/n]')
print('okay then, bye!')
