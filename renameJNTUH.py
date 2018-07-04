import os

parentPath = "D:\\folderTry\\"
count = 1
for fileName in os.listdir(parentPath):
    myPath = os.path.join(parentPath, fileName)
    if count % 2 == 0:
        os.remove(myPath)
    else:
        print("Old file: "+fileName)
        src = os.path.join(parentPath, fileName)
        dst = os.path.join(parentPath, "JNTUH_BTECH_1SEM_" +
                           str(count)+"_2017.pdf")
        os.rename(src, dst)
    count += 1
