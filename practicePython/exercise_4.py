number = int(input("give a number: "))
print(" ".join([str(x) for x in range(1,number+1) if not number%x]))  #ach te jednolinijkowce ; )