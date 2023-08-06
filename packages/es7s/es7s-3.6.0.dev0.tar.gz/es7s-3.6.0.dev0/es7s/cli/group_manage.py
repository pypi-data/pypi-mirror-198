# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2021-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import os
import shutil

import click
import pkg_resources

from ._base import CommandOption, CliGroup, CliCommand, _catch_and_log_and_exit
from .. import APP_NAME
from ..shared import get_logger, get_stdout


@click.group(__file__, cls=CliGroup)
@click.pass_context
@_catch_and_log_and_exit
def group(ctx: click.Context, **kwargs):
    """Manage es7s components."""


@group.command("install", cls=CliCommand)
@click.option(
    "-n",
    "--dry-run",
    is_flag=True,
    default=False,
    cls=CommandOption,
    help="Don't actually do anything, just pretend to.",
)
@click.option(
    "-s",
    "--symlinks",
    is_flag=True,
    default=False,
    cls=CommandOption,
    help="Make symlinks to core files instead of copying them. "
    "Useful for es7s development, otherwise unnecessary.",
)
@_catch_and_log_and_exit
class InstallCommand:
    """Install es7s system."""

    def __init__(self, dry_run: bool, symlinks: bool, **kwargs):
        self._dry_run = dry_run
        self._symlinks = symlinks
        self._run()

    def _run(self):
        self.__prepare()
        self.__copy_core()
        self.__inject_bashrc()
        self.__inject_gitconfig()
        self.__copy_bin()
        self.__install_with_apt()
        self.__install_with_pip()
        self.__install_x11()
        self.__dload_install()
        self.__build_install_tmux()
        self.__build_install_less()
        self.__install_es7s_exts()

        raise NotImplementedError("OH NOES")

    def __prepare(self):
        # install docker
        # sudo xargs -n1 <<< "docker syslog adm sudo" adduser $(id -nu)
        # ln -s /usr/bin/python3 ~/.local/bin/python
        pass

    def __copy_core(self):
        # install i -cp -v
        # git+ssh://git@github.com/delameter/pytermor@2.1.0-dev9
        pass

    def __inject_bashrc(self):
        pass

    def __inject_gitconfig(self):
        pass

    def __copy_bin(self):
        logger = get_logger()
        user_dir = os.path.expanduser("~/.es7s/bin")

        def _remove_obsolete(user_path: str) -> bool:
            msg = "Removing obsolete file: %s" % user_path
            if self._dry_run:
                logger.info(f"[DRY-RUN] {msg}")
                return True
            try:
                logger.info(msg)
                os.unlink(user_path)
            except Exception as e:
                logger.exception(e)
                return False
            return not os.path.exists(user_path)

        def _copy_to_bin(dist_path: str, user_path: str) -> bool:
            msg = "%s: %s" % ("Linking" if self._symlinks else "Copying", user_path)
            if self._dry_run:
                logger.info(f"[DRY-RUN] {msg}")
                return True
            try:
                if self._symlinks:
                    os.symlink(dist_path, user_path)
                    logger.info(f"Linked: {dist_path} -> {user_path}")
                else:
                    shutil.copy(dist_path, user_path)
                    logger.info(f"Copied: {dist_path} -> {user_path}")
            except Exception as e:
                logger.exception(e)
                return False
            return True

        successful = 0

        dist_dir_relpath = "data/bin"
        dist_dir = pkg_resources.resource_listdir(APP_NAME, dist_dir_relpath)
        for dist_relpath in dist_dir:
            dist_abspath = pkg_resources.resource_filename(
                APP_NAME, os.path.join(dist_dir_relpath, dist_relpath)
            )
            user_abspath = os.path.join(user_dir, os.path.basename(dist_relpath))
            if os.path.exists(user_abspath):
                if not _remove_obsolete(user_abspath):
                    logger.warning(f"Failed to remove file: '{user_abspath}', skipping...")
                    continue
            if not _copy_to_bin(dist_abspath, user_abspath):
                raise RuntimeError(f"Failed to copy file, aborting", [dist_abspath])
            successful += 1

        get_stdout().echo(f"Success for {successful}/{len(dist_dir)} files")

    def __install_with_apt(self):
        pass

    def __install_with_pip(self):
        pass

    def __install_x11(self):
        pass

    def __dload_install(self):
        # ginstall exa
        # ginstall bat
        pass

    def __build_install_tmux(self):
        # install tmux deps
        # build_tmux
        # ln -s `pwd`/tmux ~/bin/es7s/tmux
        # git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
        # tmux run-shell /home/delameter/.tmux/plugins/tpm/bindings/install_plugins
        pass

    def __build_install_less(self):
        # install less deps
        # build_less
        pass

    def __install_es7s_exts(self):
        # install i -i -v

        # colors
        # fonts?
        # > pipx install kolombos
        # leo
        # > pipx install macedon
        # watson
        # nalog
        pass

    def __install_shocks_service(self):
        # copy es7s-shocks.service to /etc/systemd/system
        # replace USER placeholders
        # enable shocks, reload systemd
        pass
