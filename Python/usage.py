import psutil
import smtplib
import os
import signal
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
SENDER_EMAIL = "dd1123687@gmail.com"
RECEIVER_EMAIL = "akashchandran2112@gmail.com"
SMTP_SERVER = "smtp.gmail.com"  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587
SMTP_USER = "dd1123687@gmail.com"
SMTP_PASSWORD = "qwerty@123"  # Use app-specific password if 2FA is enabled

# CPU usage threshold
CPU_THRESHOLD = 10.0

# Function to send email
def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to restart the application process
def restart_application(pid, process_name):
    try:
        print(f"Restarting application: {process_name}")
        
        # Kill the process
        os.kill(pid, signal.SIGTERM)
        
        # Wait a moment and restart the process
        # (assuming the command to start the process is known)
        subprocess.Popen(process_name)
    except Exception as e:
        print(f"Failed to restart process: {e}")

# Monitor CPU usage
def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Current CPU Usage: {cpu_usage}%")
        
        if cpu_usage > CPU_THRESHOLD:
            # Find the process consuming high CPU
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
                try:
                    if proc.info['cpu_percent'] > 10:  # Arbitrary value to filter high-CPU processes
                        pid = proc.info['pid']
                        process_name = proc.info['name']
                        process_user = proc.info['username']
                        
                        # Skip the System Idle Process (PID: 0)
                        if pid == 0:
                            print("Skipping System Idle Process (PID: 0)")
                            continue
                        
                        print(f"Process {process_name} (PID: {pid}) is using high CPU: {proc.info['cpu_percent']}%")

                        # Check if the process is a system or application process
                        if process_user == "root" or process_user == "SYSTEM":
                            # Send email if system process
                            subject = f"High CPU Usage: {process_name}"
                            body = f"The system process {process_name} (PID: {pid}) is using high CPU: {proc.info['cpu_percent']}%"
                            send_email(subject, body)
                        else:
                            # Kill and restart application processes
                            print(f"Killing and restarting process {process_name} (PID: {pid})")
                            restart_application(pid, process_name)
                            #kill if this is a application process
                            #this part is wrong remove this part

                            
                        # Kill all other processes that are consuming too much CPU (except system processes)
                        if process_user != "root" and process_user != "SYSTEM":
                            try:
                                proc.terminate()  # Kill the process
                                print(f"Terminated {process_name} (PID: {pid})")
                            except psutil.NoSuchProcess:
                                print(f"Process {process_name} (PID: {pid}) already terminated.")
                            except psutil.AccessDenied:
                                print(f"Access denied to terminate process {process_name} (PID: {pid})")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue  # Skip if process no longer exists or access is denied

if __name__ == "__main__":
    monitor_cpu_usage()
