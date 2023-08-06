# coding: utf-8
"""Work subclasses related to GS calculations."""
#import json

from abipy.core.structure import Structure
from abipy.flowtk.tasks import RelaxTask
from abipy.flowtk.works import Work


class RelaxTaskWithTargetDilatmx(RelaxTask):


    @classmethod
    def from_scf_input(cls, scf_input, target_dilatmx=1.001, workdir=None, manager=None):

        relax_input = scf_input.new_with_vars(
            optcell=2,
            ionmov=22,
            ecutsm=0.5,
            dilatmx=1.1,
        )

        task = cls(relax_input, workdir=workdir, manager=manager)
        task.target_dilatmx = target_dilatmx

        return task

    def on_ok(self):
        """
        This method is called once the `Task` has reached status S_OK.
        """
        actual_dilatmx = self.input["dilatmx"]
        if self.target_dilatmx < actual_dilatmx:
            self.reduce_dilatmx(self.target_dilatmx)
            self.history.info('Converging dilatmx. Value reduced from {} to {}.'
                               .format(actual_dilatmx, self.input['dilatmx']))
            self.restart()
            self.finalized = False
            return dict(returncode=0, message="Restarting task with smaller dilatmx")
        else:
            self.history.info(f"Reached target dilatmx: {self.target_dilatmx}. Finalized set to True")
            self.finalized = True
            return dict(returncode=0, message="Restarting task with smaller dilatmx")


#class RelaxWorkWithTargetDilatmx(Work):
#
#    @classmethod
#    def from_scf_input(cls, scf_input, target_dilatmx=None, workdir=None, manager=None):
#        new = cls(workdir=workdir, manager=manager)
#        relax_input = scf_input.new_with_vars(optcell=2, ionmov, ecutsm, dilatmx)
#
#        return new



