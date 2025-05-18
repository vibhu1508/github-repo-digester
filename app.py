import streamlit as st
from utils import fetch_repo_files

st.title("GitHub Repo Codebase Digester")

repo_url = st.text_input("Enter GitHub Repository URL:")

if st.button("Generate Digest"):
    if repo_url:
        try:
            parts = repo_url.rstrip("/").split("/")
            owner, repo = parts[-2], parts[-1]

            with st.spinner("Fetching files..."):
                files = fetch_repo_files(owner, repo)
                digest = ""
                for path, code in files:
                    digest += f"\n# File: {path}\n\n{code}\n"

                st.success("Digest generated successfully!")
                st.download_button("Download Digest", digest, file_name="digest.txt")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid GitHub URL.")