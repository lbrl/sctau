#include "GaudiEvtGen.h"

#include "GaudiKernel/MsgStream.h"

DECLARE_COMPONENT(GaudiEvtGen)

GaudiEvtGen::GaudiEvtGen(const std::string& name, ISvcLocator* ploc) :
    GaudiAlgorithm(name, ploc) {
        // Code here runs when the object gets created
}


StatusCode GaudiEvtGen::initialize() {
  StatusCode sc = Algorithm::initialize();  // must be executed first
  if(sc.isFailure() ) return sc;  // Initialize failed, propogate

  info() << "Hello World: Inilializing..." << endmsg;
  return StatusCode::SUCCESS;
}

StatusCode GaudiEvtGen::execute() {
  info() << "Hello World: Executing..." << endmsg;
  return StatusCode::SUCCESS;
}

StatusCode GaudiEvtGen::finalize() {
  info() << "Hello World: Finalizing..." << endmsg;
  return Algorithm::finalize();  // must be executed last
}

