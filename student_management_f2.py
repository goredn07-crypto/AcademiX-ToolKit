def SM():
    while True:
        print("\n" + "=" * 50)
        print("         STUDENT MANAGEMENT SYSTEM          ")
        print("=" * 50)
        print("    [1] ATTENDANCE       ")
        print("    [2] GRADES AND MARKS         ")
        print("    [0] Return to The main Menu     ")
        print("=" * 50)

        choice = input("Enter The Choice Please...>>>> ").strip()

        # 0 Return to Main Menu
        if choice == "0":
            print("Returning to main menu...")
            break

        # 1 Attendance
        elif choice == "1":
            mat_att = int(input("enter attended classes of Maths >>>  "))
            math_tot = int(input("enter total classes of Maths >>>>"))

            phy_att = int(input("enter attended classes of Physics >>>> "))
            phy_tot = int(input("enter total classes of Physics >>>>"))

            chem_att = int(input("enter attended classes of Chemistry >>>> "))
            chem_tot = int(input("enter total classes of Chemistry>>> "))

            cse_att = int(input("enter attended classes of CSE >>>> "))
            cse_tot = int(input("enter total classes of CSE >>>"))

            while True:
                print("\n" + "=" * 40)
                print("    STUDENT ATTENDANCE SYSTEM")
                print("=" * 40)
                print(" [1] View Attendance")
                print(" [2] Mark Attendance (Present/Absent)")
                print(" [0] Exit to Student Menu")
                print("=" * 40)

                att_choice = input("enter choice (0-2) >>> ").strip()

                if att_choice == "0":
                    print("returning to student management...")
                    break

                # 1. Calculation of %
                elif att_choice == "1":
                    print("\n---- current attendance ----")

                    # Maths
                    mat_p = (mat_att / math_tot) * 100 if math_tot > 0 else 0
                    if mat_p >= 75:
                        mat_status = "SAFE HAI BHAI"
                    else:
                        mat_status = "Bhai Classes Attend karte jaa , 75 se kam hai attendance"
                    print("Maths:     ", mat_att, "/", math_tot, "(", round(mat_p, 1), "%) ->", mat_status)

                    # Physics
                    phy_pct = (phy_att / phy_tot) * 100 if phy_tot > 0 else 0
                    if phy_pct >= 75:
                        phy_status = "SAFE"
                    else:
                        phy_status = "SHORTAGE (Below 75%)"
                    print("Physics:   ", phy_att, "/", phy_tot, "(", round(phy_pct, 1), "%) ->", phy_status)

                    # Chemistry
                    chem_pct = (chem_att / chem_tot) * 100 if chem_tot > 0 else 0
                    if chem_pct >= 75:
                        chem_status = "SAFE"
                    else:
                        chem_status = "SHORTAGE (Below 75%)"
                    print("Chemistry: ", chem_att, "/", chem_tot, "(", round(chem_pct, 1), "%) ->", chem_status)

                    # CSE
                    cse_p = (cse_att / cse_tot) * 100 if cse_tot > 0 else 0
                    if cse_p >= 75:
                        cse_status = "safe hai bhai"
                    else:
                        cse_status = "Class attend karte jaa , cse ke , kam hai attendance bahut"
                    print("CSE:       ", cse_att, "/", cse_tot, "(", round(cse_p, 1), "%) ->", cse_status)

                #2.Mark Attendance
                elif att_choice == "2":
                    print("\nSelect Subject:")
                    print(" [1] Maths")
                    print(" [2] Physics")
                    print(" [3] Chemistry")
                    print(" [4] CSE")
                    sub = input("Choose (1-4): ").strip()

                    if sub not in ["1", "2", "3", "4"]:
                        print("Invalid subject choice!")
                    else:
                        status = input("Present (P) or Absent (A)?: ").strip().upper()

                        if status != "P" and status != "A":
                            print("Invalid! Type only P or A.")
                        else:
                            # Update Maths
                            if sub == "1":
                                math_tot += 1
                                if status == "P":
                                    mat_att += 1
                                print("Updated Maths successfully!")

                            # Update Physics
                            elif sub == "2":
                                phy_tot += 1
                                if status == "P":
                                    phy_att += 1
                                print("Updated Physics successfully!")

                            # Update Chemistry
                            elif sub == "3":
                                chem_tot += 1
                                if status == "P":
                                    chem_att += 1
                                print("Updated Chemistry successfully!")

                            # Update CSE
                            elif sub == "4":
                                cse_tot += 1
                                if status == "P":
                                    cse_att += 1
                                print("Updated CSE successfully!")

                else:
                    print("Invalid choice, please select 0, 1, or 2.")

        #2 grades and marks (VIT relative grading system)
        elif choice == "2":
            print("\n" + "=" * 55)
            print("     VIT EXAM & RELATIVE GRADE EVALUATOR      ")
            print("=" * 55)

            subjects = ["Maths", "Physics", "Chemistry", "CSE"]
            course_credits = {
                "Maths": 4,
                "Physics": 4,
                "Chemistry": 3,
                "CSE": 3
            }

            grade_points_map = {
                "S": 10,
                "A": 9,
                "B": 8,
                "C": 7,
                "D": 6,
                "F": 0
            }

            total_points = 0
            total_credits = 0

            for sub in subjects:
                print("\n" + "-" * 45)
                print(f"  SUBJECT: {sub} (Credits: {course_credits[sub]})")
                print("-" * 45)

                # 1. Input Exam Marks
                cat1 = float(input("enter CAT 1 Marks (out of 50) >>> "))
                cat2 = float(input("enter CAT 2 Marks (out of 50) >>> "))
                internals = float(input("enter DA / Quiz Total (out of 30) >>> "))
                fat = float(input("Enter FAT Marks (out of 100) >>> "))

                # 2. Weightage Scaling:
                # CAT 1: (marks / 50) * 15
                # CAT 2: (marks / 50) * 15
                # Internals: out of 30
                # FAT: (marks / 100) * 40
                cat1_wt = (cat1 / 50) * 15
                cat2_wt = (cat2 / 50) * 15
                fat_wt = (fat / 100) * 40
                my_total = round(cat1_wt + cat2_wt + internals + fat_wt, 2)

                print(f"\n[Marks Breakdown for {sub}]")
                print(f"CAT 1 (15%): {round(cat1_wt, 2)} | CAT 2 (15%): {round(cat2_wt, 2)} | DA/Quiz (30%): {internals} | FAT (40%): {round(fat_wt, 2)}")
                print(f"Final Total (out of 100): {my_total}")

                # 3. Class Average Input
                avg_marks = float(input(f"Enter Class Average Total for {sub} (out of 100) >>> "))

                # 4. VIT Relative Grading Logic
                if my_total >= (avg_marks + 10):
                    grade = "S"
                elif my_total >= (avg_marks + 5):
                    grade = "A"
                elif my_total >= avg_marks:
                    grade = "B"
                elif my_total >= (avg_marks - 5):
                    grade = "C"
                elif my_total >= (avg_marks - 10):
                    grade = "D"
                else:
                    grade = "F"

                gp = grade_points_map[grade]
                credits = course_credits[sub]
                total_points += (gp * credits)
                total_credits += credits

                print(f"-> Result for {sub}: Grade [{grade}] | Grade Points: {gp}")

            # 5. Final SGPA Calculation
            if total_credits > 0:
                sgpa = round(total_points / total_credits, 2)
                print("\n" + "=" * 55)
                print("                 SEMESTER TRANSCRIPT                 ")
                print("=" * 55)
                print(f"Total Credits Earned : {total_credits}")
                print(f"Calculated SGPA      : {sgpa}")

                if sgpa >= 9.0:
                    print("Remark               : YOU REALLY NAILED IT BRO...!")
                elif sgpa >= 8.0:
                    print("Remark               : ITS VERRY GOOD SCORE BRP..")
                elif sgpa >= 7.0:
                    print("Remark               : ITS DECENT!")
                else:
                    print("Remark               : STUDY KAR BHAI , KAM HAI CGPA TERA ...")
                print("=" * 55)

        else:
            print("invalid option! please select 0,1,or2.")
            
if __name__ == "__main__":
    SM()
