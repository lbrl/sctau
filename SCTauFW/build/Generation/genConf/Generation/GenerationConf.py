#Sat Jan 13 13:20:43 2018"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.DataObjectHandleBase import *
from GaudiKernel.Proxy.Configurable import *

class EDMToHepMCConverter( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'hepmc' : DataObjectHandleBase("hepmc"), # DataObjectHandleBase
    'genparticles' : DataObjectHandleBase("genParticles"), # DataObjectHandleBase
    'genvertices' : DataObjectHandleBase("genVertices"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'genparticles' : """ Generated particles collection (input) [unknown owner type] """,
    'hepmc' : """ HepMC event handle (output) [unknown owner type] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'genvertices' : """ Generated vertices collection (input) [unknown owner type] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(EDMToHepMCConverter, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'EDMToHepMCConverter'
  pass # class EDMToHepMCConverter

class FlatSmearVertex( ConfigurableAlgTool ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'MonitorService' : 'MonitorSvc', # str
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'xVertexMin' : 1.0000000, # float
    'yVertexMin' : 1.0000000, # float
    'zVertexMin' : 1.0000000, # float
    'xVertexMax' : 1.0000000, # float
    'yVertexMax' : 1.0000000, # float
    'zVertexMax' : 1.0000000, # float
  }
  _propertyDocDct = { 
    'zVertexMax' : """ Max value for z coordinate [FlatSmearVertex] """,
    'yVertexMax' : """ Max value for y coordinate [FlatSmearVertex] """,
    'xVertexMax' : """ Max value for x coordinate [FlatSmearVertex] """,
    'xVertexMin' : """ Min value for x coordinate [FlatSmearVertex] """,
    'yVertexMin' : """ Min value for y coordinate [FlatSmearVertex] """,
    'ContextService' : """ the name of Algorithm Context Service [GaudiTool] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'zVertexMin' : """ Min value for z coordinate [FlatSmearVertex] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<AlgTool>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
    'AuditInitialize' : """ trigger auditor on initialize() [AlgTool] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<AlgTool>] """,
    'AuditTools' : """ [[deprecated]] unused [AlgTool] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<AlgTool>] """,
    'MonitorService' : """ name to use for Monitor Service [AlgTool] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<AlgTool>] """,
    'AuditFinalize' : """ trigger auditor on finalize() [AlgTool] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'AuditStart' : """ trigger auditor on start() [AlgTool] """,
    'OutputLevel' : """ output level [AlgTool] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [AlgTool] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<AlgTool>] """,
    'AuditRestart' : """ trigger auditor on restart() [AlgTool] """,
    'AuditStop' : """ trigger auditor on stop() [AlgTool] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<AlgTool>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(FlatSmearVertex, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'FlatSmearVertex'
  pass # class FlatSmearVertex

class GaudiEvtGen( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
  }
  _propertyDocDct = { 
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(GaudiEvtGen, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'GaudiEvtGen'
  pass # class GaudiEvtGen

class GenAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'PileUpTool' : PrivateToolHandle('ConstPileUp/PileUpTool'), # GaudiHandle
    'VertexSmearingTool' : PrivateToolHandle('FlatSmearVertex/VertexSmearingTool'), # GaudiHandle
    'HepMCMergeTool' : PrivateToolHandle('HepMCSimpleMerge/HepMCMergeTool'), # GaudiHandle
    'SignalProvider' : PrivateToolHandle('ParticleGun/HepMCProviderTool'), # GaudiHandle
    'PileUpProvider' : PrivateToolHandle('ParticleGun/HepMCProviderTool'), # GaudiHandle
    'hepmc' : DataObjectHandleBase("hepmc"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'hepmc' : """ HepMC event handle (output) [unknown owner type] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(GenAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'GenAlg'
  pass # class GenAlg

class GenMerge( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'signalGenParticles' : DataObjectHandleBase("signalGenVertices"), # DataObjectHandleBase
    'signalGenVertices' : DataObjectHandleBase("signalGenParticles"), # DataObjectHandleBase
    'pileupGenParticles' : DataObjectHandleBase("pileupGenParticles"), # DataObjectHandleBase
    'pileupGenVertices' : DataObjectHandleBase("pileupGenVertices"), # DataObjectHandleBase
    'allGenParticles' : DataObjectHandleBase("allGenParticles"), # DataObjectHandleBase
    'allGenVertices' : DataObjectHandleBase("allGenVertices"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'allGenVertices' : """ Merged vertex collection (output) [unknown owner type] """,
    'pileupGenVertices' : """ Generated pileup vertex collection (input) [unknown owner type] """,
    'pileupGenParticles' : """ Generated pileup particle collection (input) [unknown owner type] """,
    'signalGenParticles' : """ Generated signal particle collection (input) [unknown owner type] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'allGenParticles' : """ Merged particle collection (output) [unknown owner type] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'signalGenVertices' : """ Generated signal vertex collection (input) [unknown owner type] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(GenMerge, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'GenMerge'
  pass # class GenMerge

class HepMCDumper( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'hepmc' : DataObjectHandleBase("HepMC"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'hepmc' : """ The HepMC event to dump [unknown owner type] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCDumper, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCDumper'
  pass # class HepMCDumper

class HepMCFileReader( ConfigurableAlgTool ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'MonitorService' : 'MonitorSvc', # str
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'Filename' : '', # str
  }
  _propertyDocDct = { 
    'ContextService' : """ the name of Algorithm Context Service [GaudiTool] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<AlgTool>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
    'AuditInitialize' : """ trigger auditor on initialize() [AlgTool] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<AlgTool>] """,
    'AuditTools' : """ [[deprecated]] unused [AlgTool] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<AlgTool>] """,
    'MonitorService' : """ name to use for Monitor Service [AlgTool] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<AlgTool>] """,
    'AuditFinalize' : """ trigger auditor on finalize() [AlgTool] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'AuditStart' : """ trigger auditor on start() [AlgTool] """,
    'OutputLevel' : """ output level [AlgTool] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [AlgTool] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<AlgTool>] """,
    'AuditRestart' : """ trigger auditor on restart() [AlgTool] """,
    'Filename' : """ Name of the HepMC file to read [HepMCFileReader] """,
    'AuditStop' : """ trigger auditor on stop() [AlgTool] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<AlgTool>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCFileReader, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCFileReader'
  pass # class HepMCFileReader

class HepMCFileWriter( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'Filename' : 'Output_HepMC.dat', # str
    'hepmc' : DataObjectHandleBase("HepMC"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'hepmc' : """ The HepMC event to write to text file (input) [unknown owner type] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'Filename' : """ Name of the HepMC file to write [HepMCFileWriter] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCFileWriter, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCFileWriter'
  pass # class HepMCFileWriter

class HepMCFullMerge( ConfigurableAlgTool ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'MonitorService' : 'MonitorSvc', # str
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
  }
  _propertyDocDct = { 
    'ContextService' : """ the name of Algorithm Context Service [GaudiTool] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<AlgTool>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
    'AuditInitialize' : """ trigger auditor on initialize() [AlgTool] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<AlgTool>] """,
    'AuditTools' : """ [[deprecated]] unused [AlgTool] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<AlgTool>] """,
    'MonitorService' : """ name to use for Monitor Service [AlgTool] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<AlgTool>] """,
    'AuditFinalize' : """ trigger auditor on finalize() [AlgTool] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'AuditStart' : """ trigger auditor on start() [AlgTool] """,
    'OutputLevel' : """ output level [AlgTool] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [AlgTool] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<AlgTool>] """,
    'AuditRestart' : """ trigger auditor on restart() [AlgTool] """,
    'AuditStop' : """ trigger auditor on stop() [AlgTool] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<AlgTool>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCFullMerge, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCFullMerge'
  pass # class HepMCFullMerge

class HepMCHistograms( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'hepmc' : DataObjectHandleBase("HepMC"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCHistograms, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCHistograms'
  pass # class HepMCHistograms

class HepMCSimpleMerge( ConfigurableAlgTool ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'MonitorService' : 'MonitorSvc', # str
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
  }
  _propertyDocDct = { 
    'ContextService' : """ the name of Algorithm Context Service [GaudiTool] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<AlgTool>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
    'AuditInitialize' : """ trigger auditor on initialize() [AlgTool] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<AlgTool>] """,
    'AuditTools' : """ [[deprecated]] unused [AlgTool] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<AlgTool>] """,
    'MonitorService' : """ name to use for Monitor Service [AlgTool] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<AlgTool>] """,
    'AuditFinalize' : """ trigger auditor on finalize() [AlgTool] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'AuditStart' : """ trigger auditor on start() [AlgTool] """,
    'OutputLevel' : """ output level [AlgTool] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [AlgTool] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<AlgTool>] """,
    'AuditRestart' : """ trigger auditor on restart() [AlgTool] """,
    'AuditStop' : """ trigger auditor on stop() [AlgTool] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<AlgTool>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCSimpleMerge, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCSimpleMerge'
  pass # class HepMCSimpleMerge

class HepMCToEDMConverter( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : True, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'IsIOBound' : False, # bool
    'FilterCircularDependencies' : True, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'VetoObjects' : [  ], # list
    'RequireObjects' : [  ], # list
    'hepmcStatusList' : [ 1 ], # list
    'hepmc' : DataObjectHandleBase("hepmc"), # DataObjectHandleBase
    'genparticles' : DataObjectHandleBase("genParticles"), # DataObjectHandleBase
    'genvertices' : DataObjectHandleBase("genVertices"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'genparticles' : """ Generated particles collection (output) [unknown owner type] """,
    'hepmcStatusList' : """ list of hepmc statuses to keep. An empty list means             all statuses will be kept [HepMCToEDMConverter] """,
    'hepmc' : """ HepMC event handle (input) [unknown owner type] """,
    'AuditStop' : """ trigger auditor on stop() [Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Algorithm] """,
    'RequireObjects' : """ execute only if one or more of these TES objects exist [GaudiAlgorithm] """,
    'AuditStart' : """ trigger auditor on start() [Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Algorithm] """,
    'AuditEndRun' : """ trigger auditor on endRun() [Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Algorithm] """,
    'genvertices' : """ Generated vertices collection (output) [unknown owner type] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Algorithm] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Algorithm] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<Algorithm>] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'OutputLevel' : """ output level [Algorithm] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'Enable' : """ should the algorithm be executed or not [Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Algorithm] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'AuditBeginRun' : """ trigger auditor on beginRun() [Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Algorithm] """,
    'IsIOBound' : """ if the algorithm is I/O-bound (in the broad sense of Von Neumann bottleneck) [Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Algorithm] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<Algorithm>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<Algorithm>] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<Algorithm>] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<Algorithm>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<Algorithm>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<Algorithm>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<Algorithm>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<Algorithm>] """,
    'VetoObjects' : """ skip execute if one or more of these TES objects exist [GaudiAlgorithm] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HepMCToEDMConverter, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'HepMCToEDMConverter'
  pass # class HepMCToEDMConverter

class ParticleGun( ConfigurableAlgTool ) :
  __slots__ = { 
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'OutputLevel' : 0, # int
    'MonitorService' : 'MonitorSvc', # str
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'MomentumMin' : 100.00000, # float
    'ThetaMin' : 0.0000000, # float
    'PhiMin' : 0.0000000, # float
    'MomentumMax' : 2000.0000, # float
    'ThetaMax' : 3.1415927, # float
    'PhiMax' : 6.2831853, # float
    'PdgCodes' : [ -211 ], # list
  }
  _propertyDocDct = { 
    'PhiMax' : """ Maximal phi [ParticleGun] """,
    'ThetaMax' : """ Maximal theta [ParticleGun] """,
    'MomentumMax' : """ Maximal momentum [ParticleGun] """,
    'PhiMin' : """ Minimal phi [ParticleGun] """,
    'MomentumMin' : """ Minimal momentum [ParticleGun] """,
    'ContextService' : """ the name of Algorithm Context Service [GaudiTool] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'UseEfficiencyRowFormat' : """ use the special format for printout of efficiency counters [GaudiCommon<AlgTool>] """,
    'EfficiencyRowFormat' : """ The format for "efficiency" row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'RootInTES' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
    'PdgCodes' : """ list of pdg codes to produce [ParticleGun] """,
    'AuditInitialize' : """ trigger auditor on initialize() [AlgTool] """,
    'TypePrint' : """ add the actual C++ component type into the messages [GaudiCommon<AlgTool>] """,
    'AuditTools' : """ [[deprecated]] unused [AlgTool] """,
    'StatPrint' : """ print the table of counters [GaudiCommon<AlgTool>] """,
    'MonitorService' : """ name to use for Monitor Service [AlgTool] """,
    'ExtraInputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'RegularRowFormat' : """ the format for regular row in the output Stat-table [GaudiCommon<AlgTool>] """,
    'StatTableHeader' : """ the header row for the output Stat-table [GaudiCommon<AlgTool>] """,
    'AuditFinalize' : """ trigger auditor on finalize() [AlgTool] """,
    'ExtraOutputs' : """ [[deprecated]] [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgTool,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ThetaMin' : """ Minimal theta [ParticleGun] """,
    'AuditStart' : """ trigger auditor on start() [AlgTool] """,
    'OutputLevel' : """ output level [AlgTool] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [AlgTool] """,
    'ErrorsPrint' : """ print the statistics of errors/warnings/exceptions [GaudiCommon<AlgTool>] """,
    'AuditRestart' : """ trigger auditor on restart() [AlgTool] """,
    'AuditStop' : """ trigger auditor on stop() [AlgTool] """,
    'PropertiesPrint' : """ print the properties of the component [GaudiCommon<AlgTool>] """,
    'Context' : """ note: overridden by parent settings [GaudiCommon<AlgTool>] """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ParticleGun, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'Generation'
  def getType( self ):
      return 'ParticleGun'
  pass # class ParticleGun
