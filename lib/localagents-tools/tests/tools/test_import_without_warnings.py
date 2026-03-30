from pydantic.warnings import PydanticDeprecatedSince20
import pytest


@pytest.mark.filterwarnings("error", category=PydanticDeprecatedSince20)
def test_import_tools_without_pydantic_deprecation_warnings():
    # This test is to ensure that the import of localagents_tools does not raise any Pydantic deprecation warnings.
    import localagents_tools

    assert localagents_tools
