#John Hennon
#CSCI 102 - E
#Week 12 - Part A - Utilities

#A PrintOutput
def PrintOutput(st):
    print("OUTPUT",st)

#B LoadFile
def LoadFile(File_Name):
    f=open(File_Name,'r')
    File_List=f.read().splitlines()
    return File_List

#C UpdateString
def UpdateString(Initial,Change,Index):
    stl=[]
    for i in range(len(Initial)):
        stl.append(Initial[i])
    stl[Index]=Change
    print(''.join(stl))

#D FindWordCount
def FindWordCount(List_In,String_Check):
    Count=0
    Start=0
    while (List_In.find(String_Check,Start) != (-1)):
        Count+=1
        Start=List_In.find(String_Check,Start)+1
    return Count

#E ScoreFinder
def ScoreFinder(List_Names,List_Floats,Name):
    x=0
    for i in range(len(List_Names)):
        if List_Names[i].lower()==Name.lower():
            j=i
            print("OUTPUT",Name," scored ",List_Floats[j]," points")
            x=(-10000)
        else:
            x+=1
    if x>0:
        print("OUTPUT Player not found")

#F Union
def Union(L_One,L_Two):
    return (L_One+L_Two)

#G Intersection
def Intersection(L_One,L_Two):
    return list(set(L_One).intersection(L_Two))

#H NotIn
def NotIn(L_One,L_Two):
    return list(set(L_One).difference(L_Two))+list(set(L_Two).difference(L_One))
    

