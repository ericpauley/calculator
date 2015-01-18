import calculator

c = calculator.Calculator()

#Basic script for command line testing
while True:
    cmd = raw_input(":")
    print(c.run_cmd(cmd)) 
