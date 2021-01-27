
class BiograderError(Exception):
    """Base class for all exceptions we'll raise."""
    pass


class NoInternetError(BiograderError):
    """No internet."""
    pass


class HttpResponseError(BiograderError):
    """There was a problem with an HTTP response."""
    pass


class InvalidParameterError(BiograderError):
    """Invalid parameter."""
    pass


class AmbiguousLatestError(InvalidParameterError):
    """They pass "latest" for a version parameter, but index latest does not match latest version locally installed."""
    pass


class FileError(BiograderError):
    """Base class for data-related errors."""
    pass


class DatasetNotInstalledError(FileError):
    """They requested a dataset they haven't installed."""
    pass


class DataVersionNotInstalledError(FileError):
    """They requested a version they haven't installed of a dataset."""
    pass


class PackageCannotHandleDataVersionError(BiograderError):
    """They tried to load a new version of the data, but they have an old version of the package that doesn't have the code for the new data, so they need to update the package. """
    pass


class MissingFileError(FileError):
    """A data file was missing."""
    pass


class DataError(BiograderError):
    """Something was wrong with the data."""
    pass


class ReindexMapError(DataError):
    """Problem reindexing a dataframe."""
    pass


class DropFromSingleIndexError(DataError):
    """They tried to drop a level from a single-level index."""
    pass


class NoDefinitionsError(DataError):
    """They tried to access definitions for a dataset that doesn't provide any."""
    pass


class DataFrameNotIncludedError(DataError):
    """They requested a dataframe that's not included in the dataset."""
    pass


# Warnings
class BiograderWarning(UserWarning):
    """Base class for all warnings we'll generate."""
    pass


class FailedReindexWarning(BiograderWarning):
    """Error reindexing a dataframe."""
    pass


class InsertedNanWarning(BiograderWarning):
    """NaNs were inserted during a dataframe join."""
    pass


class DuplicateColumnHeaderWarning(BiograderWarning):
    """Due to a requested column multiindex flattening, the column index now has duplicate labels."""
    pass


class FlattenSingleIndexWarning(BiograderWarning):
    """They tried to flatten a single-level index. We didn't do anything."""
    pass


class FilledMutationDataWarning(BiograderWarning):
    """Mutation data was automatically filled during a dataframe join."""
    pass


class ParameterWarning(BiograderWarning):
    """We should warn them about a parameter for some reason."""
    pass


class OldDataVersionWarning(BiograderWarning):
    """They're using an old data version."""
    pass


class OldPackageVersionWarning(BiograderWarning):
    """They're using an old version of the package."""
    pass


class PublicationEmbargoWarning(BiograderWarning):
    """There is a publication embargo on the dataset."""
    pass


class DownloadingNewLatestWarning(BiograderWarning):
    """Downloading a new latest data version. If they want to use an old version, they'll have to manually specify it."""
    pass


class FileNotUpdatedWarning(BiograderWarning):
    """A file they wanted to update wasn't updated."""
    pass


# Developer-directed exceptions
class BiograderDevError(Exception):
    """For exceptions that are probably the developer's fault."""
    pass