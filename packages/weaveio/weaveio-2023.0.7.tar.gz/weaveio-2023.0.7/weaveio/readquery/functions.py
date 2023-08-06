from typing import Callable, Union, Tuple, Dict, Any
from math import floor, ceil

import numpy as np

from .utilities import mask_infs
from .objects import AttributeQuery, ObjectQuery
from .base import BaseQuery


def _template_operator(string_op: str, name: str, item: BaseQuery, python_func: Callable = None,
                       remove_infs=True, in_dtype=None, out_dtype=None, *args, **kwargs):
    if not isinstance(item, AttributeQuery):
        if python_func is None:
            raise NotImplementedError(f"{name} is not implemented for {type(item)}")
        return python_func(item, *args, **kwargs)
    if remove_infs:
        string_op = string_op.format(mask_infs('{0}'))
    return item._perform_arithmetic(string_op, name, expected_dtype=in_dtype, returns_dtype=out_dtype)


def sign(item, *args, **kwargs):
    return _template_operator('sign({0})', 'sign', item, np.sign, remove_infs=True, out_dtype='float', args=args, kwargs=kwargs)


def exp(item, *args, **kwargs):
    return _template_operator('exp({0})', 'exp', item, np.exp, remove_infs=True, out_dtype='float', args=args, kwargs=kwargs)


def log(item, *args, **kwargs):
    return _template_operator('log({0})', 'log', item, np.log, remove_infs=True, out_dtype='float', args=args, kwargs=kwargs)


def log10(item, *args, **kwargs):
    return _template_operator('log10({0})', 'log10', item, np.log10, remove_infs=True, out_dtype='float', args=args, kwargs=kwargs)


def sqrt(item, *args, **kwargs):
    return _template_operator('sqrt({0})', 'sqrt', item, np.sqrt, remove_infs=True, out_dtype='float', args=args, kwargs=kwargs)

def ismissing(item):
    return _template_operator('{0} is null', 'isnull', item, lambda x: x is None, remove_infs=False, out_dtype='boolean')
isnull = ismissing

def isnan(item):
    return _template_operator('{0} == 1.0/0.0', 'isnan', item, np.isnan, remove_infs=False, out_dtype='boolean')

def _object_scalar_operator(item: ObjectQuery, op_string: str, op_name: str, returns_type: str):
    n, wrt = item._G.add_scalar_operation(item._node, op_string, op_name, parameters=None)
    return AttributeQuery._spawn(item, n, index_node=wrt, single=True, dtype=returns_type, factor_name=op_name)

def neo4j_id(item: ObjectQuery):
    return _object_scalar_operator(item, 'id({0})', 'neo4j_id', 'number')



def switch(item: AttributeQuery, states: Union[Dict[Any, Union[AttributeQuery, Any]], Union[Any, AttributeQuery]],
           _else: Union[Any, AttributeQuery] = None):
    """
    Perform a CASE/SWITCH operation with `item` as the variable to test and with `states` being either:
        - dict of {state: result}
        - result
    So there are two call signatures
    for example:
        >>> switch(query > 1, yes, no)
        >>> switch(query, {1: querya, 2: queryb})
    """
    if not isinstance(item, AttributeQuery):
        raise TypeError(f"`item` must be an AttributeQuery")
    if not isinstance(states, dict):
        states = {True: states}

    dtypes = {result.dtype if isinstance(result, AttributeQuery) else type(result) for result in list(states.values())+[_else]}
    if ObjectQuery in dtypes:
        raise TypeError(f"Switching on objects is not yet supported")
    if dtypes.issubset({'integer', int, np.int, np.int_}):
        dtype = 'integer'
    elif dtypes.issubset({'float', float, np.float, np.float_}):
        dtype = 'float'
    elif dtypes.issubset({'number', float, int, None}):
        dtype = 'number'
    elif dtypes.issubset({'boolean', bool, None}):
        dtype = 'boolean'
    elif dtypes.issubset({'string', str, None}):
        dtype = 'string'
    else:
        raise TypeError(f"All switch result values, including else, must be of the same type. Types given: {dtypes}")
    params = []
    vars = []
    state_list = []
    for i, (k, v) in enumerate(states.items()):
        i *= 2
        kn = f'{{{i}}}'
        vn = f"{{{i+1}}}"
        if not isinstance(k, BaseQuery):
            k = item._G.add_parameter(k)
            params.append(k)
            kn = k
        if not isinstance(v, BaseQuery):
            v = item._G.add_parameter(v)
            params.append(v)
            vn = v
        _switch = f'{kn} THEN {vn}'  # k then v
        state_list.append(_switch)
        vars.append(k)
        vars.append(v)
    if _else is None:
        _else = 'null'
    elif not isinstance(_else, BaseQuery):
        _else = item._G.add_parameter(_else)
        params.append(_else)
        vars.append(_else)

    nodes = [v._node for v in vars if isinstance(v, BaseQuery)]
    switches = ' WHEN '.join(state_list)
    statement = f'CASE {{0}} WHEN {switches} ELSE {_else} END'
    if not nodes:
        n, wrt = item._G.add_scalar_operation(item._node, statement, 'op-switch', parameters=params)
    else:
        n, wrt = item._G.add_combining_operation(statement, 'op-switch', item._node, *nodes, parameters=params)
    return AttributeQuery._spawn(item, n, index_node=wrt, single=True, dtype=dtype, factor_name='switch')