#pragma once

#include "FWCore/DataHandle.h"
#include "GaudiAlg/GaudiAlgorithm.h"
#include "HepMC/GenEvent.h"
#include "HepMC/Units.h"

namespace fcc {
    class MCParticleCollection;
    class GenVertexCollection;
}

class EDMToHepMCConverter : public GaudiAlgorithm {
    friend class AlgFactory<EDMToHepMCConverter>;

    /// Handle for the HepMC to be read
    DataHandle<HepMC::GenEvent> m_hepmchandle{"hepmc",
                       Gaudi::DataHandle::Writer, this};
    /// Handle for the genparticles to be written
    DataHandle<fcc::MCParticleCollection> m_genphandle{"genParticles",
                       Gaudi::DataHandle::Reader, this};
    /// Handle for the genvertices to be written
    DataHandle<fcc::GenVertexCollection> m_genvhandle{"genVertices",
                       Gaudi::DataHandle::Reader, this};
 public:
    /// Constructor.
    EDMToHepMCConverter(const std::string& name, ISvcLocator* svcLoc);
    /// Initialize.
    virtual StatusCode initialize() final;
    /// Execute.
    virtual StatusCode execute() final;
    /// Finalize.
    virtual StatusCode finalize() final;
};

