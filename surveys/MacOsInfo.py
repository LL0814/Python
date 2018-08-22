import os
cmd = "/usr/sbin/system_profiler SPHardwareDataType "
output = os.popen(cmd)
print(output.read())