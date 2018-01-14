
import os, sys
__path__ = [d for d in [os.path.join(d, 'SimPapas') for d in sys.path if d]
            if (d.startswith('/home/razuvaev/sctau5/SCTauFW/build') or
                d.startswith('/home/razuvaev/sctau5/SCTauFW')) and
               (os.path.exists(d) or 'python.zip' in d)]
if os.path.exists('/home/razuvaev/sctau5/SCTauFW/Sim/SimPapas/python/SimPapas/__init__.py'):
    execfile('/home/razuvaev/sctau5/SCTauFW/Sim/SimPapas/python/SimPapas/__init__.py')
