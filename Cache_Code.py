import math
import matplotlib.pyplot as plt
import numpy as np
import sys

class Cache():
    def __init__(self, cachesize, blocksize, ways):
        self.count=0
        self.cachesize = cachesize
        self.blocksize = blocksize
        self.ways=ways
    
        self.index_bits=math.ceil(math.log(int(self.cachesize*1024/(self.blocksize*self.ways)),2))
        self.cache = [[[0 for i in range(4)] for i in range(self.ways)] for j in range (int(self.cachesize*1024/(self.blocksize*self.ways)))]
        
        
    def index_match(self, address):
        b=int(math.log(self.blocksize, 2))
        if(b==0):
            index_bin=address[-self.index_bits:]
        else:
            index_bin=address[-self.index_bits-b:-b]
        index=int(index_bin, 2)

        if (index < int(self.cachesize*1024/(self.blocksize*self.ways))):
            return index
        else:
            return None

    def tag_match(self, address, index):
        b=int(math.log(self.blocksize,2))
        tag_bin=address[:-self.index_bits-b]
        tag=int(tag_bin, 2)

        if index==None:
            return False
        for inst in self.cache[index]:
            if (inst[0]==1 and inst[1]==tag):
                self.count+=1
                index2=self.cache[index].index(inst)
                temp=self.cache[index][index2]
                self.cache[index].remove(temp)
                self.cache[index].append(temp)
                for i in range(len(self.cache[index])):
                    self.cache[index][i][3]=i
                return True
        
        self.cache[index].pop(0)
        self.cache[index].append([1, tag, 0,3])
        for i in range(self.ways):
            self.cache[index][i][3]=i
        return False
    
    def clear(self):
        self.cache = [[[0 for i in range(4)] for i in range(self.ways)] for j in range (int(self.cachesize*1024/(self.blocksize*self.ways)))]

def main(lines,cache1, code):
    addresslist=[]
    for line in lines:
        l=line.split()
        hex_value = l[1]
        binary_value = format(int(hex_value, 16), '032b')
        addresslist.append(binary_value)

    for address in addresslist:
        index=cache1.index_match(address)
        hit=cache1.tag_match(address, index)
    print("Details of cache with user-given inputs:")
    print("Number of addresses:", len(addresslist))
    print("Hits:", cache1.count)
    print("Misses:", len(addresslist)-cache1.count)
    print("Hit Rate:", cache1.count/len(addresslist))
    print("Miss Rate:", (len(addresslist)-cache1.count)/len(addresslist))
    print("Hit/Miss Ratio:", cache1.count/(len(addresslist)-cache1.count))
    print("____________________________________________________________________________________")

    if (code == 1):
        xpoints = np.array([128, 256, 512, 1024, 2048, 4096])
        ypoints = np.array([])
        for i in range(len(xpoints)):
            cache2=Cache(xpoints[i], blocksize, ways)
            for address in addresslist:
                index=cache2.index_match(address)
                hit=cache2.tag_match(address, index)
            print(f"Details of cache with cache size = {xpoints[i]} KB:")
            print("Number of addresses:", len(addresslist))
            print("Hits:", cache2.count)
            print("Misses:", len(addresslist)-cache2.count)
            print("Hit Rate:", cache2.count/len(addresslist))
            print("Miss Rate:", (len(addresslist)-cache2.count)/len(addresslist))
            print("Hit/Miss Ratio:", cache2.count/(len(addresslist)-cache2.count))
            print("____________________________________________________________________________________")
            ypoints = np.append(ypoints, (len(addresslist)-cache2.count)/len(addresslist))
        return ypoints
    
    elif (code == 2):
        xpoints=np.array([1,2,4,8,16,32,64,128])
        ypoints = np.array([])
        for i in range(len(xpoints)):
            cache2=Cache(cachesize, xpoints[i], ways)
            for address in addresslist:
                index=cache2.index_match(address)
                hit=cache2.tag_match(address, index)
            print(f"Details of cache with block size = {xpoints[i]} Bytes:")
            print("Number of addresses:", len(addresslist))
            print("Hits:", cache2.count)
            print("Misses:", len(addresslist)-cache2.count)
            print("Hit Rate:", cache2.count/len(addresslist))
            print("Miss Rate:", (len(addresslist)-cache2.count)/len(addresslist))
            print("Hit/Miss Ratio:", cache2.count/(len(addresslist)-cache2.count))
            print("____________________________________________________________________________________")
            ypoints = np.append(ypoints, (len(addresslist)-cache2.count)/len(addresslist))
        return ypoints

    elif (code == 3):
        xpoints=np.array([1,2,4,8,16,32,64])
        ypoints = np.array([])
        for i in range(len(xpoints)):
            cache2=Cache(cachesize, blocksize, xpoints[i])
            for address in addresslist:
                index=cache2.index_match(address)
                hit=cache2.tag_match(address, index)
            print(f"Details of cache with {xpoints[i]} ways:")
            print("Number of addresses:", len(addresslist))
            print("Hits:", cache2.count)
            print("Misses:", len(addresslist)-cache2.count)
            print("Hit Rate:", cache2.count/len(addresslist))
            print("Miss Rate:", (len(addresslist)-cache2.count)/len(addresslist))
            print("Hit/Miss Ratio:", cache2.count/(len(addresslist)-cache2.count))
            print("____________________________________________________________________________________")
            ypoints = np.append(ypoints, cache2.count/len(addresslist))
        return ypoints

code=int(input("Code no: "))
cachesize=int(input("Enter the size of the cache in KB: "))
ways=int(input("Enter the number of ways: "))
blocksize=int(input("Enter the size of the blocks in bytes: "))
print("____________________________________________________________________________________")
cache1=Cache(cachesize, blocksize, ways)

if(code==1):
    xpoints=np.array([128, 256, 512, 1024, 2048, 4096])
    f = open("gcc.trace", "r")
    lines=f.readlines()
    print("File: gcc.trace")
    print("____________________________________________________________________________________")
    ypoint1=main(lines,cache1,1)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("gzip.trace", "r")
    lines=f.readlines()
    print("File: gzip.trace")
    print("____________________________________________________________________________________")
    ypoint2=main(lines,cache1,1)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("mcf.trace", "r")
    lines=f.readlines()
    print("File: mcf.trace")
    print("____________________________________________________________________________________")
    ypoint3=main(lines,cache1,1)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("swim.trace", "r")
    lines=f.readlines()
    print("File: swim.trace")
    print("____________________________________________________________________________________")
    ypoint4=main(lines,cache1,1)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("twolf.trace", "r")
    lines=f.readlines()
    print("File: twolf.trace")
    print("____________________________________________________________________________________")
    ypoint5=main(lines,cache1,1)
    cache1.count=0
    cache1.clear()
    f.close()

    datasets = [ypoint1, ypoint2, ypoint3, ypoint4, ypoint5]
    labels = ['gcc', 'gzip', 'mcf', 'swim', 'twolf']
    for ypoint, label in zip(datasets, labels):
        plt.figure() 
        plt.plot(xpoints, ypoint, marker='o')
        plt.xlabel("Cache Size")
        plt.ylabel("Miss Rate")
        plt.title(f"Miss Rate for {label} Trace")
        plt.legend([label])
        plt.show()

#labels1=[f'(128, {ypoint1[0]} )',f'(256, {ypoint1[1]} )',f'(512, {ypoint1[2]} )',f'(1024, {ypoint1[3]} )',f'(2048, {ypoint1[4]} )',f'(4096, {ypoint1[5]} )']

#    for i, label in enumerate(labels1):
#        plt.annotate(label, (xpoints[i], ypoint1[i]), textcoords="offset points", xytext=(0,10), ha='center')

   # plt.xlabel("Cache Size")
  #  plt.ylabel("Miss Rate")

    #plt.legend()
    #plt.show()

elif (code == 2 or code ==3):
    if code==2:
        xpoints=np.array([1,2,4,8,16,32,64,128])
    elif code==3:
        xpoints=np.array([1,2,4,8,16,32,64])

    f = open("gcc.trace", "r")
    lines=f.readlines()
    print("File: gcc.trace")
    print("____________________________________________________________________________________")
    ypoint1=main(lines,cache1,code)
    cache1.count=0
    cache1.clear()
    f.close()

    f=open("gzip.trace", "r")
    lines=f.readlines()
    print("File: gzip.trace")
    print("____________________________________________________________________________________")
    ypoint2=main(lines,cache1,code)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("mcf.trace", "r")
    lines=f.readlines()
    print("File: mcf.trace")
    print("____________________________________________________________________________________")
    ypoint3=main(lines,cache1,code)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("swim.trace", "r")
    lines=f.readlines()
    print("File: swim.trace")
    print("____________________________________________________________________________________")
    ypoint4=main(lines,cache1,code)
    cache1.count=0
    cache1.clear()
    f.close()

    f = open("twolf.trace", "r")
    lines=f.readlines()
    print("File: twolf.trace")
    print("____________________________________________________________________________________")
    ypoint5=main(lines,cache1,code)
    cache1.count=0
    cache1.clear()
    f.close()

    plt.plot(xpoints, ypoint1, color='r', label='gcc',marker='o')
    plt.plot(xpoints, ypoint2, color='g', label='gzip',marker='o')
    plt.plot(xpoints, ypoint3, color='b', label='mcf',marker='o')
    plt.plot(xpoints, ypoint4, color='m', label='swim',marker='o')
    plt.plot(xpoints, ypoint5, color='y', label='twolf',marker='o')

    if (code == 2):
        plt.xlabel("Block Size")
        plt.ylabel("Miss Rate")
    elif code==3:
        plt.xlabel("Ways")
        plt.ylabel("Hit Rate")

    plt.legend()
    plt.show()
else:
    print("Invalid Input")




