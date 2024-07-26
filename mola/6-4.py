i, k, guguLine = 0, 0, ""

for i in range(9,1,-1):
    guguLine = guguLine + ("# %d단 #" %i)

print(guguLine)

for i in range(9, 1,-1):
    guguLine = ""
    for k in range(9, 1,-1):
        guguLine = guguLine + ("%2dX %2d= %2d"%(k,i,i*k))
    print(guguLine)
