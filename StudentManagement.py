# Assessment 3 @ Noroff University College
_author_ = "Thomas Thaulow"
copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"

from StudentRecordClass import StudentRecordClass
from EncodeDecodeClass import EncodeDecodeClass

# Main file
# to start program execution
def main():

    # PART 1
    # Set std_info = yes, allowing while loop underneath for first time use of loop"
    std_info = 'y'

    # Loop PART 1 until user enters "N".
    while std_info == 'y':

        std_info = input("Would you like to enter a student's information...? ( y/n ): ")
        std_info = std_info.lower()

        if std_info == "y":

            student_record = StudentRecordClass()
            student_record.validate_and_insert_record()


    # PART 2
    # If/When user selects N in part 1, they end up here.
    if std_info == "n":

        choice = ""
        while choice != "x":

            print("\n1. Would you like to see the list of all registered students:")
            print("2. Would you like to see the class list of a specific subject: ")
            print("3. Would you like to see who your oldest student is: ")
            print("4. Would you like to see who your youngest student is: ")

            choice = input("Enter the number for selected task or 'X' to skip this: ")
            choice = choice.lower()

            if choice == '1':
                print("\nThe registered students are:")

                student_record_instance = StudentRecordClass()
                student_record_instance.display_all_students()

            elif choice == '2':
                subject = input("\nEnter the name of the subject: (java, python, c, ruby, php): ")
                subject = subject.lower()
                print(f"\nThe student registered in {subject} are:")

                student_record_instance = StudentRecordClass()
                student_record_instance.display_subject_class_list(subject)

            elif choice == '3':

                student_record_instance = StudentRecordClass()
                student_record_instance.display_oldest()

            elif choice == '4':

                student_record_instance = StudentRecordClass()
                student_record_instance.display_youngest()

        while choice == 'x':

            answer = input("\nDo you want to encode the file ? ( y/n )")
            answer = answer.lower()

            if answer == 'y':
                file_name = "StudentRecords.txt"
                shift = 5
              # shift = int(input("Add the number you want to shift with: "))
                encode = EncodeDecodeClass()
                encode.EncodeStudentList(file_name, shift)
                print("\nFile Encoded.")
                break
            if answer == 'n':
                break
            else:
                print("Only Y or N input is allowed.")

        while choice == 'x':

            answer = input("\nWould you like to decode the encoded file ? ( y/n )")
            answer = answer.lower()

            if answer == 'y':
                file_name = "EncodedStudentRecords.txt"
                shift = 5
                # shift = int(input("Add the number we should shift to decode: "))
                decode = EncodeDecodeClass()
                decode.DecodeStudentList(file_name, shift)
                print("\nFile decoded.")
                print("\nThe assessment is over. Have a nice day")
                break

            elif answer == 'n':
                print("\nThe assessment is over. Have a nice day")
                break

            else:
                print("Only Y or N input is allowed.")

        else:
            print("Something is buggy")
    else:
        print("Oops something is buggy. Invalid input, please enter only Y or N.")
        main()

# calling the main method
main()