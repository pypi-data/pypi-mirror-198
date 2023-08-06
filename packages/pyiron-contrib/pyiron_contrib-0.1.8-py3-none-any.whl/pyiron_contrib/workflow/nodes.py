from __future__ import annotations

from functools import partialmethod

import matplotlib.pyplot as plt
import numpy as np
from pyiron_atomistics import Project, _StructureFactory
from pyiron_atomistics.atomistics.job.atomistic import AtomisticGenericJob
from pyiron_atomistics.atomistics.structure.atoms import Atoms
from pyiron_atomistics.lammps.lammps import Lammps as LammpsJob

from pyiron_contrib.workflow.node import Node


class BulkStructure(Node):
    @staticmethod
    def bulk_structure(
            element: str = "Fe",
            cubic: bool = False,
            repeat: int = 1,
    ) -> Atoms:
        return _StructureFactory().bulk(element, cubic=cubic).repeat(repeat)

    __init__ = partialmethod(
        Node.__init__,
        node_function=bulk_structure,
        output_labels="structure"
    )


class Lammps(Node):
    @staticmethod
    def lammps(structure: Atoms) -> LammpsJob:
        pr = Project(".")
        job = pr.atomistics.job.Lammps("NOTAREALNAME")
        job.structure = structure
        job.potential = job.list_potentials()[0]
        return job

    __init__ = partialmethod(
        Node.__init__,
        node_function=lammps,
        output_labels="job"
    )


class CalcMD(Node):
    @staticmethod
    def calc_md(
            job: AtomisticGenericJob,
            n_ionic_steps: int = 1000,
            n_print: int = 100,
            temperature: int | float = 300.0,
            pressure: float
                      | tuple[float, float, float]
                      | tuple[float, float, float, float, float, float]
                      | None = None,
    ):
        job_name = "JUSTAJOBNAME"
        pr = Project("WORKFLOWNAMEPROJECT")
        job = job.copy_to(project=pr, new_job_name=job_name, delete_existing_job=True)
        job.calc_md(
            n_ionic_steps=n_ionic_steps,
            n_print=n_print,
            temperature=temperature,
            pressure=pressure
        )
        job.run()
        cells = job.output.cells
        displacements = job.output.displacements
        energy_pot = job.output.energy_pot
        energy_tot = job.output.energy_tot
        force_max = job.output.force_max
        forces = job.output.forces
        indices = job.output.indices
        positions = job.output.positions
        pressures = job.output.pressures
        steps = job.output.steps
        temperature = job.output.temperature
        total_displacements = job.output.total_displacements
        unwrapped_positions = job.output.unwrapped_positions
        volume = job.output.volume
        job.remove()
        pr.remove(enable=True)
        return (
            cells,
            displacements,
            energy_pot,
            energy_tot,
            force_max,
            forces,
            indices,
            positions,
            pressures,
            steps,
            temperature,
            total_displacements,
            unwrapped_positions,
            volume,
        )

    __init__ = partialmethod(
        Node.__init__,
        node_function=calc_md,
        output_labels=(
            "cells",
            "displacements",
            "energy_pot",
            "energy_tot",
            "force_max",
            "forces",
            "indices",
            "positions",
            "pressures",
            "steps",
            "temperature",
            "total_displacements",
            "unwrapped_positions",
            "volume",
        ),
    )


class Scatter(Node):
    @staticmethod
    def scatter(x: list | np.ndarray, y: list | np.ndarray):
        return plt.scatter(x, y)

    __init__ = partialmethod(
        Node.__init__,
        node_function=scatter,
        output_labels="fig",
    )
