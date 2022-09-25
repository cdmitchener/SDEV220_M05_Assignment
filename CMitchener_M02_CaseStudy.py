# Chelsea Mitchener
# Dean's List or Honor Roll Checker
# ---------------------------------
# Enter a student's last name, first name, and GPA as a float.
# If the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
# If the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
# When finished please enter "ZZZ" as the student's last name.
    
last_name = ""

while last_name != "ZZZ":
    last_name = input("Enter student's last name: ")

    if last_name != "ZZZ":
        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))
        
        if gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
            
            if gpa >= 3.5:
                print(f"{first_name} {last_name} has made the Dean's List.")
            
        else:
            print(f"{first_name} {last_name} did not make the Honor Roll.")
    else:
        quit()