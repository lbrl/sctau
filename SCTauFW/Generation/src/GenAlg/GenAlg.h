#pragma once

#include "Generation/IHepMCMergeTool.h"
#include "Generation/IHepMCProviderTool.h"
#include "Generation/IVertexSmearingTool.h"

#include "FWCore/IPileUpTool.h"
#include "FWCore/DataHandle.h"

#include "GaudiAlg/GaudiAlgorithm.h"
#include "GaudiKernel/ToolHandle.h"

namespace HepMC {
    class GenEvent;
}

class GenAlg : public GaudiAlgorithm {
    friend class AlgFactory<GenAlg>;

    /// Tools to handle input from HepMC-file
    ToolHandle<IHepMCProviderTool> m_signalProvider{
               "ParticleGun/HepMCProviderTool", this};
    ToolHandle<IHepMCProviderTool> m_pileUpProvider{
               "ParticleGun/HepMCProviderTool", this};
    ToolHandle<IPileUpTool> m_pileUpTool{
               "ConstPileUp/PileUpTool", this};

    /// Tool to merge HepMC events
    ToolHandle<IHepMCMergeTool> m_HepMCMergeTool{
               "HepMCSimpleMerge/HepMCMergeTool", this};
    // Tool to smear vertices
    ToolHandle<IVertexSmearingTool> m_vertexSmearingTool{
               "FlatSmearVertex/VertexSmearingTool", this};
    // output handle for finished event
    DataHandle<HepMC::GenEvent> m_hepmchandle{
               "hepmc", Gaudi::DataHandle::Writer, this};

 public:
    /// Constructor
    GenAlg(const std::string& name, ISvcLocator* svcLoc);
    /// Initialize
    virtual StatusCode initialize() final;
    /// Execute
    virtual StatusCode execute() final;
    /// Finalize
    virtual StatusCode finalize() final;
};

