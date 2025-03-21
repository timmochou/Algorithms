from collections import deque
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] =='m'
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set() #存放已經搜尋過的人
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + "是芒果賣家!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

search("you")