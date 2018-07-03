import os


def semester_rename(myPath, stream_Name, fileName):
    sem_count = 0
    if fileName == "Semester1":
        semName = "1SEM"
    elif fileName == "Semester2":
        semName = "2SEM"
    else:
        semName = "3SEM"
    semPath = os.path.join(myPath, fileName)
    for files in os.listdir(semPath):
        print("old name: "+files)
        src = os.path.join(semPath, files)
        dst = os.path.join(semPath, "JNTUH_"+stream_Name +
                           "_"+semName+"_"+str(sem_count)+"_"+"2016.pdf")
        os.rename(src, dst)
        sem_count += 1
    sem_count = 0


parentPath = "D:\\folderTry\\"
count = 0
check = 1
stream_Name = "BTECH"
for fileName in os.listdir(parentPath):
    if fileName == "1st&2nd Combined":
        semName = "1SEM"
    elif fileName == "3rd Combined":
        semName = "3SEM"
    elif fileName == "4th Combined":
        semName = "4SEM"
    myPath = os.path.join(parentPath, fileName)
    for fileName in os.listdir(myPath):
        if check > 8:
            stream_Name = "MTECH"
        if fileName == "Semester1" or fileName == "Semester2" or fileName == "Semester3":
            semester_rename(myPath, stream_Name, fileName)
        else:
            print("old name: "+fileName)
            src = os.path.join(myPath, fileName)
            dst = os.path.join(myPath, "JNTUH_"+stream_Name +
                               "_"+semName+"_"+str(count)+"_"+"2016.pdf")
            os.rename(src, dst)
            count += 1
    count = 0
    check += 1
