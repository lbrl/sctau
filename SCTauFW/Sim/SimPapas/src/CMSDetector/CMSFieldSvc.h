#pragma once

#include "SimPapas/IPapasFieldSvc.h"

#include "GaudiKernel/MsgStream.h"
#include "GaudiKernel/Service.h"

/** @class CMSFieldSvc CMSFieldSvc.h
*
*  This service provides the Papas CMS Field
*  @author alice.robson@cern.ch
*/

namespace papas {
class Field;
}

class CMSFieldSvc : public extends1<Service, IPapasFieldSvc> {
    // Detector
    std::shared_ptr<papas::Field> m_field;
    Gaudi::Property<double> m_fieldMagnitude{this,
        "magnitude", 3.8, "Field magnitude"};
    Gaudi::Property<double> m_fieldRadius{this,
        "radius", 2.9, "Field  radius"};
    Gaudi::Property<double> m_fieldZ{this, "z", 3.6, "Field z"};

 public:
    /// Default constructor
    CMSFieldSvc(const std::string& name, ISvcLocator* svc);
    /// Default destructor
    virtual ~CMSFieldSvc() = default;
    /// Initialize function
    virtual StatusCode initialize() final;
    /// Finalize function
    virtual StatusCode finalize() final;
    /// pointer to field
    virtual std::shared_ptr<papas::Field> field() const;
};

inline std::shared_ptr<papas::Field> CMSFieldSvc::field() const {
    return m_field;
}

