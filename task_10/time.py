import time
###How long does the script run
time_beg = time.perf_counter_ns() ### record the start time
num_1 = 199999123412**199999 ### just calculation big digit
print(time.perf_counter_ns() - time_beg) ### display what time our program spend
