# 二进制数字的全排列
def back_track(seq,path,seq):



def getjourney(journey):
    journey = list(map(int,journey.split()))
    vlen = journey[0]
    hlen = journey[1]
    k = journey[-1]
    seq = 'H'*hlen+'V'*vlen
    
    seq = list(seq)

    return seq

if __name__ == '__main__':
    journey = "2 2 1"
    print(getjourney(journey))