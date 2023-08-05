from . import stag_internal
import scipy.sparse
import inspect
import numpy as np

##
# \cond
# This file is currently listed as an explicit exception in the doxyfile.
# It will not be processed for documentation at all.
##

def swig_sprs_to_scipy(swig_mat):
    """
    Take a swig sparse matrix and convert it to a scipy sparse matrix.
    """
    outer_starts = stag_internal.sprsMatOuterStarts(swig_mat)
    inner_indices = stag_internal.sprsMatInnerIndices(swig_mat)
    values = stag_internal.sprsMatValues(swig_mat)
    return scipy.sparse.csc_matrix((values, inner_indices, outer_starts))


def scipy_to_swig_sprs(scipy_mat: scipy.sparse.csc_matrix):
    """
    Take a scipy sparse matrix and convert it to a swig sprs matrix.
    """
    col_starts = stag_internal.vectorl(scipy_mat.indptr.tolist())
    row_indices = stag_internal.vectorl(scipy_mat.indices.tolist())
    values = stag_internal.vectord(scipy_mat.data.tolist())
    return stag_internal.sprsMatFromVectors(col_starts,
                                            row_indices,
                                            values)


def return_sparse_matrix(func):
    def decorated_function(*args, **kwargs):
        swig_sparse_matrix = func(*args, **kwargs)
        sp_sparse = swig_sprs_to_scipy(swig_sparse_matrix)
        del swig_sparse_matrix
        return sp_sparse

    # Set the metadata of the returned function to match the original.
    # This is used when generating the documentation
    decorated_function.__doc__ = func.__doc__
    decorated_function.__module__ = func.__module__
    decorated_function.__signature__ = inspect.signature(func)

    return decorated_function


def possibly_convert_ndarray(argument):
    """
    Check whether argument is a numpy ndarray.
    If it is, convert it to a list. Otherwise return it as-is.
    """
    if isinstance(argument, np.ndarray):
        return argument.tolist()
    else:
        return argument


def convert_ndarrays(func):
    """A decorator for methods which take lists as arguments.
    Converts *all* ndarrays in the arguments to lists."""
    def decorated_function(*args, **kwargs):
        new_args = [possibly_convert_ndarray(arg) for arg in args]
        new_kwargs = {k: possibly_convert_ndarray(v) for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)


    # Set the metadata of the returned function to match the original.
    # This is used when generating the documentation
    decorated_function.__doc__ = func.__doc__
    decorated_function.__module__ = func.__module__
    decorated_function.__signature__ = inspect.signature(func)

    return decorated_function

##
# \endcond
##
