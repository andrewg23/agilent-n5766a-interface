from optparse import OptionParser
import powerSupply as ps

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-p','--power',
                      dest = 'power',
                      help='1 - Power On, 0 - Power Off')
    parser.add_option('-v','--voltage',
                      dest = 'voltage',
                      help='Set voltage value')
    parser.add_option('-c','--current',
                      dest = 'current',
                      help='Set current value')

    (options,args) = parser.parse_args()
        
    power = options.power
    voltage = options.voltage
    current = options.current

    if(power):
        ps.setPower(int(power))

    if(voltage and current):
        ps.setOutput(v=int(voltage), c=int(current))
    elif (voltage):
        ps.setOutput(v=int(voltage))
    elif (current):
        ps.setOutput(c=int(current))

    print(ps.getStatus())
