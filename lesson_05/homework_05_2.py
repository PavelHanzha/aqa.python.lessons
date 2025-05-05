people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 1 task
people_records.insert(0, ('Pasha', 'Hanzha', 29, 'QA', 'Kyiv'))
# print(people_records[6])
# print(people_records[10])
# print(people_records[13])
# 2 task
index_5 = people_records.pop(5)
people_records.insert(1, index_5)
index_1 = people_records.pop(1)
people_records.insert(4, index_1)
print(people_records)

# 3 task
counter = 0
list_with_age_more_30 = []
for k in people_records:
    if counter == 6:
        if k[2] >= 30:
            list_with_age_more_30.append(k)
    if counter == 10:
        if k[2] >= 30:
            list_with_age_more_30.append(k)
    if counter == 13:
        if k[2] >= 30:
            list_with_age_more_30.append(k)
    counter += 1
print(list_with_age_more_30)