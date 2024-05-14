#Not Perfect

users = dict()
users["Pop"] = {"minion", "spiderman"}
users["Tim"] = {"ju-on", "minion"}
users["Pun"] = {"minion"}
users["Puk"] = {"avenger", "batman", "spiderman"}
users["Tan"] = {"spiderman"}
def calculate_user_scores(query, users):
    sortedusers=sorted(users)
    user_scores=dict()
    for i in sortedusers:
        union_set=len(users[i].union(query))
        diff_set=len(users[i].difference(query))
        intersect_set=len(users[i].intersection(query))
        prob=round(intersect_set/union_set,2)
        if prob==0.0 or prob==1:prob=0
        user_scores[i]=prob
    return user_scores
def recommend_movies(query, users, user_scores):
    recommend = list()
    if set(user_scores.values())=={0}:return 'No recommend'
    high=max(user_scores.values())
    for i in user_scores:
        if user_scores[i]==high:
            for j in users[i].difference(query):
                recommend.append(j)
    recommend.sort()
    return recommend
def main():
    n = int(input())
    query = set()
    for i in range(n):
        query.add(input().lower())
    user_scores = calculate_user_scores(query, users)
    print(sorted(user_scores.items()))
    recommend = recommend_movies(query, users, user_scores)
    print(recommend)
main()