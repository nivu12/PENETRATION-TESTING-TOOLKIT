# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: NIVYA ANTONY

*INTERN ID*: CT04DY2625

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

## The task 3 for Cybersecurity and Ethical Hacking was to create a toolkit for penetration testing. It was instructed to build a toolkit including multiple modules like port scaner, brute-forcer etc...for penetration testing. The very first thing to do is to understand clearly the terms specified in this task such as port scanner, brute-forcer so as to learn and work on it.Later then you can develop the modules. 
First I created a folder named *PENTOOLKIT* to store my all modules,scripts, output files such as html,csv etc. Inside the PENTOOLKIT FOLDER another folder named *MODULES* were created. This folder contains all individual tools such as *banner_grabber.py*, *bruteforce_demo.py*, *logger_mod.py*, *port_scanner.py*, *reporter.py*, *vuln_checks.py*. Outside the *MODULES* the given files were placed,*main.py*, *practise_server.py*.
Port scanner tool is used to identify the open ports in a system. Using the pythons 'socket' library we can connect to a specific port using the function 'scan_port'.If the connection is established then the port is open or else it is closed.
*banner_grabber.py* is used to return the banner string if data is recieved and on timeout or any error it returns an empty string.
Brute force attack is a type of cyber attack in which the attacker uses trial and error method to gain unauthorized access by inputing possible combination of credential such as usernames and passwords.*bruteforce_demo.py* run against the localhost.
*reporter.py* creates a html file to easily view and understand the scan outputs for the attacks on the localhost.
*requirement.txt* contains 'requests' as http client and 'flask' as a practise server. Using 'pip install' it was installed.
*practice_server.py* runs locally and act as a target for brute force attack and for validating http vulnerablilities. *main.py' provide the CLI to run port_scanner, bruteforce_demo,bsnner_grabber and produce html files.
*logger_mod.py* creates two log outputs one for  real time messages(console) and other for detailed records(timestamped log file)
*vuln_checks.py* uses 'requests' and perform only basic,passive http interactions which is suitable for scanning local practise server.
Created a virtual environment and run these scripts and output files such as html,csv were obtained with the results. Finally the task 3 is completed.

# OUTPUT

<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/0214fe2a-f0ec-4b59-930a-198ce9df7813" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/2007ff1b-adf1-4290-9668-c96493ab22d1" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/e169c3e1-b3c7-40ce-8ec9-14dcefaf4b54" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/779e1637-43b9-4a83-93f1-845382f9ca2a" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/d6527a94-e074-4f51-be47-92dcac4f6b76" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/06db2f55-3e01-4176-a6fa-4e1f451df6d0" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/3e26ea97-59a2-4cf7-ae78-6ae50a2737cb" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/97952cad-dada-4b74-947f-aa2dd7f4ea1c" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/227c557f-2234-40cb-9d03-8fee3f8441ae" />
<img width="1360" height="768" alt="Image" src="https://github.com/user-attachments/assets/86afd1bd-ce7d-4963-bc91-d159a1b519be" />


