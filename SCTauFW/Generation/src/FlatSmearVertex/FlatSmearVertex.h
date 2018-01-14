#pragma once

#include "GaudiAlg/GaudiTool.h"
#include "GaudiKernel/RndmGenerators.h"
#include "GaudiKernel/SystemOfUnits.h"

#include "Generation/IVertexSmearingTool.h"

/** @class FlatSmearVertex FlatSmearVertex.h "FlatSmearVertex.h"
 *
 *  Tool to smear vertex with flat smearing along the x- y- and z-axis.
 *  Concrete implementation of a IVertexSmearingTool.
 *
 *  @author Patrick Robbe
 *  @author Daniel Funke
 *  @date   2008-05-18
 */
class FlatSmearVertex : public GaudiTool, virtual public IVertexSmearingTool {
    /// Minimum value for the x coordinate of the vertex (set by options)
    Gaudi::Property<double> m_xmin{this, "xVertexMin",
                    1.0 * Gaudi::Units::mm, "Min value for x coordinate"};
    /// Minimum value for the y coordinate of the vertex (set by options)
    Gaudi::Property<double> m_ymin{this, "yVertexMin",
                    1.0 * Gaudi::Units::mm, "Min value for y coordinate"};
    /// Minimum value for the z coordinate of the vertex (set by options)
    Gaudi::Property<double> m_zmin{this, "zVertexMin",
                    1.0 * Gaudi::Units::mm, "Min value for z coordinate"};
    /// Maximum value for the x coordinate of the vertex (set by options)
    Gaudi::Property<double> m_xmax{this, "xVertexMax",
                    1.0 * Gaudi::Units::mm, "Max value for x coordinate"};
    /// Maximum value for the y coordinate of the vertex (set by options)
    Gaudi::Property<double> m_ymax{this, "yVertexMax",
                    1.0 * Gaudi::Units::mm, "Max value for y coordinate"};
    /// Maximum value for the z coordinate of the vertex (set by options)
    Gaudi::Property<double> m_zmax{this, "zVertexMax",
                    1.0 * Gaudi::Units::mm, "Max value for z coordinate"};
    /// Direction of the beam to take into account TOF vs nominal IP8, can have
    /// only values -1 or 1, or 0 to switch off the TOF and set time of
    /// interaction to zero (default = 1, as for beam 1)
    Gaudi::Property<int> m_zDir{"beamDirection", 1,
                    "Direction of the beam, possible values: -1, 1 or 0"};

  /// Flat random number generator
  Rndm::Numbers m_flatDist;

 public:
    /// Standard constructor
    FlatSmearVertex(const std::string& type,
                    const std::string& name, const IInterface* parent);
    virtual ~FlatSmearVertex();  ///< Destructor
    /// Initialize method
    virtual StatusCode initialize() final;
    /** Implements IVertexSmearingTool::smearVertex */
    virtual StatusCode smearVertex(HepMC::GenEvent& theEvent);
};

