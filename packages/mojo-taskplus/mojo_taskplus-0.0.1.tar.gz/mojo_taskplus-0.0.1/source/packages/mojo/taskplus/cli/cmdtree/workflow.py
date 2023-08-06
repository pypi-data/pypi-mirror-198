__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import os

import click
import yaml

from mojo.xmods.xlogging.levels import LOG_LEVEL_NAMES

HELP_WORK = "The file containing the workpacket detail for performing a workflow orchestration."
HELP_OUTPUT = "The output directory where results and artifacts are collected."
HELP_START = r"A time stamp to associate with the start of the run. Example: 2020-10-17T15:30:11.989120  Bash: date +%Y-%m-%dT%H:%M:%S.%N"
HELP_CONSOLE_LOG_LEVEL = "The logging level for console output."
HELP_FILE_LOG_LEVEL = "The logging level for logfile output."

@click.group("workflow", help="Contains commands that are used to work with or run workflow scripts.")
def group_taskplus_workflow():
    return

@click.command("run")
@click.argument("workflow", required=True)
@click.option("--output", "-o", required=False, help=HELP_OUTPUT)
@click.option("--start", default=None, required=False, help=HELP_START)
@click.option("--console-level", default=None, required=False, type=click.Choice(LOG_LEVEL_NAMES, case_sensitive=False), help=HELP_CONSOLE_LOG_LEVEL)
@click.option("--logfile-level", default=None, required=False, type=click.Choice(LOG_LEVEL_NAMES, case_sensitive=False), help=HELP_FILE_LOG_LEVEL)
def command_taskplus_workflow_run(workflow, output=None, start=None, console_level=None, logfile_level=None):

    # pylint: disable=unused-import,import-outside-toplevel

    # We do the imports of the automation framework code inside the action functions because
    # we don't want to startup loggin and the processing of inputs and environment variables
    # until we have entered an action method.  Thats way we know how to setup the environment.

    # IMPORTANT: We need to load the context first because it will trigger the loading
    # of the default user configuration
    from mojo.xmods.xcollections.context import Context
    from mojo.xmods.xpython import extend_path
    

    ctx = Context()
    env = ctx.lookup("/environment")

    workflow_file = os.path.abspath(os.path.expanduser(os.path.expandvars(workflow)))
    if not os.path.exists(workflow_file):
        error_msg = "The specified workflow file does not exist. file=%s" % workflow_file
        raise click.BadParameter(error_msg)

    workflow_info = None
    with open(workflow_file, 'r') as wpf:
        wpfcontent = wpf.read()
        workflow_info = yaml.safe_load(wpfcontent)

    if workflow_info is not None:

        from mojo.taskplus.entrypoints import run_workflow_entrypoint

        # Run the work packet
        run_workflow_entrypoint(workflow_file, workflow_info)

    else:
        error_msg = "Failure loading the work packet info from. file=%s" % workflow_file
        raise click.BadParameter(error_msg)

    return

group_taskplus_workflow.add_command(command_taskplus_workflow_run)
