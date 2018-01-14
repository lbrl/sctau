#include "SCTauTrackerSvc.h"
#include "papas/detectors/VolumeCylinder.h"
#include "papas/detectors/cms/SCTauTracker.h"

DECLARE_SERVICE_FACTORY(SCTauTrackerSvc)

SCTauTrackerSvc::SCTauTrackerSvc(const std::string& name, ISvcLocator* svc) :
    base_class(name, svc), m_tracker(nullptr) {}

StatusCode SCTauTrackerSvc::initialize() {
    if (Service::initialize().isFailure()) {
        error() << "Unable to initialize Service()" << endmsg;
        return StatusCode::FAILURE;
    }
    m_tracker = std::make_shared<papas::SCTauTracker>(
        m_radius,
        m_z,
        m_x0,
        m_lambdaI,
        m_resolution,
        m_ptThreshold,
        m_ptThresholdLow,
        m_ptProbabilityLow,
        m_ptThresholdHigh,
        m_ptProbabilityHigh);
    return StatusCode::SUCCESS;
}

StatusCode SCTauTrackerSvc::finalize() { return StatusCode::SUCCESS; }

