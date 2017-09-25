import vcgencmd
import time
import sys

class JJStats:
    def __init__(self):
        print("JJStats initialized!")
        self.mainStack()
        
    def mainStack(self):
        userInput = ""
        while(True):
            self.doPrompt()
            
            userInput = input("Enter a command:")
            sourceInput = ""
            if(userInput == "1"):
                sourceInput = input("Choose frequency source:")
                print("Gathering information...")
                outDisp = self.DisplayClock(str(sourceInput))
                print(outDisp)
            elif(userInput == "2"):
                sourceInput = input("Choose voltage source:")
                print("Gathering information...")
                outDisp = self.DisplayVoltage(str(sourceInput))
                print(outDisp)
            elif(userInput == "3"):
                print("No source input required.")
                print("Gathering information...")
                outDisp = self.DisplayTemperature()
                print(outDisp)
            elif(userInput == "4"):
                print("\nExiting...\n")
                break
                
            else:
                print("\nInvalid command!\n")
        sys.exit(1)
                    
    def doPrompt(self):
        print(
              "Commands:\n"+
              "1)Get Clock Frequency <arm, core, h264, isp, v3d, uart, pwm, emmc, pixel, vec, hdmi, dpi>\n"+
              "2)Get Set Voltage <core, sdram_c, sdram_i, sdram_p>\n"+
              "3)Get Temperature <no parameters available>\n"+
              "4)Exit\n"
              )
        
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
    program = JJStats()
    
if __name__ == "__main__":
    main()
