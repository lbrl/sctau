#pragma once

// Gaudi
#include "GaudiAlg/GaudiAlgorithm.h"
// FCCSW
#include "FWCore/DataHandle.h"
// papas
#include "papas/datatypes/Definitions.h"
#include "papas/datatypes/Event.h"

#include <string>

class IPapasTool;
class IPapasImportTool;
class IPapasExportTool;
class IPapasDetSvc;

namespace fcc {
    class MCParticleCollection;
}
namespace papas {
    class Detector;
}

/** @class PapasAlg Sim/SimPapasInterface/src/PapasAlg.h PapasAlg.h
 *
 *  Main algorithm that coordinate and runs papas simulation and
 *  reconstruction tools
 *  @author A.J. Robson
 */
class PapasAlg : public GaudiAlgorithm {
    friend class AlgFactory<PapasAlg>;
    /// papas detector
    /// Stores the linkages between papas objects
    /// (eg clusters, tracks, particles)
    std::shared_ptr<papas::Detector> m_spDetector;
    papas::Nodes m_history;
    /// vector of tools to be run
    std::vector<IPapasTool*> m_tools;
    /// import tool to be run
    IPapasImportTool* m_importTool;
    /// export tool to be run
    IPapasExportTool* m_exportTool;
    /// names of tools to be run
    std::vector<std::string> m_toolNames;
    /// name of import tool to be run
    std::string m_importToolName;
    /// name of export tool to be run
    std::string m_exportToolName;
    /// map to contain links between GenParticles and SimParticles
    std::unordered_map<papas::Identifier, int> m_particleLinks;
    /// the papas Event number, incremented for each event processed
    long m_eventno;
    ///<seed for random generator, default to 0 (no seed)
    Gaudi::Property<long> m_seed{this, "seed", 0, "random seed"};
    ///<seed for papas physics debug ouput default to "" no output
    Gaudi::Property<std::string> m_physicsDebugFile{this,
        "physicsDebugFile", "",
        "name of optional file to output physics info"};
    ///< Name of the papas detector service that is to be used
    Gaudi::Property<std::string> m_detServiceName{this,
        "detService", "", "name of detector service"};
 public:
    /// Constructor.
    PapasAlg(const std::string& name, ISvcLocator* svcLoc);
    /// Initialize.
    virtual StatusCode initialize() final;
    /// Execute: runs each of the tools on a PapasEvent.
    virtual StatusCode execute() final;
    /// Finalize.
    virtual StatusCode finalize() final;
};

