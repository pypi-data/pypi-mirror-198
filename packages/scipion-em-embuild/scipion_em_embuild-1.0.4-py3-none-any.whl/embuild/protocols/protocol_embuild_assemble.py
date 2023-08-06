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
import resource

class EMBuildAssembleOutputs(enum.Enum):
    assembledAtomStruct = AtomStruct

class ProtEMBuildAssemble(ProtAnalysis3D):
    """
    Wrapper protocol for the EMBuild's to assemble the protein complex.
    Input:
        Predicted main-chain probability map
        Predicted chains

    Option:
        Resolution
        Num of threads to accelerate

    Runtime environment:
        1. Intel Fortran Compiler (https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler.html). Add libiomp5.so to LD_LIBRARY_PATH by source /path/to/intel/oneapi/setvars.sh, where /path/to/intel/oneapi/ stands for the local path of the installation directory of Intel Fortran Compiler (as a part of Intel oneAPI HPC Toolkit).
        2. FFTW3 (http://fftw.org/)). Can be installed in Ubuntu via sudo apt-get install fftw3. Make sure libfftw3.so.3 is in LD_LIBRARY_PATH.
        3. The maximum allowed stacksize of the system should be no less than 100MB. Use a large stacksize limit (in KB) by setting "ulimit -s". For example, set to 1GB (1048576 KB) by ulimit -s 1048576. If the stacksize limit is too small, EMBuild may encounter "Segmentation fault".

    Detailed document:
        http://huanglab.phys.hust.edu.cn/EMBuild
    """
    _label = 'assemble'
    _possibleOutputs = EMBuildAssembleOutputs

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

        form.addParam('in_chains', params.MultiPointerParam, pointerClass='AtomStruct', allowsNull=False, 
                important=True,
                label='Input chains(PDB format)',
                help='The input chains to be docked, e.g. predicted chains by AlphaFold2. Note that each PDB should include only one chain.')

        form.addParam('SWORD_dir', params.PathParam, 
                label='SWORD directory', 
                help='Optional path/directory of SWORD, either the path of program `SWORD` or directory includes `SWORD` is OK. SWORD is used to parse structural domains, which helps EMBuild refine the domains to better fit the density map. If none provided, no domain refinement will be performed.')

        #form.addParam('symmetry', params.StringParam, default='C1',
        #        label='Global symmetry',
        #        help='Optional global symmetry of the map/structure, e.g. Cyclic symmetry Cn, Dihedral symmetry Dn, etc.')

        form.addParallelSection(threads=8, mpi=0)

    def _insertAllSteps(self):
        self._insertFunctionStep(self.createConfigStep)
        self._insertFunctionStep(self.processStep)
        self._insertFunctionStep(self.createOutputStep)

    def createConfigStep(self):
        pass

    def processStep(self):
        loc_in_vol = os.path.abspath(self.in_vol.get().getFileName())
        embuild_src_home = embuild.Plugin.getVar(EMBUILD_HOME)

        '''SWORD directory'''
        has_SWORD = self.SWORD_dir.get() is not None
        if has_SWORD:
            if os.path.isdir(self.SWORD_dir.get()):
                loc_SWORD = self.SWORD_dir.get()
            if os.path.isfile(self.SWORD_dir.get()):
                loc_SWORD = os.path.dirname(self.SWORD_dir.get())


        '''Pre process'''
        for i, chain in enumerate(self.in_chains):
            loc_in_chain = os.path.abspath(chain.get().getFileName())
            dir_chain = os.path.dirname(loc_in_chain)

            if has_SWORD:
                '''Remove PDBs_Stand and PDBs_Clean generated by SWORD'''
                if os.path.exists(os.path.join(dir_chain, "PDBs_Clean")):
                    cmd = "rm {} -rf".format(os.path.join(dir_chain, "PDBs_Clean"))
                    embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())

                if os.path.exists(os.path.join(dir_chain, "PDBs_Stand")):
                    cmd = "rm {} -rf".format(os.path.join(dir_chain, "PDBs_Stand"))
                    embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())

                '''Run SWORD'''
                cmd = "cd {} && ./SWORD -i {} -m 15 -v > sword.out && cd - && {}/asgdom {} {} {}".format(loc_SWORD, loc_in_chain, embuild_src_home + "/EMBuild_v1.0/", loc_in_chain, loc_SWORD + "/sword.out", "chain_sword_{}.pdb".format(i))
                embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())
            else:
                '''Use asgdom to assign 1 domain and add `TER` to end'''
                cmd = "touch sword.out && {}/asgdom {} sword.out {} && rm sword.out".format(embuild_src_home + "/EMBuild_v1.0/", loc_in_chain, "chain_sword_{}.pdb".format(i))
                embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())

        cmd = "cat "
        for i, chain in enumerate(self.in_chains):
            cmd += "chain_sword_{}.pdb ".format(i)
        cmd += "> init_chains.pdb"
        embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())

        '''Run EMBuild main program'''
        cmd = "{}/EMBuild_v1.0/EMBuild {} init_chains.pdb {} output.pdb -nt {}".format(embuild_src_home, loc_in_vol, self.resolution, self.numberOfThreads)
        embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())

        '''Post process'''
        cmd = "{}/EMBuild_v1.0/rearrangepdb output.pdb output_rearranged.pdb".format(embuild_src_home)
        embuild.Plugin.runProgram(self, cmd, "", cwd=self._getExtraPath())


    def createOutputStep(self):
        '''Return PDB'''
        output = AtomStruct()
        output.setFileName(self._getExtraPath('output_rearranged.pdb'))
        self._defineOutputs(**{EMBuildAssembleOutputs.assembledAtomStruct.name:output})

    def _validate(self):
        errors = []
       
        '''Check input''' 
        if self.in_vol.get() is None:
            errors.append('Please input volume')

        if self.resolution is not None and (self.resolution < 1 or self.resolution > 10.0):
            errors.append('Invalid resolution, recommend resolution range [4.0, 8.0]')

        if len(self.in_chains) == 0:
            errors.append('Please input chains')
       
        if self.SWORD_dir.get() is not None:
            if os.path.isdir(self.SWORD_dir.get()) and not os.path.exists(os.path.join(self.SWORD_dir.get(), "SWORD")):
                errors.append('Can\'t find executable SWORD program. Maybe you have input the wrong directory')
            if not (os.path.isdir(self.SWORD_dir.get()) or os.path.isfile(self.SWORD_dir.get())):
                errors.append('Please input valid directory of SWORD')

        if self.numberOfThreads.get() <= 0:
            errors.append('Please set at least 1 thread')
        
        '''Check system stack size'''
        try:
            s_limit, h_limit = resource.getrlimit(resource.RLIMIT_STACK)
            if s_limit < 100 * 1024 ** 2 or h_limit < 100 * 1024 ** 2:
                errors.append('Not enough stack size. Use command `ulimit -s` to check the stack size limit. EMBuild main program will need size of no less than 102400(100MB). Try command `ulimit -s 102400` to set a higher limit')
        except:
            pass

        return errors

    def _summary(self):
        summary = []
        summary.append('Assembled chains will be written to {}'.format(os.path.abspath(self._getExtraPath() + '/output_rearranged.pdb')))
        return summary

    def _methods(self):
        methods = []
        return methods
