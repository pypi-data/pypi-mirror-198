# **************************************************************************
# *
# * Authors: Yunior C. Fonseca Reyna    (cfonseca@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * Authors: Tao Li                  (d202280084@hust.edu.cn)
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
import resource

class EMBuildQualityCheckOutputs(enum.Enum):
    outputAtomStruct = AtomStruct

class ProtEMBuildQualityCheck(ProtAnalysis3D):
    """
    Wrapper protocol for the EMBuild's to assemble the protein complex.
    Detailed document:
        http://huanglab.phys.hust.edu.cn/EMBuild
    """
    _label = 'quality check'
    _possibleOutputs = EMBuildQualityCheckOutputs

    def _defineParams(self, form):
        form.addSection(label='Input')

        '''Settings for EMBuild main program'''
        form.addParam('in_vol', params.PointerParam, pointerClass='Volume',
                      important=True,
                      label="Main-chain probability map",
                      help='The main-chain probability map predicted by `main chain prediction` subprogram in EMBuild suite. Please run `main chain prediciton` first to get the map.')

        form.addParam('resolution', params.FloatParam, default=5.0,
                label='Resolution',
                help='Resolution of the given original map. EMBuild works better with resolution in [4.0, 8.0], This option slightly affects performance.')

        form.addParam('in_chains', params.PointerParam, pointerClass='AtomStruct', allowsNull=False, 
                important=True,
                label='Input structure(PDB format)',
                help='The docked models by EMBuild.')

        form.addParam('stride_dir', params.PathParam, 
                important=True, 
                label='stride directory', 
                help='Path/directory of stride, either the path of program `stride` or directory includes `stride` is OK. `stride` is used to assign secondary structure of known atomic structure. EMBuild will use `stride` to score the placed models. `stride` can be downloaded and installed at `http://webclu.bio.wzw.tum.de/stride/`')

        form.addParallelSection(threads=8, mpi=0)

    def _insertAllSteps(self):
        self._insertFunctionStep(self.createConfigStep)
        self._insertFunctionStep(self.processStep)
        self._insertFunctionStep(self.createOutputStep)

    def createConfigStep(self):
        pass

    def processStep(self):
        loc_in_vol = os.path.abspath(self.in_vol.get().getFileName())
        loc_in_chains = os.path.abspath(self.in_chains.get().getFileName())
        embuild_src_home = embuild.Plugin.getVar(EMBUILD_HOME)

        '''stride directory'''
        if os.path.isdir(self.stride_dir.get()):
            loc_stride = self.stride_dir.get()
        if os.path.isfile(self.stride_dir.get()):
            loc_stride = os.path.dirname(self.stride_dir.get())

        '''Run quality check'''
        cmd = "{}/EMBuild_v1.0/EMBuild {} {} {} scored.pdb --score -stride {} -nt {}".format(embuild_src_home, loc_in_vol, loc_in_chains, self.resolution.get(), loc_stride + '/stride', self.numberOfThreads.get())
        embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())

    def createOutputStep(self):
        '''Return PDB'''
        output = AtomStruct()
        output.setFileName(self._getExtraPath('scored.pdb'))
        self._defineOutputs(**{EMBuildQualityCheckOutputs.outputAtomStruct.name:output})

    def _validate(self):
        errors = []
       
        '''Check input''' 
        if self.in_vol.get() is None:
            errors.append('Please input volume')

        if self.resolution is not None and (self.resolution < 1 or self.resolution > 10.0):
            errors.append('Invalid resolution, recommend resolution range [4.0, 8.0]')

        if self.in_chains is None:
            errors.append('Please input chains')

        if self.stride_dir is None:
            errors.append('Please input the directory of `stride`')
       
        if self.stride_dir is not None:
            if os.path.isdir(self.stride_dir.get()) and not os.path.exists(os.path.join(self.stride_dir.get(), "stride")):
                errors.append('Can\'t find executable stride program. Maybe you have input the wrong directory')
            if not (os.path.isdir(self.stride_dir.get()) or os.path.isfile(self.stride_dir.get())):
                errors.append('Please input valid directory of stride')

        if self.numberOfThreads.get() <= 0:
            errors.append('Invalid threads (n >= 1!)')

        return errors

    def _summary(self):
        summary = []
        summary.append('Quality of docked model will be written to {}'.format(os.path.abspath(self._getExtraPath() + '/scored.pdb')))
        return summary

    def _methods(self):
        methods = []
        return methods
