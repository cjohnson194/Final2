from faker import Faker
import random
import csv

# file to create sample data using faker module to store in CSV file

def main() -> None:
    """
    Function to create sample data for CSV file
    """
    fake = Faker()
    sample = []

    genders = ['Male', 'Female', 'N/A']

    with open('sample.csv', 'w', newline='') as content:
        sample_data = csv.writer(content)
        sample_data.writerow(['First Name', 'Last Name', 'Gender', 'Email Address', "Phone Number", 'Username', 'Password'])

        for i in range(150):
            sample.append(fake.first_name())
            sample.append(fake.last_name())
            sample.append(random.choice(genders)) #instead of having the fake data choose from radiobuttons on register page
            sample.append(fake.ascii_email())
            sample.append(fake.msisdn()) #phone numbers without any extra characters
            sample.append(fake.user_name())
            sample.append(fake.password())
            sample_data.writerow(sample)

            sample = []


    
if __name__ == '__main__':
    main()