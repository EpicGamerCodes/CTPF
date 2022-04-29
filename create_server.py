import os
import sys
import json

def main(path = sys.argv[1]):
	if not os.path.isdir(path):
		os.mkdir(path)
	
	# Config
	config = {}
	config["status"] = {}
	config["status"]["online"] = True
	config["status"]["reason"] = "Online"
	config["status"]["eta"] = 0
	config["banned"] = {}
	config["banned"]["users"] = []
	with open(path + "/config.json", "w") as f:
		f.write(json.dumps(config, indent = 4))

if __name__ == "__main__":
	main()