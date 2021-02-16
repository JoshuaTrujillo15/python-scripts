# OPENSSL WRAPPER FOR THE AVERAGE NON CRYPTOGRAPHER LIKE ME :)
import os

def main():
	while True:
		print("[+] OPENSSL WRAPPER [+]\nRecommended Cipher: aes-256-cbc ...\n")
		cipher = input("Enter your preferred cipher: ")
		type = input("Encrypt or Decrypt? (e/d): ")
		path = input("Enter local path 'path/to/file.txt': ")
		if path.endswith("enc"):
			outPath = path[:-3] + "txt"
		elif path.endswith("txt"):
			outPath = path[:-3] + "enc"
		else:
			print("\n[!] File format not yet supported [!]")
			continue
		pwd = os.popen("pwd").read()
		pwd = pwd.strip()
		fullPath = pwd + "/" + path
		if not os.path.isfile(fullPath):
			print("\n[!] File not found [!]\npath: {}".format(fullPath))
			continue
		cmd = "openssl enc -{} -{} -pbkdf2 -in {} -out {}".format(cipher, type, path, outPath)
		print("\n[cmd] " + cmd + "\n")
		os.system(cmd)
		print("\n[+] Command Executed [+]\n\nAttempting to delete previous file ...")
		delete = "rm " + path
		print("\n[cmd] " + delete)
		os.system(delete)
		print("\n[+] Deleted [+]")
		input("\nPress ENTER to exit ...")
		break


if __name__ == "__main__":
	main()
