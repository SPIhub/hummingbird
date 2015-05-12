from numpy import sum, mean, min, max, std
import ipc
import numpy as np
from backend import ureg
from backend import Record

def printStatistics(detectors):
    for k,r in detectors.iteritems():
        v = r.data
        print "%s (%s): sum=%g mean=%g min=%g max=%g std=%g" % (k, r.unit.units,
                                                                sum(v), mean(v),
                                                                min(v), max(v),
                                                                std(v))

def getCentral4Asics(detector):
    """Returns the 4 centermost asics of the CsPAD detector as a one-dimensionsal stack.

    Args:
        :cspad(Record): A detector record
    Returns:
        Record central4Asics
    """
    central = []
    for i in range(4):
        central.append(detector.data[i*8+1,:,:194])
    return Record("central4Asics", np.hstack(central), detector.unit)
    
nrPhotons = {}    
def totalNrPhotons(detector, aduPhoton=1, aduThreshold=0):
    """Return an estimate for the total nr. of photons on the detector

    Args:
        :detector(Record): A detector record
    Kwargs:
        :aduPhoton(int):    ADU count per photon, default = 1
        :aduThreshold(int): only pixels above this threshold are valid, default = 0
    Returns:
        Record nrPhotons
    """
    data  = detector.data.flat
    valid = data > aduThreshold
    return Record("nrPhotons - " + detector.name , sum(data[valid]) / float(aduPhoton))

"""
import numpy
def slacH5ToCheetah(slacArr):
    out_arr = numpy.zeros((8*185, 4*388))
    for c in range(4):
        for r in range(8):
            slacPos = r + c*8
            (rB, rE) = (r*185, (r+1)*185)
            (cB, cE) = (c*388, (c+1)*388)
            out_arr[rB:rE, cB:cE] = (slacArr[slacPos])
    return out_arr


def cheetahToSlacH5(cheetahArr):
    out_arr = numpy.zeros((32, 185, 388))
    for c in range(4):
        for r in range(8):
            slacPos = r + c*8
            (rB, rE) = (r*185, (r+1)*185)
            (cB, cE) = (c*388, (c+1)*388)
            out_arr[slacPos] = cheetahArr[rB:rE, cB:cE]
    return out_arr
"""
