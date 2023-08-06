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

from ..protocols.protocol_embuid_quality_check import EMBuildQualityCheckOutputs

logger = logging.getLogger(__name__)
from pyworkflow.tests import BaseTest, setupTestProject, DataSet
from pwem.protocols import ProtImportVolumes, ProtImportPdb
from pyworkflow.utils import magentaStr

from ..protocols import ProtEMBuildQualityCheck
import os, resource

class TestEMBuildQualityCheck(BaseTest):
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

        # stride        
        self.stride_dir = '/path/to/stride/strde'

    def testQualityCheck(self):
        '''Check that an output was generated and the condition is valid. In addition, returns the size of the set.'''
        logger.info(magentaStr("\n==> Testing EMBuild:"))
        logger.info(magentaStr("\nTest Quality check"))
        new = cls.proj.newProtocol  # short notation
        launch = cls.proj.launchProtocol

        '''Launch test'''
        pEMBuildQualityCheck = new(ProtEMBuildQualityCheck, in_vol=self.inputVol, resolution=4.0, in_chains=self.input_PDB1, stride_dir=self.stride_dir, numberOfThreads=4)
        launch(pEMBuildQualityCheck)
        outputPDB = getattr(pEMBuildQualityCheck, EMBuildQualityCheck.outputAtomStruct.name)

        '''Assertion'''
        self.assertIsNotNone(outputPDB, 'Output scored atomic structure is not found. Quality check is failed.')
