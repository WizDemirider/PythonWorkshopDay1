Numbers = [21, -17, 9]
# Squares = [num * num for num in Numbers if num > 0]

Squares = []
for num in Numbers:
	if num>0:
		Squares.append(num*num)

print(Squares)
