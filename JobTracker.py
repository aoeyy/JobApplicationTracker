import csv
from datetime import datetime

class JobApplicationTracker:
    def __init__(self):
        self.applications = {}

    def add_application(self, company, position, contact_info, job_url, date_applied, additional_details):
        # check if company name and position are entered by the user
        if not company:
            print("\nERROR: Please enter the company name.")
            return
        if not position:
            print("\nERROR: Please enter the position.")
            return

        print("\nSelect Application Status:")
        print("1. Applied")
        print("2. Interview Scheduled")
        print("3. Offer Extended")
        print("4. Rejected")
        print("5. Withdrawn")
        status_choice = input("Enter the number for the application status: ")
        status_options = {
            '1': 'Applied', 
            '2': 'Interview Scheduled', 
            '3': 'Offer Extended', 
            '4': 'Rejected', 
            '5': 'Withdrawn'
            }
        status = status_options.get(status_choice, '')

        interview_date = ''
        # if "Interview Scheduled" is selected, then we want the user to enter the Interview Date
        if status_choice == '2': 
            interview_date = input("Interview Date (YYYY-MM-DD): ")
            while not self.validate_interview_date(interview_date):
                interview_date = input("Interview Date (YYYY-MM-DD): ")

        # make company and position case-insensitive
        company_lower = company.lower()
        self.applications.setdefault(company_lower, []).append({
            'Company': company,
            'Position': position.lower(),
            'Date Applied (YYYY-MM-DD)': date_applied,
            'Contact Information': contact_info,
            'Status': status,
            'Interview Date (YYYY-MM-DD)': interview_date,
            'Job Posting URL': job_url,
            'Additional Details': additional_details
        })

        print("\nApplication added successfully!")
        self.save_to_csv()

    # display a total count of the search result by company
    def view_application(self, company):
        company_lower = company.lower()
        if company_lower in self.applications:
            applications = self.applications[company_lower]
            print(f"\nTotal Results: {len(applications)}")
            for index, application in enumerate(applications, 1):
                print(f"\nApplication {index} Details for {application['Company']}:")
                for key, value in application.items():
                    if key == 'Interview Date (YYYY-MM-DD)' and application.get('Status') != 'Interview Scheduled':
                        continue  # skip displaying the "Interview Date" if the status is not "Interview Scheduled"
                    print(f"{key}: {value}")
        else:
            print(f"\nNo applications found for {company}.")

    def update_application_status(self, company, position):
        company_lower = company.lower()
        position_lower = position.lower()
        # output application status options for the user to select from
        if company_lower in self.applications:
            print("\nSelect New Application Status:")
            print("1. Applied")
            print("2. Interview Scheduled")
            print("3. Offer Extended")
            print("4. Rejected")
            print("5. Withdrawn")
            status_choice = input("Enter the number for the new application status: ")
            status_options = {
                '1': 'Applied', 
                '2': 'Interview Scheduled', 
                '3': 'Offer Extended', 
                '4': 'Rejected', 
                '5': 'Withdrawn'
                }
            new_status = status_options.get(status_choice, '')

            interview_date = ''
            # If "Interview Scheduled" is selected, we want the interview date
            if status_choice == '2':  
                interview_date = input("Interview Date (YYYY-MM-DD): ")
                while not self.validate_date(interview_date):
                    interview_date = input(" Interview Date (YYYY-MM-DD): ")

            application_found = False
            for application in self.applications[company_lower]:
                if application["Position"] == position_lower:
                    application['Status'] = new_status
                    if interview_date:
                        application['Interview Date (YYYY-MM-DD)'] = interview_date
                    application_found = True
                    break
            if application_found:
                print(f"\nApplication status updated successfully for {position} at {company}.")
                self.save_to_csv()
            else:
                print(f"\nNo application found for {position} at {company}.")
        else:
            print(f"\nNo applications found for {company}.")

    # delete application based on the matching company and position
    def delete_application(self, company, position):
        company_lower = company.lower()
        if company_lower in self.applications:
            application_index = next((index for (index, d) in enumerate(self.applications[company_lower]) if d["Position"] == position), None)
            if application_index is not None:
                del self.applications[company_lower][application_index]
                print(f"\nApplication for {position} at {company} deleted successfully.")
                if not self.applications[company_lower]:
                    del self.applications[company_lower]
                self.save_to_csv()
            else:
                print(f"\nNo application found for {position} at {company}.")
        else:
            print(f"\nNo applications found for {company}.")

    # list all applications that match by the searched company
    def list_applications(self):
        if not self.applications:
            print("\nNo applications to display.")
        else:
            print("\nList of Companies Applied To:")
            for company in self.applications:
                print(f"- {company.title()}")

    def show_analytics(self):
        if not self.applications:
            print("\nNo applications to display.")
            return

        total_applications = sum(len(apps) for apps in self.applications.values())
        status_counts = {'Applied': 0, 'Interview Scheduled': 0, 'Offer Extended': 0, 'Rejected': 0, 'Withdrawn': 0}

        for company_applications in self.applications.values():
            for application in company_applications:
                status = application['Status']
                if status in status_counts:
                    status_counts[status] += 1

        print(f"\nTotal Job Applications: {total_applications}")
        print("Status Count:")
        for status, count in status_counts.items():
            print(f"- {status}: {count}")

        interview_scheduled_count = status_counts['Interview Scheduled']
        offer_extended_count = status_counts['Offer Extended']

        # calculate the percentages of application to interview rate and application to offer
        if total_applications > 0:
            interview_rate = (interview_scheduled_count / total_applications) * 100
            offer_rate = (offer_extended_count / total_applications) * 100
            print(f"Application to Interview Rate: {interview_rate:.2f}%")
            print(f"Application to Offer Rate: {offer_rate:.2f}%")
        else:
            print("Application to Interview Rate: N/A")
            print("Application to Offer Rate: N/A")

    # check if the inputted interview date is in YYYY-MM-DD format and not in the past
    def validate_interview_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            current_date = datetime.now()
            if date_obj.date() < current_date.date():
                print("The date cannot be in the past.")
                return False
            return True
        except ValueError:
            print("Invalid date or format (expected YYYY-MM-DD).")
            return False
        
    # check if the inputted applied date is in YYYY-MM-DD format and not in the future
    def validate_applied_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            current_date = datetime.now()
            if date_obj.date() > current_date.date():
                print("The date cannot be in the future.")
                return False
            return True
        except ValueError:
            print("Invalid date or format (expected YYYY-MM-DD).")
            return False

    # write the application input to the csv file
    def save_to_csv(self):
        with open('job_applications.csv', 'w', newline='') as csvfile:
            fieldnames = ['Company', 'Position', 'Date Applied (YYYY-MM-DD)', 'Contact Information', 'Status', 'Interview Date (YYYY-MM-DD)', 'Job Posting URL', 'Additional Details']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for applications_list in self.applications.values():
                for application in applications_list:
                    writer.writerow(application)

    # load the csv file or create one if it doesn't already exist
    def load_from_csv(self):
        self.applications.clear()
        try:
            with open('job_applications.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    company_lower = row['Company'].lower()
                    self.applications.setdefault(company_lower, []).append(row)
        except FileNotFoundError:
            print("\nNo csv file for existing job applications found. A new csv file will be created.")
            print("The csv file may be found in the same location as the Job Application Tracker Python Source File")

def main():
    tracker = JobApplicationTracker()
    tracker.load_from_csv()

    while True:
        print("\nNOTE: the csv file must be closed while adding, updating or deleting a record.")
        print("\nJob Application Tracker Menu:")
        print("1. Add Application")
        print("2. Search Applications by Company")
        print("3. Update Application Status")
        print("4. List of Companies Applied To")
        print("5. Delete an Application")
        print("6. Analytics")
        print("7. Exit")

        choice = input("Enter your desired option (1-7): ")

        # 1 = Add Application
        if choice == '1':
            # remove any trailing spaces and check prompt the user to enter a company if they didn't
            while True:
                company = input("\nCompany Name: ").strip()
                if company:
                    break
                print("ERROR: Company name cannot be blank. Please enter the company name.")

            while True:
                # remove any trailing spaces and check prompt the user to enter a position if they didn't
                position = input("Position: ").strip()
                if position:
                    break
                print("ERROR: Position cannot be blank. Please enter the position.")

            date_applied = input("Date Applied (YYYY-MM-DD): ")
            while not tracker.validate_applied_date(date_applied):
                date_applied = input("Date Applied (YYYY-MM-DD): ")

            contact_info = input("Contact Information: ")
            job_url = input("Job Posting URL: ")
            additional_details = input("Additional Details: ")
            tracker.add_application(company, position, contact_info, job_url, date_applied, additional_details)

        # 2 = Search Applications by company
        elif choice == '2':
            company = input("\nCompany Name: ")
            tracker.view_application(company)

        # 3 = Update Application Status based on the copmany and position
        elif choice == '3':
            company = input("\nCompany Name: ")
            position = input("Position for the application you want to update: ")
            tracker.update_application_status(company, position)

        # 4 = List of Companies Applied To
        elif choice == '4':
            tracker.list_applications()

        # 5 = Delete an Application based on the company and position
        elif choice == '5':
            company = input("\nCompany Name: ")
            position = input("Position for the application you want to delete: ")
            tracker.delete_application(company, position)

        # 6 = Analytics
        elif choice == '6':
            tracker.show_analytics() 

        # 7 = Exit the program
        elif choice == '7':
            print("Exiting Job Application Tracker...")
            break
        
        else:
            print("\nInvalid input. Please refer to the menu and enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
