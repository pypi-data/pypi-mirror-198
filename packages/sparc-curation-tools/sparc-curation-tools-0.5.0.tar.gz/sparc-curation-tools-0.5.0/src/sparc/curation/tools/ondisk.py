import csv
import json
import os
from pathlib import Path
import pandas as pd


try:
    from sparc.curation.tools.plot_utilities import create_thumbnail_from_plot
    px = True
except ImportError:
    create_thumbnail_from_plot = None
    px = None


from sparc.curation.tools.base import Singleton

ZINC_GRAPHICS_TYPES = ["points", "lines", "surfaces", "contours", "streamlines"]


def _is_graphics_entry(entry):
    if 'URL' in entry and 'Type' in entry:
        entry_type = entry['Type']
        if entry_type.lower() in ZINC_GRAPHICS_TYPES:
            return True

    return False


def _is_view_entry(entry):
    if 'URL' in entry and 'Type' in entry:
        entry_type = entry['Type']
        if entry_type.lower() == "view":
            return True

    return False


def test_for_metadata(json_data):
    have_viewable_graphics = False
    have_view_reference = False
    if json_data:
        if isinstance(json_data, list):
            for entry in json_data:
                if not have_viewable_graphics and _is_graphics_entry(entry):
                    have_viewable_graphics = True
                if not have_view_reference and _is_view_entry(entry):
                    have_view_reference = True

    return have_view_reference and have_viewable_graphics


def test_for_view(json_data):
    is_view = False
    if json_data:
        if isinstance(json_data, dict):
            expected_keys = ["farPlane", "nearPlane", "upVector", "targetPosition", "eyePosition"]
            missing_key = False
            for expected_key in expected_keys:
                if expected_key not in json_data:
                    missing_key = True

            is_view = not missing_key

    return is_view


def get_plot(csv_file, is_tsv=False):
    if is_tsv:
        plot_df = pd.read_csv(csv_file, sep='\t')
    else:
        plot_df = pd.read_csv(csv_file)
    plot_df.columns = plot_df.columns.str.lower()
    plot = None
    x_loc = 0
    y_loc = []
    if "time" in plot_df.columns:
        if plot_df["time"].is_monotonic_increasing and plot_df["time"].is_unique:
            x_loc = plot_df.columns.get_loc("time")
            if x_loc != 0:
                y_loc = list(range(x_loc + 1, len(plot_df.columns)))
            plot = OnDiskFiles.Plot(csv_file, "timeseries", x=x_loc, y=y_loc)
        else:
            plot = OnDiskFiles.Plot(csv_file, "heatmap")
    else:
        if is_tsv:
            plot_df = pd.read_csv(csv_file, header=None, sep='\t')
        else:
            plot_df = pd.read_csv(csv_file, header=None)
        for column in plot_df.columns[:3]:
            if plot_df[column].is_monotonic_increasing and plot_df[column].is_unique:
                if x_loc != 0:
                    y_loc = list(range(x_loc + 1, len(plot_df.columns)))
                plot = OnDiskFiles.Plot(csv_file, "timeseries", x=x_loc, y=y_loc, no_header=True)
                break
            x_loc += 1
        if not plot:
            plot = OnDiskFiles.Plot(csv_file, "heatmap", no_header=True)
    return plot


def is_context_data_file(json_data):
    if json_data:
        if isinstance(json_data, dict):
            # "version" and "id" are required keys for a context data file.
            if "version" in json_data and "id" in json_data:
                return json_data["id"] == "sparc.science.context_data"

    return False


def is_annotation_csv_file(csv_reader):
    if csv_reader:
        first = True
        for row in csv_reader:
            if first:
                if len(row) == 2 and row[0] == "Term ID" and row[1] == "Group name":
                    first = False
                else:
                    return False
            elif len(row) != 2:
                return False

        return True

    return False


def is_json_of_type(r, max_size, test_func):
    result = False
    if os.path.getsize(r) < max_size and os.path.isfile(r):
        try:
            with open(r, encoding='utf-8') as f:
                file_data = f.read()
        except UnicodeDecodeError:
            return result
        except IsADirectoryError:
            return result

        try:
            data = json.loads(file_data)
            result = test_func(data)
        except json.decoder.JSONDecodeError:
            return result

    return result


def is_csv_of_type(r, max_size, test_func):
    result = False
    if os.path.getsize(r) < max_size and os.path.isfile(r):
        try:
            with open(r, encoding='utf-8') as f:
                csv_reader = csv.reader(f)
                result = test_func(csv_reader)
        except UnicodeDecodeError:
            return result
        except IsADirectoryError:
            return result
        except csv.Error:
            return result

    return result


def get_view_urls(metadata_file):
    view_urls = []
    try:
        with open(metadata_file, encoding='utf-8') as f:
            file_data = f.read()
        json_data = json.loads(file_data)
        if json_data:
            if isinstance(json_data, list):
                for entry in json_data:
                    if 'URL' in entry and 'Type' in entry:
                        entry_type = entry['Type']
                        if entry_type.lower() == "view":
                            view_url = os.path.join(os.path.dirname(metadata_file), entry['URL'])
                            view_urls.append(view_url)

    except json.decoder.JSONDecodeError:
        return view_urls

    return view_urls


def search_for_metadata_files(dataset_dir, max_size):
    metadata = []
    metadata_views = {}
    result = list(Path(dataset_dir).rglob("*"))
    for r in result:
        meta = is_json_of_type(r, max_size, test_for_metadata)

        if meta:
            metadata.append(str(r))
            view_urls = get_view_urls(str(r))
            metadata_views[str(r)] = view_urls

    return metadata, metadata_views


def search_for_thumbnail_files(dataset_dir, view_files):
    potential_thumbnails = list(Path(dataset_dir).rglob("*thumbnail*"))
    potential_thumbnails += list(Path(dataset_dir).rglob("*.png"))
    potential_thumbnails += list(Path(dataset_dir).rglob("*.jpeg"))
    potential_thumbnails += list(Path(dataset_dir).rglob("*.jpg"))
    potential_thumbnails = list(set(potential_thumbnails))

    result = []
    for view_file in view_files:
        view_dir = os.path.dirname(view_file)
        result.extend([image_file for image_file in potential_thumbnails if view_dir == os.path.dirname(image_file)])

    result = list(set(result))
    # For each result:
    #   - Is this file actually an image?
    # Probably just leave this for now and go with the simple name comparison.
    return [str(x) for x in result]


def search_for_view_files(dataset_dir, max_size):
    metadata = []
    result = list(Path(dataset_dir).rglob("*"))
    for r in result:
        meta = is_json_of_type(r, max_size, test_for_view)

        if meta:
            metadata.append(str(r))

    return metadata


def search_for_plot_files(dataset_dir):
    plot_file = []
    csv_files = list(Path(os.path.join(dataset_dir, "primary")).rglob("*csv"))
    for r in csv_files:
        csv_plot = get_plot(r)
        if csv_plot:
            plot_file.append(csv_plot)
    tsv_files = list(Path(os.path.join(dataset_dir, "primary")).rglob("*tsv"))
    for r in tsv_files:
        tsv_plot = get_plot(r, is_tsv=True)
        if tsv_plot:
            tsv_plot.delimiter = "tab"
            plot_file.append(tsv_plot)

    txt_files = list(Path(os.path.join(dataset_dir, "primary")).rglob("*txt"))
    for r in txt_files:
        csv_location = create_csv_from_txt(r)
        csv_plot = get_plot(csv_location)
        if csv_plot:
            plot_file.append(csv_plot)

    return plot_file


def create_csv_from_txt(r):
    data = open(r)
    start = False
    finish = False
    csv_rows = []
    for line in data:
        if "+Fin" in line:
            finish = True
        elif start and not finish:
            line_data_list = line.split()
            if line_data_list[1].startswith("D"):
                clean_data = line_data_list[1][1:].split(",")
                line_data_list.pop()
                if line_data_list[0].endswith("s"):
                    line_data_list[0] = line_data_list[0][:-1]
                line_data_list += clean_data
                csv_rows.append(line_data_list)
        else:
            if "EIT STARTING" in line:
                start = True
    file_path = os.path.splitext(r)[0]
    csv_file_name = file_path + '.csv'
    with open(csv_file_name, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(csv_rows)
    return csv_file_name


class OnDiskFiles(metaclass=Singleton):
    # dataFrame_dir = ""
    _onDiskFiles = None
    _scaffold = None
    _plot_files = []

    class Scaffold(object):
        _scaffold_files = {
            'metadata': [],
            'view': [],
            'thumbnail': [],
        }

        _metadata_views = {}

        '''
        _scaffold_structure = {
            'metadata.json':{
                'view.json':'thumbnail.png',
                'view2.json':'thumbnail2.png'
            },
            'metadata2.json':{
                'view.json':'thumbnail.png'
            },
        }

        '''

        def set_metadata_files(self, files, metadata_views):
            self._scaffold_files['metadata'] = files
            self._metadata_views = metadata_views

        def get_metadata_files(self):
            return self._scaffold_files['metadata']

        def get_metadata_children_files(self):
            return self._metadata_views

        def set_view_files(self, files):
            self._scaffold_files['view'] = files

        def get_view_files(self):
            return self._scaffold_files['view']

        def set_thumbnail_files(self, files):
            self._scaffold_files['thumbnail'] = files

        def get_thumbnail_files(self):
            return self._scaffold_files['thumbnail']

    class Plot(object):
        def __init__(self, location, plot_type, no_header=False, delimiter='comma', x=0, y=None, row_major=False, thumbnail=None):
            self.location = location
            self.plot_type = plot_type
            self.x_axis_column = x
            self.delimiter = delimiter
            self.y_axes_columns = [] if y is None else y
            self.no_header = no_header
            self.row_major = row_major
            self.thumbnail = thumbnail

        def set_thumbnail(self, thumbnail):
            self.thumbnail = thumbnail

    def get_scaffold_data(self):
        return self._scaffold

    def get_plot_files(self):
        return self._plot_files

    def get_plot_data(self):
        file_names = []
        for p in self._plot_files:
            file_names.append(p.location)
        return file_names

    def generate_plot_thumbnail(self):
        for plot in self._plot_files:
            plot_df = None
            if plot.location.suffix == ".tsv" and not plot.no_header:
                plot_df = pd.read_csv(plot.location, sep='\t')
                plot_df.columns = plot_df.columns.str.lower()
            elif plot.location.suffix == ".csv" and not plot.no_header:
                plot_df = pd.read_csv(plot.location)
                plot_df.columns = plot_df.columns.str.lower()
            elif plot.location.suffix == ".tsv" and plot.no_header:
                plot_df = pd.read_csv(plot.location, header=None, sep='\t')
            elif plot.location.suffix == ".csv" and plot.no_header:
                plot_df = pd.read_csv(plot.location, header=None)

            if px is None:
                print("Plotly is not available, install for thumbnail generating functionality.")
            else:
                create_thumbnail_from_plot(plot, plot_df)

    def setup_dataset(self, dataset_dir, max_size):
        self._scaffold = OnDiskFiles.Scaffold()
        scaffold_files_dir = os.path.join(dataset_dir, "derivative")
        metadata_file, metadata_views = search_for_metadata_files(scaffold_files_dir, max_size)
        self._scaffold.set_metadata_files(metadata_file, metadata_views)
        self._scaffold.set_view_files(search_for_view_files(scaffold_files_dir, max_size))
        self._scaffold.set_thumbnail_files(search_for_thumbnail_files(scaffold_files_dir, self._scaffold.get_view_files()))
        self._plot_files = search_for_plot_files(dataset_dir)
        # self.generate_plot_thumbnail()
        return self
