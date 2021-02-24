#!/usr/bin/env python3
import os

class PAM(object):

    def __init__(self):
        os.system('module load ccp4')

    def inputs(self):
        self.datain = str(input('Data file in (hkl/sca/mtz): '))
        self.model = str(input('Model in: '))
        self.pdbin = str(input('Fixed origin model: '))

    def pointless(self):
        if self.datain.endswith('.hkl' or '.HKL'):
            self.pointless = ('pointless HKLOUT pointless.mtz HKLIN ' + str(self.datain))
        elif self.datain.endswith('.sca' or '.SCA'):
            self.pointless = ('pointless HKLOUT pointless.mtz SCAIN ' + str(self.datain))
        elif self.datain.endswith('.mtz' or '.MTZ'):
            self.pointless = ('pointless HKLOUT pointless.mtz MTZIN ' + str(self.datain))
        else:
            print('\nNo data given\n')

        if self.pdbin.endswith('.pdb' or '.PDB'):
            self.pointless = (str(self.pointless) + ' XYZIN ' +  str(self.pdbin))
        else:
            print('\nNo origin reference model given\n')

        os.system(str(self.pointless))

    def aimless(self):
        os.system('aimless HKLIN pointless.mtz HKLOUT scaled.mtz --no-input')

    def molrep(self):
        if self.model.endswith('.pdb' or '.PDB'):
            self.model = ('molrep HKLIN scaled.mtz PATH_OUT ./ MODEL ' + str(self.model))
            os.system(str(self.model))

    def dimple(self):
        os.system('dimple --anode -s -f png scaled.mtz molrep.pdb dimp')
        os.system('cd dimp; bash anom-coot.sh')

if __name__ == '__main__':
    PAMpy = PAM()
    PAMpy.inputs()
    PAMpy.pointless()
    PAMpy.aimless()
    PAMpy.molrep()
    PAMpy.dimple()