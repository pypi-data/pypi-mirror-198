# **************************************************************************
# *
# * Authors: Yunior C. Fonseca Reyna    (cfonseca@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * Authors: Jiahua He                  (d201880053@hust.edu.cn)
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
# *
# **************************************************************************

from pwem.objects import Volume, AtomStruct
import pyworkflow.protocol.params as params
from pwem.protocols import ProtAnalysis3D
from pwem.emlib.image import ImageHandler

import os
import re
import embuild
from embuild.constants import *
import enum

class EMBuildMainChainPredictionOutputs(enum.Enum):
    predictedVolume = Volume

class ProtEMBuildMainChainPrediction(ProtAnalysis3D):
    """
    Wrapper protocol for the EMBuild's to assemble the protein complex.
    Input:
        MRC density map

    Option:
        GPU ID
        BATCH SIZE
        STRIDE

    Detailed document:
        http://huanglab.phys.hust.edu.cn/EMBuild
    """
    _label = 'main chain prediction'
    _possibleOutputs = EMBuildMainChainPredictionOutputs

    def _defineParams(self, form):
        form.addSection(label='Input')

        '''Settings for main-chain probability prediction'''
        form.addParam('in_vol', params.PointerParam, pointerClass='Volume',
                      important=True,
                      label="Input volume",
                      help='The input volume to be docked.')

        form.addParam('use_gpu', params.BooleanParam, default=True,
                        label="Use GPU(s)?",
                        help='Whether run main-chain probability prediction on GPU(s).')

        form.addParam('gpu_id', params.StringParam, default='0',
                        label='Choose GPU ID(s)', 
                        help='IDs of GPU devices to run, e.g. "0" for GPU #0, and "2,3,6" for GPUs #2, #3, and #6.')

        form.addParam('batch_size', params.IntParam, default=40,
                        label='Batch size',
                        help='Number of boxes input in one batch. Users can adjust batch_size according to the VRAM of their GPU devices. Empirically, a GPU with 40 GB VRAM can afford a batch_size of 160.')

        form.addParam('stride', params.IntParam, default=16,
                        label='Stride for sliding window',
                        help='The step of the sliding window for cutting the input map into overlapping boxes. Its value should be an integer within [12, 48]. The smaller, the better, if your computer memory is enough.')


    def _insertAllSteps(self):
        self._insertFunctionStep(self.createConfigStep)
        self._insertFunctionStep(self.processStep)
        self._insertFunctionStep(self.createOutputStep)

    def createConfigStep(self):
        pass

    def processStep(self):
        loc_in_vol = os.path.abspath(self.in_vol.get().getFileName())

        # Commands to run prediction
        '''Predict main-chain probability map'''
        embuild_src_home = embuild.Plugin.getVar(EMBUILD_HOME)
        program = "%s/EMBuild_v1.0/mcp/mcp-predict.py" % (embuild_src_home)

        if self.use_gpu:
            args = " -i {} -o MC.map -g {} -b {} -s {} -m {}".format(loc_in_vol, self.gpu_id, self.batch_size, self.stride, embuild_src_home + "/EMBuild_v1.0/mcp/model_state_dict")
        else:
            args = " -i {} -o MC.map --use_cpu -b {} -s {} -m {}".format(loc_in_col, self.batch_size, self.stride, embuild_src_home + "/EMBuild_v1.0/mcp/model_state_dict")

        embuild.Plugin.runMCP(self, program, args, cwd=self._getExtraPath())

    def createOutputStep(self):
        '''Return predicted map'''
        out_vol = Volume()
        out_vol.setSamplingRate(1.0)
        out_vol.setFileName(self._getExtraPath('MC.map'))

        self._defineOutputs(**{EMBuildMainChainPredictionOutputs.predictedVolume.name:out_vol})
        self._defineTransformRelation(self.in_vol, out_vol)


    def _validate(self):
        errors = []
        if (48 < self.stride or self.stride < 12):
            errors.append('`Stride` should be within [12, 48].')
        
        if (self.batch_size <= 0):
                errors.append('`Batch_size` should be greater than 0.')
        
        return errors

    def _summary(self):
        summary = []
        summary.append('Predicted main chain probability map will be written to {}'.format(os.path.abspath(self._getExtraPath() + '/MC.map')))
        return summary

    def _methods(self):
        methods = []
        return methods
