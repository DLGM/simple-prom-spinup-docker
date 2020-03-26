import sys
import subprocess

PROM_VER_VAR = "PROM_VER"
PROM_DRH = "PROM_DRH"
NODEXP_VER = "NODEXP_VER"
GRAF_VER = "GRAF_VER"
ENV_FILE_PATH = ".env"
BASH_COMMAND = "docker-compose up"



def main():

    # output data after replace
    out_data = ""

    # read env file
    with open(".env", 'r') as f:
        data = f.readlines()
    
    # replace values with arguments
    for line in data:
        if PROM_VER_VAR in line:
            line = line.split("=")[0] + "=" + sys.argv[1] + "\n"
        elif PROM_DRH in line:
            line = line.split("=")[0] + "=" + sys.argv[2] + "\n"
        elif NODEXP_VER in line:
            line = line.split("=")[0] + "=" + sys.argv[3] + "\n"
        elif GRAF_VER in line:
            line = line.split("=")[0] + "=" + sys.argv[4] + "\n"
        out_data += line
    with open('.env', 'w') as f:
        f.write(out_data)
    
subprocess.run(BASH_COMMAND.split())

if  __name__ == "__main__":
    main()