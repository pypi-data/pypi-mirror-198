#-*- coding: utf-8 -*-
# pylint: disable=protected-access

"""This module provides the Field class. It is used by the `relation <#module-half_orm.relation>`_ module."""

import psycopg2

from half_orm.null import NULL

class Field():
    """The class Field is for Relation internal usage. It is called by
    the RelationFactory metaclass for each field in the relation considered.
    """
    def __init__(self, name, relation, metadata):
        self.__relation = relation
        self.__name = name
        self.__is_set = False
        self.__metadata = metadata
        self.__sql_type = self.__metadata['fieldtype']
        self.__value = None
        self.__unaccent = False
        self.__comp = '='

    @property
    def _relation(self): # pragma: no cover
        return self.__relation

    def is_set(self):
        "Returns if the field is set or not."
        return self.__is_set

    def _is_part_of_pk(self):
        "Returns True if the field is part of the PK"
        return bool(self.__metadata['pkey'])

    def is_not_null(self):
        "Returns True if the field is defined as not null."
        return bool(self.__metadata['notnull'])

    def __repr__(self):
        md_ = self.__metadata
        field_constraint = f"{md_['notnull'] and 'NOT NULL' or ''}"
        repr_ = f"({md_['fieldtype']}) {field_constraint}"
        if self.__is_set:
            repr_ = f"{repr_} ({self.__name} {self.__comp} {self.__value})"
        return repr_.strip()

    def __str__(self):
        return str(self.__value)

    def _praf(self, query, _ho_id):
        """Returns field_name prefixed with relation alias if the query is
        select. Otherwise, returns the field name quoted with ".
        """
        _ho_id = f'r{_ho_id}'
        if query == 'select':
            return f'{_ho_id}."{self.__name}"'
        return f'"{self.__name}"'

    def _where_repr(self, query, _ho_id):
        """Returns the SQL representation of the field for the where clause
        """
        where_repr = ''
        comp_str = '%s'
        comp = self._comp()
        if comp == '@@':
            comp_str = 'websearch_to_tsquery(%s)'
        if isinstance(self.__value, (list, tuple)):
            if self.__sql_type[0] != '_': # not an array type
                comp_str = 'any(%s)'
                if comp == '@@':
                    comp_str = 'any(websearch_to_tsquery(%s))'
        if not self.unaccent:
            where_repr = f"{self._praf(query, _ho_id)} {comp} {comp_str}"
        else:
            where_repr = f"unaccent({self._praf(query, _ho_id)}) {comp} unaccent({comp_str})"
        return where_repr

    @property
    def value(self):
        "Returns the value of the field object"
        return self.__value

    def _set(self, *args):
        "Sets the value of the field object"
        self.__set__(self.__relation, *args)

    def __set__(self, obj, *args):
        """Sets the value (and the comparator) associated with the field."""
        self.__relation._ho_is_singleton = False
        value = args[0]
        if value is None:
            self._unset()
            return
        comp = None
        self.__relation = obj
        if isinstance(value, tuple):
            if len(value) != 2:
                raise ValueError(f"Can't match {value} with (comp, value)!")
            comp, value = value
        if value is None:
            raise ValueError("Can't have a None value with a comparator!")
        if value is NULL and comp is None:
            comp = 'is'
        elif comp is None:
            comp = '='
        comp = comp.lower()
        if value is NULL:
            if not comp in {'is', 'is not'}:
                raise ValueError("comp should be 'is' or 'is not' with NULL value!")
        self.__is_set = True
        self.__value = value
        self.__comp = comp

    def _unset(self):
        "Unset a field"
        self.__is_set = False
        self.__value = None
        self.__comp = '='

    @property
    def unaccent(self):
        return self.__unaccent
    @unaccent.setter
    def unaccent(self, value):
        if not isinstance(value, bool):
            raise RuntimeError('unaccent value must be True or False!')
        self.__unaccent = value

    def _comp(self):
        "Returns the comparator associated to the value."
        if self.__comp == '%':
            return '%%'
        return self.__comp

    @property
    def _relation(self):
        """Internal usage.

        Returns:
            Relation: The Relation class for which self is an attribute.
        """
        return self.__relation

    def _psycopg_adapter(self):
        """Return the SQL representation of self.__value"""
        return psycopg2.extensions.adapt(self.__value)

    @property
    def _name(self):
        return self.__name

    def __call__(self):
        """In case someone inadvertently uses the name of a field for a method."""
        rel_class = self.__relation.__class__
        rcn = rel_class.__name__
        method = rel_class.__dict__.get(self.__name)
        err_msg = "'Field' object is not callable."
        warn_msg = f"'{self.__name}' is an attribute of type Field of the '{rcn}' object."
        if method:
            err_msg = f"{err_msg}\n{warn_msg}"
            err_msg = f"{err_msg}\nDo not use '{self.__name}' as a method name."
        raise TypeError(err_msg)

psycopg2.extensions.register_adapter(Field, Field._psycopg_adapter)
psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)
