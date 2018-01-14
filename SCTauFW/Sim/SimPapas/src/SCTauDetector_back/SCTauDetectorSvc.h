#pragma once

#include "SimPapas/IPapasCalorimeterSvc.h"
#include "SimPapas/IPapasDetSvc.h"
#include "SimPapas/IPapasFieldSvc.h"
#include "SimPapas/IPapasTrackerSvc.h"

#include "GaudiKernel/MsgStream.h"
#include "GaudiKernel/Service.h"

/** @class SCTauDetSvc SCTauDetectorSvc.h
 *
 *  This service provides the Papas Super c-tau Detector
 *  @author vvorob@inp.nsk,su
 */

namespace papas {
    class Detector;
}

class SCTauDetSvc : public extends1<Service, IPapasDetSvc> {
    /// Detector
    std::shared_ptr<papas::Detector> m_detector;
    Gaudi::Property<std::string> m_ecalServiceName{this,
        "ecalService", "", "Ecal service"};
    Gaudi::Property<std::string> m_hcalServiceName{this,
        "hcalService", "", "Hcal service"};
    Gaudi::Property<std::string> m_trackerServiceName{this,
        "trackerService", "", "Tracker service"};
    Gaudi::Property<std::string> m_fieldServiceName{this,
        "fieldService", "", "Field service"};
    Gaudi::Property<double> m_electronAcceptanceMagnitude{this,
        "electronAcceptanceMagnitude", 5., "electron acceptance magnitude"};
    Gaudi::Property<double> m_electronAcceptanceEta{this,
        "electronAcceptanceEta", 2.5, "electron acceptance eta"};
    Gaudi::Property<double> m_muonAcceptanceMagnitude{this,
        "muonAcceptanceMagnitude", 7.5, "muon acceptance magnitude"};
    Gaudi::Property<double> m_muonAcceptanceTheta{this,
        "muonAcceptanceTheta", 80, "muon acceptance theta"};
    Gaudi::Property<double> m_electronEnergyFactor{this,
        "electronEnergyFactor", 0.1, "electron energy factor"};
    Gaudi::Property<double> m_muonResolution{this,
        "muonResolution", 0.02, "Moun resolution"};

 public:
    /// Default constructor
    SCTauDetSvc(const std::string& name, ISvcLocator* svc);
    /// Default destructor
    virtual ~SCTauDetSvc() = default;
    /// Initialize function
    virtual StatusCode initialize() override final;
    /// Finalize function
    virtual StatusCode finalize() override final;
    /// pointer to detector
    virtual std::shared_ptr<papas::Detector> detector() const;
};

inline std::shared_ptr<papas::Detector> SCTauDetSvc::detector() const {
    return m_detector;
}

