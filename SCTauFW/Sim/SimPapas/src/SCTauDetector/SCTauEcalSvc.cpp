#include "SCTauEcalSvc.h"
#include "SCTauEcal.h"

DECLARE_SERVICE_FACTORY(SCTauEcalSvc)

SCTauEcalSvc::SCTauEcalSvc(const std::string& name, ISvcLocator* svc) :
    base_class(name, svc), m_ecal(nullptr) {}

StatusCode SCTauEcalSvc::initialize() {
    if (Service::initialize().isFailure()) {
        error() << "Unable to initialize Service()" << endmsg;
        return StatusCode::FAILURE;
    }
    m_ecal = std::make_shared<papas::SCTauECAL>(
        m_innerRadius,
        m_innerZ,
        m_outerRadius,
        m_outerZ,
        m_x0,
        m_lambdaI,
        m_clusterSizePhoton,
        m_clusterSize,
        m_etaCrack,
        m_etaAcceptance,
        m_ptAcceptance,
        m_etaEndcapMin,
        m_etaEndcapMax,
        m_emin,
        m_eres,
        m_eresp);
    return StatusCode::SUCCESS;
}

StatusCode SCTauEcalSvc::finalize() { return StatusCode::SUCCESS; }

