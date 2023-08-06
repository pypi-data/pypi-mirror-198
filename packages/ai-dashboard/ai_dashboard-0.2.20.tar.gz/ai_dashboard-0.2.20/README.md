# RelevanceAI Explore App SDK

### Installation

```bash
pip install ai_dashboard
```

This repo is for managing/configuring deployables through a Python SDK.

# How to

## Eplore

Instantiate the Client

```python

from ai_dashboard import Client
client = Client(token=os.getenv("TOKEN"))

```

Load your most recently updated deployable...

```python
deployable = client.recent()
```

...or call it with its unique `deployabled_id`.

```python
deployable = client.Deployable(deployabled_id="")
```

...or from `dataset_id` and `dashboard name`

```python
dashboard = client.Dashboard(dataset_id=..., name=...)
```

Make edits to the `config` as you see fit.
Once done, simply...

```python
deployable.push()
```

To retrieve edits made in the browser...

```python
deployable.pull()
```

## Data Report

```python
dashboard = client.Dashboard(
    dataset_id="iris-csv",
    name="My Dashboard" # Dashboard Name
)

tab = dashboard.DataReport(
    title="My 2nd Report" # Report Tab Title
)

tab.add_markdown("""# My Report
## Sub Heading
Below is average *Petal Width* and minimum **Petal Length**
""")

tab.add_metric(
    query=[
        {
            "name": "avg Petal Width",
            "field": "petal_width",
            "agg": "avg",
        },
        {
            "name": "min Petal Length",
            "field": "petal_length",
            "agg": "min",
        },
    ],
)

tab.add_image("path/to/image.jpg")

tab.add_markdown("Below is an aggregation chart")

tab.add_aggregation(
    groupby=[
        {
            "agg": "category",
            "field": "variety",
            "name": "groupby 1",
        }
    ],
    metric=[
        {
            "name": "avg Sepal Length",
            "field": "sepal_length",
            "agg": "avg",
        }
    ],
)

deployable.push()
```

## Document View


```python
dashboard = client.Dashboard(
    dataset_id="iris-csv",
    name="My Dashboard" # Dashboard Name
)

tab = dashboard.DocumentView(title="My Document View")
tab.set_metric(metric="PetalLengthCm")

deployable.push()
```

## Category View



```python
dashboard = client.Dashboard(
    dataset_id="iris-csv",
    name="My Dashboard" # Dashboard Name
)

tab = dashboard.CategoryView(title="My Category View")
tab.set_view(
    primary_field="PetalLengthCm",
    secondary_field="SepalWidthCm",
)

deployable.push()
```

## Chart View

TBA

## Report View Example

```python
app = DASHBOARD_CLIENT.DataReport(title=REPORT_APP_TITLE)

app.reset()
app.add_blocks([
    bl.H1("Heading 1"),
    bl.H2("Heading 2"),
    bl.H3("Heading 3"),
    bl.P("Paragraph"),
    bl.P(
        bl.BoldMark("bolded paragraph")
    ),
    bl.H1(
        bl.ItalicMark("italic heading")
    ),
    
    bl.Plotly(plotly_fig),
    bl.Altair(altair_fig),
    
    bl.Code("""
    import pandas as pd
    df = pd.read_csv("data.csv")"""),
    
    bl.UnorderedList([
        "Item 1",
        "Item 2",
        "Item 3"
    ]),
    bl.Space(),
    bl.OrderedList([
        "Item 1",
        "Item 2",
        "Item 3"
    ]),
    bl.Space(),
    bl.UnorderedList([
        [ bl.ItalicMark([bl.BoldMark("Item:")]), "1" ],
        "Item 2",
        "Item 3"
    ]),
    
    bl.Columns([
        bl.ColumnContent([bl.Plotly(plotly_fig)]),
        bl.ColumnContent([bl.Plotly(plotly_fig), "this is some extra txt for the column"]),
    ]),
    bl.Quote([
        bl.Plotly(plotly_fig)
    ]),
    bl.Card([
        bl.Plotly(plotly_fig),
        "coolio"
    ], width=500, color="blue"),
    bl.Tooltip([
        bl.Plotly(plotly_fig),
    ], tooltip_text="extra coolio"),
])
```
