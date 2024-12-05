"""Run or update the project. This file uses the `doit` Python package. It works
like a Makefile, but is Python-based
"""

from pathlib import Path
OUTPUT_DIR = Path("./")
NOTEBOOK_BUILD_DIR = Path("./")

# fmt: off
## Helper functions for automatic execution of Jupyter notebooks
def jupyter_execute_notebook(notebook):
    return f"jupyter nbconvert --execute --to notebook --ClearMetadataPreprocessor.enabled=True --inplace {notebook}.ipynb"
def jupyter_to_html(notebook):
    return f"jupyter nbconvert --to html --output-dir='./' {notebook}.ipynb"
def jupyter_to_md(notebook):
    """Requires jupytext"""
    return f"jupytext --to markdown {notebook}.ipynb"
def jupyter_to_python(notebook, build_dir):
    """Requires jupytext"""
    return f"jupyter nbconvert --to python {notebook}.ipynb --output {notebook}.py --output-dir {build_dir}"
def jupyter_clear_output(notebook):
    return f"jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --inplace {notebook}.ipynb"
# fmt: on


# def copy_notebook_to_folder(notebook, destination_folder):
#     destination_path = Path(destination_folder) / f"_{notebook}.ipynb"
#     return f"cp  {notebook}.ipynb {destination_path}"


def task_pull_data():
    """ """
    file_dep = ["load_fred.py", "load_ofr_api_data.py"]
    file_output = [
        "fred_repo_related_data.parquet",
        "fred_repo_related_data_all.parquet",
        "ofr_public_repo_data.parquet",
    ]
    targets = [DATA_DIR / "pulled" / file for file in file_output]

    return {
        "actions": [
            "ipython ./load_fred.py",
            "ipython ./load_ofr_api_data.py",
        ],
        "targets": targets,
        "file_dep": file_dep,
    }


def task_convert_notebooks_to_scripts():
    """Converts notebooks to .py scripts. This is used for
    version control. Changes to these files trigger execution.
    """

    notebooks = [
        "repo_spikes.ipynb",
    ]
    file_dep = notebooks
    stems = [notebook.split(".")[0] for notebook in notebooks]
    targets = [NOTEBOOK_BUILD_DIR / f"{stem}.py" for stem in stems]

    actions = [
        # *[jupyter_execute_notebook(notebook) for notebook in notebooks_to_run],
        # *[jupyter_to_html(notebook) for notebook in notebooks_to_run],
        # *[jupyter_clear_output(notebook) for notebook in stems],
        *[jupyter_to_python(notebook, NOTEBOOK_BUILD_DIR) for notebook in stems],
    ]
    return {
        "actions": actions,
        "targets": targets,
        "task_dep": [],
        "file_dep": file_dep,
    }


def task_run_notebooks():
    """Preps the notebooks for presentation format.
    Execute notebooks with summary stats and plots and remove metadata.
    """
    notebooks_to_run = [
        "repo_spikes.ipynb",
    ]
    stems = [notebook.split(".")[0] for notebook in notebooks_to_run]

    file_dep = [
        # Dependers:
        ## repo_spikes.ipynb
        "load_merged_repo_data.py",
        "load_fred.py",
        "load_ofr_api_data.py",
        *[NOTEBOOK_BUILD_DIR / f"{stem}.py" for stem in stems],
    ]

    targets = [
        ## repo_spikes.ipynb output
        # OUTPUT_DIR / 'is_spike.csv',
        ## Notebooks converted to HTML
        *[OUTPUT_DIR / f"{stem}.html" for stem in stems],
    ]

    actions = [
        *[jupyter_execute_notebook(notebook) for notebook in stems],
        # *[copy_notebook_to_folder(notebook, Path('../../../lectures/Week1')) for notebook in stems],
        *[jupyter_to_html(notebook) for notebook in stems],
        *[jupyter_clear_output(notebook) for notebook in stems],
        # *[jupyter_to_python(notebook, NOTEBOOK_BUILD_DIR) for notebook in notebooks_to_run],
    ]
    return {
        "actions": actions,
        "targets": targets,
        "task_dep": [],
        "file_dep": file_dep,
    }
