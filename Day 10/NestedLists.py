# Step 1: First we created an empty list.

# Step 2: then we created a loop that will also take input of the total number of students.

# Step 3: After this, we have taken the input of names and scores inside our loop.

# Step 4: After this, we sorted our list and converted it into a set. 
# And we have also used list comprehension in which score is our output and we have used for loop after this.

# Step 5: In the last step, we used another list comprehension in which the name is our output 
# and we used for loop after this with if condition. Here, ‘\n’.join will print the names in different lines.

if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])

second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))