import pypot.dynamixel
ports = pypot.dynamixel.get_available_ports()
if not ports:
 raise IOError('no port found')
print(ports[0])
dxl_io1 = pypot.dynamixel.DxlIO(ports[0],baudrate=1000000,use_sync_read=False)#upper
print(dxl_io1.scan(range(60)))
print (ports[1])
dxl_io2 = pypot.dynamixel.DxlIO(ports[1],baudrate=1000000,use_sync_read=False)#lower
print(dxl_io2.scan(range(60)))