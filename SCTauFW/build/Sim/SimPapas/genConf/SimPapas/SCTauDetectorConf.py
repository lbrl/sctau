#Sun Jan 14 22:25:46 2018"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.Proxy.Configurable import *

class SCTauDetSvc( ConfigurableService ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'AuditServices' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'ecalService' : '', # str
    'hcalService' : '', # str
    'trackerService' : '', # str
    'fieldService' : '', # str
    'electronAcceptanceMagnitude' : 0.50000000, # float
    'electronAcceptanceEta' : 2.5000000, # float
    'muonAcceptanceMagnitude' : 0.50000000, # float
    'muonAcceptanceTheta' : 80.000000, # float
    'electronEnergyFactor' : 0.10000000, # float
    'muonResolution' : 0.020000000, # float
  }
  _propertyDocDct = { 
    'AuditStop' : """ trigger auditor on stop() [Service] """,
    'muonResolution' : """ Moun resolution [SCTauDetSvc] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Service] """,
    'trackerService' : """ Tracker service [SCTauDetSvc] """,
    'AuditRestart' : """ trigger auditor on restart() [Service] """,
    'electronAcceptanceMagnitude' : """ electron acceptance magnitude [SCTauDetSvc] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Service] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Service] """,
    'OutputLevel' : """ output level [Service] """,
    'AuditServices' : """ [[deprecated]] unused [Service] """,
    'ecalService' : """ Ecal service [SCTauDetSvc] """,
    'electronEnergyFactor' : """ electron energy factor [SCTauDetSvc] """,
    'AuditStart' : """ trigger auditor on start() [Service] """,
    'electronAcceptanceEta' : """ electron acceptance eta [SCTauDetSvc] """,
    'hcalService' : """ Hcal service [SCTauDetSvc] """,
    'fieldService' : """ Field service [SCTauDetSvc] """,
    'muonAcceptanceMagnitude' : """ muon acceptance magnitude [SCTauDetSvc] """,
    'muonAcceptanceTheta' : """ muon acceptance theta [SCTauDetSvc] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SCTauDetSvc, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SCTauDetector'
  def getType( self ):
      return 'SCTauDetSvc'
  pass # class SCTauDetSvc

class SCTauEcalSvc( ConfigurableService ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'AuditServices' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'innerRadius' : 1.0000000, # float
    'innerZ' : 1.1000000, # float
    'depth' : 1.5000000, # float
    'outerZ' : 2.0000000, # float
    'x0' : 14.000000, # float
    'lambdaI' : 0.27500000, # float
    'clusterSizePhoton' : 0.040000000, # float
    'clusterSize' : 0.070000000, # float
    'etaCrack' : 1.4790000, # float
    'etaAcceptance' : 2.9300000, # float
    'ptAcceptance' : 0.20000000, # float
    'etaEndcapMin' : 1.4790000, # float
    'etaEndcapMax' : 3.0000000, # float
    'emin' : [ 0.30000000 , 1.0000000 ], # list
    'eres' : [ [ 0.042216300 , 0.15590300 , 0.0071416600 ] , [ -0.20804800 , 0.32509700 , 0.0073424400 ] ], # list
    'eresp' : [ [ 1.0007100 , -9.0497300 , -2.4855400 ] , [ 0.99566500 , -3.3177400 , -2.1112300 ] ], # list
  }
  _propertyDocDct = { 
    'emin' : """ Ecal barrel and endcap emin [SCTauEcalSvc] """,
    'etaEndcapMin' : """ Ecal eta endcap min [SCTauEcalSvc] """,
    'ptAcceptance' : """ Ecal pt acceptance [SCTauEcalSvc] """,
    'eresp' : """ Ecal energy response parameters [SCTauEcalSvc] """,
    'etaAcceptance' : """ Ecal eta acceptance [SCTauEcalSvc] """,
    'etaCrack' : """ Ecal eta crack [SCTauEcalSvc] """,
    'AuditStop' : """ trigger auditor on stop() [Service] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Service] """,
    'eres' : """ Ecal energy resolution parameters [SCTauEcalSvc] """,
    'AuditStart' : """ trigger auditor on start() [Service] """,
    'AuditRestart' : """ trigger auditor on restart() [Service] """,
    'innerZ' : """ Ecal inner z [SCTauEcalSvc] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Service] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Service] """,
    'OutputLevel' : """ output level [Service] """,
    'AuditServices' : """ [[deprecated]] unused [Service] """,
    'innerRadius' : """ Ecal inner radius [SCTauEcalSvc] """,
    'clusterSizePhoton' : """ Ecal cluster size Photon [SCTauEcalSvc] """,
    'depth' : """ Ecal  outer radius [SCTauEcalSvc] """,
    'outerZ' : """ Ecal outer z [SCTauEcalSvc] """,
    'x0' : """ Ecal material x0 [SCTauEcalSvc] """,
    'etaEndcapMax' : """ Ecal eta endcap max [SCTauEcalSvc] """,
    'clusterSize' : """ Ecal cluster size [SCTauEcalSvc] """,
    'lambdaI' : """ Ecal material lambdaI [SCTauEcalSvc] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SCTauEcalSvc, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SCTauDetector'
  def getType( self ):
      return 'SCTauEcalSvc'
  pass # class SCTauEcalSvc

class SCTauFieldSvc( ConfigurableService ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'AuditServices' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'magnitude' : 3.8000000, # float
    'radius' : 2.9000000, # float
    'z' : 3.6000000, # float
  }
  _propertyDocDct = { 
    'magnitude' : """ Field magnitude [SCTauFieldSvc] """,
    'AuditServices' : """ [[deprecated]] unused [Service] """,
    'OutputLevel' : """ output level [Service] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Service] """,
    'radius' : """ Field  radius [SCTauFieldSvc] """,
    'AuditRestart' : """ trigger auditor on restart() [Service] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Service] """,
    'AuditStart' : """ trigger auditor on start() [Service] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Service] """,
    'z' : """ Field z [SCTauFieldSvc] """,
    'AuditStop' : """ trigger auditor on stop() [Service] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SCTauFieldSvc, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SCTauDetector'
  def getType( self ):
      return 'SCTauFieldSvc'
  pass # class SCTauFieldSvc

class SCTauHcalSvc( ConfigurableService ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'AuditServices' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'innerRadius' : 1.5250000, # float
    'innerZ' : 2.0250000, # float
    'outerRadius' : 1.5750000, # float
    'outerZ' : 2.0750000, # float
    'clusterSize' : 0.20000000, # float
    'x0' : 0.0000000, # float
    'lambdaI' : 0.17000000, # float
    'etaCrack' : 1.3000000, # float
    'eres' : [ [ 0.80620000 , 2.7530000 , 0.15010000 ] , [ 6.8030000e-06 , 6.6760000 , 0.17160000 ] ], # list
    'eresp' : [ [ 1.0360000 , 4.4520000 , -2.4580000 ] , [ 1.0710000 , 9.4710000 , -2.8230000 ] ], # list
    'acceptanceParameters' : [ 1.0000000 , 1.0000000 , -1.9381000 , -1.7533000 , 3.0000000 , 1.1000000 , 10.000000 , 1.0563400 , -0.16694300 , 0.010599700 , 0.80952200 , -9.9085500 , -5.3036600 , 5.0000000 , 7.0000000 ], # list
  }
  _propertyDocDct = { 
    'acceptanceParameters' : """ Hcal  acceptance parameters vector [SCTauHcalSvc] """,
    'eresp' : """ Hcal energy response parameters  [SCTauHcalSvc] """,
    'AuditStop' : """ trigger auditor on stop() [Service] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Service] """,
    'eres' : """ Hcal energy resolution parameters  [SCTauHcalSvc] """,
    'AuditStart' : """ trigger auditor on start() [Service] """,
    'AuditRestart' : """ trigger auditor on restart() [Service] """,
    'innerZ' : """ Hcal inner z [SCTauHcalSvc] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Service] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Service] """,
    'OutputLevel' : """ output level [Service] """,
    'AuditServices' : """ [[deprecated]] unused [Service] """,
    'innerRadius' : """ Hcal inner radius [SCTauHcalSvc] """,
    'outerZ' : """ Hcal outer Z [SCTauHcalSvc] """,
    'x0' : """ Hcal material x0 [SCTauHcalSvc] """,
    'clusterSize' : """ Hcal cluster size [SCTauHcalSvc] """,
    'lambdaI' : """ Hcal material lambdaI [SCTauHcalSvc] """,
    'outerRadius' : """ Hcal outer radius [SCTauHcalSvc] """,
    'etaCrack' : """ Hcal etaCrack [SCTauHcalSvc] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SCTauHcalSvc, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SCTauDetector'
  def getType( self ):
      return 'SCTauHcalSvc'
  pass # class SCTauHcalSvc

class SCTauTrackerSvc( ConfigurableService ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'AuditServices' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'radius' : 0.90000000, # float
    'z' : 1.0000000, # float
    'x0' : 0.0000000, # float
    'lambdaI' : 0.0000000, # float
    'resolution' : 0.011000000, # float
    'ptThreshold' : 0.50000000, # float
    'etaThresholdLow' : 1.3500000, # float
    'ptProbablityLow' : 0.95000000, # float
    'etaThresholdHigh' : 2.5000000, # float
    'ptProbablityHigh' : 0.90000000, # float
  }
  _propertyDocDct = { 
    'etaThresholdHigh' : """ Tracker upper pt threshold [SCTauTrackerSvc] """,
    'AuditStop' : """ trigger auditor on stop() [Service] """,
    'z' : """ Tracker cylinder z [SCTauTrackerSvc] """,
    'ptProbablityHigh' : """ Tracker upper pt probablility [SCTauTrackerSvc] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Service] """,
    'AuditStart' : """ trigger auditor on start() [Service] """,
    'AuditRestart' : """ trigger auditor on restart() [Service] """,
    'radius' : """ Tracker cylinder radius [SCTauTrackerSvc] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Service] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Service] """,
    'OutputLevel' : """ output level [Service] """,
    'AuditServices' : """ [[deprecated]] unused [Service] """,
    'x0' : """ tracker material x0 [SCTauTrackerSvc] """,
    'lambdaI' : """ Tracker material lambdaI [SCTauTrackerSvc] """,
    'etaThresholdLow' : """ Tracker lower pt threshold [SCTauTrackerSvc] """,
    'resolution' : """ Tracker resolution [SCTauTrackerSvc] """,
    'ptThreshold' : """ Tracker pt threshold [SCTauTrackerSvc] """,
    'ptProbablityLow' : """ Tracker lower pt probablility [SCTauTrackerSvc] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SCTauTrackerSvc, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SCTauDetector'
  def getType( self ):
      return 'SCTauTrackerSvc'
  pass # class SCTauTrackerSvc
