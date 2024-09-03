def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


# print("Base price: ${:.2f}. With Tax: ${2:.2f}".format(price, with_tax))
# the above code is for formatting and getting the output with 2 decimals

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:2.1f} km".format(miles,km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


























