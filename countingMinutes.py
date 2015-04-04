def CountingMinutesI(str): 

  # separate the times at -
  
   time = str.split("-")
  
  # split at : into two lists
  
   time_1 = time[0].split(":") # List 0 would be nums before :
   time_2 = time[1].split(":") # List 1 would be nums after :
  
  # if either list has 12 in it set count to 0
  
   if (int(time_1[0])) == 12:
     time_1[0] = 0
   if (int(time_2[0])) == 12:
     time_2[0] = 0
    
  # insert time_1 num from list 0 + [:2] round to 2 places after .
  
   time_start = int(time_1[0]) * 60 + int(time_1[1][:2])
   if time_1[1][2:] == "pm":
     time_start += (60*12) # 60mins*12hrs = 720
    
  # same as previous statement but for time_2
  
   time_end = int(time_2[0]) * 60 + int(time_2[1][:2])
   if time_2[1][2:] == "pm":
     time_end += (60*12)
  
  # simple if statement to solve and print
  
   if time_start > time_end:
     return (60 * 24) - (time_start - time_end) # 60 for min 24 for hours
   else:
     return time_end - time_start

print CountingMinutesI(raw_input()) 