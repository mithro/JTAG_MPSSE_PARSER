from pcapfile import savefile

def bulk_out_in(pack):
    pack = bytearray.fromhex(elem.packet);
    if(pack[10]==0x02):
        return 1;
    return 0;


testcap = open('jtag.pcap', 'rb')
capfile = savefile.load_savefile(testcap, verbose = True)
data = [];
temp = [];
row = 0;
column = 0;
for count, elem in enumerate(capfile.packets): 
    #print "Packet number " + str(count) + " capture_len is " + str(elem.capture_len) + "\r\n";
    temp_str = bytearray.fromhex(elem.packet)
    if(bulk_out_in(temp_str)):
        temp_str = temp_str[64: ];
        for elem1 in temp_str:
            temp.append(elem1);
        temp_str = ":".join(map(str, temp_str));
        #temp_str = temp_str[: -1];
        data.append(temp_str);
        temp_length = elem.capture_len;
        #print "Data is " + temp_str[64: ]
target = open('packet_data.txt', 'w');
target.truncate();
for packet in data: 
    target.write(packet);
    target.write("\r\n");
target.close();


x=[];

with open('packet_data.txt','rw') as file1:
    for line in file1:
        if line.strip():
            #file1.write(line)
            line=line.replace("\n","");
            line=line.replace("\r","");
            x.append(line);
x=':'.join(x);
target1 = open('py_helper.py', 'w');
target1.truncate();
target1.write("dat=\"");
target1.write(x);
target1.write("\";\r\n");
target1.write("dat=dat.split(':');\r\n");
target1.write("dat = [int(x, 10) for x in dat];\r\n");
target1.close();












