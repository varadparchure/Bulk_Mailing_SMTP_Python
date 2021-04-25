Bulk mailing using python

A script that can send multiple emails at once.
Input: An email draft, Email Id's(in CSV). 
Output: An receiving person can only see the sender's id and not the other Id's that were sent together.  


---------------------------------------------------------------------------------------------------------

Files and Contents:

README ---> This File.
Emaillist.csv ---> Contains all names and email id's.
Settings.py ---> Holds sender's email address and password.
BulkEmailScript.py ---> Main Python script with comments added for explanation.
Attachment.txt ---> sample attachment file.


---------------------------------------------------------------------------------------------------------

Steps To Follow:

1. Open and extract the zip file so that all files are in the same location/directory.
2. Open Emaillist.csv file and update name and email id's accordingly.
3. Open Settings.py and update your email and password from which you want to send the email.
4. Go to google account settings of that email id and make sure you have turned on Less secure app access.
   Link to do so: # https://myaccount.google.com/u/5/lesssecureapps?gar=1&pli=1&rapt=AEjHL4NxVArdeJDNDIfhiM1CaKIFWEz1N7O6Uer6bZPqyiIi9hYJ6VdVJvWF-h8v55ZaiVu-Q1VRcW_WnS4odXoS06knopYuvA    


Conditional:
If you are using Anaconda Spyder to run the BulkEmailScript.py script ---> No need to update anything
If you are using VS CODE to run the BulkEmailScript.py script ---> Put in the full address of CSV file and attachment file, eg: "C:\Users\Desktop\Emaillist.csv"


5. Run the script 
    1. Enter Subject
    2. Enter Message 
    3. Select if you want to attach an attachment (which needs to be edited in script, In place of --> filename="attachment.txt")
    4. check if mail is sent


--------------------------------------------------------------------------------------------------------
 