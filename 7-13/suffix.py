def getfile_fix(filename):
    return filename[filename.rfind('.') + 1:]


def getfile_fix2(filename):
    return filename[filename.rindex('.') + 1:]


print(getfile_fix('runoob.txt.txt'))
print(getfile_fix2('runoob.txt.txt'))