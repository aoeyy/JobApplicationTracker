**Adding an application:** the user is able to add a new application in which the application details saves to a csv file. If the csv file does not currently exist, a csv file named job_applications.csv will be created in the same folder that houses the Job Application Tracker Python Source File
**Adding an application with the status as Interview scheduled:** the user will enter their application details and once the status is set to Interview Scheduled, the user will be prompted to input their interview date.
**Adding an application without the company name or position:** the program will output error messages indicating that the user must enter a company name and position if these fields are left empty.
**Updating the status of an application that exists:** the user can select from a list of status options (applied, interview scheduled, offer extended, rejected, and withdrawn). If the user selects Interview Scheduled, then the program will prompt them to enter the date of their interview. The application analytics will also be updated based on status updates.
**Updating the status of an application that does not exist:** if the user enters a company name and/or a position that does not exist, then an error message will be displayed indicating that there are no matching results to update.
**Deleting an application that exists:** the user will enter the company name and position of the application they want to delete.
**Deleting an application that does not exist:** if the user enters a company name and/or a position that does not exist, then an error message will be displayed indicating that there are no matching results to delete.
**Entering an applied date with a date in the future:** an error message will be displayed that the date cannot be in the future and the user will be prompted to enter a valid date.
**Entering an applied date that are not in the YYYY-MM-DD format:** an error message will be displayed indicating that the inputted date format is incorrect.
**Entering an interview date with a date in the past:** an error message will be displayed that the date cannot be in the past and the user will be prompted to enter a valid date.
**Entering an interview date that are not in the YYYY-MM-DD format:** an error message will be displayed indicating that the inputted date format is incorrect.
**Search for an application by company:** all applications found according to the inputted company will be displayed with a total count of the results. The company field is case-insensitive to reduce errors based on case.
**List all companies applied to:** the user can seamlessly view a list of all the companies they submitted applications to from the main menu.
**View application analytics:** the user can select to view application analytics from the main menu.
**Exit the program:** the user can exit the program from the main menu.
**Open the csv file while trying to add, update or delete a record:** currently, the program is not able to handle this use-case and will throw an error. To mitigate this error, the following message is displayed before the main menu, “NOTE: the csv file must be closed while adding, updating or deleting a record.”
