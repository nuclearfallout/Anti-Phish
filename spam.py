# Get revenge on phishing websites
# Flood their web form with fake emails/passwords

import random, string, os, requests, json

file = 'FilePath.json'
num_lines = sum(1 for line in open(file))
randomChars = string.ascii_letters + string.digits + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
random.seed = (os.urandom(1024))
count = 0
url = '' # Phish site to flood
send_stat = 0
names = json.loads(open(file).read())
print("- Initiating Flood against %s -" % (url))
for line in names:
	nameExtention = ''.join(random.choice(string.digits))
	count = count + 1
	username = name.lower() + nameExtention + '@gmail.com' # Can be anything
	password = ''.join(random.choice(chars) for i in range(8))
	requests.post(url, allow_redirects=False, data={
	    'username': username,  # Websites username input
	    'password': password  # Websites password input
	})
	if requests.ConnectionError:
		send_stat = "Blocked!"
	else:
		send_stat = "Sent!"
	if count == num_lines:
		print("[%s/%s] Post Data Packets Sent Successfully!" % (count, num_lines))
	print("[%s/%s] Post Data -> '%s : %s' Status: %s" % (count, num_lines, username, password, send_stat))

