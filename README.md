# JJStats-Python3
A small utility program to get system information.


## jjstats.py
This utility is CLI only and it requires user input.
Instructions are provided within the interface.


## jjstats_args.py
This utility is CLI only and it requires command line arguments.

### Commands Format:
"python3 jjstats_args.py <command type> <command source>"
"python3 jjstats_args.py <command type>"

### Available Commands:
#### Displays frequency of the chosen source -
"1 <arm, core, h264, isp, v3d, uart, pwm, emmc, pixel, vec, hdmi, dpi>"
#### Displays set voltage of the chosen source -
"2 <core, sdram_c, sdram_i, sdram_p>"
#### Displays temperature (no source required) - 
"3 <none>"
