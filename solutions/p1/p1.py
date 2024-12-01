text_file1 = open("data_p1.txt", "r")
doc1 = text_file1.read().split()
text_file2 = open("data_p1_right.txt", "r")
doc2 = text_file2.read().split()

doc1.sort()
doc2.sort()

diff = 0

for i in range(len(doc1)):
    num1 = doc1[i]
    num2 = doc2[i]
    diff = diff + abs(int(num1) - int(num2))
    print(diff)

print()

sim = 0

for i in range(len(doc1)):
    num1 = doc1[i]
    occur = doc2.count(num1)
    temp_var = int(num1) * occur
    sim = sim + temp_var
    print(sim)
