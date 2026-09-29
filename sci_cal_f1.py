import math

def cal():

    while True:
        print("\n" + "="*50)
        print("        SCIENTIFIC AND UTILITY CALCULATOR         ")
        print("=" *50)
        print("  [1] ADDITION (+)   ")
        print(" [2] SUBTRACTION (-)   ")
        print("  [3] MULTIPLICATION (*)   ")
        print(" [4] DIVISION (/)   ")
        print("  [5] LOGARITHM (log base b of x)   ")
        print(" [6] TRIGONOMETRY (sin , cos ,tan )   ")
        print("  [7] COMPOUND INTEREST CALCULATOR    ")
        print("  [8] BODY MASS INDEX AND CAT (BMI)   ")
        print(" [9] UNIT CONVERTER  (uniconv)   ")
        print("  [10] POWER AND SQUARE ROOT ")
        print(" [11] Numeric System Converter")
        print("  [12] Password Generator")
        print(" [0] back to main menu   ")
        print("="*50)

        choice  = input("Enter your choice (0-10:>>>)").strip()

        #0 return to main menu
        if choice  == "0":
            print('\nreturning bro.....')
            break
        #1 add
        if choice=='1':
            a = float(input("enter first no. >>> "))
            b = float(input("enter second no.>>> "))
            c = (a+b)
            print("Answer IS   >>>" , c )

        #sub
        elif choice=='2':
            a = float(input("enter first no.>>> "))
            b = float(input("enter second no.  >>> "))
            c = (a-b)
            print("Answer IS >>> " , c)

        #mul 
        elif choice=='3':
            a = float(input("enter first no.>> "))
            b = float(input("enter second no.>>> "))
            c = (a*b)
            print("Answer IS >>>",c)

        #div
        elif choice=='4':
            a = float(input("enter first no.>>>"))
            b = float(input("enter second no. >>"))
            if b==0:
                c =  ",,,infinity,,,"
            else:
                c = (a/b)
            print("Answer IS >>>" , c )

        #log
        elif choice=="5":
            x = float(input("enter the value of x (x>0)>>>"))
            if x <= 0:
                print("MATH ERROR : I TOLD U TO CHOOSE X>0")
            else:
                base_inp = input("enter the b [nothing means default 10 ] >>>").strip()
                if base_inp=="":
                    base = 10.0
                else:
                    base = float(base_inp)

                if base <= 0 or base ==1:
                    print("MATH ERROR BRO... base must be +ve and not equal to 1 , i thought u know that !")
                else:
                    c = math.log(x, base)
                    print("ANSWER IS >>> ",c)

        #6 tri
        elif choice == "6":
            print("choose: [1] sin , [2] cos , [3] tan >>> ")
            t_choice = input("select >>> ").strip()
            deg = float(input("enter angles in degrees >>> "))
            rad = math.radians(deg)
            if t_choice == "1":
                c = math.sin(rad)
                print("Answer IS >>> ", c)
            elif t_choice == "2":
                c = math.cos(rad)
                print("Answer IS >>> ", c)
            elif t_choice == "3":
                if deg % 180 == 90:
                    print("Answer IS >>> UNDEFINED")
                else:
                    c = math.tan(rad)
                    print("Answer IS >>> ", c)
            else:
                print("Invalid trigonometry choice")

        #ci+-
        elif choice==7:
            p = float(input("enter principal amount (p)>>> "))
            r = float(input("enter annual rate in % (R) >>>"))
            t = float(input("enter the time period in yrs (t)>>>"))
            n = float(input("enter the compounding frequency (n)>>>"))

            total_amount = p*((1+(r/(100*n)))**(n*t))
            c = total_amount - p 
            print("Total Accrued Is >>>",total_amount)
            print("Compound Interest Is >>> ", c)

        # [8] BMI and Cat 
        elif choice == "8":
            w = float(input("enter weight >>>"))
            h_cm = float(input("enter height in cm >>>"))
            h_m = h_cm / 100
            bmi = w/(h_m**2)

            if bmi < 18.5:
                cat = 'Underweight , eat bro eat!'
            elif bmi < 25.0:
                cat = "normal , thats good!"
            elif bmi < 30.0:
                cat = "Overweight , do exercise bro.."
            else:
                cat = "obese"
            print("BMI is >>.",round(bmi, 2))
            print("category is >>>",cat)

        #[9] unit converter
        elif choice =="9":
            print("[1] C to F  [2] F to C  [3] KM to Miles  [4] KG to LBS")
            u_choice = input("select >>> ").strip()

            if u_choice == "1":
                val = float(input("enter temp in °C >>> "))
                c = (val * 9/5) + 32
                print("Answer IS >>> ", c, "°F")
            elif u_choice == "2":
                val = float(input("enter temp in °F >>> "))
                c = (val - 32) * 5/9
                print("Answer IS >>> ", c, "°C")
            elif u_choice == "3":
                val = float(input("enter km >>> "))
                c = val * 0.621371
                print("Answer IS >>> ", c, "miles")
            elif u_choice == "4":
                val = float(input("enter kg >>> "))
                c = val * 2.20462
                print("Answer IS >>> ", c, "lbs")
            else:
                print("arre bhai option to thik se chua a kar 🙄 ")

        #[10] power and root
        elif choice == "10":
            print("[1] power and [2] square root ")
            p_choose = input("select >>>>").strip()
            if p_choose =="1":
                x = float(input("enter the base x >>>"))
                y = float(input("enter the exponent y >>>"))
                c = x**y
                print("Answer IS >>> ", c)
            elif p_choose == "2":
                x = float(input("enter number x >>> "))
                if x < 0:
                    print("Math Error: Cannot take square root of negative number")
                else:
                    c = math.sqrt(x)
                    print("Answer IS >>> ", c)
            else:
                                print("invalid option ")

        # [11]number system converter(custom logic)
        elif choice  == "11":
            print("\n"+ "-" * 35)
            print("   NUMBER SYSTEM CONVERTER")
            print("-" * 35)
            print(" [1]  BINARY TO DECIMAL")
            print(" [2]DECIMAL TO BINARY")
            print(" [3] DECIMAL TO OCTAL")
            print(" [4] DECIMAL TO HEXADECIMAL")
            print(" [5]BINARY TO OCTAL")
            print(" [6]BINARY TO HEXADECIMAL")
            print(" [7] Back ")
            print("-" * 35)

            sub_choice = input("Select conversion (1-6) >>> ").strip()

            # 1. Binary to Decimal
            if sub_choice == "1":
                b_str = input("Enter binary number >>> ").strip()
                # Validation
                if not all(ch in "01" for ch in b_str):
                    print("Error: Input must contain only 0s and 1s.")
                else:
                    b_num = int(b_str)
                    decimal = 0
                    power = 0
                    while b_num > 0:
                        digit = b_num % 10
                        decimal += digit * (2 ** power)
                        b_num = b_num // 10
                        power += 1
                    print("your Answer IS >>>", decimal)

            # 2. Decimal to Binary
            elif sub_choice == "2":
                n = int(input("Enter decimal number >>> "))
                if n == 0:
                    print("Answer IS >>> 0")
                else:
                    binary_str = ""
                    temp = n
                    while temp > 0:
                        rem = temp % 2
                        binary_str = str(rem) + binary_str
                        temp = temp // 2
                    print("your Answer IS >>>", binary_str)

            #3.Decimal to Octal
            elif sub_choice == "3":
                n = int(input("Enter decimal number >>> "))
                if n == 0:
                    print("Answer IS >>> 0")
                else:
                    octal_str = ""
                    temp = n
                    while temp > 0:
                        rem = temp % 8
                        octal_str = str(rem) + octal_str
                        temp = temp // 8
                    print(" your Answer IS >>>>", octal_str)

            #4.Decimal to Hexadecimal
            elif sub_choice == "4":
                n = int(input("enter decimal number >>> "))
                if n == 0:
                    print("Answer IS >>> 0")
                else:
                    hex_digits = "0123456789ABCDEF"
                    hex_str = ""
                    temp = n
                    while temp > 0:
                        rem =temp % 16
                        hex_str= hex_digits[rem]+hex_str
                        temp =temp//16
                    print("Answer IS >>>", hex_str)

            #5.Binary to Octal (Binary -> Decimal -> Octal)
            elif sub_choice == "5":
                b_str = input("Enter binary number >>> ").strip()
                if not all(ch in "01" for ch in b_str):
                    print("Error: Input must contain only 0s and 1s.")
                else:
                    # Step 1: Binary to Decimal using % and //
                    b_num = int(b_str)
                    decimal = 0
                    power = 0
                    while b_num > 0:
                        digit = b_num % 10
                        decimal += digit * (2 ** power)
                        b_num = b_num // 10
                        power += 1

                    # Step 2: Decimal to Octal using % and //
                    if decimal == 0:
                        print("Answer IS >>> 0")
                    else:
                        octal_str = ""
                        temp = decimal
                        while temp > 0:
                            rem = temp % 8
                            octal_str = str(rem) + octal_str
                            temp = temp // 8
                        print("Answer IS >>>", octal_str)

            # 6. Binary to Hexadecimal (Binary -> Decimal -> Hex)
            elif sub_choice == "6":
                b_str = input("Enter binary number >>> ").strip()
                if not all(ch in "01" for ch in b_str):
                    print("Error: Input must contain only 0s and 1s.")
                else:
                    # Step 1: Binary to Decimal using % and //
                    b_num = int(b_str)
                    decimal = 0
                    power = 0
                    while b_num > 0:
                        digit = b_num % 10
                        decimal += digit * (2 ** power)
                        b_num = b_num // 10
                        power += 1

                    # Step 2: Decimal to Hex using % and //
                    if decimal == 0:
                        print("Answer IS >>> 0")
                    else:
                        hex_digits = "0123456789ABCDEF"
                        hex_str = ""
                        temp = decimal
                        while temp > 0:
                            rem = temp % 16
                            hex_str = hex_digits[rem] + hex_str
                            temp = temp // 16
                        print("Answer IS >>>", hex_str)
            elif sub_choice == "0":
                break
            else:
                print("Invalid selection! Please choose between 1 and 6.")
        # [12] Password Generator (Using Sets, No Libraries)
        elif choice == "12":
            print("\n" + "-" * 35)
            print("  PASSWORD GENERATOR")
            print("-" * 35)
            print(" [1]8 Character Password")
            print(" [2]12 Character Password")
            print(" [3]4 Digit PIN")
            print(" [0]Exit")
            print("-" * 35)

            sub_choice = input("ENTER THE OPTIONS (0-3) >>> ").strip()

            # Character pools stored as sets
            char_pool = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','-','_','+','=','?'}
            digit_pool = {'0','1','2','3','4','5','6','7','8','9'}

            if sub_choice == "0":
                print("Returning to calculator menu...")
                break

            elif sub_choice == "1":
                pwd = ""
                pool_copy =set(char_pool)  # Work on a copy so the base set stays intact
                for _ in range(8):
                    char =pool_copy.pop()   # Pops an arbitrary character from the set
                    pwd +=char
                print("generated 8-char password >>>>", pwd)

            elif sub_choice== "2":
                pwd = ""
                pool_copy =set(char_pool)
                for _ in range(12):
                    char =pool_copy.pop()
                    pwd +=char
                print("Generated 12-Char Password >>>", pwd)

            elif sub_choice== "3":
                pin = ""
                pool_copy = set(digit_pool)
                for _ in range(4):
                    digit = pool_copy.pop()
                    pin += digit
                print("Generated 4-Digit PIN >>>", pin)

            else:
                print("Invalid selection! Please enter 0, 1, 2, or 3.")
        else:
            print("Invalid choice! Please select 0 to 10.")     

if __name__ == "__main__":
   cal()
