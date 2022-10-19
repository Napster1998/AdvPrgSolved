# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

with open('fake','w') as f:
  f.write('''3 5:1 2 3 4 5 6 7 8 9
3 5 2: 1 2 3 4 5 6 7 8 9 10 11 12 11 12
3: 5:1 2 3 4 5 6 7 8 9
3 5 2 1 2 3 4 5 6 7 8 9 10 11 12 11 12
3 5:1 2 3 4 5 6 7 8 9 1O9 9 10
Hello World 3 5 2: 1 2 3 4 5 6 7 Goodbye 8 9 10 11 12 11 12'''
  )


def rect(x):
    try:
        return int(x)
    except:
        return x

#
# with open('fake') as f:
#     line = f.read()
#     for a in line.split():
#         print(rect(a))

def s(a,l):
  total=0
  for i in l:
    for j in a:
      if i%j==0:
        total+=i
        break
  return total

def ff(inputFileName, outputFileName):
  with open(inputFileName) as i, open(outputFileName,'w') as o:
    for line in i:
      try:
        f, m = [[rect(line) for line in a.split()] for a in line.split(':')]
        o.write(str(s(f,m))+':'+line)
      except:
        o.write('Corrupt\n')
        print(line)
      # o.write(str(s(f,m))+':'+line)

ff('fake','output')