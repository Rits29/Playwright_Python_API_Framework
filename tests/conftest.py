import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def apicontext():
    with sync_playwright() as p:
        context = p.request.new_context()
        yield context
        context.dispose()

'''Setup the environment option for pytest. This allows you to specify the execution environment (qa or prod) when 
running tests.'''
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Execution environment (qa, prod)"
    )
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

# ***Generate Pytest HTML Report*** to do so we add hooks to conftest.py file.
@pytest.hookimpl(optionalhook=True)
def pytest_html_metadata(metadata):
    metadata['Project Name'] = 'Playwright Python API automation Framework'
    metadata['Scope'] = 'Covers API flow for RESTAPI, GRAPHQL, MAP, OAuth'
    metadata['Tester'] = 'Rits'
# It is hook for modify//delete environment information in the HTML report.
    metadata.pop('JAVA_HOME', None)  # Remove JAVA_HOME from metadata
    metadata.pop('Plugins', None)  # Remove Plugins from metadata

