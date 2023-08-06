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

from ..protocols.protocol_embuid_main_chain_prediction import EMBuildMainChainPredictionOutputs

logger = logging.getLogger(__name__)
from pyworkflow.tests import BaseTest, setupTestProject, DataSet
from pwem.protocols import ProtImportVolumes, ProtImportPdb
from pyworkflow.utils import magentaStr

from ..protocols import ProtEMBuildMainChainPrediction


class TestEMBuildMainChainPrediction(BaseTest):
    '''Import map'''
    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)
        cls.dataSet = DataSet.getDataSet('xmipp_tutorial')

        # Imports
        logger.info(magentaStr("\n==> Importing data - Input data"))
        new = cls.proj.newProtocol  # short notation
        launch = cls.proj.launchProtocol

        # Volume 1
        pImpVolume = new(ProtImportVolumes, samplingRate='1.06',
                         filesPath=cls.dataSet.getFile('emd_0346.map'))
        launch(pImpVolume, wait=True)
        cls.inputVol = pImpVolume.outputVolume
      
    def testMainChainPrediction(self):
        '''Check that an output was generated and the condition is valid. In addition, returns the size of the set.'''
        logger.info(magentaStr("\n==> Testing EMBuild:"))
        logger.info(magentaStr("\nTest Main Chain Prediction:"))
        new = cls.proj.newProtocol  # short notation
        launch = cls.proj.launchProtocol

        '''Launch test'''
        pEMBuildMCP = new(ProtEMBuildMainChainPrediction, in_vol=self.inputVol, use_gpu=True, gpu_id='0', batch_size=20, stride=24)
        launch(pEMBuildMCP)
        outputVol = getattr(pEMBuildMCP, EMBuildMainChainPrediction.predictedVolume.name)

        '''Assertion'''
        self.assertIsNotNone(outputVol, 'Predicted main-chain probability map is not found')
        self.assertAlmostEqual(1.0, outputVol.getSamplingRate(), 'Sample rate of main-chain map is not 1.0')
