#pragma once

#include "SimPapas/IPapasTrackerSvc.h"

#include "GaudiKernel/MsgStream.h"
#include "GaudiKernel/Service.h"

/** @class SCTauTrackerSvc
 *
 *  This service provides the Papas SCTau tracker
 *  @author vvorob@inp.nsk.su
 */

namespace papas {
    class Tracker;
}

class SCTauTrackerSvc : public extends1<Service, IPapasTrackerSvc> {
    ///< Tracker
    std::shared_ptr<papas::Tracker> m_tracker;
    Gaudi::Property<double> m_radius{this,
        "radius", 0.9, "Tracker cylinder radius"};
    Gaudi::Property<double> m_z{this,
        "z", 1.0, "Tracker cylinder z"};
    Gaudi::Property<double> m_x0{this,
        "x0", 0.0, "tracker material x0"};
    Gaudi::Property<double> m_lambdaI{this,
        "lambdaI", 0.0, "Tracker material lambdaI"};
    Gaudi::Property<double> m_resolution{this,
        "resolution", 1.1e-2, "Tracker resolution"};
    Gaudi::Property<double> m_ptThreshold{this,
        "ptThreshold", 0.5, "Tracker pt threshold"};
    Gaudi::Property<double> m_ptThresholdLow{this,
        "etaThresholdLow", 1.35, "Tracker lower pt threshold"};
    Gaudi::Property<double> m_ptProbabilityLow{this,
        "ptProbablityLow", 0.95, "Tracker lower pt probablility"};
    Gaudi::Property<double> m_ptThresholdHigh{this,
        "etaThresholdHigh", 2.5, "Tracker upper pt threshold"};
    Gaudi::Property<double> m_ptProbabilityHigh{this,
        "ptProbablityHigh", 0.9, "Tracker upper pt probablility"};

 public:
    /// Default constructor
    SCTauTrackerSvc(const std::string& name, ISvcLocator* svc);
    /// Default destructor
    virtual ~SCTauTrackerSvc() = default;
    /// Initialize function
    virtual StatusCode initialize() override final;
    /// Finalize function
    virtual StatusCode finalize() override final;
    /// pointer to tracker
    virtual std::shared_ptr<papas::Tracker> tracker() const;
};

inline std::shared_ptr<papas::Tracker> SCTauTrackerSvc::tracker() const {
    return m_tracker;
}

