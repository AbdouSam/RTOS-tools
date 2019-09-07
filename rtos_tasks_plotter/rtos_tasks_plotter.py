# This file uses Debuging Data from the UART's controller to display
# the ON and OFF time of the tasks.
# The code works only with python3
# Dependencies are numpy and matplotlib

# The code may cause some issues in a Windows machine due to timestamp()
#
# you will find arrays that defines these characters in this code
# If more tasks should be added the w,h variables should be adapted
# w : task number
# h : data length collected from file (correspond to number of lines to read)
# plot_arry_size should not exceed the value for h
#



#Tasks are ordered as follow :
# task         start    end

# 'task_00'    A       1    
# 'task_01'    B       2    
# 'task_02'    C       3      
# 'task_03'    D       4          
# 'task_04'    E       5      
# 'task_05'    F       6         
# 'task_06'    G       7          
# 'task_07'    H       8         
# 'task_08'    I       9        
# 'task_09'    J       Z          
# 'task_10'    K       W          
# 'task_11'    L       X          
# 'task_12'    M       U    
# 'task_13'    N       V          
# 'task_14'    O       Y 
#
# If more tasks are added, their str and end charcter should be added

import re
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np 

w, h = 15, 7200;


plot_arry_size = 20  # lines to read
plot_arry_start = 0  # offset to display 
task_states = np.zeros([w,h])
time_x = []

     

# the Starting Charcters for tasks
taks_tag_list_str = [ 'A', \
                      'B', \
                      'C', \
                      'D', \
                      'E', \
                      'F', \
                      'G', \
                      'H', \
                      'I', \
                      'J', \
                      'K', \
                      'L', \
                      'M', \
                      'N', \
                      'O']  

taks_tag_list_end = [ '1',\
                      '2',\
                      '3',\
                      '4',\
                      '5',\
                      '6',\
                      '7',\
                      '8',\
                      '9',\
                      'Z',\
                      'W',\
                      'X',\
                      'U',\
                      'V',\
                      'Y']
def main():
  line_num = 0
  first_time = 1

  f = open("debug_data.txt", "r")

  fl = f.readlines()

  for x in fl:
    line_num = line_num + 1

    try:
      time_stamp = re.search('\\[(.+?)\\]', x).group(1)
      date_timestamp = datetime.strptime(time_stamp, '%H:%M:%S:%f')

      if first_time == 1 :
        first_time = 0
        time_start = date_timestamp.timestamp() * 1000

    except Exception as e:
      date_timestamp = 'XXX'
      time_stamp = 'xxxx'
      print("Error Time stamp")
      quit()

    try:
      task_tag = re.search('\\] (.+?)', x).group(1)
      prin(str(task_tag))

      for ii in range(15):

        if(task_tag == taks_tag_list_str[ii]):
          task_states[ii][line_num] = 1

        elif(task_tag == taks_tag_list_end[ii]):
          task_states[ii][line_num] = 0

        else:
          # Othertasks stays the same 
          task_states[ii][line_num] = task_states[ii][line_num - 1]

    except Exception as e:
      task_tag = '00'
      print("Error Tag")
      quit()
    millisec = date_timestamp.timestamp() * 1000 - time_start
    time_x.append(millisec)

    if line_num > plot_arry_size:
      break  
    
    print('line ' + str(line_num) + ' : ' + str(millisec))

  f.close()
  x_plot = time_x[plot_arry_start:plot_arry_size]
  
  y_plot   = .9 * task_states[0][plot_arry_start:plot_arry_size]  + 0;
  y_plot2  = .9 * task_states[1][plot_arry_start:plot_arry_size]  + 1;
  y_plot3  = .9 * task_states[2][plot_arry_start:plot_arry_size]  + 2;
  y_plot4  = .9 * task_states[3][plot_arry_start:plot_arry_size]  + 3;
  y_plot5  = .9 * task_states[4][plot_arry_start:plot_arry_size]  + 4;
  y_plot6  = .9 * task_states[5][plot_arry_start:plot_arry_size]  + 5;
  y_plot7  = .9 * task_states[6][plot_arry_start:plot_arry_size]  + 6;
  y_plot8  = .9 * task_states[7][plot_arry_start:plot_arry_size]  + 7;
  y_plot9  = .9 * task_states[8][plot_arry_start:plot_arry_size]  + 8;
  y_plot10 = .9 * task_states[9][plot_arry_start:plot_arry_size]  + 9;
  y_plot11 = .9 * task_states[10][plot_arry_start:plot_arry_size] + 10;
  y_plot12 = .9 * task_states[11][plot_arry_start:plot_arry_size] + 11;
  y_plot13 = .9 * task_states[12][plot_arry_start:plot_arry_size] + 12;
  y_plot14 = .9 * task_states[13][plot_arry_start:plot_arry_size] + 13;
  y_plot15 = .9 * task_states[14][plot_arry_start:plot_arry_size] + 14;

  plt.close('all')
  plt.grid()

  y_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  y_ticks =['task_00', \
            'task_01', \
            'task_02', \
            'task_03', \
            'task_04', \
            'task_05', \
            'task_06', \
            'task_07', \
            'task_08', \
            'task_09', \
            'task_10', \
            'task_11', \
            'task_12', \
            'task_13', \
            'task_14']

  plt.yticks(y_y, y_ticks)

  plt.step(x_plot, y_plot,   )  # task 00
  plt.step(x_plot, y_plot2,  )  # task 01
  plt.step(x_plot, y_plot3,  )  # task 02
  plt.step(x_plot, y_plot4,  )  # task 03
  plt.step(x_plot, y_plot5,  )  # task 04
  plt.step(x_plot, y_plot6,  )  # task 05
  plt.step(x_plot, y_plot7,  )  # task 06
  plt.step(x_plot, y_plot8,  )  # task 07
  plt.step(x_plot, y_plot9,  )  # task 08
  plt.step(x_plot, y_plot10, )  # task 09
  plt.step(x_plot, y_plot11, )  # task 10
  plt.step(x_plot, y_plot12, )  # task 11
  plt.step(x_plot, y_plot13, )  # task 12
  plt.step(x_plot, y_plot14, )  # task 13
  plt.step(x_plot, y_plot15, )  # task 14
  plt.show()

if __name__  == "__main__":
  main()
