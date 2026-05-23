import subprocess
import psutil
import time
PID = int(input("Specify PID: "))
aR = int(input("Specify Kill Attempts: "))
i = 1	

def Task_Killer():
	print(PID)
	cmd = f"TASKKILL /PID {PID}"
	print(aR)
	for i in range(aR):
		if not psutil.pid_exists(PID):
			break
			print(f"PID {PID} is no longer running.")
			return
		
		
		subprocess.run(cmd, shell=True)

# FUNCTIONS
Task_Killer()

# POST
print(f"{PID} has been killed\nQuitting in 5 Seconds...")
time.sleep(5)
quit()