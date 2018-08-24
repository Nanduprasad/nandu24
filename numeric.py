userInput = 0
while True:
  try:
     userInput = int(input("enter something:"))       
  except ValueError:
     print("No")
     continue
  else:
     print("Yes")
     break
