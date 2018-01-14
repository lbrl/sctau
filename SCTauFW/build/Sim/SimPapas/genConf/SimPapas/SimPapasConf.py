#Sat Jan 13 13:20:41 2018"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.DataObjectHandleBase import *
from GaudiKernel.Proxy.Configurable import *

class PapasAlg( ConfigurableAlgorithm ) :
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
    'seed' : 0, # int
    'physicsDebugFile' : '', # str
    'detService' : '', # str
    'tools' : [  ], # list
    'importTool' : '', # str
    'exportTool' : '', # str
  }
  _propertyDocDct = { 
    'detService' : """ name of detector service [PapasAlg] """,
    'physicsDebugFile' : """ name of optional file to output physics info [PapasAlg] """,
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
    'seed' : """ random seed [PapasAlg] """,
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
      super(PapasAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasAlg'
  pass # class PapasAlg

class PapasBuildBlocksTool( ConfigurableAlgTool ) :
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
    'ecalSubtype' : '', # str
    'hcalSubtype' : '', # str
    'trackSubtype' : '', # str
  }
  _propertyDocDct = { 
    'trackSubtype' : """ track subtype [PapasBuildBlocksTool] """,
    'hcalSubtype' : """ hcal subtype [PapasBuildBlocksTool] """,
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
    'ecalSubtype' : """ ecal subtype [PapasBuildBlocksTool] """,
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
      super(PapasBuildBlocksTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasBuildBlocksTool'
  pass # class PapasBuildBlocksTool

class PapasExportParticlesTool( ConfigurableAlgTool ) :
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
    'particleSubtype' : '', # str
    'recparticles' : DataObjectHandleBase("recparticles"), # DataObjectHandleBase
    'genparticles' : DataObjectHandleBase("MCparticles"), # DataObjectHandleBase
    'particleMCparticleAssociations' : DataObjectHandleBase("particleMCparticleAssociations"), # DataObjectHandleBase
  }
  _propertyDocDct = { 
    'particleSubtype' : """ particle subtype [PapasExportParticlesTool] """,
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
      super(PapasExportParticlesTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasExportParticlesTool'
  pass # class PapasExportParticlesTool

class PapasImportParticlesTool( ConfigurableAlgTool ) :
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
    'genparticles' : DataObjectHandleBase("MCparticles"), # DataObjectHandleBase
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
      super(PapasImportParticlesTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasImportParticlesTool'
  pass # class PapasImportParticlesTool

class PapasMergeClustersTool( ConfigurableAlgTool ) :
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
    'TypeAndSubtype' : '', # str
  }
  _propertyDocDct = { 
    'ContextService' : """ the name of Algorithm Context Service [GaudiTool] """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary [GaudiCommon<AlgTool>] """,
    'TypeAndSubtype' : """ type and subtype to merge [PapasMergeClustersTool] """,
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
      super(PapasMergeClustersTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasMergeClustersTool'
  pass # class PapasMergeClustersTool

class PapasPFReconstructorTool( ConfigurableAlgTool ) :
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
    'blockSubtype' : '', # str
  }
  _propertyDocDct = { 
    'blockSubtype' : """ block subtype [PapasPFReconstructorTool] """,
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
      super(PapasPFReconstructorTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasPFReconstructorTool'
  pass # class PapasPFReconstructorTool

class PapasSimplifyBlocksTool( ConfigurableAlgTool ) :
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
    'blockSubtype' : '', # str
  }
  _propertyDocDct = { 
    'blockSubtype' : """ block subtype [PapasSimplifyBlocksTool] """,
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
      super(PapasSimplifyBlocksTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasSimplifyBlocksTool'
  pass # class PapasSimplifyBlocksTool

class PapasSimulatorTool( ConfigurableAlgTool ) :
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
    'particleSubtype' : '', # str
  }
  _propertyDocDct = { 
    'particleSubtype' : """ particle subtype [PapasSimulatorTool] """,
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
      super(PapasSimulatorTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'SimPapas'
  def getType( self ):
      return 'PapasSimulatorTool'
  pass # class PapasSimulatorTool
