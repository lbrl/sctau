## Simple Papas Run
## Runs papas using as a sequence of tools
## The reconstructed particles are written to a ROOT file

#
#  To run PapasTools
#  > ./run gaudirun.py Sim/SimPapas/options/simple_papastool.py
#

import sys
sys.path.append('/home/vvorob/ctau/GaudiCTau/Sim/SimPapas/python')

from Gaudi.Configuration import *
from Configurables import ApplicationMgr, FCCDataSvc, PodioOutput
from GaudiKernel import SystemOfUnits as units

from Configurables import HepMCFileReader
from Configurables import ParticleGun, GenAlg

from Configurables import HepMCToEDMConverter

from Configurables import PodioOutput

from Configurables import ApplicationMgr, Gaudi__ParticlePropertySvc

# DATAPATH = '/home/vvorob/ctau/GaudiCTau/Generation/data'
DATAPATH = '/home/razuvaev/sctau5/SCTauFW/Generation/data'

particlePropertySvc = Gaudi__ParticlePropertySvc(
    "ParticlePropertySvc",
    ParticlePropertiesFile=DATAPATH+'/ParticleTable.txt')

### Example of pythia configuration file to generate events
#pythiafile="Test/TestGeneration/data/ee_ZH_Zmumu_Hbb.txt"

#### Data service
podioevent = FCCDataSvc("EventDataSvc")

### PYTHIA algorithm
#pythia8gentool = PythiaInterface("Pythia8Interface", Filename=pythiafile)
#pythia8gen = GenAlg("Pythia8", SignalProvider=pythia8gentool)
#pythia8gen.hepmc.Path = "hepmcevent"
# guntool = ParticleGun("SignalProvider", PdgCodes=[211, 22, 11, -13, 2112, 2212])
guntool = ParticleGun("SignalProvider", PdgCodes=[11])
gun = GenAlg('ParticleGunAlg', SignalProvider=guntool)
gun.hepmc.Path = "hepmcevent"

### Reads an HepMC::GenEvent from the data service and writes a collection of EDM Particles
hepmc_converter = HepMCToEDMConverter("Converter")
hepmc_converter.hepmc.Path="hepmcevent"
hepmc_converter.genparticles.Path="GenParticle"
hepmc_converter.genvertices.Path="Genvertex"

# from CMS_detector_cfg import detservice
from SCTau_detector_cfg import detservice
from papas_cfg import papasalg

#output fcc particles to root
# out = PodioOutput("out", OutputLevel=INFO)
out = PodioOutput("out", OutputLevel=DEBUG)
out.outputCommands = ["keep *"]

ApplicationMgr(
    ## all algorithms should be put here
    TopAlg=[gun, hepmc_converter, papasalg, out],
    EvtSel='NONE',
    ## number of events
    EvtMax=10000,
    ## all services should be put here
    ExtSvc = [podioevent, detservice, particlePropertySvc],
    OutputLevel = DEBUG,
    SvcOptMapping = ["Gaudi::ParticlePropertySvc/ParticlePropertySvc"]
)

