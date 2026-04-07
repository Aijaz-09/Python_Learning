#Set operations

while True:
    A=set()
    B=set()
    print("\n****************************************************************")
    n_A=int(input("how many elements in set A: "))
    for i in range(n_A):
        A.add(input("Enter element {0}: ".format(i+1)))

    n_B=int(input("how many elements in set B: "))
    for i in range(n_B):
        B.add(input("Enter element {0}: ".format(i+1)))
    print("A =",A)
    print("B =",B)

    print("What operation:"
          "\nUnion: U"
          "\nIntersection: I"
          "\nDifference: D"
          "\nSymmetric Difference: S")
    op=input("Your Choice: ").upper()

    match op:
        case 'U':
            print("A U B =",A.union(B))
        case 'I':
            print("A inter B = ",A.intersection(B))
        case 'D':
            print("A - B = ",A.difference(B))
        case 'S':
            print("A ^ B = ",A.symmetric_difference(B))
        case _:
            print("Please enter a valid operation!")
    print("\n****************************************************************")
    status=input("Do you want to continue: Y/N: ").upper()
    if status=='N':
        print("Thanks for using my program!")
        break
    
