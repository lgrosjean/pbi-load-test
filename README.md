# pbi-load-test
Python package and CLI application to measure Power BI reports loading capacity, using different filters and parameters.

It simulates a realistic set of user actions such as changing slicers, filters (soon), bookmarks (soon)

## Prerequisites

- It requires and Azure AD login method. Ensure you have [**Azure CLI**](https://learn.microsoft.com/fr-fr/cli/azure/install-azure-cli) installed locally and authentificate (`az login`) in order to generate a token easily. Soon:

> [!NOTE]  
> - Soon: the package will open a Window to authentificate if the Azure login has not be installed
> - Soon: the package will be able to load Service Principal to to the test (Tenant ID, Client ID and Client Secret)

- This package is based on **Selenium** python package. It will open a Chromium window to launch the test. In any case, it may require the Chromium driver locally. The latest versions for each OS can be found [here](https://chromedriver.chromium.org/downloads).

## Configuration

The load test is configurated through a `config.yaml` file which should be located in the current working directory. 

```yaml
# authentification: oauth
workspace: ... # PBI Workspace Name
report: ... # Report name
page: ... # Page name

slicers:
  - table: ... # Table name from dataset which contains the column to filter on
    column: ... # The column name containing the values to filter on
    values:
      - ... # The value to filter on
      - ...
```

> [!NOTE]
> For the moment, only [slicers](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers?tabs=powerbi-desktop) are usable to filter on. Later, [filters](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter?tabs=powerbi-desktop) will be available.
> Also, one slicer can be used in this first version. In the future, the tool will be able to iterate between slicers list and create combinations between slicer and filter values.
> 
## Example

It ensures that a `config.yaml` file exists in the current working directory

> [!NOTE]  
> The package will in the future be able to parse `config.yaml` file from different project through the CLI application.

```
❯ poetry run pbi-load-test run

CORE - MARKETING [DEV]
SFE Country Dashboard TMDL
Activity Field Days
Workspace ID: 310d9fbb-1474-4939-bcb8-669a536ec959
Report ID: c89485c6-e0c3-4715-a710-ddd450491a9a
groups/310d9fbb-1474-4939-bcb8-669a536ec959/reports/c89485c6-e0c3-4715-a710-ddd450491a9a/pages
Page ID: ReportSectioncbd8077dfb6a167ccb5e
Duration: 30.085
Press Enter to continue...
```

<img width="1312" alt="Capture_d’écran_2023-09-04_à_08_32_04_bis" src="https://github.com/lgrosjean/pbi-load-test/assets/34337781/2373d37e-c1c8-4338-8255-b4d0a1dc9284">

After the test, all created files will be removed.