#!/usr/bin/env python3

# API to generate a range of all the IP addresses that it represents 
# (in a given range) for ipv4 and ipv6 you have a CIDR network 
# e.g. 123.45.67.89/27
import sys
import ipaddress

def ipaddress_generator(cidr_add): # Generates a range of IP addresses from an IPv4 or IPv6 address input
    try:
        ip_add_obj = ipaddress.ip_network(cidr_add,strict=False) # Using ip_network() to automatically check for both IPv4 and IPv6 address
        useable_hosts = ip_add_obj.hosts() # Iterator for all useable hosts in the network (excl. network and broadcast addresses)
        ip_range = list(str(host) for host in useable_hosts) # Turn iterator into list

        print("Here is a list of hosts available for you: {}".format(ip_range))
    
    except ValueError: # Error message when you dont enter a valid IPv4 or IPv6 address
        print("Please enter a valid IP address")

if __name__ == "__main__":
    ipaddress_generator(sys.argv[1]) # So you can enter a args when directly testing from Terminal