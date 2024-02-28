# Job Application Tracker
Project #1 for ENGM 4620 – Python for Engineers

# Documents
[View PDF](./JobApplicationTrackerReport.pdf)

# Description
In today's competitive job market, individuals often find themselves juggling numerous job applications simultaneously, leading to potential confusion, missed deadlines, and disorganization. Without a centralized system to manage applications, candidates may struggle to keep track of important details such as application status, interview dates, contact information, and additional details. This lack of organization can hinder chances of securing employment opportunities efficiently. Therefore, there is a practical need for a user-friendly job application tracker tool that can streamline the application process, increase organization, and enhance the prospects of job seekers by providing them with a structured platform to manage their job applications effectively.

# Key Features
•	Add a job application.
•	Update a job application.
•	Delete a job application.
•	Search job applications by company.
•	List all companies applied to.
•	Analytics: provides users with insights into their job application activity such as:
  o	Total amount of job applications
  o	Status Count: Breakdown of job applications by status categories within a specified time period. It gives users an overview of their overall job search activity.
    -	Applied: Number of applications that have been submitted but not yet progressed to the next stage.
    -	Interview Scheduled: Number of applications where interviews have been scheduled.
    -	Offer Extended: Number of applications where a job offer has been extended to the user.
    -	Rejected: Number of applications that have been rejected by the employer.
    -	Withdrawn: Number of applications that the user has withdrawn from consideration.
  o	Application to Interview Rate:
Percentage of applications that have progressed to the interview stage. This metric helps users evaluate the effectiveness of their job search strategies and identify areas for improvement.
  o	Application to Offer Rate:
Percentage of applications that have resulted in job offers.
•	Exit the program.
•	The data saves to a CSV file in which the user can open and edit on their own accord.


# Prerequisites
Python 3.x must be installed.
Download or clone the package repository.
There are no other requirements so there is no requirements.txt file.

# Running the application
Run JobTracker.py
Select option 1 from the main menu to add an application.
A CSV file will be created in the same path as the Job Application Tracker Python Source File.
Do not open the CSV file while attempting to add, update or delete an application.
