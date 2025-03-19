voted = {}
def check_voter(name):
    if name in voted:
        print("請他離開")

    else:
        voted[name]= True
        print("讓他投票!")
check_voter("tom")
check_voter("mike")
check_voter("tom")
print(voted)
