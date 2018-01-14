/**
 * @file SCTauEcal.cc
 * @brief Implementation of the SCTau ECAL  */
#include "SCTauEcal.h"

#include "papas/datatypes/Cluster.h"
#include "papas/datatypes/Particle.h"
#include "papas/utility/TRandom.h"


// #include <iostream>
// #include <fstream>
// using namespace std;

namespace papas {

SCTauECAL::SCTauECAL(
    double innerRadius,
    double innerZ,
    double outerRadius,
                     double outerZ,
                     double x0,
                     double lambdaI,
                     double clusterSizePhoton,
                     double clusterSize,
                     double etaCrack,
                     double etaAcceptanceThreshold,
                     double ptAcceptanceThreshold,
                     double etaEndcapMin,
                     double etaEndcapMax,
                     const std::vector<double> emin,
                     const std::vector<std::vector<double>> eres,
                 const std::vector<std::vector<double>>
                     eresp)
    : Calorimeter(Layer::kEcal,
                  VolumeCylinder(Layer::kEcal, outerRadius, outerZ, innerRadius, innerZ),
                  Material("SCTau_ECAL", x0, lambdaI)),
      m_etaCrack(etaCrack),
      m_clusterSizePhoton(clusterSizePhoton),
      m_clusterSize(clusterSize),
      m_etaAcceptanceThreshold(etaAcceptanceThreshold),
      m_ptAcceptanceThreshold(ptAcceptanceThreshold),
      m_etaEndcapMin(etaEndcapMin),
      m_etaEndcapMax(etaEndcapMax),
      m_emin(emin),
      m_eres(eres),
      m_eresp(eresp) {}

double SCTauECAL::clusterSize(const Particle& ptc) const {
  int pdgid = abs(ptc.pdgId());
  if ((pdgid == 22) | (pdgid == 11))
    return m_clusterSizePhoton;
  else
    return m_clusterSize;
}

bool SCTauECAL::acceptance(const Cluster& cluster) const {
    // ofstream myfile;
    // myfile.open( "theta.dat", ios::app );
    // myfile << cluster.theta() << "\n";
    // myfile.close();
    // return cluster.energy() > .05;
    /*
    */
    double pi = 3.14159265359;
    // printf("theta %f\n", cluster.theta());
    double theta = cluster.theta() + pi/2;
    // double theta = M_PI/2 + cluster.theta();
    double energy = cluster.energy();
    double theta0 = 0.174533;
    if( theta < theta0 || theta > pi-theta0 ){
        // printf("theta=%f < %f || theta=%f > pi-%f=%f\n", theta, theta0, theta, theta0, (pi-theta0));
        return false;
    }
    if( energy < .05 ){
        return false;
    }
    double dice = rootrandom::Random::uniform(0, 1);
    double thr = 0.975;
    return thr > dice;
    /*
  double energy = cluster.energy();
  double eta = fabs(cluster.eta());
  if (eta < m_etaCrack)
    return energy > m_emin[kBarrel];
  else if (eta < m_etaAcceptanceThreshold)                                           // 2.93)
    return ((energy > m_emin[kEndCap]) & (cluster.pt() > m_ptAcceptanceThreshold));  // 0.2));
  else
    return false;
    */
}

double SCTauECAL::energyResolution(double energy, double eta) const {
    double s1 = 1.5e-3;
    double s2 = 5.e-4;
    double s3 = 1.55903e-01;
    double s4 = 7.14166e-03;
    return sqrt(pow(s1/pow(energy, .25), 2) +  pow(s2/sqrt(energy), 2) + pow(s3/energy, 2) + pow(s4, 2));
    /*
  int location = kBarrel;
  if (fabs(eta) > m_etaEndcapMin && fabs(eta) < m_etaEndcapMax) location = kEndCap;  // endcap
  // if (fabs(eta) > 1.479 && fabs(eta) < 3.0) location = kEndCap;
  double stoch = m_eres[location][0] / sqrt(energy);
  double noise = m_eres[location][1] / energy;
  double constant = m_eres[location][2];
  return sqrt(pow(stoch, 2) + pow(noise, 2) + pow(constant, 2));
    */
}

double SCTauECAL::energyResponse(double energy, double eta) const {
  int location = kBarrel;
  if (fabs(eta) > m_etaCrack) location = kEndCap;  // endcap
  // using fermi-dirac function : [0]/(1 + exp( (energy-[1]) /[2] );
  return m_eresp[location][0] / (1 + exp((energy - m_eresp[location][1]) / m_eresp[location][2]));
}

}  // end namespace papas
