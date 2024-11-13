#Задание №8
def isSubstring(str1, str2):
    if str1 in str2:
        return True
    else:
        return False

string1 = "employ"
string2 = "employment"

if isSubstring(string1, string2):
    print("Строка 1 входит в строку 2")
else:
    print("Строка 1 не входит в строку 2")