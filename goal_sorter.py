def define_goals():
    num_goals = int(input("Number of goals: "))
    list_of_goals = []
    for goal in range(num_goals):
        list_of_goals.append(input("Goal " + str(goal + 1) + ": "))
    return list_of_goals


def add_proposals(list_of_goals):
    num_proposals = int(input("Number of people sorting: "))
    lists_of_proposals = []
    for person in range(num_proposals):
        print("")
        proposer_name = input("Name of person " + str(person + 1) + ": ")
        lists_of_proposals.append([])
        for goal in list_of_goals:
            print("")
            print(goal)
            goal_placement = int(input(proposer_name + " placed this goal at number: "))
            lists_of_proposals[person].append(goal_placement)
    return lists_of_proposals


def score_goals(list_of_goals, lists_of_proposals):
    for goal in range(len(list_of_goals)):
        list_of_goals[goal] = [list_of_goals[goal], 0]
        for proposal in range(len(lists_of_proposals)):
            list_of_goals[goal][1] += lists_of_proposals[proposal][goal]


def return_score(goal):
    return goal[1]


def print_score(list_of_goals):
    list_of_goals.sort(key=return_score)
    print("")
    for i in range(len(list_of_goals)):
        print(list_of_goals[i][0] + ": " + str(list_of_goals[i][1]))


def start():
    goal_list = define_goals()
    proposals_list = add_proposals(goal_list)
    score_goals(goal_list, proposals_list)
    print_score(goal_list)


start()
