import os

from reggisearch import search_values


def get_bluestacks_config_file():
    di = search_values(
        mainkeys=r"HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks_nxt", subkeys="UserDefinedDir"
    )
    bstconfigpath = di[r"HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks_nxt"]["UserDefinedDir"]
    return bstconfigpath

def get_bluestacks_user_folder():
    bstconfigpath=get_bluestacks_config_file()
    bstconfigpath = os.path.normpath(os.path.join(bstconfigpath, "bluestacks.conf"))
    return bstconfigpath

def get_tesseract_exe():
    tesserkey = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Tesseract-OCR'
    tesserf='UninstallString'
    di = search_values(mainkeys=tesserkey, subkeys=(tesserf,))
    pa = f'{os.sep}'.join(di[tesserkey][tesserf].split(os.sep)[:-1])
    pa = os.path.normpath(os.path.join(pa,'tesseract.exe'))
    return pa
