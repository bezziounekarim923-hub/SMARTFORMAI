from backend.core.layout.smart_layout_analyzer import SmartLayoutAnalyzer
from backend.models.form_field import FormField
from backend.models.rectangle import Rectangle


def test_detect_tables_returns_only_large_rectangles():
    analyzer = SmartLayoutAnalyzer()

    rectangles = [
        Rectangle(x=10, y=10, width=200, height=100),
        Rectangle(x=20, y=20, width=50, height=20),
        Rectangle(x=30, y=30, width=160, height=90),
    ]

    tables = analyzer._detect_tables(rectangles)

    assert len(tables) == 2
    assert all(table.width >= 150 for table in tables)


def test_detect_option_groups_groups_nearby_checkboxes_and_radios():
    analyzer = SmartLayoutAnalyzer()

    fields = [
        FormField(
            id="1",
            page=1,
            label="",
            field_type="checkbox",
            rectangle=Rectangle(x=10, y=10, width=30, height=30),
        ),
        FormField(
            id="2",
            page=1,
            label="",
            field_type="checkbox",
            rectangle=Rectangle(x=55, y=12, width=30, height=30),
        ),
        FormField(
            id="3",
            page=1,
            label="",
            field_type="radio",
            rectangle=Rectangle(x=12, y=70, width=40, height=40),
        ),
    ]

    groups = analyzer._detect_option_groups(fields)

    assert len(groups) == 1
    assert len(groups[0]) == 2
    assert all(field.field_type in {"checkbox", "radio"} for field in groups[0])
