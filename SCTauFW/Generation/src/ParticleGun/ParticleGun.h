#pragma once

#include <vector>
#include <string>

#include "GaudiAlg/GaudiTool.h"
#include "GaudiKernel/PhysicalConstants.h"
#include "GaudiKernel/RndmGenerators.h"
#include "GaudiKernel/SystemOfUnits.h"

#include "Generation/IParticleGunTool.h"

/** @class ParticleGun ParticleGun.h "ParticleGun.h"
 *
 *  Particle gun with given momentum range
 *
 *  @author Patrick Robbe (adaptation to tool structure)
 *  @author Benedikt Hegner (adaption for non LHCb use cases)
 *  @author Valentin Volkl (rewrite as tool)
 *  @date   2008-05-18
 *  @author Vitaly Vorobyev (integration to SCTF software)
 *  @date   2017-12-21
 */
class ParticleGun : public GaudiTool, virtual public IParticleGunTool {
    /// Minimum momentum (Set by options)
    Gaudi::Property<double> m_minMom{this,
           "MomentumMin", 0.1 * Gaudi::Units::GeV, "Minimal momentum"};
    /// Minimum theta angle (Set by options)
    Gaudi::Property<double> m_minTheta{this,
           "ThetaMin", 0. * Gaudi::Units::rad, "Minimal theta"};
    /// Minimum phi angle (Set by options)
    Gaudi::Property<double> m_minPhi{this,
           "PhiMin", 0. * Gaudi::Units::rad, "Minimal phi"};

    /// Maximum momentum (Set by options)
    Gaudi::Property<double> m_maxMom{this,
           "MomentumMax", 2.0 * Gaudi::Units::GeV, "Maximal momentum"};
    /// Maximum theta angle (Set by options)
    Gaudi::Property<double> m_maxTheta{this,
           "ThetaMax", Gaudi::Units::pi * Gaudi::Units::rad, "Maximal theta"};
    /// Maximum phi angle (Set by options)
    Gaudi::Property<double> m_maxPhi{this,
           "PhiMax", Gaudi::Units::twopi * Gaudi::Units::rad, "Maximal phi"};

    /// Momentum range
    double m_deltaMom;
    /// Theta range
    double m_deltaTheta;
    /// Phi range
    double m_deltaPhi;

    /// Pdg Codes of particles to generate (Set by options)
    Gaudi::Property<std::vector<int>> m_pdgCodes{this,
                    "PdgCodes", {-211}, "list of pdg codes to produce"};

    /// Masses of particles to generate (derived from PDG codes)
    std::vector<double> m_masses;

    /// Names of particles to generate (derived from PDG codes)
    std::vector<std::string> m_names;

    /// Flat random number generator
    Rndm::Numbers m_flatGenerator;

 public:
    /// Constructor
    ParticleGun(const std::string& type, const std::string& name,
                const IInterface* parent);
    /// Destructor
    virtual ~ParticleGun();
    /// Initialize particle gun parameters
    virtual StatusCode initialize() override;
    /// Generation of particles
    virtual void generateParticle(Gaudi::LorentzVector& momentum,
                                  Gaudi::LorentzVector& origin,
                                  int& pdgId) final;
    /// Print counters
    virtual void printCounters() override { ; };
    virtual StatusCode getNextEvent(HepMC::GenEvent&) final;
};

