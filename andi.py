fullName = "andi wiranto"
title = "dr."

def greeting(title, fullName):
    print("good morning, ", title, fullName)
    
def farewell(title, fullName):
    print("see you later, ", title, fullName)
    
import sys
print(sys.argv)

if (sys.argv[1]):
    if (sys.argv[1] == 'greet', 'meet'):
        if (len(sys.argv)>3):
            greeting(sys.argv[2], sys.argv[3])
        else:
            print("fungsi cek memerlukan title dan nama")