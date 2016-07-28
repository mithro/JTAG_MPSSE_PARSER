from py_helper import *
index = 0;
bit_clock = 0;
count0x4b=0;
count0x1b=0;
count0x39=0;
count0x3b=0;
count0x81=0;
count0x87=0;

def func0x4b():
    global count0x4b;
    count0x4b+=1;
    global index;
    global bit_clock;
    print "Command is :"+str(dat[index])+" "+str(dat[index+1])+" "+str(dat[index+2]);
    bit_clock = bit_clock + dat[index+1]+1;
    index=index+ 2;
def func0x1b():
    global count0x1b;
    global bit_clock;
    count0x1b+=1;
    global index;
    print "Command is :"+str(dat[index])+" "+str(dat[index+1])+" "+str(dat[index+2]);
    bit_clock = bit_clock + dat[index+1]+1;
    index=index+ 2;
def func0x39():
    global count0x39;
    global bit_clock;
    count0x39+=1;
    global index;
    length=dat[index+1]+dat[index+2]*256+1;
    print "Length "+ str(length);
    index=index+length+2;
    bit_clock = bit_clock + length;
    print "Command is 39 "
def func0x3b():
    global count0x3b;
    global bit_clock;
    count0x3b+=1;
    global index;
    print "Command is :"+str(dat[index])+" "+str(dat[index+1])+" "+str(dat[index+2]);
    bit_clock = bit_clock + dat[index+1]+1;
    index=index+ 2;
def func0x81():
    global count0x81;
    count0x81+=1;
    global index;
    print "Command is :"+str(dat[index]);
    index=index+ 0;
def func0x87():
    global count0x87;
    count0x87+=1;
    global index;
    print "Command is :"+str(dat[index]);
    index=index+ 0;


options={
0x4b :func0x4b,
0x1b :func0x1b,
0x39 :func0x39,
0x3b :func0x3b,
0x81 :func0x81,
0x87 :func0x87
};
#options[75]();

while index < len(dat):
    curr_command = dat[index];
    print("Index is "+ str(index)+" command is "+str(curr_command))
    print("Bit count is "+str(bit_clock))
    options[(curr_command)]();
    index += 1
    #print '\r\n'
