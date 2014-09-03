import redis
import time

class IPTable(object):
    

    def __init__(self):
        self.redis = redis.StrictRedis(host="localhost", port="6379")
        self.ip_addr_table = ['140.122.184.' + str(i) for i in xrange(211, 226)] 
        self.state_IDLE, self.state_BUSY, self.state_OTHER = "idle", "busy", "other"
        self.state_table = [self.state_IDLE, state_BUSY, state_OTHER]

    def modified_ip_record(self, ip_addr, name, state):
        if state in self.state_table:
            self.redis.hset(str(ip_addr), "name", name)
            self.redis.hset(str(ip_addr), "state", state)
            self.redis.hset(str(ip_addr), "time_stamp", time.time())


if __name__ == '__main__':
    ip_table = IPTable()
    print ip_table.state_IDLE
