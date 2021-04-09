# Assessment 3 @ Noroff University College
_author_ = "Thomas Thaulow"
copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"
import re
from datetime import date

class StudentRecordClass:

    # Constructor
    def __init__(self, idnum=None, fname=None, lname=None, age=None, email=None, subject=None):
        self.idnum = idnum
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.subject = subject

    # print out the full name of the student
    def displayName(self, object):
        print(f"{object.fname} {object.lname}")

    def validate_and_insert_record(self):

        try:
            idnum = get_idnum()
            fname = get_first_name().capitalize()
            lname = get_last_name().capitalize()
            age = get_age()
            impersonator(idnum,age)
            email = get_email()
            course = get_course()

            print(f"{idnum},{fname},{lname},{age},{email},{course}")

            print("Writing Student Information to Student Record File")
            file = open("StudentRecords.txt", "a")
            file.write(f"{idnum},{fname},{lname},{age},{email},{course}")
            file.write("\n")
            file.close()

        except Exception:
            print("Something went wrong while writing record to file")

    def get_data_from_file(self):

        records = []
        file = open("StudentRecords.txt").readlines()
        for line in file:
            record = line.split(",")
            records.append(record)

        return records

    def display_all_students(self):

        records = self.get_data_from_file()
        student_list = []

        for record in records:

            student = StudentRecordClass()

            student.idnum = record[0]
            student.fname = record[1]
            student.lname = record[2]
            student.age = record[3]
            student.email = record[4]
            student.course = record[5]

            student_list.append(student)

        for std in student_list:
            self.displayName(std)

    def display_subject_class_list(self, subject):

        records = self.get_data_from_file()

        for record in records:
            if str(record[5].strip('\n')) == subject:
                print(record[1] + " " + record[2])

    def display_youngest(self):

        records = self.get_data_from_file()
        names = []

        minimum = int(records[0][3])
        for record in records:
            record = int(record[3])
            if record < minimum:
                minimum = record

        for record in records:
            if int(record[3]) == minimum:
                names.append(f"{record[1]} {record[2]}")

        print(f"The youngest student(s) of age {minimum} is/are: ")
        for name in names:
            print(name)

    def display_oldest(self):
        records = self.get_data_from_file()
        names = []

        maximum = int(records[0][3])
        for record in records:
            record = int(record[3])
            if record > maximum:
                maximum = record

        for record in records:
            # record = int(record[3])
            if int(record[3]) == maximum:
                names.append(f"{record[1]} {record[2]}")

        print(f"The oldest student(s) of age {maximum} is/are: ")
        for name in names:
            print(name)


################################################
################ GET & VALIDATE ################
################################################

# Fødselsnummer
def get_idnum():
    try:
        idnum = input("\nEnter ID Number... (11 digits) : ")
        idnum = idnum.replace(" ", "")
        if idnum != "":
            idnum = validate_idnum(idnum)
            return idnum
        else:
            print("idnum cannot be empty")
            raise Exception
    except Exception:
        print("Oops something is buggy")
        print("cannot validate ID number. Please try again. ")
        return get_idnum()

def validate_idnum(idnum):

    # As length is used multiple times, we rather store it in a variable
    length = len(idnum)

    try:
        if length == 11:
            idnum = int(idnum)
            return idnum
        elif length >= 11:
            print("To many digits. You entered ",length,"numbers. Norwegian ID numbers are 11 digits. ")
            raise Exception

        elif length <=11:
            print("To few digits. You entered only",length,"numbers. Norwegian ID numbers are 11 digits.")
            raise Exception

        else:
            print("cannot validate ID number")
            raise Exception

    except Exception:
        print("Oops something is buggy. Cannot validate ID number. Please try again...")
        return get_idnum()


# First Name
def get_first_name():
    name = input("\nEnter the first name... : ")
    if name != "":
        name = validate_name(name)
        return name
    else:
        print("First Name cannot be empty")
        get_first_name()


# Last Name
def get_last_name():
    name = input("\nEnter the last name... : ")
    if name != "":
        name = validate_name(name)
        return name
    else:
        print("Last Name cannot be empty")
        get_first_name()


def validate_name(name):
    name = name.lower()
    return name


# Course
def get_course():
    try:
        course = input("\nEnter the course name from [python, ruby, c, java, php]...: ")
        if course != "":
            course = validate_course(course)
            return course
        else:
            print("Course name cannot be empty")
            raise Exception
    except Exception:
        print("Oops something is buggy")
        return get_course()


def validate_course(course):
    try:
        course = course.lower().replace(" ", "")
        course_list = ['python', 'ruby', 'c', 'java', 'php']

        if course in course_list:
            course = course
            return course
        else:
            print("Please enter a valid course from the list")
            raise Exception
    except Exception:
        return get_course()


# Age
def get_age():
    try:
        age = input("\nEnter the age... : ")
        if age != "":
            age = validate_age(age)
            return age
        else:
            print("Age field cannot be empty")
            raise Exception
    except Exception:
        print("Oops something is buggy")
        return get_age()

def validate_age(age):
    try:
        if 16 <= int(age) <= 100:
            age = int(age)
            return age
        elif int(age) >=100:
            print("Sorry. We only accept students under the age of 100.")
            raise Exception
        elif int(age) <=16:
            print("Sorry. We only accept students over the age of 16.")
            raise Exception
        else:
            raise Exception
    except Exception:
        print("Oops something is buggy. Only numbers is allowed. Please try again...")
        return get_age()


#Mail
def get_email():
    try:
        email = input("\nEnter your email... : ")
        if email != "":
            email = validate_email(email)
            return email
        else:
            print("Email field cannot be empty")
            raise Exception

    except Exception:
        return get_email()


def validate_email(email):
    try:
        if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-åA-Å0-9!@#$%^&*\-]{2,6}$", email):
        # Possibility for adding SMTP validation. due to uncertainty about Noroff´s network ports, this was not added
            return email
        else:
            print("Could not validate email address. Format must be: example@domain.com ")
            raise Exception
    except Exception:
        return get_email()

#Age and ID Validation
def impersonator(idnum, age):

    idnum = str(idnum)
    born = idnum[0:6]
    birth_year = born[4:]
    today = date.today()
    today_year = today.year
    today_year = str(today_year)
    today_year = today_year[2:]

    # If year is greater than today- year e.g. 20 (last two digits)
    # add 19, else add 20

    if int(birth_year) > int(today_year):
        birth_year = "19" + birth_year
    else:
        birth_year = "20" + birth_year

    # we convert string to integers
    difference = int(today.year) - int(birth_year)

    # check for validation
    if difference != age:
        print("WARNING: Discrepancy between age and ID number. ID Theft is a criminal offence punishable by law.")
