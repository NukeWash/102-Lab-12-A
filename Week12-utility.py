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
def UpdateString(Initial,Change,Index):
    stl=[]
    for i in range(len(Initial)):
        stl.append(Initial[i])
    stl[Index]=Change
    print(''.join(stl))
         
    

