def calculate_average(value_list):
    sum = 0
    for i in value_list:
        sum += i
    return sum / len(value_list)

# used eval to resolve input str; could not do it without
marks_list = eval(input("Marks: ")) 
print("Average Marks: ", calculate_average(marks_list))
