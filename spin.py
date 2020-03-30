import sys
import subprocess
import time

PROM_VER_VAR = "PROM_VER"
PROM_DRH = "PROM_DRH"
NODEXP_VER = "NODEXP_VER"
GRAF_VER = "GRAF_VER"
STORAGE_PATH_CONV_VAR="STORAGE_PATH_CONV"
STORAGE_RETENTION_CONV_VAR="STORAGE_RETENTION_CONV"
ENV_FILE_PATH = ".env"
BASH_COMMAND = "docker-compose up"
OLD_DATA_PATH = "storage.local.path"
OLD_DATA_RETENTION = "storage.local.retention"
NEW_DATA_PATH="storage.tsdb.path"
MID_DATA_RETENTION = "storage.tsdb.retention"
NEW_DATA_RETENTION = "storage.tsdb.retention.time"
ERR_MSG_MISSING_ARG = "missing argument, please check README.md for correct tool usage"
ERR_MSG_PROM_VER_NOT_VALID="Sorry, Prometheus version is not valid"


def main():
    print('starting script...')
    if len(sys.argv) is not 5:
        print(ERR_MSG_MISSING_ARG)
        return
    
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
        elif STORAGE_PATH_CONV_VAR in line:
            if sys.argv[1].split('.')[0] == '1' or sys.argv[1].split('.')[0] == 'v1':
                line = STORAGE_PATH_CONV_VAR + "=" + OLD_DATA_PATH + "\n"
            elif sys.argv[1].split('.')[0] == '2' or sys.argv[1].split('.')[0] == 'v2':
                line = STORAGE_PATH_CONV_VAR + "=" + NEW_DATA_PATH + "\n"
            else:
                print(ERR_MSG_PROM_VER_NOT_VALID)
                return
        elif STORAGE_RETENTION_CONV_VAR in line:
            if sys.argv[1].split('.')[0] == '1' or sys.argv[1].split('.')[0] == 'v1':
                line = STORAGE_RETENTION_CONV_VAR + "=" + OLD_DATA_RETENTION + "\n"
            elif sys.argv[1].split('.')[0] == '2'  or sys.argv[1].split('.')[0] == 'v2':
                if int(sys.argv[1].split('.')[1]) >= 0 and int(sys.argv[1].split('.')[1]) < 7:
                    line = STORAGE_RETENTION_CONV_VAR + "=" + MID_DATA_RETENTION + "\n"
                elif int(sys.argv[1].split('.')[1]) >= 7 and int(sys.argv[1].split('.')[1]) < 18:
                    line = STORAGE_RETENTION_CONV_VAR + "=" + NEW_DATA_RETENTION + "\n"
        out_data += line
    with open('.env', 'w') as f:
        f.write(out_data)
    
    print('--------------------------')
    print('final data: ')
    print(out_data)
    print('--------------------------')
    time.sleep(5)
    subprocess.run(BASH_COMMAND.split())

if  __name__ == "__main__":
    main()