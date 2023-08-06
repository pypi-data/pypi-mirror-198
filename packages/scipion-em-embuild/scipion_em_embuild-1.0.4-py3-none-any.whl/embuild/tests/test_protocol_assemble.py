# ***************************************************************************
# *
# * Authors:     Pablo Conesa (pconesa@cnb.csic.es) (2018)
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# ***************************************************************************


import logging

from ..protocols.protocol_embuid_assemble import EMBuildAssembleOutputs

logger = logging.getLogger(__name__)
from pyworkflow.tests import BaseTest, setupTestProject, DataSet
from pwem.protocols import ProtImportVolumes, ProtImportPdb
from pyworkflow.utils import magentaStr

from ..protocols import ProtEMBuildAssemble
import os, resource

class TestEMBuildAssemble(BaseTest):
    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)
        cls.dataSet = DataSet.getDataSet('xmipp_tutorial')

        # Imports
        logger.info(magentaStr("\n==> Importing data - Input data"))
        new = cls.proj.newProtocol  # short notation
        launch = cls.proj.launchProtocol

        # Volume 1
        pImpVolume = new(ProtImportVolumes, samplingRate='1.0', filesPath=cls.dataSet.getFile('0346_MC.mrc'))
        launch(pImpVolume, wait=True)
        cls.inputVol = pImpVolume.outputVolume
      
        # Chain 1
        pImpPDB1 = new(ProtImportPdb, filesPath=cls.dataSet.getFile('6N52.A.pdb'))
        launch(pImpPDB1, wait=True)
        cls.inputPDB1 = pImpPDB1.outputPdb

        # Chain 2
        pImpPDB2 = new(ProtImportPdb, filesPath=cls.dataSet.getFile('6N52.B.pdb'))
        launch(pImpPDB2, wait=True)
        cls.inputPDB2 = pImpPDB2.outputPdb

    def testStackSize(self):
        '''Check stack size'''
        try:
            s_limit, h_limit = resource.getrlimit(resource.RLIMIT_STACK)
            self.assertTrue(s_limit >= 100 * 1024 ** 2 and h_limit >= 100 * 1024 ** 2, 'Not enough stack size, EMBuid may encounter `Segmentation Fault`')
        except Exception as e:
            raise self.failureException(str(e))

    def testAssembleWithoutSWORD(self):
        '''Check that an output was generated and the condition is valid. In addition, returns the size of the set.'''
        logger.info(magentaStr("\n==> Testing EMBuild:"))
        logger.info(magentaStr("\nTest Assembling:"))
        new = cls.proj.newProtocol  # short notation
        launch = cls.proj.launchProtocol

        '''Launch test'''
        pEMBuildAssemble = new(ProtEMBuildAssemble, in_vol=self.inputVol, resolution=4.0, in_chains=[self.input_PDB1, self.input_PDB2], numberOfThreads=4)
        launch(pEMBuildAssemble)
        outputPDB = getattr(pEMBuildAssemble, EMBuildAssemble.assembledAtomStruct.name)

        '''Assertion'''
        self.assertIsNotNone(outputPDB, 'Output atomic structure is not found')
  
    def testAssembleWithSWORD(self):
        pass
