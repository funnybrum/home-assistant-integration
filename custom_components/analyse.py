# from collections import defaultdict
#
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
# prev_bits = None
# changing_bits = set()
#
# def analyse(cmd):
#      bits = ''
#      global prev_bits
#
#      for i in range(0, len(cmd)):
#           pulse_type = 'on' if i % 2 == 0 else 'off'
#           pulse_len_us = cmd[i]
#           if pulse_type == 'off':
#                bits += '0' if pulse_len_us < 1000 else '1'
#
#      if prev_bits:
#           for i in range(0, len(bits)):
#                if i < len(bits) and i < len(prev_bits) and bits[i] != prev_bits[i]:
#                     changing_bits.add(i)
#
#      prev_bits = bits
#
#      tmp_bits = ''
#      for i in range(0, len(bits)):
#           if i in changing_bits:
#                tmp_bits += bcolors.FAIL
#           tmp_bits += bits[i]
#           if i in changing_bits:
#                tmp_bits += bcolors.ENDC
#
#      print(tmp_bits)
#
#
# import serial
# import ast
#
# ser = serial.Serial('/dev/cu.wchusbserial1420', 115200)
#
# while True:
#      line =  ser.readline()
#      line = str(line)
#      if '] = {' in line:
#           raw_cmd = ast.literal_eval(line[line.index('{')+1:line.index('}')])
#           analyse(raw_cmd)
#
#
# print(ser.readline())
#
#
# analyse(CMDS[18])
# analyse(CMDS[20])
# analyse(CMDS[22])
# analyse(CMDS[24])
# analyse(CMDS[26])
#
#
# # 01101  011010  18  8 + 4 + 1
# # 10101  101010  20  16 + 4 + 1
# # 00101  001010  22
# # 11001  110010  24
# # 01001  010010  26
