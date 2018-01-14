#! /usr/bin/env python

import ROOT as r
# import os
import sys
# import glob
import math


def tuneh1(h, lc=r.kBlack, lw=1):
    if lc != -1:
        print 'Set line colour.'
        h.SetLineColor(lc)
    if lw != -1:
        print 'Set line width.'
        h.SetLineWidth(lw)

def geth1(t, sel, cut=''):
    n = t.Draw(sel, cut, 'goff')
    name = sel.split('>>')[-1].split('(')[0]
    name = name.replace(' ', '')
    print 'Histogram name is {}.'.format(name)
    h = r.gDirectory.Get(name)
    return h


def main():
    Finname = 'output.root'
    Fin = r.TFile(Finname)
    t = Fin.Get('events')
    print '{} entries in the tree.'.format(t.GetEntries())
    ################
    massi = 'GenParticle.core.p4.mass'
    massf = 'RecParticle.core.p4.mass'
    pdgidi = 'GenParticle.core.pdgId'
    pdgidf = 'RecParticle.core.pdgId'
    pxi = 'GenParticle.core.p4.px'
    pyi = 'GenParticle.core.p4.py'
    pzi = 'GenParticle.core.p4.pz'
    pxf = 'RecParticle.core.p4.px'
    pyf = 'RecParticle.core.p4.py'
    pzf = 'RecParticle.core.p4.pz'
    pti = '({}**2+{}**2)**.5'.format(pxi, pyi)
    ptf = '({}**2+{}**2)**.5'.format(pxf, pyf)
    pi = '(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5'
    pf = '(RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5'
    thetai = 'acos(GenParticle.core.p4.pz / (GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5)'
    thetaf = 'acos(RecParticle.core.p4.pz / (RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5)'
    ################
    t.Draw('{} >> hpi(100,0,5.0)'.format(pi),
            '',# 'GenParticle.core.pdgId==-211',
            'goff')
    hpi = r.gDirectory.Get('hpi')
    tuneh1(hpi, lc=r.kRed, lw=2)
    ########
    t.Draw('{} >> hpf(100,0,5.0)'.format(pf),
            '',# 'GenParticle.core.pdgId==-211',
            'goff')
    hpf = r.gDirectory.Get('hpf')
    tuneh1(hpf, lc=r.kBlue, lw=2)
    ########
    hthetai = geth1(t, '{} >> hthetai(100,0,{})'.format(thetai, math.pi), '')
    tuneh1(hthetai, lc=r.kRed, lw=2)
    ########
    hthetaf = geth1(t, '{} >> hthetaf(100,0,{})'.format(thetaf, math.pi), '')
    tuneh1(hthetaf, lc=r.kBlue, lw=2)
    ########
    h2pxpyi = geth1(t, '{} : {} >> h2pxpyi(100,-5,5,100,-5,5)'.format(pyi, pxi), '')
    h2pxpyf = geth1(t, '{} : {} >> h2pxpyf(100,-5,5,100,-5,5)'.format(pyf, pxf), '')
    ########
    h2ptpzi = geth1(t, '{} : {} >> h2ptpzi(100,-5,5,100,-5,5)'.format(pti, pzi), '')
    h2ptpzf = geth1(t, '{} : {} >> h2ptpzf(100,-5,5,100,-5,5)'.format(ptf, pzf), '')
    ########
    h2dp = geth1(t, '100*({}-{})/{} : {} >> h2dp(100,0,5,100,-5,5)'.format(pf, pi, pi, pi))
    h2dp_wide = geth1(t, '100*({}-{})/{} : {} >> h2dp_wide(100,0,5,100,-50,50)'.format(pf, pi, pi, pi))
    ########
    h2dp_th = geth1(t, '100*({}-{})/{} : {} >> h2dp_th(100,0,{},100,-5,5)'.format(pf, pi, pi, thetai, math.pi))
    h2dp_th_wide = geth1(t, '100*({}-{})/{} : {} >> h2dp_th_wide(100,0,{},100,-50,50)'.format(pf, pi, pi, thetai, math.pi))
    ########
    hpdgidi = geth1(t, '{} >> hpdgidi(5000,-2500,2500)'.format(pdgidi), '')
    tuneh1(hpdgidi, lc=r.kRed, lw=2)
    hpdgidf = geth1(t, '{} >> hpdgidf(5000,-2500,2500)'.format(pdgidf), '')
    tuneh1(hpdgidf, lc=r.kBlue, lw=2)
    ########
    hmassi = geth1(t, '{} >> hmassi(1e4,0,2)'.format(massi), '')
    tuneh1(hmassi, lc=r.kRed, lw=2)
    hmassf = geth1(t, '{} >> hmassf(1e4,0,2)'.format(massf), '')
    tuneh1(hmassf, lc=r.kBlue, lw=2)
    ################
    if '-b' in sys.argv:
        wx, wy = 600, 600
    else:
        wx, wy = 250, 250
    c1 = r.TCanvas('c1', 'c1', wx*4, wy*3)
    lat = r.TLatex()
    lat.SetTextFont(12)
    lat.SetTextSize(.04)
    c1.Divide(4, 3)
    ########
    c1.cd(1)
    hpi.Draw()
    hpf.Draw('same')
    hpi.GetXaxis().SetTitle(r'Momentum, GeV/c')
    lat.SetTextColor(r.kRed)
    lat.DrawLatexNDC(.15, .9, 'Initial')
    lat.SetTextColor(r.kBlue)
    lat.DrawLatexNDC(.55, .9, 'Final')
    ########
    c1.cd(2)
    hthetai.Draw()
    hthetai.GetXaxis().SetTitle(r'Polar angle #theta')
    hthetai.GetXaxis().SetRangeUser(0, hthetai.GetMaximum()*1.05)
    hthetaf.Draw('same')
    lat.SetTextColor(r.kRed)
    lat.DrawLatexNDC(.15, .9, 'Initial')
    lat.SetTextColor(r.kBlue)
    lat.DrawLatexNDC(.55, .9, 'Final')
    ########
    c1.cd(3)
    h2pxpyi.Draw('colz')
    h2pxpyi.GetXaxis().SetTitle(r'Initial X momentum p_{x}, GeV/c')
    h2pxpyi.GetYaxis().SetTitle(r'Initial Y momentum p_{y}, GeV/c')
    ########
    c1.cd(4)
    h2pxpyf.Draw('colz')
    h2pxpyf.GetXaxis().SetTitle(r'Final X momentum p_{x}, GeV/c')
    h2pxpyf.GetYaxis().SetTitle(r'Final Y momentum p_{y}, GeV/c')
    ########
    c1.cd(5)
    h2ptpzi.Draw('colz')
    h2ptpzi.GetXaxis().SetTitle(r'Initial Z momentum p_{z}, GeV/c')
    h2ptpzi.GetYaxis().SetTitle(r'Initial transverse momentum p_{T}, GeV/c')
    ########
    c1.cd(6)
    h2ptpzf.Draw('colz')
    h2ptpzf.GetXaxis().SetTitle(r'Final Z momentum p_{z}, GeV/c')
    h2ptpzf.GetYaxis().SetTitle(r'Final transverse momentum p_{T}, GeV/c')
    ########
    c1.cd(7)
    h2dp.Draw('colz')
    h2dp.GetXaxis().SetTitle('Initial momentum, GeV/c')
    h2dp.GetYaxis().SetTitle(r'(p_{f}-p_{i})/p_{i}, %')
    ########
    c1.cd(8)
    h2dp_wide.Draw('colz')
    h2dp_wide.GetXaxis().SetTitle('Initial momentum, GeV/c')
    h2dp_wide.GetYaxis().SetTitle(r'(p_{f}-p_{i})/p_{i}, %')
    ########
    c1.cd(9)
    h2dp_th.Draw('colz')
    h2dp_th.GetXaxis().SetTitle('Initial polar angle #theta, GeV/c')
    h2dp_th.GetYaxis().SetTitle(r'(p_{f}-p_{i})/p_{i}, %')
    ########
    c1.cd(10)
    h2dp_th_wide.Draw('colz')
    h2dp_th_wide.GetXaxis().SetTitle('Initial polar angle #theta, GeV/c')
    h2dp_th_wide.GetYaxis().SetTitle(r'(p_{f}-p_{i})/p_{i}, %')
    ########
    c1.cd(11)
    hpdgidi.Draw()
    hpdgidf.Draw('same')
    hpdgidi.GetXaxis().SetTitle(r'Particle ID')
    lat.SetTextColor(r.kRed)
    lat.DrawLatexNDC(.15, .9, 'Initial')
    lat.SetTextAngle(90)
    for i, x in enumerate(hpdgidi):
        if x > 0:
            bcen = hpdgidi.GetBinCenter(i)
            lat.DrawLatex(bcen, x, '{}'.format(int(bcen-.5)))
    lat.SetTextAngle(0)
    lat.SetTextColor(r.kBlue)
    lat.DrawLatexNDC(.55, .9, 'Final')
    lat.SetTextAngle(90)
    for i, x in enumerate(hpdgidf):
        if x > 0:
            bcen = hpdgidf.GetBinCenter(i)
            lat.DrawLatex(bcen, x, '{}'.format(int(bcen-.5)))
    lat.SetTextAngle(0)
    ########
    c1.cd(12)
    hmassi.Draw()
    hmassf.Draw('same')
    hmassi.GetXaxis().SetTitle(r'Mass, GeV/c^{2}')
    lat.SetTextColor(r.kRed)
    lat.DrawLatexNDC(.15, .9, 'Initial')
    lat.SetTextColor(r.kBlue)
    lat.DrawLatexNDC(.55, .9, 'Final')
    r.gPad.SetLogx()
    ########
    c1.cd()
    c1.Update()
    ################
    if not '-b' in sys.argv:
        raw_input()
    ################
    if 'save' in sys.argv:
        name = 'afina.png'
        for i, arg in enumerate(sys.argv):
            if arg == 'name':
                name = sys.argv[i+1]
        c1.SaveAs(name)


if __name__ == '__main__':
    main()
