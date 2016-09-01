# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException


class Error(Exception):
    """Base Module Exception."""
    pass


class FileException(Error):
    """
    Base file exception.Thrown when a file is not available.

    For example, file not exists.
    """
    pass


class DataFileNotAvailableException(FileException):
    """
    Thrown when data file not available.
    """
    pass


class SheetTypeError(Error):
    """
    Thrown when sheet type passed in not int or str.
    """
    pass


class SheetError(Error):
    """
    Thown when specified sheet not exists.
    """
    pass


class DataError(Error):
    """
    Thrown when something wrong with the data.
    """
    pass


class LogFileNotAvailableException(FileException):
    """
    Thrown when log file not available.
    """
    pass


class LogError(Error):
    """
    Thrown when something wrong when logging.
    """
    pass


class ReportFileNotAvailableException(FileException):
    """
    Thrown when report file not available.
    """
    pass


class ReportError(Error):
    """
    Thrown when something wrong when generate the report file.
    """
    pass


class DriverNotExistsException(WebDriverException):
    """
    Thrown when driver not exists.
    """
    pass


class UnSupportBrowserTypeException(WebDriverException):
    """
    Thrown when the browser type not support.
    """
    pass


class ParameterError(Error):
    """
    Thrown when pass wrong parameter to a method.
    """
    pass

