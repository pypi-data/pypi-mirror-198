from llfpga.register import Register
from typing import List
import ft4222

class KoraRpc:
    def __init__(self, bar: int, port="FT4222 A", timeout=5000):
        self.bar = bar
        dev = ft4222.openByDescription(port)
        dev.i2cMaster_Init(100000)
        dev.setTimeouts(timeout, timeout)
        self.dev = dev
        self.slave_addr = 11

    def read(self, reg: Register) -> int:
        address = reg.address - self.bar
        fetch_cmd = bytearray([address, reg.size])
        self.dev.i2cMaster_Write(
            self.slave_addr, fetch_cmd) 
        rb = self.dev.i2cMaster_ReadEx(
            self.slave_addr, ft4222.I2CMaster.Flag.START_AND_STOP, reg.size)
        return int.from_bytes(rb, "little")
    
    def fifo_read(self, target_to_host, read_count: int) -> List[int]:
        return [self.read(target_to_host.data) \
                for _ in range(read_count)]
    
    def fifo_write(self, host_to_target, data: List[int]):
        for val in data:
            self.write(host_to_target.data, val)
    
    def fifo_num_elements(self, fifo) -> int:
        return self.read(fifo.numelements)
    
    def write(self, reg: Register, val: int):
        address_and_cmd = reg.address - self.bar + 0x80
        val_bytes = int.to_bytes(val, reg.size, "little")
        write_cmd = int.to_bytes(address_and_cmd, 1, "little") + val_bytes
        self.dev.i2cMaster_Write(self.slave_addr, write_cmd)

    
if __name__ == "__main__":
    ll = KoraRpc(bar=0, port="FT4222 A", timeout=5000)
    test_reg = Register(address=1, size=2)
    ll.read(test_reg)
    ll.write(test_reg, 2)
