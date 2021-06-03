# import os
# import shutil

# path = input("Import Directory Path: ")
# allFiles = os.listdir(path)

# for eachFile in allFiles:
#     name, extension = os.path.splitext(eachFile)
#     ext = extension[1:]
    
#     if ext == "":
#         continue

#     pathExist = os.path.exists(path + "/" + ext)
#     if  pathExist:
#         shutil.move(path+"/"+ eachFile, path + "/" + ext + "/" + eachFile)
#     else:
#         os.mkdir(path + "/" + ext)
#         shutil.move(path+"/"+ eachFile, path + "/" + ext + "/" + eachFile)

# source = "/Users/RavinderRaghunayakula/Desktop/Coding/WhiteHat Projects/IntroToPython/classes/files/"
# destination = "/Users/RavinderRaghunayakula/Desktop/Coding/WhiteHat Projects/IntroToPython/classes/backup/"
# allFiles = os.listdir(source)


# for eachFile in allFiles:
#     if os.path.exists(destination):
#         if  os.path.isfile(source + eachFile):
#             shutil.copy((source + eachFile), destination)
#     else:
#         os.mkdir(destination)
#         if  os.path.isfile(source + eachFile):
#             shutil.copy((source + eachFile), destination)
        

# shutil.copytree(source, destination)
