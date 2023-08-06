import enum
import itertools
import os
import pathlib
import platform
import shlex
import subprocess
import tempfile
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, List, Optional, Union

PathType = Union[str, pathlib.Path]

__all__ = ["PowerView", "Connection", "T32Interface"]


_PATH_OS_SPECIFIC = {
    # OS     : ( 64-bit exe , 32-bit exe  )
    "Windows": ("windows64", "windows"),
    "Linux": ("pc_linux64", "pc_linux64"),
    "Darwin": ("macosx64", "macosx64"),
    # TODO: Solaris SUN
}


class PowerView:
    """PowerView is a class to manage TRACE32 PowerView instances.

    Args:
        connection: Specifies how to communicate with the target.
        target: Name of the executable without file extension e.g. 't32marm'
        system_path: Directory where the executable and system files of TRACE32 are located.
        force_executable: Overrides ``system_path`` and ``target`` settings when deriving the executable.
        pbi_index: In case of using a PBIConnection, the 0 based index in the pbi-chain else must be 0.
    """

    def __init__(
        self,
        connection: "Connection",
        target: str = "",
        *,
        system_path: "PathType" = "",
        force_executable: "PathType" = "",
        pbi_index: int = 0,
    ) -> None:
        self.target: str = target
        """name of executable (t32m*) without file extension. This value is not required if ``force_executable`` is set.
        """
        self._connection: "Connection" = connection
        self._connection._register(self, pbi_index)
        self._process: Optional[subprocess.Popen[bytes]] = None
        self.interfaces: Dict[Any, List[T32Interface]] = dict()

        # paths
        self.system_path: "PathType" = system_path
        """Directory where the executable and system files of TRACE32 are located."""
        self.temp_path: "PathType" = ""
        """Directory, where temporary files can be created. The source files are copied to the temporary directory while
        debugging."""
        self.id: str = ""
        """Prefix for all files that are saved by the TRACE32 PowerView instance into the TMP directory. We recommend to
        set a unique id for every PowerView instance running simultaneously."""
        self.help_path: "PathType" = ""
        """Directory where the pdf-files for the TRACE32 online help are located."""
        self.license_file: "PathType" = ""
        """Directory where a license file can be located. A license file provides the software maintenance keys."""
        self.force_executable: Optional["PathType"] = pathlib.Path(force_executable) if force_executable else None
        """Overrides ``system_path`` and ``target`` settings when deriving the executable.

        Use this option only if you know what you are doing.
        """
        self.force_32bit_executable: Optional[bool] = None
        """If set, pystart will start the 32-bit executable located under ``bin/windows`` instead of the 64-bit
        executable located under ``bin/windows64``. This could be e.g. needed if a 32-bit DLL has to be loaded in
        TRACE32 PowerView."""
        # rlm license
        self.rlm_port: int = 5055
        """The Floating License Client (RLM Client) needs to know which (RLM) port number should be used to get the
        license."""
        self.rlm_server: str = ""
        """The Floating License Client (RLM Client) needs to know which (RLM) Server to contact to get the license."""
        self.rlm_file: "PathType" = ""
        """Sets a license file (.lic) which includes the floating license parameters."""
        self.rlm_timeout: Optional[int] = None
        """RLM timeout in minutes"""
        self.rlm_pool_port: Optional[int] = None
        """TCP/IP port for license pool. Refer to the chapter “Floating License Pools” in Floating Licenses, page 19
        (floatinglicenses.pdf) for more information."""
        # screen
        self.screen: Optional[bool] = None
        """If ``False`` the main window of TRACE32 and all other dialogs and windows of TRACE32 remain hidden - even if
        an error occurs. If ``None`` the global default is used."""
        self.title: str = ""
        """Sets the window title of the TRACE32 instance."""
        self.font_size: Optional[FontSize] = None
        """Selects the used font size used by the TRACE32 instance (Normal, Small or Large)."""
        self.clear_type: Optional[bool] = None
        """Select if Cleartype display of fonts is switched ON or OFF.

            ``True``: ON if it is supported by the OS. The monospaced truetype font "Lucida Console" is used as basic
            font and should be installed.

            ``False``: OFF, TRACE32 fonts are used (t32font.fon).

            ``None``: Use global setting.
        """
        self.palette: Optional[Palette] = None
        """Sets up display theme."""
        self.full_screen: Optional[bool] = None
        """If set to true, the TRACE32 instance is started in full screen mode."""
        self.ionic: Optional[bool] = None
        """If True: Startup iconized (minimized)"""
        self.invisible: Optional[bool] = None
        """If True: The main window of TRACE32 remains hidden. However, dialogs and other windows of TRACE32 can still
        be opened."""
        self.window_mode: Optional[WindowMode] = None
        """Specify how child windows appear."""
        self.language: Optional[Language] = None
        """Set up the language used by TRACE32."""
        # startup script
        self.startup_script: "PathType" = ""
        """A cmm script being executed on start of TRACE32."""
        self.startup_parameter: Union[str, Iterable[str]] = ""
        """Parameter for ``startup_script``"""
        self.safe_start: bool = False
        """Suppresses the automatic execution of any PRACTICE script after starting TRACE32. This allows you to test or
        debug the scripts that are normally executed automatically."""

        self._config_file_name: Optional[str] = None

    def __del__(self) -> None:
        if self._config_file_name:
            os.remove(self._config_file_name)

    def start(self, *, delay: float = 6.0) -> None:
        """start the powerview executable as a process

        Args:
            delay: time to wait for complete start of PowerView

        Raises:
            FileNotFoundError: if the executable can not be found within the specified path
            RuntimeError: if process is already running
        """
        if self._process and self._process.poll() is None:
            raise RuntimeError("PowerView instance is already running")

        if not self.executable.exists() and not self.executable.is_file():
            raise FileNotFoundError(f"Executable {self.executable} not found")

        # create config-file
        config_file = tempfile.NamedTemporaryFile("w+", delete=False)
        config_string = self.get_configuration_string()
        config_file.write(config_string)
        config_file.close()
        self._config_file_name = config_file.name

        # start program
        cmd = [str(self.executable)]
        if self.startup_script and self.safe_start:
            cmd.append("--t32-safestart")
        cmd.extend(["-c", self._config_file_name])
        if self.startup_script:
            cmd.append("-s")
            cmd.append(str(self.startup_script))
            if isinstance(self.startup_parameter, str):
                cmd.extend(shlex.split(self.startup_parameter))
            else:
                cmd.extend(self.startup_parameter)

        self._process = subprocess.Popen(cmd, env=os.environ)
        time.sleep(delay)

    def wait(self, timeout: Optional[float] = None) -> None:
        """wait for process to terminate

        Args:
            Timeout: optional timeout in seconds.
        """
        if self._process:
            self._process.wait(timeout)

    def stop(self) -> None:
        """terminates the process

        After stopping a PowerView instance running with a hardware based connection, the hardware must be power cycled
        before connecting again. Alternatively, to stop TRACE32 click the close button in the GUI or execute command
        "QUIT" within TRACE32.
        """
        if self._process:
            self._process.terminate()

    def get_pid(self) -> Optional[int]:
        """Returns the process id

        Returns:
            process id of the PowerView instance or ``None`` if process is not running
        """
        if self._process and self._process.poll() is None:
            return self._process.pid
        return None

    @property
    def executable(self) -> pathlib.Path:
        """Getter for the executable being used to start a PowerView instance.

        Returns:
            The executable being used to start the PowerView instance.

        Raises:
            ValueError: If the executable could not be derived because of missing settings
        """
        if self.force_executable is not None:
            return pathlib.Path(self.force_executable)

        if not self.target:
            raise ValueError("no target specified")

        env_system_path = os.environ.get("T32SYS")
        if self.system_path:
            current_system_path = pathlib.Path(self.system_path)
        elif defaults.system_path:
            current_system_path = pathlib.Path(defaults.system_path)
        elif env_system_path:
            current_system_path = pathlib.Path(env_system_path)
        elif platform.system() == "Windows":
            current_system_path = pathlib.Path(r"C:\T32")
        else:
            raise ValueError("no system_path specified")

        system = platform.system()
        sys_specific = _PATH_OS_SPECIFIC[system][
            self.force_32bit_executable if self.force_32bit_executable is not None else defaults.force_32bit_executable
        ]
        extension = ".exe" if system == "Windows" else ""
        executable = f"{self.target}{extension}"

        path = current_system_path.joinpath("bin", sys_specific, executable)
        if not path.exists():
            sys_specific = _PATH_OS_SPECIFIC[system][True]  # Force 32-bit executable
            path = current_system_path.joinpath("bin", sys_specific, executable)
        return path

    def add_interface(self, interface: "T32Interface") -> "T32Interface":
        """Add a interface for inter-process communication

        Args:
            interface: interface to add

        Returns:
            added interface

        Raises:
            ValueError: raised if an interface which can be added only once is already added
        """
        if not isinstance(interface, T32Interface):
            raise ValueError("parameter is not of type _T32Interface")

        interface_type = type(interface)

        interfaces_same_type = self.interfaces.get(interface_type)
        if interfaces_same_type is None:
            interfaces_same_type = []
            self.interfaces[interface_type] = interfaces_same_type

        limit = interface_type._get_max_instances()
        if limit is not None and limit <= len(interfaces_same_type):
            class_name = interface.__class__.__name__
            raise ValueError(f"maximum number of {class_name} already set")

        interfaces_same_type.append(interface)
        return interface

    def get_configuration_string(self) -> str:
        """Generates the content of the config file.

        Returns:
            generated config file content
        """
        fragments = [
            "; THIS FILE IS GENERATED BY PYSTART, CHANGES WILL BE DISCARDED",
            self._get_configuration_string_os(),
            self._connection._get_config_string(self),
            self._get_config_string_license(),
            self._get_config_string_screen(),
            self._get_config_string_interface(),
        ]

        if self.license_file:
            fragments.append(f"LICENSE={self.license_file}")
        elif defaults.license_file:
            fragments.append(f"LICENSE={defaults.license_file}")

        return "\n\n".join(filter(None, fragments))

    def _get_configuration_string_os(self) -> str:
        args = ["OS="]
        T32ID = os.environ.get("T32ID")
        if self.id:
            args.append(f"ID={self.id}")
        elif T32ID:
            args.append(f"ID={T32ID}")

        T32TMP = os.environ.get("T32TMP")
        if self.temp_path:
            args.append(f"TMP={self.temp_path}")
        elif defaults.temp_path:
            args.append(f"TMP={defaults.temp_path}")
        elif T32TMP:
            args.append(f"TMP={T32TMP}")

        # global system_path
        T32SYS = os.environ.get("T32SYS")
        if self.system_path:
            args.append(f"SYS={self.system_path}")
        elif defaults.system_path:
            args.append(f"SYS={defaults.system_path}")
        elif T32SYS:
            args.append(f"SYS={T32SYS}")

        if self.help_path:
            args.append(f"HELP={self.help_path}")
        elif defaults.help_path:
            args.append(f"HELP={defaults.help_path}")

        return "\n".join(args) if len(args) > 1 else ""

    def _get_config_string_license(self) -> str:
        args = ["LICENSE="]
        if self.rlm_pool_port:
            args.append(f"POOLPORT={self.rlm_pool_port}")
        elif defaults.rlm_pool_port:
            args.append(f"POOLPORT={defaults.rlm_pool_port}")

        if self.rlm_file:
            args.append(f"RLM_LICENSE={self.rlm_file}")
        elif self.rlm_server:
            args.append(f"RLM_LICENSE={self.rlm_port}@{self.rlm_server}")
        elif defaults.rlm_file:
            args.append(f"RLM_LICENSE={defaults.rlm_file}")
        elif defaults.rlm_server:
            args.append(f"RLM_LICENSE={defaults.rlm_port}@{defaults.rlm_server}")

        if self.rlm_timeout:
            args.append(f"TIMEOUT={self.rlm_timeout}")
        elif defaults.rlm_timeout:
            args.append(f"TIMEOUT={defaults.rlm_timeout}")

        if len(args) - bool(self.rlm_timeout) > 1:
            return "\n".join(args)
        else:
            return ""

    def _get_config_string_screen(self) -> str:
        if self.screen is False or (self.screen is None and defaults.screen is False):
            return "SCREEN=OFF"
        args = ["SCREEN="]

        if self.window_mode is None:
            if defaults.window_mode != WindowMode.MDI:
                args.append(defaults.window_mode.value)
        elif self.window_mode != WindowMode.MDI:
            args.append(self.window_mode.value)

        if self.full_screen or (self.full_screen is None and defaults.full_screen):
            args.append("VFULL")
        if self.ionic or (self.ionic is None and defaults.ionic):
            args.append("VICON")
        if self.invisible or (self.invisible is None and defaults.invisible):
            args.append("INVISIBLE")

        if self.font_size is None:
            if defaults.font_size != FontSize.MEDIUM:
                args.append(f"FONT={defaults.font_size.value}")
        elif self.font_size != FontSize.MEDIUM:
            args.append(f"FONT={self.font_size.value}")

        if self.clear_type is None:
            if defaults.clear_type is not None:
                args.append("CLEARTYPE" if defaults.clear_type else "NOCLEARTYPE")
        elif self.clear_type is not None:
            args.append("CLEARTYPE" if self.clear_type else "NOCLEARTYPE")

        if self.language is None:
            if defaults.language != Language.ENGLISH:
                args.append(f"LANGUAGE={defaults.language.value}")
        elif self.language != Language.ENGLISH:
            args.append(f"LANGUAGE={self.language.value}")

        if self.title:
            args.append(f"HEADER={self.title}")

        if self.palette is None:
            if defaults.palette not in (Palette.DEFAULT, Palette.KEEP):
                args.append(defaults.palette.value)
        elif self.palette not in (Palette.DEFAULT, Palette.KEEP):
            args.append(self.palette.value)
        return "\n".join(args)

    def _get_config_string_interface(self) -> str:
        cfg = [x._get_config_string() for x in itertools.chain.from_iterable(self.interfaces.values())]
        return "\n\n".join(cfg)


class Connection(ABC):
    """An interface for different debug connections.

    A Connection is used to specify with which hardware (e.g. USB-Debugger) or software (e.g. Simulator) to work for
    your debug session.
    """

    @abstractmethod
    def _get_config_string(self, power_view: "PowerView") -> str:
        """return the Connection-Specific part of a TRACE32 config file"""
        raise NotImplementedError()

    @abstractmethod
    def _register(self, power_view: "PowerView", pbi_index: int) -> None:
        """register a PowerView-Instance

        Args:
            power_view: PowerView-Instance
            pbi_index: in case of a PBIConnection, the 0 based index in the pbi-chain else ignored
        """
        pass


class T32Interface(ABC):
    """An interface for several TRACE32 interfaces.

    A T32Interface enables the use of TRACE32 as backend being controlled from an other process.
    """

    @abstractmethod
    def _get_config_string(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def _get_max_instances(cls) -> Optional[int]:
        pass


####################
# Screen setting types:
####################
class FontSize(enum.Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}.{self.name}"


class Palette(enum.Enum):
    """Enumeration of basic color schemes."""

    DEFAULT = "DEFAULT"
    KEEP = "KEEP"
    """Keep last used palette"""
    DARK_THEME = """PALETTE 0 = 181 181 181
PALETTE 1 = 41 49 52
PALETTE 2 = 63 75 78
PALETTE 5 = 255 111 111
PALETTE 7 = 255 255 206
PALETTE 8 = 192 192 192
PALETTE 11 = 160 130 189
PALETTE 13 = 102 116 123
PALETTE 19 = 192 192 192
PALETTE 20 = 192 192 192
PALETTE 21 = 192 192 192
PALETTE 22 = 192 192 192
PALETTE 23 = 192 192 192
PALETTE 25 = 192 192 192
PALETTE 26 = 192 192 192
PALETTE 27 = 47 57 60
PALETTE 28 = 192 192 192
PALETTE 29 = 47 57 60
PALETTE 30 = 47 57 60
PALETTE 31 = 192 192 192
PALETTE 36 = 232 172 99
PALETTE 37 = 147 199 99
PALETTE 47 = 47 57 60
PALETTE 54 = 255 255 255"""

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}.{self.name}"


class WindowMode(enum.Enum):
    MDI = "MDI"
    """Multiple Document Interface (default).
        All child windows appear inside the TRACE32 main window.
    """
    FDI = "FDI"
    """Floating Document Interface.
        All child windows can be placed on any position on the desktop independently form the main window. Minimizing
        the main window, minimizes also the child windows. Only the main window appears in the task bar.
    """
    MTI = "MTI"
    """Multiple Top-level window Interface
        All child windows can be placed on any position on the desktop independently form the main window. Minimizing
        the main window, minimizes none of the child windows. Both the main and all child windows appear in the task
        bar.
    """

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}.{self.name}"


class Language(enum.Enum):
    ENGLISH = "EN"
    JAPANESE = "JP"

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}.{self.name}"


class PowerViewGlobalDefaults:
    """A class to handle ``PowerView`` default settings on a centralized place."""

    def __init__(self) -> None:
        # paths
        self.system_path: "PathType" = ""
        """Directory where the executable and system files of TRACE32 are located.

        Initially the value is set to environment variable ``T32SYS``. If the environment variable is not set, on
        Windows systems ``"C:\\T32"`` is taken, on Linux system a value must be set before start."""

        self.temp_path: "PathType" = ""
        """Directory, where temporary files can be created. The source files are copied to the temporary directory while
        debugging.

        Initially the value is set to environment variable ``T32TMP``. If the environment variable is not set TRACE32 is
        responsible for the path being used."""
        self.help_path: "PathType" = ""
        """Directory where the pdf-files for the TRACE32 online help are located."""
        self.license_file: "PathType" = ""
        """Directory where a license file can be located. A license file provides the software maintenance keys."""
        self.force_32bit_executable: bool = False
        """If set, pystart will start the 32-bit executable located under ``bin/windows`` instead of the 64-bit
        executable located under ``bin/windows64``. This could be e.g. needed if a 32-bit DLL has to be loaded in
        TRACE32 PowerView."""
        # rlm license
        self.rlm_port: int = 5055
        """The Floating License Client (RLM Client) needs to know which (RLM) port number should be used to get the
        license. Defaults to 5055."""
        self.rlm_server: str = ""
        """The Floating License Client (RLM Client) needs to know which (RLM) Server to contact to get the license."""
        self.rlm_file: "PathType" = ""
        """Sets a license file (.lic) which includes the floating license parameters."""
        self.rlm_timeout: Optional[int] = None
        """RLM timeout in minutes"""
        self.rlm_pool_port: Optional[int] = None
        """TCP/IP port for license pool. Refer to the chapter “Floating License Pools” in Floating Licenses, page 19
        (floatinglicenses.pdf) for more information."""
        # screen
        self.screen: bool = True
        """If ``False`` the main window of TRACE32 and all other dialogs and windows of TRACE32 remain hidden - even if
        an error occurs."""
        self.font_size: FontSize = FontSize.MEDIUM
        """Selects the used font size used by the TRACE32 instance (Normal, Small or Large)."""
        self.clear_type: Optional[bool] = None
        """Select if Cleartype display of fonts is switched ON or OFF.

            ``True``: ON if it is supported by the OS. The monospaced truetype font "Lucida Console" is used as basic
            font and should be installed.

            ``False``: OFF, TRACE32 fonts are used (t32font.fon).

            ``None``: Use DEFAULT.
        """
        self.palette: Palette = Palette.KEEP
        """Sets up display theme."""
        self.full_screen: bool = False
        """If set to true, the TRACE32 instance is started in full screen mode."""
        self.ionic: bool = False
        """If True: Startup iconized (minimized)"""
        self.invisible: bool = False
        """If True: The main window of TRACE32 remains hidden. However, dialogs and other windows of TRACE32 can still
        be opened."""
        self.window_mode: WindowMode = WindowMode.MDI
        """Specify how child windows appear."""
        self.language: Language = Language.ENGLISH
        """Set up the language used by TRACE32."""


defaults: PowerViewGlobalDefaults = PowerViewGlobalDefaults()
"""If attributes of a ``PowerView`` instance are not set, the values are taken from the attribute with same name from
this object. Therefore, even for multiple instances of ``PowerView`` some attributes can be set on a single point."""
