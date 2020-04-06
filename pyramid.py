def piramid(n):
    for i in range(1,n+1):
        print("")
        for j in range(1,n-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print("* ", end="")
          
number = int(input("Enter the number "))
piramid(number)
# b) the piramid (n=5)
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *