def main():
    import os
    import shutil
    import datetime

    # setup
    date = datetime.datetime.now()
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    try:
        from seting import dstPath as dstPath
        if(dstPath[0] == "~"):
            dstPath = dstPath.replace("~", os.getenv("HOME")) 
        if(dstPath[len(dstPath) -1] != "/"):
            dstPath = dstPath + "/"
        from seting import dowPath as dowPath
        if(dowPath[0] == "~"):
            dowPath = dowPath.replace("~", os.getenv("HOME"))
        if(dowPath[len(dowPath) -1] != "/"):
            dowPath = dowPath + "/"
                
    except:
        print('Error File seting.py dosnt exit')
        exit()

    # checking for folders 
    if(os.path.isdir(dstPath) == False):
        os.mkdir(dstPath)
    
    if(os.path.isdir(dstPath) == False):
        os.mkdir(dowPath)

    # make dir for curnent time 
    if(os.path.isdir(dstPath + date) == False):
        os.mkdir(dstPath + date)
    
    # move files 
    list = os.listdir(dowPath)
    for file in list:
        try:
            shutil.move(dowPath + file, dstPath +date)
            print("moving file " + file)
        except:
            print("can not move file " + file)


if(__name__ == "__main__"):
    main()
