# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from pathlib import Path

from pdkmaster.io.spice import SpicePrimsParamSpec, PySpiceFactory

from .pdkmaster import tech as _tech


__all__ = ["prims_spiceparams", "pyspicefab"]


_file = Path(__file__)
_libfile = _file.parent.joinpath("models", "all.spice")
_prims = _tech.primitives
prims_spiceparams = SpicePrimsParamSpec()
for dev_name, params in (
    ("nmos_3p3", {}),
    ("pmos_3p3", {}),
    ("nmos_5p0", dict(model="nmos_6p0")),
    ("pmos_5p0", dict(model="pmos_6p0")),
):
    prims_spiceparams.add_device_params(prim=_prims[dev_name], **params)
pyspicefab = PySpiceFactory(
    libfile=str(_libfile),
    corners=(
        "init",
        "typical", "ff", "ss", "fs", "sf",
    ),
    conflicts={
        "typical": ("ff", "ss", "fs", "sf"),
        "ff": ("typical", "ss", "fs", "sf"),
        "ss": ("typical", "ff", "fs", "sf"),
        "fs": ("typical", "ff", "ss", "sf"),
        "sf": ("typical", "ff", "ss", "fs"),
    },
    prims_params=prims_spiceparams,
)
