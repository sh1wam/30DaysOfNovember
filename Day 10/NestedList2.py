nested_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nested_list.append([name, score])
        
scores = [score for name, score in nested_list]
scores_sorted = sorted(set(scores))[1]

names = [name for name, score in nested_list if score == scores_sorted]
names.sort()

for name in names:
    print(name)