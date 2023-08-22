a=input("hello. are you ready for a quiz :")
if a.lower()!="yes":
    print("sorry:)")
else:
    print("okey lets start")
    total_marks=20
    score=0
    q1=input("what is CPU stands for :")
    if q1=="central processing unit":
        score+=4
    else:
        print("")
    q1=input("what is GUI stands for :")
    if q1=="graphical user interface":
        score+=4
    else:
        print("")
    q1=input("what is RAM stands for :")
    if q1=="random access memory":
        score+=4
    else:
        print("")
    q1=input("what is ROM stands for :")
    if q1=="read only memory":
        score+=4
    else:
        print("")
    q1=input("what is GPS stands for :")
    if q1=="global positioning system":
        score+=4
    else:
        print("")

    x=input("Do you want to know your marks ? :")
    print(score)
    y=total_marks*40//100
    z = score//2
    if x=="" and score>=y:
        print("passed")
    else:
        print("failed")


