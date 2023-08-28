def getProperty(object : object, property : str):
    try:
        return object[property]
    except:
        return None