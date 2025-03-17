
# https://leetcode.com/discuss/post/949160/goldman-sachs-phone-most-frequent-ip-add-f9h5/

# Given a list of logs with IP addresses in the following format.
# lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]

# Return the most frequent IP address from the logs. The retuned IP address value must be in a string format. If multiple IP addresses have the count equal to max count, then return the address as a comma-separated string with IP addresses in sorted order.


def most_freq_ips(logs: list[list[str]]) -> str:
    '''Extract IPs and count them'''
    freq = {} # create empty dict, ip:count
    for log in logs:  # for each log
        ip = log.split()[0]  # split strings on spaces, return first element
        freq[ip] = freq.get(ip, 0) + 1  # set dict key = ip, value is 0 if key doesn't exist or add 1 to existing value

    '''Calculate the max'''
    vals = set(freq.values())  # remove dupes
    max_val = 0  # set initial max
    for val in vals:  # if val is larger than max val, set max val = val
        if val > max_val:  
            max_val = val

    '''Subset just the strings that have the max freq value'''
    # ip_list = []
    # for k,v in freq.items():
    #     if v == max_val:
    #         ip_list.append(k)
    ip_list = [ip for ip, count in freq.items() if count == max_val]
    '''
    # return(", ".join(ip_list))
    ### Returns a list, but it won't necessarily be sorted how you want it
    '''
    
    '''sort IPs that have the max freq value, convert IP to integer'''
    binary={}
    for ip in ip_list:
        parts = ip.split(".") # split ip by octet
        result = 0  # result is ip as integer/binary
        for part in parts: # for each octet
          result = (result << 8) + int(part) # shift 8 bits to the left (octet) and add int value of each octet
        binary[ip]=result # save it in the dict ip: ip_int

    '''sort the ip list by ip_int smallest to largest w/ bubble sort, then return IPs'''
    items = list(binary.items()) # save the key value pairs as a list of tuples
    n = (len(binary.items())) # lenght of the list
    for i in range(n): # for each list element
        for j in range(0, n-1-i): # for the unsorted portions (moves left as items get sorted)
            if items[j][1] > items[j+1][1]: # if the left element is larger than the right 
                items[j], items[j+1] = items[j+1], items[j] # swap the left/right elements
    return ", ".join([item for item, ip in items]) # return the list of IPs as strings


def most_freq_ips2(logs: list[str]) -> str:
    '''get ips and freqs'''
    freq = {}
    for log in logs:
        ip = log.split()[0]
        freq[ip] = freq.get(ip, 0) + 1

    '''calculate max and created list of ips == max_count'''
    max_count = max(freq.values(), default = 0)
    # ip_max_val_list = []
    # for ip, count in freq.items():
    #     if count == max_val:
    #         ip_max_val_list.append(ip)
    ip_max_count_list = [ ip for ip, count in freq.items() if count == max_count ]

    '''sort list in order'''
    return ", ".join(sorted(ip_max_count_list))

# Test cases
inputs = [
    # [
    #     "192.168.1.2 - GET 2022-01-01",
    #     "192.168.1.3 - GET 2022-01-01",
    #     "192.168.1.1 - GET 2022-01-01",
    #     "192.168.1.4 - GET 2022-01-02",
    #     "192.168.1.1 - GET 2022-01-02",
    #     "192.168.1.2 - GET 2022-01-02",
    #     "192.168.1.3 - GET 2022-01-02",
    #     "192.168.1.4 - GET 2022-01-03",
    # ],
    # [
    #     *["192.168.1.1 - GET 2022-01-01"] * 1000,
    #     *["192.168.1.3 - GET 2022-01-01"] * 1001
    # ]
]