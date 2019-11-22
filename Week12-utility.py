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
''' is a function that takes in two lists and a string. The first list is a list of strings (player names), the second list is a list of floats (player scores), and the string is a name (player to find). If the player to find exists in the list of player names, then print the name of that player along with their associated score (which is in the second list at the same index). If the player to find does not exist in the list of player names, print player not found. Here are two examples of using this function:
>>> players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
>>> scores = [5, 8, 10, 6, 10, 4]
>>> ScoreFinder(players, scores, "jill") % NOTE: upper and lowercase should both work
OUTPUT Jill got a score of 6
>>> ScoreFinder(players, scores, "Manuel")
OUTPUT player not found'''

         
    

