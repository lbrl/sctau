#! /usr/bin/env python

# import ROOT as r
import os
import sys
# import glob
# import math


def main():
    tmpl = 'SCTauFW/build/run /ceph/groups/sctau/fccsw/FCCSW/scripts/fccrun.py SCTauFW/Sim/SimPapas/options/papa_test/simple_papastool_'
    if 'test' in sys.argv:
        prts = ['gamma']
    else:
        prts = ['gamma', 'electron', 'muon', 'charged_pion', 'neutron']
    first = 'SCTauFW/build/run /ceph/groups/sctau/fccsw/FCCSW/scripts/fccrun.py'
    for prt in prts:
        line = '{}{}.py'.format(tmpl, prt)
        print line
        os.system(line)
        os.system('./afina.py -b save name afina_{}.png'.format(prt))


if __name__ == '__main__':
    main()
