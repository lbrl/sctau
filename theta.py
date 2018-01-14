#! /usr/bin/env python

import ROOT as r
# import os
import sys
# import glob
import math


def main():
    t = r.TTree('t', 't')
    t.ReadFile('theta.dat', 'theta/F')
    c1 = r.TCanvas('c1', 'c1', 300, 300)
    t.Draw('theta')
    c1.Update()
    raw_input()
    t.Draw('theta + pi/2')
    c1.Update()
    raw_input()


if __name__ == '__main__':
    main()
