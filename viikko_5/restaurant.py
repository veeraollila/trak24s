def find(a, d):
    
    sorted_events = sorted([(time, 'arrival') for time in a] + [(time, 'departure') for time in d])
 
    customers = 0
    longest_waiting_time = 0
    last_departure = None
 
    for aika, event_type in sorted_events:
        if event_type == 'arrival':
            
            if customers == 0 and last_departure is not None and aika > last_departure:
                longest_waiting_time = max(longest_waiting_time, aika - last_departure)
            customers += 1
            last_departure = None
        else:
            customers -= 1
            if customers == 0:
                last_departure = aika
 
    return longest_waiting_time
 
 
if __name__ == "__main__":
    print(find([1, 6], [2, 9])) # 4
    print(find([1, 2, 3], [2, 3, 4])) # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9])) # 1
    print(find([1, 10**9], [2, 10**9+1])) # 999999998