nominee1 = input("Enter nominee 1 name: ")
nominee2 = input("Enter nominee 2 name: ")

num_1_votes = 0
num_2_votes = 0

voters_id = [1,2,3,4,5,6,7,8,9,10]

total_voters = len(voters_id)

while True:
    if voters_id == []:
        print("Voting session Over")
        if num_1_votes> num_2_votes:
            percent = ((num_1_votes/total_voters)*100)
            print(nominee1," has won with ",percent,"% votes.")
            break

        elif num_2_votes> num_1_votes:
            percent = ((num_2_votes/total_voters)*100)
            print(nominee2," has won with ",percent,"& votes.")
            break

        else:
            print("Its a Tie.")
            break
    else:
        voter = int(input("Enter your voter ID number: "))
        if voter in voters_id:
            print("You are a voter")
            voters_id.remove(voter)
            vote = int(input("Enter your vote(1 or 2): "))
            if vote ==1:
                num_1_votes +=1
                print("Thank You for voting.")

            elif vote ==2:
                num_2_votes +=1
                print("Thank You for voting.")

            else:
                print("Invalid Vote")
                break
        else:
            print("You have already voted or you are not a valid voter.")

