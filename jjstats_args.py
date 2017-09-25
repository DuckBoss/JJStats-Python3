import vcgencmd
import time
import sys

class JJStats_Args:
    def __init__(self):
        print("JJStats_Args initialized!")
        self.mainStack()
        
    def mainStack(self):
        if(len(sys.argv) > 0):
            commandType = str(sys.argv[1])
            
            if(commandType == "-h"):
                print("format: jjstats_args.py <command type> <command source>")
                print("available commands:\n"+
                      "1 <arm, core, h264, isp, v3d, uart, pwm, emmc, pixel, vec, hdmi, dpi> - Displays frequency of the chosen source\n"+
                      "2 <core, sdram_c, sdram_i, sdram_p> - Displays set voltage of the chosen source\n"+
                      "3 <none> - Displays temperature in celsius\n")
                sys.exit(1)
            
            if(len(sys.argv) == 3):
                commandSource = str(sys.argv[2])
                if(commandType == "1"):
                    print("Gathering information...")
                    outDisp = self.DisplayClock(commandSource)
                    print(outDisp)
                    sys.exit(1)
                elif(commandType == "2"):
                    print("Gathering information...")
                    outDisp = self.DisplayVoltage(commandSource)
                    print(outDisp)
                    sys.exit(1)
            
                
            if(commandType == "3"):
                print("Gathering information...")
                outDisp = self.DisplayTemperature()
                print(outDisp)
                sys.exit(1)
            else:
                print("\nInvalid Arguments!\n")
                print("Correct format is 'python3 jjstats_args.py <commandType> <commandSource>'\n")
                sys.exit(0)
        else:
            print("This program requires 2 command line arguments.\nFor help -> jjstats_args.py -h\n")
            sys.exit(0)
        sys.exit(1)
        
        
    def DisplayClock(self, item):
        outItem = "\n" + str(vcgencmd.measure_clock(item)/1000000) + " Mhz\n"
        return outItem
    def DisplayVoltage(self, item):
        outItem = "\n" + str(vcgencmd.measure_volts(item)) + "V\n"
        return outItem
    def DisplayTemperature(self):
        outItem = "\n" + str(vcgencmd.measure_temp()) + "C\n"
        return outItem
    
    


def main():
    program = JJStats_Args()
    
if __name__ == "__main__":
    main()
