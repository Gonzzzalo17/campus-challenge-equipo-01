from challenge_tools import unique_tags


def test_unique_tags_preserves_first_occurrence_order_and_is_case_sensitive():
    # R-07: se conserva la primera aparición y el orden original;
    # la comparación distingue mayúsculas y minúsculas, por lo que
    # "Tag" y "tag" son etiquetas distintas.
    assert unique_tags(["b", "a", "b", "Tag", "tag", "a"]) == [
        "b",
        "a",
        "Tag",
        "tag",
    ]