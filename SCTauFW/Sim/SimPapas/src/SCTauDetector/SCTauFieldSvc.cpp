#include "SCTauFieldSvc.h"
#include "SCTauField.h"

DECLARE_SERVICE_FACTORY(SCTauFieldSvc)

SCTauFieldSvc::SCTauFieldSvc(const std::string& name, ISvcLocator* svc) :
    base_class(name, svc), m_field(nullptr) {}

StatusCode SCTauFieldSvc::initialize() {
    if (Service::initialize().isFailure()) {
        error() << "Unable to initialize Service()" << endmsg;
        return StatusCode::FAILURE;
    }
    m_field = std::make_shared<papas::SCTauField>(
        m_fieldMagnitude,
        m_fieldRadius,
        m_fieldZ);
    return StatusCode::SUCCESS;
}

StatusCode SCTauFieldSvc::finalize() { return StatusCode::SUCCESS; }

