#pragma once

#include "HepMC/GenEvent.h"
#include "FWCore/DataHandle.h"
#include <GaudiAlg/GaudiAlgorithm.h>

class GaudiEvtGen : public GaudiAlgorithm {
    // Output
    DataHandle<HepMC::GenEvent> m_hepmchandle{"hepmc", Gaudi::DataHandle::Writer, this};

 public:
    /// Needs a constructor or delagating constructor
    GaudiEvtGen(const std::string& name, ISvcLocator* pSvcLocator); 
    
    /// Runs at algorithm initialization
    StatusCode initialize() override;
    
    /// This runs every event
    StatusCode execute() override;

    /// Any finalization goes here
    StatusCode finalize() override;
};

