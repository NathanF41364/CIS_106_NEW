                         ##Functions##

#Function List Maker
def CompListMaker(lists):
  l = int(input("Enter the length of the list: "))
  for a in range(0, l, 1):
    inp = (int(input("Enter a number: ")))
    lists.append(inp)
  return lists

#Function Display List
def CompPrint(lists):
  print ()
  print ()
  print ("Lists:")
  for list in lists:
    print (list)

#Function Insert Score(99)
def CompInsert(lists):
  lists.insert(1,99)
  return lists

#Function Replace(100)
def CompReplace(lists):
  lists[1] = 100

#Function New List/ Combine Lists
def CompCombine(lists):
  lists2 = [500, 600, 700, 800, 900]
  print ()
  print ("Lists 2:")
  print (lists2)
  lists.extend(lists2)

#Function Remove(800)
def CompRemove(lists):
  lists.remove(800)

#Function Remove Item(3)
def CompRemoveItem(lists):
  del lists[3]

#Function Count (A)
def CompCount(grades):
  count = grades.count("A")
  print (count)

#Function Find (B)
def CompFind(grades):
  find_b = grades.index("B")
  print (find_b)

#Function Find Failed(F)
def CompFindFail(grades):
  find_f = "F"
  if find_f in grades:
    found = grades.index(find_f)
    print (found)
  else:
    print ("F is not in the list")

#Function Clear list
def CompClear(lists2):
  lists2.clear()
  print (lists2)

#Function Delete Lists2
def CompDelete(lists2):
  del lists2
  print (lists2)

#Function Sort List
def CompSort(players):
  players.sort()
  print (players)

#Function Copy
def CompCopy(players):
  players2 = players.copy()
  print (players2)

#Function Reverse(players2)
def CompReverse(players):
  players.reverse()
  print (players)
  


                ##Lists(Remove the # to use)##
  
#lists = []
#lists2 = [500, 600, 700, 800, 900]
#players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

                 ##Main(remove the # to use)##
  
#list = CompListMaker(lists)
#insert = CompInsert(lists)
#replace = CompReplace(lists)
#combine = CompCombine(lists)
#remove = CompRemove(lists)
#remove_item = CompRemoveItem(lists)
#print = CompPrint(list)
#grades = ["A", "B", "C", "A", "A", "C"]
#count = CompCount(grades)
#find_b = CompFind(grades)
#findfail = CompFindFail(grades)
#clearlist = CompClear(lists2)
#delete = CompDelete(lists2)
#sort = CompSort(players)
#copy = CompCopy(players)
#reverse = CompReverse(players)