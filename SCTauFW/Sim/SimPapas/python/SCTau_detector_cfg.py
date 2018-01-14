## SCTau detector configuration for papas

from Gaudi.Configuration import *

from Configurables import SCTauFieldSvc, SCTauTrackerSvc, SCTauEcalSvc, SCTauHcalSvc
fieldsvc = SCTauFieldSvc("SCTauFieldSvc"); #todo add in remaining parameters
ecalsvc = SCTauEcalSvc("SCTauEcalSvc");
hcalsvc = SCTauHcalSvc("SCTauHcalsvc");
trackersvc = SCTauTrackerSvc("SCTauTrackerSvc");

from Configurables import SCTauDetSvc
detservice = SCTauDetSvc("PapasDetSvc",
                        ecalService = "SCTauEcalSvc",
                        hcalService = "SCTauHcalSvc",
                        trackerService = "SCTauTrackerSvc",
                        fieldService = "SCTauFieldSvc");


