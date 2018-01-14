#include "SCTauDetectorSvc.h"
#include "SCTauEcalSvc.h"
#include "SCTauFieldSvc.h"
#include "SCTauTrackerSvc.h"

#include "papas/detectors/cms/SCTau.h"

DECLARE_SERVICE_FACTORY(SCTauDetSvc)

SCTauDetSvc::SCTauDetSvc(const std::string& name, ISvcLocator* svc) :
    base_class(name, svc), m_detector(nullptr) {}

StatusCode SCTauDetSvc::initialize() {
    if (Service::initialize().isFailure()) {
        error() << "Unable to initialize Service()" << endmsg;
        return StatusCode::FAILURE;
    }
    SmartIF<IPapasFieldSvc> papasFieldSvc;
    SmartIF<IPapasCalorimeterSvc> papasEcalSvc;
//    SmartIF<IPapasCalorimeterSvc> papasHcalSvc;
    SmartIF<IPapasTrackerSvc> papasTrackerSvc;
    papasEcalSvc = service(m_ecalServiceName);
//    papasHcalSvc = service(m_hcalServiceName);
    papasTrackerSvc = service(m_trackerServiceName);
    papasFieldSvc = service(m_fieldServiceName);
    m_detector = std::make_shared<papas::SCTau>(
        papasEcalSvc->calorimeter(),
//        papasHcalSvc->calorimeter(),
        papasTrackerSvc->tracker(),
        papasFieldSvc->field(),
        m_electronAcceptanceMagnitude,
        m_electronAcceptanceEta,
        m_muonAcceptanceMagnitude,
        m_muonAcceptanceTheta,
        m_electronEnergyFactor,
        m_muonResolution
    );

    return StatusCode::SUCCESS;
}

StatusCode SCTauDetSvc::finalize() { return StatusCode::SUCCESS; }
