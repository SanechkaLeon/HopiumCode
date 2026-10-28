from hopiumcode.prompts import SYSTEM_PROMPT, ENRICHED_TEMPLATE


def test_templates_have_placeholders():
    assert "{repo_name}" in SYSTEM_PROMPT
    for key in ("{question}", "{context_blocks}", "{graph_facts}"):
        assert key in ENRICHED_TEMPLATE
