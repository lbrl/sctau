#include "SCTauTracker.h"

#include "papas/datatypes/Track.h"
#include "papas/utility/TRandom.h"

namespace papas {

SCTauTracker::SCTauTracker(double radius, double z, double x0, double lambdaI,
                       double resolution, double ptThreshold,
                       double etaThresholdLow, double ptProbabilityLow,
                       double etaThresholdHigh,
                       double ptProbabilityHigh) :
    Tracker(Layer::kTracker,
            VolumeCylinder(Layer::kTracker, radius, z),
            Material("void", x0, lambdaI)),
    m_resolution(resolution),
    m_ptThreshold(ptThreshold),
    m_etaThresholdLow(etaThresholdLow),
    m_ptProbabilityLow(ptProbabilityLow),
    m_etaThresholdHigh(etaThresholdHigh),
    m_ptProbabilityHigh(ptProbabilityHigh) {}

bool SCTauTracker::acceptance(const Track& track) const {
    bool accept;
    // double theta = track.p3().Theta() + M_PI/2;
    double theta = track.p3().Theta();
    if( theta > M_PI / 2 ){
        theta = M_PI - theta;
    }
    double thr = 0.975 / (1+exp(-(theta-0.6)/(0.7/10)));
    double dice = rootrandom::Random::uniform(0, 1);
    accept = thr > dice;
    return accept;
    /*
  double pt = track.p3().Perp();
  double eta = fabs(track.p3().Eta());
  bool accept = false;
  if (eta < m_etaThresholdLow && pt > m_ptThreshold) {                // (eta < 1.35 && pt > 0.5)
    accept = rootrandom::Random::uniform(0, 1) < m_ptProbabilityLow;  // 0.95
  } else if (eta < m_etaThresholdHigh && pt > m_ptThreshold) {
    accept = rootrandom::Random::uniform(0, 1) < m_ptProbabilityHigh;  // 0.9  }
    return accept;
  }
  return accept;
    */
}

double SCTauTracker::resolution(const Track& track) const {
    double pt = track.p3().Perp();
    return 0.0013 * pt + 0.0045;
    /*
  double pt = track.p3().Perp();
  (void)pt;             // suppress unused parameter warning
  return m_resolution;  // updated on 9/16 from 5e-3;
    */
}

}  // end namespace papas

