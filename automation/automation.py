import re
from faker import Faker


fake = Faker('en_US')


potential_contacts = ""

for i in range(200):
    email = fake.email()
    phone_number = fake.phone_number()
    potential_contacts += " " + email + " "
    potential_contacts += phone_number
  
   
  
    potential_contacts += "\n"
with open("potential-contacts.txt", "w+") as f:
    f.write(potential_contacts)


email_after_editting = list(re.findall(r'[\w\.-]+@[\w\.-]+', potential_contacts))

phone_after_editting = list(re.findall(r"\w{3}-\w{3}-\w{4}", potential_contacts))




def test(email_after_editting):
     return (('\n').join(email_after_editting))
email_space=test(email_after_editting)

def test2(phone_after_editting):
     return (('\n').join(phone_after_editting))
phone_space=test2(phone_after_editting)


with open("email.txt" , "w") as f:
    f.write(email_space)


with open("phone_numbers.txt" , "w") as f:
    f.write(phone_space)

