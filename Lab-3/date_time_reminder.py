# 3) Datetime Reminder Script
#    - Ask user for a date (YYYY-MM-DD).
#    - Calculate how many days remain until that date.
#    - If it is in the past, print "This date has already passed."
#    - Otherwise, save the reminder into "reminders.txt" in format:
#         "{date} -> {days_left} days left"
#    - Append multiple reminders without overwriting.


from datetime import datetime


def datetime_reminder():

    while True:
        # Ask user for a date
        date_str = input("Enter The Date in This Format (YYYY-MM-DD): ")

        try:
            if (date_str.lower() == "exit") or (date_str == ""):
                print("Exiting The Program ...")
                break

            # Parse The Input Date
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            today = datetime.today().date()

            # Calculate days left
            days = (target_date - today).days

            if days < 0:
                print("This Date Passed !!")
            elif days == 0:
                print("The Date is Today !!")
            else:
                print(f"{days} Days Left Until {target_date}")

                # Save The Reminder
                with open("reminders.txt", "a") as file:
                    file.write(f"{target_date} -> {days} Days Left\n")
                    file.close()

        except ValueError:
            print("Invalid Date Format. Please Use YYYY-MM-DD.")


if __name__ == "__main__":
    datetime_reminder()
