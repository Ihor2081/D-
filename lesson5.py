# file=open("notes.txt","w")
# file.write("Hello!")
# file.close()
# file=open("notes.txt","r")
# print(file.read())
# file.close()

# with open("notes.txt","w") as file: file.write("Hello World")
# with open("notes.txt","r") as file: print(file.read())

count=0
search=input()
with open("notes.txt","r") as file:
    words=file.read().lower().split()
    for i in words:
        if i==search:
            count+=1

print(f"Слово", search, 'зустрічається у файлі', count, "разів")