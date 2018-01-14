#pragma once

#include "GaudiAlg/GaudiAlgorithm.h"
#include "FWCore/DataHandle.h"
#include "HepMC/GenEvent.h"

class HepMCDumper : public GaudiAlgorithm {
    friend class AlgFactory<HepMCDumper>;

    /// Handle for the HepMC to be read
    DataHandle<HepMC::GenEvent> m_hepmchandle{
              "HepMC", Gaudi::DataHandle::Reader, this};

 public:
    /// Constructor.
    HepMCDumper(const std::string& name, ISvcLocator* svcLoc);
    /// Initialize.
    virtual StatusCode initialize() final;
    /// Execute.
    virtual StatusCode execute() final;
    /// Finalize.
    virtual StatusCode finalize() final;
};

