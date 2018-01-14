#include "SCTauHcalSvc.h"

#include "papas/detectors/VolumeCylinder.h"
#include "SCTauHcal.h"

DECLARE_SERVICE_FACTORY(SCTauHcalSvc)

SCTauHcalSvc::SCTauHcalSvc(const std::string& name, ISvcLocator* svc) : base_class(name, svc), m_hcal(nullptr) {}

StatusCode SCTauHcalSvc::initialize() {
  if (Service::initialize().isFailure()) {
    error() << "Unable to initialize Service()" << endmsg;
    return StatusCode::FAILURE;
  }
  m_hcal = std::make_shared<papas::SCTauHCAL>(m_innerRadius,
                                            m_innerZ,
                                            m_outerRadius,
                                            m_outerZ,
                                            m_clusterSize,
                                            m_x0,
                                            m_lambdaI,
                                            m_etaCrack,
                                            m_eres,
                                            m_eresp,
                                            m_acceptanceParameters);
  return StatusCode::SUCCESS;
}

StatusCode SCTauHcalSvc::finalize() { return StatusCode::SUCCESS; }
