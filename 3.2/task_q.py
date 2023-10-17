def task_q():
    """задание q: Друзья дузей"""
    friendships = {}
    while (ppl := input()) != "":
        name, friend = ppl.split(" ")
        if name not in friendships:
            friendships[name] = set()
            friendships[name].add(friend)
        else:
            friendships[name].add(friend)
    # frienships are bidirectional :(
    for name, friends in friendships.copy().items():
        for friend in friends:
            if friend not in friendships:
                friendships[friend] = set()
                friendships[friend].add(name)
            else:
                friendships[friend].add(name)
    for name, friends in sorted(friendships.items()):
        fr_2 = set()
        for x in friends:
            fr_2 |= friendships[x]
        fr_2.discard(name)
        fr_2 -= friends
        print(f"{name}: {', '.join(sorted(fr_2))}")


if __name__ == '__main__':
    task_q()
