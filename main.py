from student_management_f2 import SM
from sci_cal_f1 import cal
from system_dig_f3 import sys_diag
while True:
    print("\n" + "=" * 58)
    print("           STUDENT UTILITY & ENGINEERING TOOLKIT          ")
    print("=" * 58)
    print("  DEVELOPER : ATHARV GORE")
    print("  REG NO    : 26BCE10757")
    print("  PROJECT   : MULTI-PURPOSE  TOOLKIT ")
    print("-" * 58)
    print("  ABOUT:")
    print("  An all-in-one console application built to handle")
    print("  scientific math calculations, subject attendance,")
    print("  and academic tools in one unified interface.")
    print("=" * 58)
    print("  [1] Scientific & Utility Calculator")
    print("  [2] Student Management System (Attendance & Grades)")
    print("  [3] System Digonistic ")
    print("  [0] Exit Toolkit")
    print("=" * 58)

    choice = input("Enter your choice (0-3) >>> ").strip()

    # 0 Exit
    if choice == "0":
        print("\n" + "*" * 45)
        print("  Logging off: ATHARV GORE (26BCE10757)")
        print("  Thanks for using the toolkit. Goodbye!")
        print("*" * 45 + "\n")
        break

    # 1 Scientific Calculator
    elif choice == "1":
        print("\nOpening Calculator...")
        cal()  # Calls your calculator function
        input("\nPress Enter to return to main menu...")

    # 2 Student Management
    elif choice == "2":
        print("\nOpening Student Management System...")
        SM()   # Calls your student management function
        input("\nPress Enter to return to main menu...")

    # 3 Placeholder for next tool
    elif choice == "3":
        print("\nOpening System Dignostic System.......")
        sys_diag()
        input("\nPress Enter to return to main menu...")

    # Invalid input
    else:
        print("\nInvalid selection! Please enter 0, 1, 2, or 3.")
