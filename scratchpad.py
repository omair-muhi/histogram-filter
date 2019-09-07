print("hello-world")

list =[[1,1],[2,2],[3,3]]
print("List length is " + str(len(list)))
for i in range(len(list)):
    for j in range(len(list[i])):
        print("Value at row="+str(i)+",col="+str(j)+" "+str(list[i][j]))
