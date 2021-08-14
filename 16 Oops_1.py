
class student:
    school_name = "AMAR NATH VIDYA ASHRAM"
    no_of_students = 0
    def __init__(self,fname, dob, roll_no, section):
        self.fname =fname
        self.dob = dob
        self.roll_no = roll_no
        self.section = section
        student.no_of_students +=1

    def studentInfo(self):
        return print(f"\t\t\t{student.school_name}\nThe Name of the Student is: {self.fname}\nD.O.B is: {self.dob}\nRoll number is: {self.roll_no}\nSection is: {self.section}\nTHANK YOU!")

vikash = student("vikash sharma", "28/09/2002", 44, 'B')
ankush = student("Ankush Sharma", "12/07/2004", 28, "C")

print("\t\t\tWELCOME TO STUDENT INFORMATION PORTAL")
print(f"Total students:{student.no_of_students}")

name = input("Enter the student name: ")
if name == "vikash":
    vikash.studentInfo()
elif name=="ankush":
    ankush.studentInfo()
else:
    print(f"Sorry!\nThe student of name {name} is not in our school\nPlease enter the correct name\nThank you")