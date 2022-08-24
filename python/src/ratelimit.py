import time
#fixed window limit
class UsageMonitor:
    def __init__(self):
        self.window_size = 60
        self.max_requests = 100000
        self.counter = 0
        self.request_store = dict()

    #add to request store
    #O(# of user ids in request store) and O(1) lookup
    def add_request(self, user_id, time_stamp):
        if user_id not in self.request_store:
            self.request_store[user_id] = dict()
        self.request_store[user_id][time_stamp] += 1

    def is_over_the_limit(self, user_id):
        current_time = int(time.time())
        start_time = current_time - self.window_size
        this_window_tot_reqs = self.get_current_window(start_time)
        if this_window_tot_reqs > self.max_requests:
            return True
        self.add_request(user_id, current_time)
        return False

    #O(1) for lookup and O(# of timestamps for this user_id)
    def get_current_window(self, user_id, start_time):
        if user_id not in self.request_store:
            return 0
        
        total_requests = 0
        timestamps = self.request_store[user_id]
        for timestamp, count in timestamps.items():
            if timestamp > start_time:
                total_requests += 1
            else:
                del timestamps[timestamp]
        return total_requests

