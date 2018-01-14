#pragma once

#include "FWCore/DataHandle.h"
#include "GaudiAlg/GaudiAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
#include "HepMC/GenEvent.h"

#include "TH1F.h"

class HepMCHistograms : public GaudiAlgorithm {
    friend class AlgFactory<HepMCHistograms>;
    /// Handle for the HepMC to be read
    DataHandle<HepMC::GenEvent> m_hepmchandle{"HepMC",
               Gaudi::DataHandle::Reader, this};
    ///< THistogram service
    ITHistSvc* m_ths{nullptr};
    ///< histogram for pT of particles
    TH1F* m_pt{nullptr};
    ///< histogram for pseudorapidity of particles
    TH1F* m_eta{nullptr};
    ///< histogram for transversal IP
    TH1F* m_d0{nullptr};
    ///< histogram for longidudinal IP
    TH1F* m_z0{nullptr};

 public:
    /// Constructor.
    HepMCHistograms(const std::string& name, ISvcLocator* svcLoc);
    /// Initialize.
    virtual StatusCode initialize() final;
    /// Execute.
    virtual StatusCode execute() final;
    /// Finalize.
    virtual StatusCode finalize() final;
};

