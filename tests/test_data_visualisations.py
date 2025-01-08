import os

# Test for the existence of the updated figure
def test_updated_figure_exists():
    figure_path = './figures/cost_by_income_group_with_gridline.png'
    assert os.path.exists(figure_path), f"Updated figure not found at {figure_path}"

# Test for archive of old figure
def test_old_figure_archived():
    archived_path = './archive/cost_by_income_group.png'
    assert os.path.exists(archived_path), f"Old figure not found in archive at {archived_path}"

# Test that the old figure is no longer in the figures folder
def test_old_figure_removed_from_figures_folder():
    old_figure_path = './figures/cost_by_income_group.png'
    assert not os.path.exists(old_figure_path), f"Old figure still exists in /figures/ folder at {old_figure_path}"
