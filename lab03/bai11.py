a=int(input("nhập độ rộng tam giác"))
for i in range(a+1):
    print(" "*(a+1-i),"* "*(i))
for i in range(a-1):
    if i==0:
        print(" "*a,"*")
        print("{}*{}*".format(" "*(a-i) ," "*(2*i+1)))
    elif i>0 and i<a-2:
        print("{}*{}*".format(" "*(a-i) ," "*(2*i+1)))
    else:
        print(" "*(a-1-i),"* "*(i+2))
print("        *")
print(" ")
print("      *   *")
print(" ")
print("    *   *   *")
print(" ")
print("  *   *   *   *")
print(" ")
print("*  *  *   *  *  *")
print("     *")
print(" ")
print("   *   *")
print(" ")
print("  *     * ")
print(" ")
print(" *       *")
print(" ")
print("* * * * * *")
