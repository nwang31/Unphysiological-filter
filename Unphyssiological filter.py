import os
import shutil
import numpy as np
import reslast

def results_output(fileName):
    filePath = "/mnt/parscratch/users/mep21nw/micromale/" + fileName
    destinationPath = "/mnt/parscratch/users/mep21nw/microhealthy/virtual_population/"
    fileList = os.listdir(filePath)
    os.chdir(filePath)

    filteredFiles = []

    for file in fileList:
        if file.endswith('_results'):
            file_path = os.path.join(filePath, file)
            size = os.path.getsize(file_path)  # Get the size of the file in bytes
            if size >= 24576:
                filteredFiles.append(file)

    print("Number of filtered Files:", len(filteredFiles))
sbp=np.normal.random()
dbp=np.normal.random()
ri=np.normal.random()
    for f in filteredFiles:
        q, a, p, u, c, n, t = reslast.resu(filePath, f)
        if '7-c' in p and '21-c' in p:
            bp_7c = p['7-c'][:, 2]
            bp_21c = p['21-c'][:, 2]
        if '42-S1' in u and '44-S1' in u:
            u_42A = 100 * u['42-S1'][:, 2]
            u_44A = 100 * u['44-S1'][:, 2]
            u_max = np.max(u_42A)
            end = u_42A[-1]
            ri = (u_max - end) / u_max

            if ( < np.min(bp_7c) <  or  < np.max(bp_7c) < ) and  < ri < :

# Call the function with the specific folder name
results_output('micromale')