import dataclasses

import pytest

import greenplumpython as gp
from greenplumpython.type import to_pg_type
from tests import db


def test_type_cast(db: gp.Database):
    db._execute(
        f"""
        DROP TYPE IF EXISTS complex_number CASCADE;
        CREATE TYPE complex_number AS (r float8, i float8);
        """,
        has_results=False,
    )
    complex_type = gp.type_("complex_number")
    result = db.assign(complex=lambda: complex_type("(1, 2)"))
    for row in result:
        assert row["complex"] == {"i": 2, "r": 1}


def test_type_create(db: gp.Database):
    @dataclasses.dataclass
    class Person:
        _first_name: str
        _last_name: str

    type_name = to_pg_type(Person, db=db)
    assert isinstance(type_name, str)


def test_type_no_annotation(db: gp.Database):
    # Classes with no annotations cannot be used to represent composite types.
    class Person:
        def __init__(self, _first_name: str, _last_name: str) -> None:
            self._first_name = _first_name
            self._last_name = _last_name

    with pytest.raises(Exception) as exc_info:
        to_pg_type(Person, db=db)
    assert "Failed to get annotations" in str(exc_info.value)
