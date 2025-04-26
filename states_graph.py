import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from util.constants import ShapeFiles


def get_all_state_names() -> list[str]:
    states = gpd.read_file(ShapeFiles.US_STATES.value)
    return list(states["name"])


def get_country_names_by_filter(filter_column: str, filter_value: str) -> list[str]:
    world = gpd.read_file(ShapeFiles.WORLD.value)
    return list(world[world[filter_column] == filter_value]["NAME"])


def graph_state_data(
    data: pd.DataFrame, top_5_str: str, bottom_5_str: str, title: str = "US Values"
) -> None:
    states = gpd.read_file(ShapeFiles.US_STATES.value)
    # Merge the data with the GeoDataFrame
    states = states.merge(data, on="name", how="left")

    # Plot the map
    # Get new figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    states.plot(
        column="value",
        ax=ax,
        legend=True,
        legend_kwds={
            "shrink": 0.8,  # Makes the colorbar 80% of its original height
            "orientation": "vertical",
            "aspect": 20,  # Keeps it thin
        },
        cmap="coolwarm",
        edgecolor="black",
        linewidth=0.5,
        missing_kwds={"color": "lightgrey", "label": "No data"},
    )
    fig.suptitle(title, fontsize=20, y=0.95)
    ax.axis("off")
    # Combine the text
    full_text = f"Top 5:\n{top_5_str}\n\nBottom 5:\n{bottom_5_str}"

    # Place text on the left side of the plot, vertically centered
    ax.text(
        x=0.3,  # relative figure coords
        y=0.4,
        s=full_text,
        transform=ax.transAxes,
        fontsize=12,
        va="center",
        ha="left",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.5"),
    )

    # Make it tight
    plt.tight_layout()

    # Adjust margins - left, bottom, right, top
    plt.subplots_adjust(left=-0.2, bottom=0, right=1.1, top=1)


# Haven't used this, try it at your own peril
def graph_world_subset_data(data: pd.DataFrame, title: str = "World Values") -> None:
    world = gpd.read_file(ShapeFiles.WORLD.value)

    data_names = list(data["NAME"])
    print(f"Data Names: {data_names}")

    # Filter world to only include items that appear in data
    world = world[world["NAME"].isin(data_names)]

    # Merge with world GeoDataFrame
    world = world.merge(data, on="NAME", how="left")

    # Plot
    fig, ax = plt.subplots(figsize=(15, 10))
    world.plot(
        column="value",
        ax=ax,
        legend=True,
        cmap="YlGnBu",
        edgecolor="black",
        missing_kwds={"color": "lightgrey", "label": "No data"},
    )
    ax.set_title(title, fontsize=15)
    ax.axis("off")


# Also haven't used this, same thing (try at your own peril)
def graph_europe_data(data: pd.DataFrame, title: str = "Europe Values") -> None:
    world = gpd.read_file(ShapeFiles.WORLD.value)

    # Merge with world GeoDataFrame
    world = world.merge(data, on="NAME", how="left")

    # Plot
    fig, ax = plt.subplots(figsize=(15, 10))
    world.plot(
        column="value",
        ax=ax,
        legend=True,
        cmap="YlGnBu",
        edgecolor="black",
        missing_kwds={"color": "lightgrey", "label": "No data"},
    )
    ax.set_title(title, fontsize=15)
    ax.axis("off")
