import calculator

c = calculator.Calculator()

while True:
    cmd = raw_input(":")
    print(c.run_cmd(cmd)) 
