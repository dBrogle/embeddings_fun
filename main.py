import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from states_graph import get_all_state_names, graph_state_data
from states_queries import SAMPLE_STATE_QUERIES
from util.get_embeddings import get_embedding


def run_states_graph_with_phrase(phrase: str):
    # Get the embedding for the value
    phrase_embedding = get_embedding(phrase)

    # Get the embeddings for all the states
    state_names = get_all_state_names()
    state_similarities = [
        cosine_similarity([phrase_embedding], [get_embedding(state_name)])[0][0]
        for state_name in state_names
    ]

    # Format state embeddings as a dataframe
    state_similarities_df = pd.DataFrame(
        {"name": state_names, "value": state_similarities}
    )

    # Multiply all values by 100 ([0,1] -> [0,100])
    state_similarities_df["value"] = state_similarities_df["value"] * 100

    # Sort the states by similarity
    state_similarities_df = state_similarities_df.sort_values(
        by="value", ascending=False
    )

    # Get the top 5 and bottom 5 as strings (State: Score)
    top_5 = state_similarities_df.head(5)
    bottom_5 = state_similarities_df.tail(5)
    top_5_strings = [
        f"{row['name']}: {row['value']:.1f}" for index, row in top_5.iterrows()
    ]
    bottom_5_strings = [
        f"{row['name']}: {row['value']:.1f}" for index, row in bottom_5.iterrows()
    ]
    top_5_str = "\n".join(top_5_strings)
    bottom_5_str = "\n".join(bottom_5_strings)

    # Graph the states
    graph_state_data(state_similarities_df, top_5_str, bottom_5_str, title=f"{phrase}")


def run_states_graphs_with_list_of_phrases(phrases: list[str]):
    for phrase in phrases:
        run_states_graph_with_phrase(phrase)


def main_run_graphs_with_phrases(save_as_images: bool = False):
    print("Running graphs with phrases...")
    print("\n".join(SAMPLE_STATE_QUERIES))
    print("To change the phrases, edit the SAMPLE_STATE_QUERIES variable")

    run_states_graphs_with_list_of_phrases(SAMPLE_STATE_QUERIES)
    # Save all of them as images
    if save_as_images:
        print("Saving all graphs as images...")
        for i in plt.get_fignums():
            fig = plt.figure(i)
            fig.savefig(f"graphs/figure_tab_{i}.png", dpi=300)
    plt.show()


def main():
    main_run_graphs_with_phrases(save_as_images=False)


if __name__ == "__main__":
    main()
