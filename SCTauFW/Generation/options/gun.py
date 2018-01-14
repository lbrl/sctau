from Gaudi.Configuration import *
from GaudiKernel import SystemOfUnits as units
from Configurables import ApplicationMgr, Gaudi__ParticlePropertySvc
from Configurables import HepMCDumper, ParticleGun
from Configurables import HepMCHistograms, FlatSmearVertex, ConstPileUp
from Configurables import GenAlg
from Configurables import HepMCFileWriter
from Configurables import THistSvc

from Configurables import HepMCToEDMConverter
from Configurables import PodioOutput

from Configurables import FCCDataSvc
## Data service
podioevent = FCCDataSvc("EventDataSvc")

dumper = HepMCDumper("Dumper")
dumper.hepmc.Path="hepmc"

writer = HepMCFileWriter("MyHepMCFileWriter")
writer.hepmc.Path="hepmc"

DATAPATH = '/ceph/groups/sctau/SCTauFW/Generation/data'

particlePropertySvc = Gaudi__ParticlePropertySvc(
    "ParticlePropertySvc",
    ParticlePropertiesFile=DATAPATH+'/ParticleTable.txt')

guntool = ParticleGun("SignalProvider", PdgCodes=[-211])
#guntool2 = ParticleGun("PileUpProvider", PdgCodes=[11])

smeartool = FlatSmearVertex("VertexSmearingTool")
smeartool.xVertexMin = -10*units.mm
smeartool.xVertexMax = 10*units.mm
smeartool.yVertexMin = -10*units.mm
smeartool.yVertexMax = 10*units.mm
smeartool.zVertexMin = -30*units.mm
smeartool.zVertexMax = 30*units.mm

#pileuptool = ConstPileUp("MyPileUpConfig", numPileUpEvents=1)

gun = GenAlg()
gun.hepmc.Path = "hepmc"

hepmc_converter = HepMCToEDMConverter("Converter")
hepmc_converter.hepmc.Path="hepmc"
hepmc_converter.genparticles.Path="allGenParticles"
hepmc_converter.genvertices.Path="allGenVertices"

histo = HepMCHistograms("GenHistograms")
histo.hepmc.Path="hepmc"

THistSvc().Output = ["rec DATAFILE='GenHistograms.root' TYP='ROOT' OPT='RECREATE'"]
THistSvc().PrintAll=True
THistSvc().AutoSave=True
THistSvc().AutoFlush=True
THistSvc().OutputLevel=VERBOSE

out = PodioOutput("out", filename = "output_gen.root")
out.outputCommands = ["keep *"]

ApplicationMgr(
    TopAlg=[gun, dumper, histo, writer, hepmc_converter, out],
    EvtSel='NONE',
    ExtSvc = [podioevent],
    EvtMax=10000,
    OutputLevel=VERBOSE,
    SvcOptMapping = ["Gaudi::ParticlePropertySvc/ParticlePropertySvc"]
)

