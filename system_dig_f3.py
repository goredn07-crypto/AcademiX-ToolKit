import os
import platform
import math

def sys_diag():
    while True:
        print("\n" + "=" * 52)
        print("          SYSTEM & HARDWARE DIAGNOSTICS")
        print("=" * 52)
        print("  [1] Machine & OS Specifications")
        print("  [2] Storage & Disk Usage")
        print("  [3] Current Directory & Environment Info")
        print("  [0] Back to Main Menu")
        print("=" * 52)

        choice = input("Select diagnostic option (0-3) >>> ").strip()

        # 0 Back
        if choice == "0":
            print("Exiting Diagnostics...")
            break

        # 1 OS Specs
        elif choice == "1":
            print("\n--- OPERATING SYSTEM & MACHINE INFO ---")
            print("Operating System :", platform.system())
            print("OS Release       :", platform.release())
            print("OS Version       :", platform.version())
            print("Architecture     :", platform.architecture()[0])
            print("Machine Type     :", platform.machine())
            print("Processor        :", platform.processor())
            print("Python Runtime   :", platform.python_version())

        # 2 Storage
        elif choice == "2":
            print("\n--- STORAGE & DISK USAGE ---")
            # os.statvfs works on Linux/Mac/WSL; for Windows, standard fallback is root check
            try:
                # Target path (current active drive/directory)
                path = os.getcwd()
                stat = os.statvfs(path)
                
                # Math calculations: block size * blocks = total bytes
                total_bytes = stat.f_frsize * stat.f_blocks
                free_bytes = stat.f_frsize * stat.f_bavail
                used_bytes = total_bytes - free_bytes

                # Convert bytes to Gigabytes (1 GB = 1024^3 bytes)
                gb = math.pow(1024, 3)
                total_gb = round(total_bytes / gb, 2)
                free_gb = round(free_bytes / gb, 2)
                used_gb = round(used_bytes / gb, 2)
                pct_used = round((used_bytes / total_bytes) * 100, 1)

                print("Scanned Path :", path)
                print("Total Space  :", total_gb, "GB")
                print("Used Space   :", used_gb, "GB (", pct_used, "% )")
                print("Free Space   :", free_gb, "GB")

            except AttributeError:
                # Windows fallback using simple directory check
                print("Current Drive:", os.path.splitdrive(os.getcwd())[0])
                print("Working Path :", os.getcwd())

        # 3 Environment Info
        elif choice == "3":
            print("\n--- CURRENT ENVIRONMENT PATHS ---")
            print("Current Working Folder :", os.getcwd())
            print("System Logged-in User  :", os.getlogin() if hasattr(os, 'getlogin') else "Active User")
            print("Total Files in Folder  :", len(os.listdir(".")))

        else:
            print("Invalid choice! Enter 0, 1, 2, or 3.")


sys_diag()