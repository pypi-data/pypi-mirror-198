"""
"""
import abc
import os
import logging
import numpy as np

#from typing import
#from monty.io import FileLock
#from pymatgen.core.xcfunc import XcFunc
#from abipy.core.structure import Structure
#from abipy.abio.factories import ion_ioncell_relax_input
#from abipy.flowtk.abiobjects import SpinMode, Smearing, KSampling, RelaxationMethod
#from abipy.flowtk.tasks import RelaxTask
#from abipy.flowtk.works import Work, RelaxWork, PhononWork
#from abipy import abilab
#from pseudo_dojo.core.dojoreport import DojoReport, dojo_dfact_esults, dojo_gbrv_results
#from pseudo_dojo.refdata.gbrv import gbrv_database
#from pseudo_dojo.refdata.deltafactor import df_database
#from pseudo_dojo.refdata.lantanides.database import raren_database


def _build_scf_input(pseudo):

    inp = AbinitInput(structure, pseudo)
    #inp.set_vars(
    #)

    return inp


class PseudoTestsFlow(Flow):

    @classmethod
    def from_pseudo_filepath(cls, pseudo_filepath, ecut_list, workdir, manager=None):
        new = cls(workdir=workdir, manager=manager)
        new.pseudo_filepath = os.path.abspath(pseudo_filepath)
        scf_input = _build_scf_input_from_pseudo(pseudo)
        work = GsEcutConvWork.from_scf_input(cls, scf_input, pseudo, ecut_list, workdir=None, manager=None)
        new.register_work(work)

        return new

    def on_all_ok(self):
        """
        This method is called when all tasks have reached S_OK.
        It reads the energies and the volumes from the GSR file
        """
        for work in self:
            with open(work.outdir.path_in("ecut_conv.json"), "wt") as fh:
                data[work.KEY] = json.read(fh)

        with open(self.outdir.path_in("ecut_conv.json"), "wt") as fh:
            json.dump(data, fh, indent=4, sort_keys=True)


class _BaseWork(Work):
    """Base class for Works."""
    #__metaclass__ = abc.ABCMeta

    #@abc.abstractproperty
    #def dojo_pseudo(self):
    #    """:class:`Pseudo` object"""

    #@abc.abstractproperty
    #def dojo_trial(self):
    #    """String identifying the DOJO trial. Used to write results in the DOJO_REPORT."""

    #@property
    #def djrepo_path(self):
    #    """Path to the djrepo file."""
    #    root, ext = os.path.splitext(self.dojo_pseudo.filepath)
    #    return root + ".djrepo"

    #def add_entry_to_dojoreport(self, entry, overwrite_data=False, pop_trial=False):
    #    """
    #    Write/update the DOJO_REPORT section of the pseudopotential.
    #    Important parameters such as the name of the dojo_trial and the energy cutoff
    #    are provided by the sub-class.
    #    Client code is responsible for preparing the dictionary with the data.

    #    Args:
    #        entry: Dictionary with results.
    #        overwrite_data: If False, the routine raises an exception if this entry is
    #            already filled.
    #        pop_trial: True if the trial should be removed before adding the new entry.
    #    """
    #    djrepo = self.djrepo_path
    #    self.history.info("Writing dojreport data to %s" % djrepo)

    #    # Update file content with Filelock.
    #    with FileLock(djrepo):
    #        # Read report from file.
    #        file_report = DojoReport.from_file(djrepo)

    #        # Create new entry if not already there
    #        dojo_trial = self.dojo_trial

    #        if pop_trial:
    #            file_report.pop(dojo_trial, None)

    #        if dojo_trial not in file_report:
    #            file_report[dojo_trial] = {}

    #        # Convert float to string with 1 decimal digit.
    #        dojo_ecut = "%.1f" % self.ecut

    #        # Check that we are not going to overwrite data.
    #        if dojo_ecut in file_report[dojo_trial]:
    #            if not overwrite_data:
    #                raise RuntimeError("dojo_ecut %s already exists in %s. Cannot overwrite data" %
    #                        (dojo_ecut, dojo_trial))
    #            else:
    #                file_report[dojo_trial].pop(dojo_ecut)

    #        # Update file_report by adding the new entry and write new file
    #        file_report[dojo_trial][dojo_ecut] = entry

    #        # Write new dojo report and update the pseudo attribute
    #        file_report.json_write()
    #        self._pseudo.dojo_report = file_report


class GsEcutConvWork(_PseudoWork):
    """
    This work computes GS properties for different ecut values
    and save the results in the outdata directory of the Work.
    """
    KEY = "gs_vs_ecut"

    def from_scf_input(cls, scf_input, pseudo, ecut_list, workdir=None, manager=None):
        new = cls(workdir=workdir, manager=manager)

        new.natom = len(scf_input.structure)
        new.ecut_list = list(ecut_list)
        for ecut in self.ecut_list:
            new.register_scf_task(scf_input.new_with_vars(ecut=ecut))

        return new

    def on_all_ok(self):
        """
        This method is called when all tasks have reached S_OK.
        It reads the energies and the volumes from the GSR file
        """
        energy_per_atom_ev = []
        pressure_gpa = []
        for task in self:
            with task.open_gsr() as gsr:
                energy_per_atom_ev.append(float(gsr.energy_per_atom))
                pressure_gpa.append(float(gsr.pressure))

        data = dict(
            natom=self.natom,
            ecut_list=self.ecut_list,
            energy_per_atom_ev=energy_per_atom_ev,
            pressure_gpa=pressure_gpa,
        )

        with open(self.outdir.path_in("ecut_conv.json"), "wt") as fh:
            json.dump(data, fh, indent=4, sort_keys=True)


class PhEcutConvWork(_PseudoWork):
    """
    This work computes DFPT phonons for different ecut values
    and save the results in the outdata directory of the Work.
    """
    KEY = "phonons_vs_ecut"

    def from_scf_input(cls, scf_input, pseudo, ecut_list, workdir=None, manager=None):
        new = cls(workdir=workdir, manager=manager)

        new.natom = len(scf_input.structure)
        new.ecut_list = list(ecut_list)
        #for ecut in self.ecut_list:
        #    new.register_scf_task(scf_input.new_with_vars(ecut=ecut))

        return new

    def on_all_ok(self):
        """
        This method is called when all tasks have reached S_OK.
        It reads the energies and the volumes from the GSR file
        """
        energy_per_atom_ev = []
        pressure_gpa = []
        for task in self:
            with task.open_ddb() as ddb:
                energy_per_atom_ev.append(float(gsr.energy_per_atom))
                #pressure_gpa.append(float(gsr.pressure))

        data = dict(
            natom=self.natom,
            #ecut_list=self.ecut_list,
            #energy_per_atom_ev=energy_per_atom_ev,
            #pressure_gpa=pressure_gpa,
        )

        with open(self.outdir.path_in("ecut_conv.json"), "wt") as fh:
            json.dump(data, fh, indent=4, sort_keys=True)
