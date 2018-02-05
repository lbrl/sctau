# sctau

## Papas :)

### Usage

First of the whole you should build the project:
```bash
$ cd SCTauFW
$ mkdir build
$ cd build
$ cmake ../
$ make
```

How to run:
```sh
$ SCTauFW/build/run /ceph/groups/sctau/fccsw/FCCSW/scripts/fccrun.py SCTauFW/Sim/SimPapas/options/papa_test/simple_papastool.py
```
The file `simple_papastool.py` operates the process.
In particular it deals with partcile gun.
For example to tune the gun for photons use:
```python
guntool = ParticleGun("SignalProvider", PdgCodes=[11])
```
or generate different particles:
```python
guntool = ParticleGun("SignalProvider", PdgCodes=[211, 22, 11, -13, 2112, 2212])
```
On the other hand you can easy change the number of event to be generated.
```python
   ## number of events
   EvtMax=10000, 
```

As an output you will get an ```output.root``` file.
There are trees ```metadata``` and ```events```.
They are made automatically as it was from the source.
Some example of work with ```events``` can be found in ```afina.py```.
