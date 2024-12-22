# Explanation: List comprehension is a concise way to create lists. 
# It makes the code shorter and potentially improves performance.

# Code using a loop
marks = [20, 35, 50, 78, 40]
new_marks = []
for x in marks:
    new_marks.append(x + 2)  # Fixed the ">" and "append" typo
print(new_marks)

# Code using list comprehension
marks = [20, 35, 50, 78, 40]
new_marks = [x + 2 for x in marks]
print(new_marks)

#code using set comprehensing
marks1={39,25,21,56,75}
new_marks1={x+2 for x in marks1}
print(new_marks1)
