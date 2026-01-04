from datetime import datetime
from collections import defaultdict
import re

LOG_FILE="secure.log"
WINDOW_SECONDS=300

def parse_timestamp(line):
	return datetime.striptime(line[:15],"%b %d %H:%M:%S")

def extract_ip(line):
	match = re.search(r"from (\d+\. \d+\. \d+\. \d+\.)",line)
	return match.group(1) if match else None

def sliding_window_per_ip(log_file):
	failures = defaultdict(list)

	with open(log_file,"r") as f:
		for line in f:
			if "Failed password" in line:
				ip = extract_ip(line)
				if ip:
					failures[ip].append(parse_timestamp(line))

	results = {}

	for ip,times in failures.items():
		left = 0
		max_attempts = 0

		for right in range(len(times)):
			while (times[right] - time[left]).seconds > WINDOW_SECONDS:
				left += 1

			max_attempts = max(max_attempts , right - left +1)

		results[ip] = max_attempts

	return results

if __name__ == '__main__':
	result = sliding_window_per_ip(LOG_FILE)

	for ip,count in sorted(result.items(),key = lambda x: x[1], reverse=True):
		print(f"{ip} -> {count} failed attempts in 5 minutes")

