# Job Application Tracker
Project #1 for ENGM 4620 – Python for Engineers

# Documents
[View Report PDF](./JobApplicationTrackerReport.pdf) from Project 1

[Link to Video Presentation](https://drive.google.com/drive/folders/1rqkwDqe_OY9tXtGrhJx5wNVuYGCgJzu2?usp=sharing) from Project 1

Note: Files for Project 3 were uploaded to Brightspace.

# Description
In today's competitive job market, individuals often find themselves juggling numerous job applications simultaneously, leading to potential confusion, missed deadlines, and disorganization. Without a centralized system to manage applications, candidates may struggle to keep track of important details such as application status, interview dates, contact information, and additional details. This lack of organization can hinder chances of securing employment opportunities efficiently. Therefore, there is a practical need for a user-friendly job application tracker tool that can streamline the application process, increase organization, and enhance the prospects of job seekers by providing them with a structured platform to manage their job applications effectively.

# Key Features From Project 1
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

# Key Features From Project 3
1)	Global Search:
Previously, the user was only able to search by company. With this iteration of the project, the user can enter a value into the Global Search and it will display all records containing the searched value. This is helpful to the user to search any and all of the fields.
2)	Status Update Log:
Every time an application’s status changes (i.e., from Applied to Interview Scheduled), the update will be logged. The user is able to view the log in the console, or they can open the application_updates.log text file. It will show all of the original and updated statuses of the user’s applications. This is useful to the user to track their progress for each application and it gives them an overview of their application status changes.
3)	Added table borders to enhance readability of data
Previously, the console results did not have any borders. After doing the Peer Review for Project 1, I saw that the other student that I reviewed had borders. Borders were added to the Status Update Log to improve user readability of the data.
4)	Numerical Analytics
The main numerical analytics have been relocated so that on start up of the program, they are displayed. The analytics that are displayed are the Application Status (interview scheduled, applied, rejected, or withdrawn) vs Count. For this project, I decided to focus more on the visual graphs than numerical since it is easier for the user to view.
5)	Visual Analytics:
a.	Histogram of Application Status:
This plot shows the user how many applications are in which status (interview scheduled, applied, rejected, or withdrawn).
 
b.	Pie Chart of Application Status:
This plot shows the percentages of the application statuses in the form of a pie chart.
 
c.	Bar chart of Company vs Number of Applications:
This bar chart gives the user an easy visual to view how many applications they submitted per company.
 
d.	Bar Chart of Number of Application vs Position:
This bar chart allows the user to easily view their trending positions that they applied to. An example of how the user may re-evaluate their career goals in the case that they realize they are not applying enough to their desired position. 

# Prerequisites
Python 3.x must be installed.
Download or clone the package repository.
There are no other requirements so there is no requirements.txt file.

# Running the application
Run JobTracker.py
Select option 1 from the main menu to add an application.
A CSV file will be created in the same path as the Job Application Tracker Python Source File.
Do not open the CSV file while attempting to add, update or delete an application.
