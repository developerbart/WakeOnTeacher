# WakeOnTeacher

WakeOnTeacher can be seen as the human version of **Wake on LAN** (WoL).
The script makes use of the `smtplib` built-in Python module.
To use the script for your own needs (e.g. send email to specific user), the following needs to be changed:

* Alter the `fromaddr` and `toaddr` variable to respectively the receiver and sender email address.
* Specify a subject in the `header` variable.
* Write out your plain text body.
* Specify the FQDN/IP-address of the mailserver in the object (by default starttls is used).
* Specify the credentials.

To automate the script, one can simply create a cronjob. As a quick refresher, a cronjob can be created using the `crontab` command as root (not sudo).

```bash
crontab -u USERNAME -e
```
To run the script every 10 minutes use the following layout.
```bash
*/10 * * * * script.py
```
**Note:**Please make sure that the script is executable.

To view scheduled cronjobs for a user, use the following command.
```bash
crontab -u USERNAME -l
```
