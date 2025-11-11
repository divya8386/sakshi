def add_call(F, R, queue, size): 
    if (F == (R+1)%size): 
        print("The queue is full, cannot add event") 
        return (F,R) 
    cusid = input("Enter the customer ID: ") 
    ct = input("Enter the call time: ") 
    if F == -1: 
        F = R = 0 
        queue[R] = [cusid, ct] 
    else: 
        R = (R+1) % size 
        queue[R] = [cusid, ct] 
    return (F,R) 
       
def view_queue(F, R, queue, size): 
    if F == -1: 
        print("The queue is empty.") 
    elif (R > F): 
        for i in range(F, R+1): 
            print(queue[i]) 
    elif (R < F): 
        for i in range(F, size): 
            print(queue[i]) 
        for i in range(0, R+1): 
            print(queue[i]) 
    else: 
        print(queue[F]) 
 
def answer_call(F, R, queue, size): 
    if F == -1: 
        print("No call in the queue.") 
    elif F == R: 
        print(f"The call \"{queue[F][0]}\" was answered.") 
        F = R = -1 
    else: 
        print(f"The call \"{queue[F][0]}\" was answered.") 
        F = (F + 1) % size 
    return (F, R) 
 
def isQmt(F, R, queue, size): 
    if F == -1: 
        print("True") 
    else: 
        print("False") 
 
def Menu(): 
    size = int(input("Enter the size of the queue: ")) 
    queue = [0]*size 
    B = E = -1 
    
    while(True): 
        
        print("""Choose a number to execute the function corresponding to it: 
              0 - Exit 
              1 - Add call 
              2 - Answer call 
              3 - View queue 
              4 - Is the queue empty? 
              """) 
    
        choice = input("Enter the choice: ") 
    
        if choice == "0": 
            return 
        elif choice == "1": 
            B, E = add_call(B, E, queue, size) 
        elif choice == "2": 
            B, E = answer_call(B, E, queue, size) 
        elif choice == "3": 
            view_queue(B, E, queue, size) 
        elif choice == "4": 
            isQmt(B, E, queue, size) 
        else: 
            print("Select a valid option: ") 
 
Menu() 
 
 
 
 
 
 
 
 
