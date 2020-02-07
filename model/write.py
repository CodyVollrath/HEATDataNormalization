def writeToFile(filename, data):
    try: 
        f = open(filename,"w+")
        f.write(data)
        return True
    except:
        return False
    finally:
        f.close()

def appendTXT(filename, data):
    try:
        f = open(filename, "a+")
        f.writelines(data + "\n")
        return True
    except:
        return False
    finally:
        f.close()