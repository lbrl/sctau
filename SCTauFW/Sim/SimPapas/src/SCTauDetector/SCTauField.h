#pragma once

#include "papas/detectors/Field.h"

namespace papas {

/// SCTau specific implementation of Detector Field element
///
class SCTauField : public Field {
 public:
    /** Constructor
     * @param[in] magnitude field strength
     * @param[in] radius field cylinder radius
     * @param[in] z field cylinder z
     * @param[in] x0 field material X0
     * @param[in] lambdaI field material lambdaI
     */
    SCTauField(double magnitude = 1.0, double radius = 2.5, double z = 3.0);
};

}  // end namespace papas

