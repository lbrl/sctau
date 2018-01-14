
#pragma once

#include "GaudiAlg/GaudiTool.h"
#include "Generation/IHepMCProviderTool.h"

#include "HepMC/GenEvent.h"
#include "HepMC/IO_GenEvent.h"

class HepMCFileReader : public GaudiTool, virtual public IHepMCProviderTool {
    void close();
    Gaudi::Property<std::string> m_filename{this,
                 "Filename", "", "Name of the HepMC file to read"};
    std::unique_ptr<HepMC::IO_GenEvent> m_file;

 public:
    HepMCFileReader(const std::string& type,
                    const std::string& name, const IInterface* parent);
    virtual ~HepMCFileReader();  ///< Destructor
    virtual StatusCode initialize() override;
    virtual StatusCode finalize() override;

    /// Wrapper for HepMC's fill_next_event() --
    ///  as in the hepmc original, the user is responsible
    ///  for the deletion of the event returned from this function
    virtual StatusCode getNextEvent(HepMC::GenEvent& event) override;
    /// Wrapper for HepMC file io.
};

