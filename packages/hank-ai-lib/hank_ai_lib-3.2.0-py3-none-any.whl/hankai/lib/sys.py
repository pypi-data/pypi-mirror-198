#
# MIT License
#
# Copyright © 2022 Hank AI, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Classes for Sys/Os Utilities."""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Union

import magic

from .enum import (
    EncodeBinaryBase,
    EncodeStringCodec,
    MimeType,
    PathItemState,
    PathItemType,
)
from .log_env import LogEnv
from .util_util import Util


@dataclass
class Encoding:
    """Data binary encoding base and decoding codec.
    Default encoding binary base [EncodeBinaryBase.BASE_64]
    Default encoding string codec [EncodeStringCodec.UTF_8]
    """

    base: EncodeBinaryBase = EncodeBinaryBase.BASE_64
    codec: EncodeStringCodec = EncodeStringCodec.UTF_8

    def __str__(self) -> str:
        return f"{str(self.base)}/{str(self.codec)}"

    @staticmethod
    def unpicklable(encoding_type: Optional[str]) -> Optional[Encoding]:
        """Set the Encoding fields from the encoding_type.

        ! NOTE: Ideally this method should not exist. It's strongly encouraged
        to utilize the jsonpickle encode/decode for wire transmission. Using
        this method is hacky and doesn't allow for greater type hint utilization.
        """
        if encoding_type is None:
            return None

        encoding = Encoding()
        if not encoding_type:
            return encoding

        base_str, codec_str = encoding_type.split("/")
        base: Optional[EncodeBinaryBase] = EncodeBinaryBase.member_by(member=base_str)
        codec: Optional[EncodeStringCodec] = EncodeStringCodec.member_by(
            member=codec_str
        )

        if base is None or codec is None:
            raise ValueError(
                f"Encoding type [{encoding_type}] is not supported. "
                "Encoding base must be one of ["
                f"{'|'.join(EncodeBinaryBase.members_str())}]. "
                "Encoding codec must be one of ["
                f"{'|'.join(EncodeStringCodec.members_str())}]."
            )

        encoding.base = base
        encoding.codec = codec

        return encoding


@dataclass
class FileProperties:  # pylint: disable=too-many-instance-attributes
    """General file properties. [extension_separator_regex] my be a REGEX string.
    The filename and extension REGEX search is of the form:
    r"(.*)(\u005C.)(.*)$" The REGEX match will only access group(1) the
    [name_excl_extension], group(2) the [extension_separator] and group(2) the
    [extension].
    """

    path: str
    source_path: str
    extension_separator_regex: str = r"(.*)(\.)(.*)$"
    mime_type: Optional[MimeType] = None
    encoding: Encoding = Encoding(
        base=EncodeBinaryBase.BASE_64, codec=EncodeStringCodec.UTF_8
    )

    def __str__(self) -> str:
        return json.dumps(
            {
                "path": self.path,
                "source_path": self.source_path,
                "extension_separator_regex": self.extension_separator_regex,
                "canonical_path": self.canonical_path,
                "directory": self.directory,
                "name": self.name,
                "name_excluding_extension": self.name_excl_extension,
                "extension_separator": self.extension_separator,
                "extension": self.extension,
                "md5sum": self.md5sum,
                "size_bytes": self.size_bytes,
                "encoded": self.encoded,
            },
            indent=2,
        )

    def __post_init__(self) -> None:
        self.canonical_path = os.path.abspath(self.path)
        self.directory: str = os.path.dirname(self.canonical_path)
        self.name: str = os.path.basename(self.canonical_path)
        self.name_excl_extension: str = self.name
        self.extension_separator: Optional[str] = None
        self.extension: Optional[str] = None
        self.md5sum: Optional[str] = None
        self.size_bytes: Optional[int] = None
        self.encoded: Optional[str] = None

        if not os.path.isdir(self.source_path):
            self.source_path = os.path.dirname(self.source_path)

        if not self.name:
            raise ValueError(f"Argument [path={self.path}] has no name.")

        match = re.search(self.extension_separator_regex, self.name)
        if match:
            if match.group(1) is not None:
                self.name_excl_extension = match.group(1)
            if match.group(2) is not None:
                self.extension_separator = match.group(2)
            if match.group(3) is not None:
                self.extension = match.group(3)

        if self.mime_type is None:
            try:
                self.mime_type = MimeType.member_by(
                    member=magic.from_file(self.canonical_path, mime=True)
                )
            except FileNotFoundError:
                pass

            if self.mime_type is None and self.extension:
                self.mime_type = MimeType.member_by(member=self.extension)

    def encode_binary(self) -> None:
        """Read the file as binary and encode it setting [md5sum], [size_bytes]
        and [encoded].
        """
        if not os.path.isfile(self.canonical_path):
            raise AssertionError(
                f"Argument [canonical_path={self.canonical_path}] is not a file."
            )
        data_bytes = Sys.read_file(file=self.canonical_path, binary=True)
        if isinstance(data_bytes, bytes):
            self.md5sum = hashlib.md5(data_bytes).hexdigest()
            self.size_bytes = os.stat(self.canonical_path).st_size
            self.encoded = Util().base_encode(
                decoded=data_bytes,
                base=self.encoding.base,
                codec=self.encoding.codec,
            )

    def encode_non_binary(self) -> None:
        """Read the file as non binary and setting [md5sum], [size_bytes]
        and [encoded].
        """
        if not os.path.isfile(self.canonical_path):
            raise AssertionError(
                f"Argument [canonical_path={self.canonical_path}] is not a file."
            )
        data_str = Sys.read_file(file=self.path, binary=False)
        if isinstance(data_str, str):
            self.md5sum = hashlib.md5(data_str.encode()).hexdigest()
            self.size_bytes = os.stat(self.canonical_path).st_size
            self.encoded = data_str


class SourcePathItems:  # pylint: disable=too-many-instance-attributes,disable=too-many-branches
    """Collection of source path items."""

    def __init__(self, source_path: str) -> None:
        self._source_path = source_path
        self._inc_dirs: List[str] = []
        self._inc_files: List[str] = []
        self._inc_links: List[str] = []
        self._exc_dirs: List[str] = []
        self._exc_files: List[str] = []
        self._exc_links: List[str] = []

    def source_path(self) -> str:
        """Return the source path."""
        return self._source_path

    def append(
        self,
        item_state: PathItemState,
        item_type: PathItemType,
        item: str,
    ) -> None:
        """Append items from the source path."""
        if not item:
            return

        if item_type is PathItemType.DIRECTORY:
            if item_state is PathItemState.INCLUDED:
                self._inc_dirs.append(item)
            elif item_state is PathItemState.EXCLUDED:
                self._exc_dirs.append(item)
        elif item_type is PathItemType.FILE:
            if item_state is PathItemState.INCLUDED:
                self._inc_files.append(item)
            elif item_state is PathItemState.EXCLUDED:
                self._exc_files.append(item)
        elif item_type is PathItemType.SYMLINK:
            if item_state is PathItemState.INCLUDED:
                self._inc_links.append(item)
            elif item_state is PathItemState.EXCLUDED:
                self._exc_links.append(item)

    def included_directories(self) -> List[str]:
        """Return included directory paths."""
        return self._inc_dirs

    def excluded_directories(self) -> List[str]:
        """Return excluded directory paths."""
        return self._exc_dirs

    def included_files(self) -> List[str]:
        """Return included file paths."""
        return self._inc_files

    def excluded_files(self) -> List[str]:
        """Return excluded file paths."""
        return self._exc_files

    def included_symlinks(self) -> List[str]:
        """Return included symlink paths."""
        return self._inc_files

    def excluded_symlinks(self) -> List[str]:
        """Return excluded symlink paths."""
        return self._exc_files


@dataclass
class SourceItems:  # pylint: disable=too-many-instance-attributes
    """Collection of included and excluded files from recursive or single depth
    scan of directory paths. [AssertionError] raised for paths that are not
    found.
    """

    paths: List[str]
    exclude_dirs: Optional[List[str]] = None
    exclude_files: Optional[List[str]] = None
    recursive: bool = True

    def __post_init__(self) -> None:
        self._items: List[SourcePathItems] = []

        globbed_abs_paths: List[str] = []
        for path in self.paths:
            glob_paths = glob.glob(path)
            if not glob_paths:
                raise AssertionError(f"Path [{path}] was not found.")
            for gpath in glob_paths:
                globbed_abs_paths.append(os.path.abspath(gpath))

        # Reassign globbed explicit paths to original paths.
        self.paths = globbed_abs_paths

        for path in self.paths:
            src_path_items = SourcePathItems(source_path=path)
            self._get_path_items(source_path_items=src_path_items)

    def _exclude_dir(self, path: str) -> bool:
        """Exclude directory on canonical path and basename REGEXs."""
        if self.exclude_dirs is not None:
            exclude_dirs_regex = re.compile(rf"^{'|'.join(self.exclude_dirs)}$")
            # Match first on full path.
            match_canonical = re.search(exclude_dirs_regex, path)
            # Match on basename.
            match_basename = re.search(exclude_dirs_regex, os.path.basename(path))
            if match_canonical or match_basename:
                return True

        return False

    def _exclude_file(self, path: str) -> bool:
        """Exclude file on canonical path and basename REGEXs."""
        if self.exclude_files is not None:
            exclude_files_regex = re.compile(rf"^{'|'.join(self.exclude_files)}$")
            # Match first on full path.
            match_canonical = re.search(exclude_files_regex, path)
            # Match on basename.
            match_basename = re.search(exclude_files_regex, os.path.basename(path))
            if match_canonical or match_basename:
                return True

        return False

    def _get_path_items(  # pylint: disable=too-many-statements,too-many-branches
        self,
        source_path_items: SourcePathItems,
    ) -> None:
        """Get path items. Exclude by file/dir."""
        scan_path = source_path_items.source_path()

        item_state: PathItemState
        item_type: PathItemType

        if os.path.isdir(scan_path):
            if not self.recursive:
                scans = os.scandir(scan_path)
                for item in scans:
                    item_state = PathItemState.INCLUDED
                    item_type = PathItemType.OTHER

                    if item.is_dir():
                        item_type = PathItemType.DIRECTORY
                        if self._exclude_dir(path=item.path):
                            item_state = PathItemState.EXCLUDED
                    elif item.is_file():
                        item_type = PathItemType.FILE
                        if self._exclude_file(path=scan_path):
                            item_state = PathItemState.EXCLUDED

                    source_path_items.append(
                        item_state=item_state,
                        item_type=item_type,
                        item=item.path,
                    )

                    if item.is_symlink():
                        source_path_items.append(
                            item_state=item_state,
                            item_type=PathItemType.SYMLINK,
                            item=item.path,
                        )
            else:
                for root, dirs, files in os.walk(
                    scan_path, topdown=True, followlinks=True
                ):
                    item_type = PathItemType.DIRECTORY
                    for wdir in dirs:
                        abs_path = os.path.join(root, wdir)
                        item_state = PathItemState.INCLUDED
                        if self._exclude_dir(path=abs_path):
                            item_state = PathItemState.EXCLUDED

                        source_path_items.append(
                            item_state=item_state,
                            item_type=item_type,
                            item=abs_path,
                        )

                        if os.path.islink(abs_path):
                            source_path_items.append(
                                item_state=item_state,
                                item_type=PathItemType.SYMLINK,
                                item=abs_path,
                            )

                    item_type = PathItemType.FILE
                    for file in files:
                        abs_path = os.path.join(root, file)
                        item_state = PathItemState.INCLUDED
                        if self._exclude_file(path=abs_path):
                            item_state = PathItemState.EXCLUDED

                        source_path_items.append(
                            item_state=item_state,
                            item_type=item_type,
                            item=abs_path,
                        )

                        if os.path.islink(abs_path):
                            source_path_items.append(
                                item_state=item_state,
                                item_type=PathItemType.SYMLINK,
                                item=abs_path,
                            )
        else:
            item_state = PathItemState.INCLUDED
            item_type = PathItemType.OTHER

            # Collect the base dirname.
            base_path = os.path.dirname(scan_path)
            if self._exclude_dir(path=base_path):
                item_state = PathItemState.EXCLUDED

            source_path_items.append(
                item_state=item_state,
                item_type=PathItemType.DIRECTORY,
                item=base_path,
            )

            if os.path.islink(scan_path):
                source_path_items.append(
                    item_state=item_state,
                    item_type=PathItemType.SYMLINK,
                    item=base_path,
                )

            if item_state is PathItemState.EXCLUDED:
                return

            # Address other non directory items.
            item_state = PathItemState.INCLUDED
            item_type = PathItemType.OTHER

            if os.path.isfile(scan_path):
                item_type = PathItemType.FILE

            if self._exclude_file(path=scan_path):
                item_state = PathItemState.EXCLUDED

            source_path_items.append(
                item_state=item_state,
                item_type=item_type,
                item=scan_path,
            )

            if os.path.islink(scan_path):
                source_path_items.append(
                    item_state=item_state,
                    item_type=PathItemType.SYMLINK,
                    item=base_path,
                )

        self._items.append(source_path_items)

    def items(self) -> List[SourcePathItems]:
        """Return list of source path items."""
        return self._items

    def all_included_dirs(self) -> List[str]:
        """Return all included directory paths."""
        dirs: List[str] = []
        for item in self._items:
            dirs.extend(item.included_directories())

        return dirs

    def all_excluded_dirs(self) -> List[str]:
        """Return all excluded directory paths."""
        dirs: List[str] = []
        for item in self._items:
            dirs.extend(item.excluded_directories())

        return dirs

    def all_included_files(self) -> List[str]:
        """Return all included file paths."""
        files: List[str] = []
        for item in self._items:
            files.extend(item.included_files())

        return files

    def all_excluded_files(self) -> List[str]:
        """Return all excluded file paths."""
        files: List[str] = []
        for item in self._items:
            files.extend(item.excluded_files())

        return files

    def all_included_symlinks(self) -> List[str]:
        """Return all included file paths."""
        files: List[str] = []
        for item in self._items:
            files.extend(item.included_symlinks())

        return files

    def all_excluded_symlinks(self) -> List[str]:
        """Return excluded file paths."""
        files: List[str] = []
        for item in self._items:
            files.extend(item.excluded_symlinks())

        return files


@dataclass
class Sys:
    """Collection of sys/os support utilities."""

    logenv: LogEnv

    @staticmethod
    def run(  # pylint: disable=too-many-arguments
        cmd: Union[str, List[str]],
        stdin_input: Optional[Union[bytes, str]] = None,
        shell: bool = False,
        stdin: Any = subprocess.PIPE,
        stderr: Any = subprocess.PIPE,
        stdout: Any = subprocess.PIPE,
        encoding: Optional[EncodeStringCodec] = EncodeStringCodec.UTF_8,
        timeout: Optional[int] = None,
    ) -> Tuple[Optional[Union[bytes, str]], Optional[Union[bytes, str]], int]:
        """Run a system command with optional stdin string. Return a tuple of
        STDOUT, STDERR and the return code.

        The data will be strings if streams were opened in text mode; otherwise,
        bytes.

        shell=False raises OSError exception on error. shell=True does not raise
        exception on error. If intermediate shell errors, error is contained
        in stderr and returncode.

        https://docs.python.org/3.8/library/subprocess.html
        """
        text: bool = True
        encoding_val: Optional[str] = None
        if encoding:
            encoding_val = encoding.value

        if isinstance(stdin_input, bytes):
            encoding_val = None
            text = False

        process = subprocess.Popen(  # pylint: disable=consider-using-with
            cmd,
            shell=shell,
            text=text,
            encoding=encoding_val,
            stdin=stdin,
            stderr=stderr,
            stdout=stdout,
        )

        stdout_output: Any
        stderr_output: Any
        returncode: int
        try:
            if stdin_input is not None:
                stdout_output, stderr_output = process.communicate(
                    input=stdin_input, timeout=timeout
                )
            else:
                stdout_output, stderr_output = process.communicate(timeout=timeout)
            returncode = process.returncode
        except subprocess.TimeoutExpired:
            process.kill()
            stdout_output, stderr_output = process.communicate()
            returncode = process.returncode

        return (stdout_output, stderr_output, returncode)

    @staticmethod
    def get_python_version() -> Tuple[int, int]:
        """Return the python version major and minor."""
        return (sys.version_info.major, sys.version_info.minor)

    @staticmethod
    def get_aws_cli_version() -> Optional[int]:
        """Retrun the AWS CLI version number."""
        response, _, _ = Sys.run(cmd=["aws", "--version"])
        version = None
        if response and isinstance(response, str):
            if re.search(r"aws-cli.{0,1}2", response):
                version = 2
            else:
                version = 1

        return version

    # pylint: disable=too-many-arguments
    @staticmethod
    def write_file(
        file: str,
        data: Union[str, bytes],
        chmod: int = 0o0600,
        append: bool = False,
        encoding: EncodeStringCodec = EncodeStringCodec.UTF_8,
        replace_existing: bool = False,
        make_missing_dirs: bool = False,
        chmod_dir: int = 0o0700,
    ) -> None:
        """Overwrite or append data to file and chmod."""
        if not append and not replace_existing:
            if os.path.exists(file):
                raise AssertionError(
                    f"File [{file}] exists and [replace_existing="
                    f"{replace_existing}]."
                )

        str_open_mode = "wt"
        byte_open_mode = "wb"
        if append:
            str_open_mode = "at"
            byte_open_mode = "ab"

        if make_missing_dirs:
            file_canonical_path = os.path.abspath(file)
            file_directory = os.path.dirname(file_canonical_path)
            if not os.path.exists(path=file_directory):
                os.makedirs(name=file_directory, mode=chmod_dir)

        if isinstance(data, bytes):
            with open(file=file, mode=byte_open_mode) as filer:
                filer.write(data)
                filer.close()
        else:
            with open(
                file=file,
                mode=str_open_mode,
                encoding=encoding.value,
            ) as filer:
                filer.write(data)
                filer.close()

        os.chmod(file, chmod)

    @staticmethod
    def read_file(
        file: str,
        binary: bool = False,
        encoding: EncodeStringCodec = EncodeStringCodec.UTF_8,
    ) -> Union[str, bytes]:
        """Read file data."""
        if binary:
            with open(file=file, mode="rb") as filer:
                data_b = filer.read()
                filer.close()
                return data_b

        with open(
            file=file,
            mode="rt",
            encoding=encoding.value,
        ) as filer:
            data_t = filer.read()
            filer.close()
            return data_t
