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

# Root folder where EMBUILD is installed, we will look here for the client

# Variable names
EMBUILD_HOME = 'EMBUILD_HOME'
EMBUILD_ENV_ACTIVATION = 'EMBUILD_ENV_ACTIVATION'
EMBUILD_MODEL_STATE_DICT_VAR = 'EMBUILD_MODEL_STATE_DICT_VAR'

EMBUILD_MODEL_STATE_DICT = 'model_state_dict'

# Installation constants
EMBUILD_VERSION_1_0_0= "1.0.0"
DEFAULT_EMBUILD_VERSION = EMBUILD_VERSION_1_0_0

def getEnvName(version):
    return 'embuild-%s' % version
    #return 'emreadyEnv'

DEFAULT_ENV_NAME = getEnvName(DEFAULT_EMBUILD_VERSION)
DEFAULT_ACTIVATION_CMD = 'conda activate ' + DEFAULT_ENV_NAME


