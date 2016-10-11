import sys

import odbAccess as oa
import numpy as np
import numpy.testing

DATA = [('E1IP1_', 'Element PART-1-1.1 Int Point 1', ),
        ('E2IP1_', 'Element PART-1-1.2 Int Point 1', ),
        ('N3_', 'Node PART-1-1.3', ),
        ('N4_', 'Node PART-1-1.4', ),
        ('N5_', 'Node PART-1-1.5', ),
        ('N6_', 'Node PART-1-1.6', ),
       ]

def main():
    path = sys.argv[1]

    dbpath = path + '.odb'
    savepath = path + '.npz'

    odb = oa.openOdb(dbpath, readOnly=True)

    print '-'*60
    print 'name:', odb.name
    print 'analysisTitle:', odb.analysisTitle
    print 'creationTime:', odb.jobData.creationTime

    step = odb.steps['TRACTION']

    print 'step name:', step.name
    print 'step procedure:', step.procedure
    print 'step description:', step.description
    print 'step domain:', step.domain
    print 'step frames: %d' % (len(step.frames), )

    t = np.fromiter((i.frameValue for i in odb.steps['TRACTION'].frames),
                    dtype=np.float)

    res = {}
    for label, hreg, in DATA:
        houts = step.historyRegions[hreg].historyOutputs
        for key in houts.keys():
            t1, v = np.asarray(houts[key].data).T
            np.testing.assert_array_equal(t, t1)
            res[label+key] = v

    print 'saving %s to %s' % (sorted(res.keys()), savepath)
    np.savez(savepath, **res)
    print '-'*60

if __name__ == '__main__':
    main()
