#!/usr/bin/python3
import os
import argparse

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False


# def main():
#    switchlist = ["172.0.1.2", "10.10.1.10", "192.168.1.1" "8.8.8.8"]   # CUSTOMIZE THIS LIST WITH IPs to PING
def ping():
    pings = argparse.ArugmentsParser()
    pings.add_argument("-ip", help="ip you want to ping")
    args = pings.pings_args()
    return args

def main():
    args = ping()



#    ## Use a loop to check each device for ICMP responses
#    print("\n***** STARTING ICMP CHECKING *****")
#    for x in switchlist:
#        if ping_router(x):
#            print(f"IP address {x} is responding to ICMP")
#        else:
#           print(f"IP address {x} is not responding to ICMP")

#if __name__ == "__main__":
    main()

