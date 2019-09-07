### FreeRTOS tasks timming plotter
  FreeRTOS contain natively libraries to monitor tasks State, WaterMark
  and Running Time, but it could be a difficult to impliment

  An alternative (a crude one), is to get the ON and OFF time through UART port.
  The idea is to print through UART one byte (0-255) every time the tasks is called
  and print another byte when the tasks is finished like so,
  
  for (;; )
  {
    UART_putc('A');

    task_();

    UART_putc('B');
  }

  You do that for All the tasks, then you run the Board with FreeRtos and you 
  capture UART data with a time stamp for each byte (there are plenty of free
  tools that let you do that like cutecom)
  
  For Tasks One 'A' indicate tasks is ON, 'B', tasks is OFF, and other letters 
  or hex values can be used for other tasks as ON and OFF values.

  You take all these timestamp and save them to a debug_data.txt
  the file "debug_data.txt" should be in same dir as this python file.
  the debug_data.txt is formed of lines.
  each line has this form : [hh:mm:ss:ms] X
  line format : timestamp between '[]' followed by space followed by One Character.
  Example of how the file should be :
  [17:54:47:227] A
  [17:54:47:228] B

  Define you arrays of Start_asks and End_Task.
  Run the code.