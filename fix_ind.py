import pandas as pd
import numpy as np
import os

data_dir = 'C:\Users\Molly Babel\Documents\Martin\Accelerometer\Activity Recognition from Single Chest-Mounted Accelerometer'
# filenames are 1 to 15
data_files = [data_dir+os.path.sep+str(i)+'.csv' for i in range(1,16)]
# column names
col_names = ['ts','xa','ya','za','act']
# xyz motion columns
xyz = ['xa','ya','za']


#
# Helper functions
#


def do_fixes(fix):
    for f in fix:
        write_fixed_file(f)

def write_fixed_file(fix):
    index_num = fix[0]
    dat_file = data_files[index_num]
    segs = fix[1]
    print dat_file

    #read data file
    dat = pd.read_csv(dat_file, 
        names=col_names, 
        usecols=['act'])
    
    print 'index_num', index_num

    # create new action vector
    new_ind = []
    for s in segs:
        act,a,b = s
        #print act,a,b
        n_samp = b-a
        new_ind.extend([act]*n_samp)

    # append remainder of original if new_ind is shorter
    print len(dat.act)
    print len(new_ind)
    diff = len(dat.act) - len(new_ind)
    if diff > 0:
        print "appending original"
        new_ind.extend(dat.act[-diff:])
        print len(new_ind)
    else:
        print 'all samples accounted for'
    #print len(dat.act) - len(new_ind)


    new_file = dat_file[:-3]+'txt'
    print new_file
    with open(new_file, 'w') as f:
        for i in new_ind:
            f.write(str(i)+'\n')
    print







#dat_file 1
fix = []
# 0 is good
fix.append([0, 
    [[1, 0, 33676],
    [2, 33677, 34604], 
    [3, 34605, 39099], 
    [4, 39100, 65347]]])

fix.append([1,
[[1,  0,  46592],
[2,  46593, 50232],
[3,  50233, 61096],
[4,  61097,   83308],
[3,  83309,   92872],
[5,  92873,   96980],
[3,  96981,   99840]]])

fix.append([2,
[[1,0, 41673],
[2, 41674, 47788],
[3, 47789, 48616],
[4, 48617, 74568],
[3, 74569, 76752],
[5, 76753, 79456],
[3, 79457, 80444]]])

fix.append([3,
    [[1, 0, 33332],
    [2, 33333, 36348],
    [3, 36349, 45128],
    [4, 45129, 68016],
    [3, 68017, 75452],
    [5, 75453, 79144],
    [3, 79145, 86708],
    [6, 86709, 88764]]])

#index 4 is good
fix.append([4,
    [[1, 0, 30979],
     [2, 30980, 36349],
     [3, 36350, 42399],
     [4, 42400, 68949],
     [3, 68950, 73199],
     [5, 73200, 76199],
     [3, 76200, 79519],
     [6, 79520, 82399],
     [7, 82400, 159999]]])

fix.append([5,
    [[1, 0, 46540],
    [2, 46541, 49920],
    [3, 49921, 61140],
    [4, 61141, 83148],
    [3, 83149, 92820],
    [5, 92821, 96824],
    [3, 96825, 106548],
    [6, 106549, 109304]]])

fix.append([6,
    [[1, 0, 33540],
    [2, 33541, 36348],
    [3, 36349, 40340],
    [4, 40341, 46241],
    [0, 46242, 46500],
    [4, 46501, 67028],
    [3, 67029, 71136],
    [5, 71137, 74360],
    [3, 74361, 77324],
    [6, 77325, 80132]]]) 

fix.append([7,
    [[1, 0, 47638],
    [2, 47639, 50596],
    [3, 50597, 62620],
    [4, 62621, 83876],
    [3, 83877, 93600],
    [5, 93601, 97604],
    [3, 97605, 107484],
    [6, 107485, 112372]]])

fix.append([8,
    [[1,0, 38220],
    [2, 38221, 41236],
    [3, 41237, 45328],
    [4, 45329, 71864],
    [3, 71865, 76232],
    [5, 76233, 79404],
    [3, 79405, 79050],
    [6, 79051, 85124]]])

# figured out that all boundaries are off by the same amount
fix.append([9,
    [[1, 0, 47048],
 [2, 47049, 50483],
 [3, 50484, 61458],
 [4, 61459, 83607],
 [3, 83608, 93347],
 [5, 93348, 97237],
 [3, 97238, 100118],
 [6, 100119, 107567]]])

# off by 1664
fix.append([10,
    [[1, 0, 55832],
 [2, 55833, 58162],
 [3, 58163, 61212],
 [4, 61213, 78962],
 [3, 78963, 82577],
 [5, 82578, 85802],
 [3, 85803, 87912],
 [6, 87913, 88961],
 [7, 88962, 104448]]])

# 11 is good
fix.append([11, 
    [[1, 0, 48749],
     [2, 48750, 53089],
     [3, 53090, 57599],
     [4, 57600, 87329],
     [3, 87330, 90799],
     [5, 90800, 94449],
     [3, 94450, 98599],
     [6, 98600, 99799],
     [7, 99800, 114700]]])

# off by 1092
fix.append([12,
    [[1, 0, 19370],
 [2, 19371, 21020],
 [3, 21021, 24040],
 [4, 24041, 41690],
 [3, 41691, 45190],
 [5, 45191, 48590],
 [3, 48591, 50290],
 [6, 50291, 51491],
 [7, 51492, 67648]]])

#off by 780
fix.append([13, 
    [[1, 0, 53653],
 [2, 53654, 54158],
 [3, 54159, 59263],
 [4, 59264, 78064],
 [0, 87065, 78364],
 [4, 78365, 88078],
 [3, 88079, 92478],
 [5, 92479, 96098],
 [3, 96099, 99878],
 [6, 99879, 101378],
 [7, 101379, 116098]]])

 # off by 5616
fix.append([14,
    [[1, 0, 57214],
 [2, 57215, 61894],
 [3, 61895, 64104],
 [4, 64105, 78205],
 [0, 78206, 78805],
 [4, 78806, 81614],
 [3, 81615, 85214],
 [5, 85215, 88514],
 [3, 88515, 90614],
 [6, 90615, 91614],
 [7, 91615, 103498]]])

