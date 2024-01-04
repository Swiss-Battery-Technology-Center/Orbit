# Copyright (c) 2022-2023, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from dataclasses import MISSING
from typing import TYPE_CHECKING
from typing_extensions import Literal

import omni.isaac.orbit.sim as sim_utils
from omni.isaac.orbit.utils import configclass

from .terrain_importer import TerrainImporter

if TYPE_CHECKING:
    from .terrain_generator_cfg import TerrainGeneratorCfg


@configclass
class TerrainImporterCfg:
    """Configuration for the terrain manager."""

    class_type: type = TerrainImporter
    """The class to use for the terrain importer.

    Defaults to :class:`omni.isaac.orbit.terrains.terrain_importer.TerrainImporter`.
    """

    collision_group: int = -1
    """The collision group of the terrain. Defaults to -1."""

    prim_path: str = MISSING
    """The absolute path of the USD terrain prim.

    All sub-terrains are imported relative to this prim path.
    """

    num_envs: int = MISSING
    """The number of environment origins to consider."""

    terrain_type: Literal["generator", "plane", "usd"] = "generator"
    """The type of terrain to generate. Defaults to "generator".

    Available options are "plane", "usd", and "generator".
    """

    terrain_generator: TerrainGeneratorCfg | None = None
    """The terrain generator configuration.

    Only used if ``terrain_type`` is set to "generator".
    """

    usd_path: str | None = None
    """The path to the USD file containing the terrain.

    Only used if ``terrain_type`` is set to "usd".
    """

    env_spacing: float | None = None
    """The spacing between environment origins when defined in a grid. Defaults to None.

    Note:
      This parameter is used only when the ``terrain_type`` is ``"plane"`` or ``"usd"``.
    """

    visual_material: sim_utils.VisualMaterialCfg | None = sim_utils.PreviewSurfaceCfg(
        diffuse_color=(0.065, 0.0725, 0.080)
    )
    """The visual material of the terrain. Defaults to a dark gray color material.

    The material is created at the path: ``{prim_path}/visualMaterial``. If `None`, then no material is created.

    .. note::
        This parameter is used only when the ``terrain_type`` is ``"generator"``.
    """

    physics_material: sim_utils.RigidBodyMaterialCfg = sim_utils.RigidBodyMaterialCfg()
    """The physics material of the terrain. Defaults to a default physics material.

    The material is created at the path: ``{prim_path}/physicsMaterial``.

    .. note::
        This parameter is used only when the ``terrain_type`` is ``"generator"`` or ``"plane"``.
    """

    max_init_terrain_level: int | None = None
    """The maximum initial terrain level for defining environment origins. Defaults to None.

    The terrain levels are specified by the number of rows in the grid arrangement of
    sub-terrains. If None, then the initial terrain level is set to the maximum
    terrain level available (``num_rows - 1``).

    Note:
      This parameter is used only when sub-terrain origins are defined.
    """

    debug_vis: bool = False
    """Whether to enable visualization of terrain origins for the terrain. Defaults to False."""
