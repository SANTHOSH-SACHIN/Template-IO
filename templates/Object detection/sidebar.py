import streamlit as st


def show():
    """Shows the sidebar components for the template and returns user inputs as dict."""

    inputs = {}

    with st.sidebar:
        st.write(
            "Coming soon! "
        )

    return inputs


if __name__ == "__main__":
    show()

