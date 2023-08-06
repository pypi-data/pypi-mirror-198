"""
ConvertXFM
==========

Examples
--------

>>> task = ConvertXFM(input_matrix="input.mat", inverse=True)
>>> task.cmdline  # doctest: +ELLIPSIS
'convert_xfm -omat ...input_cxfm.mat -inverse input.mat'

>>> task = ConvertXFM(
...     input_matrix="AtoB.mat",
...     concat_matrix="BtoC.mat",
...     output_matrix="AtoC.mat",
... )
>>> task.cmdline
'convert_xfm -omat AtoC.mat -concat BtoC.mat AtoB.mat'
"""
import os

import attrs

import pydra

__all__ = ["ConvertXFM"]


@attrs.define(slots=False, kw_only=True)
class ConvertXFMSpec(pydra.specs.ShellSpec):
    """Specifications for convert_xfm."""

    input_matrix: os.PathLike = attrs.field(
        metadata={
            "help_string": "input matrix in 4x4 ASCII format",
            "mandatory": True,
            "argstr": "",
            "position": -1,
        }
    )

    output_matrix: str = attrs.field(
        metadata={
            "help_string": "output matrix in 4x4 ASCII format",
            "argstr": "-omat",
            "output_file_template": "{input_matrix}_cxfm",
            "requires": {"input_matrix"},
        }
    )

    concat_matrix: os.PathLike = attrs.field(
        metadata={
            "help_string": "concatenate this matrix with input matrix",
            "argstr": "-concat",
        }
    )

    inverse: bool = attrs.field(
        metadata={
            "help_string": "return inverse of computed matrix",
            "argstr": "-inverse",
        }
    )


class ConvertXFM(pydra.engine.ShellCommandTask):
    """Task definition for convert_xfm."""

    input_spec = pydra.specs.SpecInfo(name="ConvertXFMInput", bases=(ConvertXFMSpec,))

    executable = "convert_xfm"
