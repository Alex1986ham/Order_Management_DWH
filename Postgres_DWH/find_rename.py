import glob, os
"""
os.chdir('\\data')
for file in glob.glob("*.txt"):
    print(file)
"""







"""
for file in glob.glob('*.txt'):
    with open(file) as f:
        contents = f.read()
        print(f)
        #print(contents)
"""

"""
    if 'struct' in contents:
        print file
"""

"""
f = glob.glob('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\*.txt')
with open(f) as fo:
    print(fo)
"""

"""
os.chdir('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data')
i=1
for file in os.listdir():
    src=file
    dst="1"+".txt"
    os.rename(src,dst)
    i+=1
"""


os.remove('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\1.txt')

#path = glob.glob('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\*.txt')

#print(path)


#f = os.rename('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\*.txt', 'C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\11.txt')
