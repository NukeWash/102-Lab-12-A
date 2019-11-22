#John Hennon
#CSCI 102 - E
#Week 12 - Part A - Utilities


def PrintOutput(st):
    print("OUTPUT",st)
st=input("STRING> ")
(PrintOutput(st))

#B LoadFile
def LoadFile(File_Name):
    f=open(File_Name,'r')
    File_List=f.read().splitlines()
    return File_List
print(LoadFile('Example.txt'))

#C UpdateString
'''is a function that takes in two strings and an index integer (no return). The function should print a
string that is the first string modified to replace the character at the index provided with the second
string. (Remember that strings are immutable, i.e., some_string[5] = 'a' will give you an error.) 
Here's an example of using this function:
>>> UpdateString("Hello World", "a", 3)
OUTPUT Helao World'''

