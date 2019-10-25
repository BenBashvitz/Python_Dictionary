#בן בשביץ
#י"א
"""
Spyder Editor

This is a temporary script file.
"""

def CreateDict():
    #טענת כניסה: קלט של שמות שהם המפץחות במילון ומספרים שהם הערך במילון
    #טענת יציאה: מחזירה את המילון שנוצר
    names = {}
    for i in range(3):
        names [input("enter a name ")] = int(input("enter a number "))
    return names

def CheckDict(Dict):
    #טענת כניסה: מקבלת מילון וקולטת שם לחפש במילון
    #טענת יציאה: אם השם נמצא במילון מדפיסה "yes" אחרת מדפיסה "no"
    name = input("enter a name to search in the dictionary ")
    if name in Dict:
        print("yes ")
    else:
        print("no ")

def NumSquared():
    #טענת כניסה: קולטת את המספר הראשון והאחרון שיופיעו במילון
    #טענת יציאה: מחזירה מילון שבו המפתחות הם כל המספרים בין שני המספרים שנקלטו כולל והערך הוא המפתח בריבוע
    numbers = {}
    start = int(input("enter a number to begin on"))
    end = int(input("enter a number to end on"))
    for x in range(end-start+1):
        numbers [x + start] = (x + start)**2
    return numbers

def main():
    nameDict = CreateDict()
    CheckDict(nameDict)
    numDict = NumSquared()
    for x,y in numDict.items():
        print(x,y)
    
if __name__ == "__main__":
    main()