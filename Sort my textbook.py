def sorter(textbooks):
    textbooks.sort(key=str.lower)
    return textbooks
print (sorter(['Algebra', 'history', 'Geometry', 'english'])) 