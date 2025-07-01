from django.db.models import CheckConstraint, Q, F


class Constraint:
    cannot_be_self_parent_constraint = CheckConstraint(
        name="cannot_be_self_parent",
        check=~Q(parent_id=F("id")),
    )
