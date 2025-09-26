# OS File Manager
#    - Ask user for a directory path.
#    - Automatically:
#         - Create a folder "backup" inside it if not exists.
#         - Copy all .txt files into "backup".
#         - Print summary: how many files copied.
#    - If directory invalid, retry until correct.

import os
import shutil


def os_file_manager():
    while True:
        dir_path = input("Enter a Directory Path: ").strip()

        # Check if directory is valid
        if not os.path.isdir(dir_path):
            print("❌ Invalid directory. Please Try Again.\n")
            continue

        # Create Backup Directory if Not Exists
        backup_path = os.path.join(dir_path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        # Backup All *.txt Files
        copied_count = 0
        for file in os.listdir(dir_path):
            if file.endswith(".txt"):
                src = os.path.join(dir_path, file)
                dest = os.path.join(backup_path, file)
                shutil.copy2(src, dest)  # copy2 preserves metadata
                copied_count += 1

        print(f"\n{copied_count} .txt File(s) Copied Into `{backup_path}`\n")
        break


if __name__ == "__main__":
    os_file_manager()
