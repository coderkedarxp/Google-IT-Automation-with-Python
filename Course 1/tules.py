# tuples are immutable
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))
  

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)




multiples = [x*7 for x in range(1,11)]
print(multiples)


z = [x for x in range(0,101) if x % 3 == 0]
print(z)

