# There are a lot of horses in the yard, and we want to count how many there are. Unfortunately, we've only got a
# recording of the sounds from the yard. All the horses say "neigh". The problem is they can "neigh' many times. The
# recording from the yard is sadly all mixed together. So, we need to figure out from the overlapping sounds how many
# horses there could be. For example, we've got two horses in the yard, and we hear this "neigneighh". From this
# recording, we can successfully deduce there are 2 horses. Another example is "neighneigh". From this example,
# we can only tell there is one horse in the yard. As an additional complexity, our recording might not be perfect.
# If it's a bad recording, we should give "Invalid" as the response. The input will be given as a string on one line.
# The output should be printed on its own line.

# Sample Input
# nenigehnieighgh

# Sample Output
# 2

recording = input("Input Audio : ")

# Number of n's before the first h
count = 0
for i in recording:
    if i == "h":
        print(count)
        break
    elif i == "n":
        count += 1

