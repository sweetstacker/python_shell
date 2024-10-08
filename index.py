import os
import subprocess

def my_shell():
    print(f"{os.getcwd()} ||| python_fakeos(shell) by sweetstacker ")
    while True:
        #디렉토리 경로(현재의 디렉토리?)
        command_cmd = input("==>  ")

        #명령어 processing
        if command_cmd == "exit": #Exit
            print("Exiting os...")
            break
        elif command_cmd.startswith("cd"): #Compact Disk
            try:
                os.chdir(command_cmd.split(" ")[1])
            except IndexError:
                print("Please provide a path.")
            except FileNotFoundError:
                print("Directory not found.")
            except PermissionError:
                print("Permission denied: You do not have access to read this file.")
        elif command_cmd == "pwd": #Print Working Directory
            print(os.getcwd)
        elif command_cmd == "ls": #List Segments ( == dir) 리스트 세그멘트
            print("\n".join(os.listdir()))
        elif command_cmd.startswith("cat"): #catenate 파일 내용 표시
            try:
                with open(command_cmd.split(" ")[1], "r") as file:
                    print(file.read())
            except IndexError:
                print("Please provide a file.")
            except FileNotFoundError:
                print("File not forund.")
            except PermissionError:
                print("Permission denied: You do not have access to read this file.")
        elif command_cmd == "clr": #CLEar
            subprocess.run("clear" if os.name != 'nt' else "cls", shell=True)
        else:
            print(f"command not found: {command_cmd}")

if __name__ == "__main__":
    my_shell()