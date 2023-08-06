import os
import multiprocessing as mp

def getUserName():
    osName = os.name.lower()
    if osName == 'nt' or 'win' in osName:
        return os.getenv("USERNAME", "user")
    else:
        return os.getenv("USER", "user")

def getFullUserName():
    osName = os.name.lower()
    if osName == 'nt' or 'win' in osName:
        import ctypes

        GetUserNameExW = ctypes.windll.secur32.GetUserNameExW
        nameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameExW(nameDisplay, None, size)

        displayNameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameExW(nameDisplay, displayNameBuffer, size)
        return displayNameBuffer.value or getUserName()
    else:
        import pwd

        unixDisplayName = ( entry[4] for entry in pwd.getpwall() if entry[2] == os.geteuid() )
        return unixDisplayName.__next__() or getUserName()

def startBrowser(hostUrl):
    def __startBrowserIntl(hostUrl):
        try:
            import webbrowser
            webbrowser.open(hostUrl, new=2)
        except:
            pass

    osName = os.name.lower()
    if osName == 'nt' or 'win' in osName:
        __startBrowserIntl(hostUrl)
    else:
        browserProcess = mp.Process(target=__startBrowserIntl, args=(hostUrl,))
        browserProcess.daemon = True
        browserProcess.start()
