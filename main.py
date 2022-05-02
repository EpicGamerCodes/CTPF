import json
import os
import requests

def ask(prompt: str, yes: str = "Y", no: str = "N"):
    responce = "Not Set"
    while not ((responce.upper() == yes.upper()) or (responce.upper() == no.upper())):
        responce = input(prompt + f" ({yes}/{no}): ")
    if responce.upper() == yes.upper():
        return True
    else:
        return False

class Config:
	def create(self, file: str, username: str, version: str) -> dict:
		config = {}
		info = {}
		info["creator"] = username
		info["version"] = version
		config["perms"] = {username:{"alert":True}}
		config["info"] = info
		with open(file, "w") as f:
			f.write(json.dumps(config, indent = 4))
		return config
	
	def read(self, file: str, username: str) -> dict:
		with open(file, "r") as f:
			config = json.load(f)
		
		try:
			config["perms"][username]
		except Exception:
			config = self.perms(config, username)
			with open(file, "w") as f:
				f.write(json.dumps(config, indent = 4))
		
		if not config["info"]["version"] == Chat.version:
			input("WARN: Server Storage Slot is outdated.")
		return config
	
	def perms(self, config, username) -> dict:
		config["perms"][username] = {"alert":False}
		return config

class Chat:
	version: str = "v1.0.0-alpha"
	
	def __init__(self, server: str = None):
		self.title = "Chat through Python File"
		self.server = server
		self.version = Chat.version
		self.config = Config()
		
		gh = requests.get("https://api.github.com/repos/EpicGamerCodes/CTPF/releases/latest").json()
		if not gh["name"] == f"{self.version}":
			gh_version = gh["name"]
			gh_body = gh["body"]
			gh_published = gh["published_at"]
			if ask(f"An update is required. {gh_version} (Published at {gh_published}) includes:\n{gh_body}\nUpdate?"):
				gh_url = gh["html_url"]
				os.system(f'start "" "{gh_url}"')
				exit()
			else:
				exit()
		
		os.system("title " + self.title)
		with open(self.server + "/config.json", "r") as f:
			self.server_conf: dict = json.load(f)

		self.username = os.getlogin()
		if not self.username in list(self.server_conf["users"].keys()):
			if ask("Would you like a chat nickname?"):
				nickname = input("Nickname: ")
				self.server_conf["users"][self.username] = [nickname, 0]
				with open(self.server + "/config.json", "w") as f:
					f.write(json.dumps(self.server_conf, indent = 4))
			else:
				self.server_conf["users"][self.username] = [self.username, 0]
				with open(self.server + "/config.json", "w") as f:
					f.write(json.dumps(self.server_conf, indent = 4))	
	
	def checks(self):
		if self.server_conf["status"]["online"] is False:
			reason = self.server_conf["status"]["reason"]
			eta = self.server_conf["status"]["eta"]
			input(f"ERROR: Server is offline.\nReason: {reason}\n Online in: {eta}")
			exit()
		if self.username in self.server_conf["banned"]:
			input("ERROR: You have been banned\nPress Anything to Exit.")
			exit()
		
	def ask(self):
		self.cont = True
		check = False
		while not check:
			x = input("Would you like to login to a server? (Y/N): ")
			if x == "Y":
				if self.server is None:
					exists = False
					while not exists:
						self.server = input("Enter the Server Path: ")
						if os.path.isdir(self.server):
							exists = True
				
				exists = False
				while not exists:
					self.hostname = input("What is the username of the SSP's creator?: ")
					if not os.path.isdir(self.server + "/" + self.hostname):
						print("ERROR: SSP host does not exist!")
					else:
						exists = True
				
				exists = False
				while not exists:
					self.code = input("Chat Code: ")
					if not os.path.isdir(self.server + "/" + self.hostname + "/" + self.code):
						print("ERROR: Chat Code does not exist!")
					else:
						exists = True
				
				self.path = self.server + "/" + self.hostname + "/" + self.code
				check = True
			elif x == "N":
				if self.server_conf["users"][self.username][1] > 3:
					print("You can not have more than 3 active chats!")
					print("Chats are automaticly deleted every Friday, but you can send a request to the Owner to delete an old chat.")
				else:
					os.system("cls")
					print("<< Creating SSP >>")
					self.hostname = self.username
					self.code = input("Enter an acess code for users to enter: ")
					if self.server is None:
						exists = False
						while not exists:
							self.server = input("Enter the Server Path: ")
							if os.path.isdir(self.server):
								exists = True
					self.path = self.server + "/" + self.hostname + "/" + self.code
					try:
						os.mkdir(self.server + "/" + self.hostname)
					except Exception:
						pass

					try:
						os.mkdir(self.path)
					except Exception as e:
						print(e)

					self.host_conf = self.config.create(self.path + "/config.json", self.hostname, self.version)
					self.cont = False
					self.server_conf["users"][self.username][1] += 1
					with open(self.server + "/config.json", "w") as f:
						f.write(json.dumps(self.server_conf, indent = 4))
					
					check = True
		
		self.file = self.path + "/" + self.code + ".txt"

	def chat(self):
		os.system("cls")
		self.nickname = self.server_conf["users"][self.username][0]
		if self.cont:
			self.host_conf = self.config.read(self.path + "/config.json", self.username)
		else:
			with open(self.file, "w") as f:
				f.write(f"Created by {self.username}")
		
		loop = True
		os.system(f"start cmd /C {os.path.dirname(os.path.abspath(__file__))}/.assets/read.bat {self.code} 1 {self.path}\\{self.code}.txt")
		with open(self.file, "a") as f:
			f.write(f"\n{self.nickname} ({self.username}) joined the chat.")

		text = ""
		while loop:
			if text.lower()[:7] == "alert: ": # Here because screen gets cleared later on.
				print("You don't have the permissions for that!")
			
			text = input("> ")
			with open(self.file, "a") as f:
				print("OPEN FILE")
				if text.lower() == "exit":
					print("exit...")
					f.write(f"\n>> {self.nickname} ({self.username}) has left the chat <<")
					loop = False
				elif text.lower() == "/reader":
					print("reader...")
					os.system(f"start cmd /C {os.path.dirname(os.path.realpath(__file__))}\\.assets\\read.bat {self.code} 1 {self.path}\\{self.code}.txt")
				elif text.lower()[:7] == "alert: ":
					if self.host_conf["perms"][self.username]["alert"] is True:
						f.write(f"\n>> {text[7:]} <<")
				else:
					print("Writing...")
					f.write(f"\n{self.nickname}: {text}")
			os.system("cls")

if __name__ == "__main__":
	app = Chat("//curriculum.lan/filestore/home/2019/bevyn.fernandes/PublicServer")
	app.ask()
	app.checks()
	app.chat()
