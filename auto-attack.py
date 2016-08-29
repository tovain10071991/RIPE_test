import os, sys

line = str()
control_flow = str()

while(1):

  try:
    control_input = open("control_output", "r")
    line = control_input.readline()
    control_input.close()
  except IOError:
    pass

  if len(line) != 0:
    if line[len(line)-1] == '\n':
      control_flow = line[:len(line)-1]
    else:
      control_flow = line

  i = 0
  for i in range(len(control_flow)-1, -1, -1):
    if control_flow[i] == '0':
      control_flow = control_flow[:i] + '1'
      break

  if i != -1:
    print "now control flow: " + control_flow
    os.system('/mnt/sdb/saib-with-triton-v3/bin/saib ./attackee-64bit-v2 0x4016a5 0x401ac4 ' + control_flow)
  else:
    break
