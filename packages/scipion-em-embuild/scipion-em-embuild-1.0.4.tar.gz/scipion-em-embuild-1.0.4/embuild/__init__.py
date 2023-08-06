# **************************************************************************
# *
# * Authors: Yunior C. Fonseca Reyna    (cfonseca@cnb.csic.es)
# *
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
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

import os
import pwem
import shutil
import pyworkflow as pw

from pyworkflow.utils import Environ
from .constants import *

__version__ = '1.0.4'
_references = ['HeJ2022']



class Plugin(pwem.Plugin):
    _homeVar = EMBUILD_HOME
    _pathVars = [EMBUILD_HOME]

    @classmethod
    def _defineVariables(cls):
        default_embuildHome = 'EMBuild-%s' % DEFAULT_EMBUILD_VERSION
        cls._defineEmVar(EMBUILD_HOME, default_embuildHome)
        cls._defineVar(EMBUILD_ENV_ACTIVATION, DEFAULT_ACTIVATION_CMD)
        cls._defineEmVar(EMBUILD_MODEL_STATE_DICT_VAR,
                         os.path.join(default_embuildHome, EMBUILD_MODEL_STATE_DICT))

    @classmethod
    def getEnviron(cls):
        """ Setup the environment variables needed to launch EMBuild. """
        environ = Environ(os.environ)

        environ.update({
            'PATH': Plugin.getHome()
        }, position=Environ.BEGIN)

        return environ

    @classmethod
    def getEMBuildEnvActivation(cls):
        return cls.getVar(EMBUILD_ENV_ACTIVATION)

    @classmethod
    def isVersionActive(cls):
        return cls.getActiveVersion().startswith(__version__)

    @classmethod
    def getDependencies(cls):
        # try to get CONDA activation command
        condaActivationCmd = cls.getCondaActivationCmd()
        neededProgs = ['wget']
        if not condaActivationCmd:
            neededProgs.append('conda')

        return neededProgs

    @classmethod
    def defineBinaries(cls, env):

        emBuildInstalled = "embuild_installed.txt"
        pythonVersion = "3.8"
        EMBuild_commands = []
        # Config conda env
        # TODO modify dependencies
        EMBuild_commands.append(('%s conda create -y -n %s -c conda-forge -c pytorch ' \
                                 'python=%s "pillow<7.0.0" pytorch==1.8.1 cudatoolkit=10.2 mrcfile numpy tqdm && '
                                 'touch %s' \
                                 % (cls.getCondaActivationCmd(), DEFAULT_ENV_NAME, pythonVersion, emBuildInstalled), [emBuildInstalled]))

        # Download sources codes from website and compile codes
        EMBuild_commands.append(('wget -c http://huanglab.phys.hust.edu.cn/EMBuild/EMBuild_v1.0.tgz', 'EMBuild_v1.0.tgz'))
        EMBuild_commands.append(('tar -xvf EMBuild_v1.0.tgz', []))
        EMBuild_commands.append(('cd EMBuild_v1.0/mcp && %s %s && f2py -c interp3d.f90 -m interp3d' % (cls.getCondaActivationCmd(), DEFAULT_ACTIVATION_CMD), []))
        env.addPackage('EMBuild', version=DEFAULT_EMBUILD_VERSION,
                       commands=EMBuild_commands,
                       tar='void.tgz',
                       default=True)


    @classmethod
    def runMCP(cls, protocol, program, args, cwd=None):
        """ Run EMBuild command from a given protocol. """
        # TODO
        fullProgram = '%s %s && python %s' % (cls.getCondaActivationCmd(), cls.getEMBuildEnvActivation(), program)
        protocol.runJob(fullProgram, args, env=cls.getEnviron(), cwd=cwd,
                        numberOfMpi=1)

    @classmethod
    def runProgram(cls, protocol, program, args, cwd=None):
        # TODO
        fullProgram = program
        protocol.runJob(fullProgram, args, env=cls.getEnviron(), cwd=cwd,
                        numberOfMpi=1)

    @classmethod
    def getEMBuildModelStateDict(cls):
        return os.path.abspath(cls.getVar(EMBUILD_MODEL_STATE_DICT_VAR))
