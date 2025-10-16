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
