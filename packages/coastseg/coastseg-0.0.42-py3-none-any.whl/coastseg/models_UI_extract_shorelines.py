# standard python imports
import os
import glob
import logging

# internal python imports
from coastseg import common
from coastseg import zoo_model
from coastseg import settings_UI

# external python imports
import ipywidgets
from IPython.display import display
from ipywidgets import Button
from ipywidgets import ToggleButton
from ipywidgets import HBox
from ipywidgets import VBox
from ipywidgets import Layout
from ipywidgets import HTML
from ipywidgets import RadioButtons
from ipywidgets import Output
from ipyfilechooser import FileChooser

# icons sourced from https://fontawesome.com/v4/icons/

logger = logging.getLogger(__name__)


class UI_Models:
    # all instances of UI will share the same debug_view
    model_view = Output(layout={"border": "1px solid black"})
    run_model_view = Output(layout={"border": "1px solid black"})

    def __init__(self):
        self.settings_dashboard = settings_UI.Settings_UI()
        self.zoo_model_instance = zoo_model.Zoo_Model()
        # Controls size of ROIs generated on map
        self.model_dict = {
            "sample_direc": None,
            "use_GPU": "0",
            "implementation": "BEST",
            "model_type": "sat_RGB_4class_6950472",
            "otsu": False,
            "tta": False,
        }
        # list of RGB and MNDWI models available
        self.RGB_models = [
            "sat_RGB_2class_7448405",
            "sat_RGB_4class_6950472",
        ]
        self.five_band_models = [
            "sat_5band_4class_7344606",
            "sat_5band_2class_7448390",
        ]
        self.MNDWI_models = [
            "sat_MNDWI_4class_7352850",
            "sat_MNDWI_2class_7557080",
        ]
        self.NDWI_models = [
            "sat_NDWI_4class_7352859",
            "sat_NDWI_2class_7557072",
        ]
        self.session_name = ""
        self.session_directory = ""

        # Declare widgets and on click callbacks
        self._create_HTML_widgets()
        self._create_widgets()
        self._create_buttons()
 

    def get_model_instance(self):
        return self.zoo_model_instance

    def set_session_name(self, name: str):
        self.session_name = str(name).strip()

    def get_session_name(
        self,
    ):
        return self.session_name

    def get_session_selection(self):
        output = Output()
        self.session_name_text = ipywidgets.Text(
            value="",
            placeholder="Enter a session name",
            description="Session Name:",
            disabled=False,
            style={"description_width": "initial"},
        )

        enter_button = ipywidgets.Button(description="Enter")

        @output.capture(clear_output=True)
        def enter_clicked(btn):
            session_name = str(self.session_name_text.value).strip()
            session_path = common.create_directory(os.getcwd(), "sessions")
            new_session_path = os.path.join(session_path, session_name)
            if os.path.exists(new_session_path):
                print(f"Session {session_name} already exists at {new_session_path}")
            elif not os.path.exists(new_session_path):
                print(f"Session {session_name} will be created at {new_session_path}")
                self.set_session_name(session_name)

        enter_button.on_click(enter_clicked)
        session_name_controls = HBox([self.session_name_text, enter_button])
        return VBox([session_name_controls, output])

    def create_dashboard(self):
        model_choices_box = HBox(
            [self.model_input_dropdown, self.model_dropdown, self.model_implementation]
        )
        checkboxes = HBox([self.otsu_radio, self.tta_radio])
        instr_vbox = VBox(
            [
                self.line_widget,
                self.instr_select_images,
                self.instr_run_model,
                self.select_model_session_button,
                self.extract_shorelines_button,
            ]
        )
        self.file_row = HBox([])
        self.warning_row = HBox([])
        display(
            self.settings_dashboard.render(),
            checkboxes,
            model_choices_box,
            self.get_session_selection(),
            instr_vbox,
            self.use_select_images_button,
            self.line_widget,
            self.warning_row,
            self.file_row,
            UI_Models.model_view,
            self.run_model_button,
            UI_Models.run_model_view,
        )

    def _create_widgets(self):
        self.model_implementation = RadioButtons(
            options=["ENSEMBLE", "BEST"],
            value="BEST",
            description="Select:",
            disabled=False,
        )
        self.model_implementation.observe(self.handle_model_implementation, "value")

        self.otsu_radio = RadioButtons(
            options=["Enabled", "Disabled"],
            value="Disabled",
            description="Otsu Threshold:",
            disabled=False,
            style={"description_width": "initial"},
        )
        self.otsu_radio.observe(self.handle_otsu, "value")

        self.tta_radio = RadioButtons(
            options=["Enabled", "Disabled"],
            value="Disabled",
            description="Test Time Augmentation:",
            disabled=False,
            style={"description_width": "initial"},
        )
        self.tta_radio.observe(self.handle_tta, "value")

        self.model_input_dropdown = ipywidgets.RadioButtons(
            options=["RGB", "MNDWI", "NDWI", "RGB+MNDWI+NDWI"],
            value="RGB",
            description="Model Input:",
            disabled=False,
        )
        self.model_input_dropdown.observe(self.handle_model_input_change, names="value")

        self.model_dropdown = ipywidgets.RadioButtons(
            options=self.RGB_models,
            value=self.RGB_models[0],
            description="Select Model:",
            disabled=False,
        )
        self.model_dropdown.observe(self.handle_model_type, "value")

    def _create_buttons(self):
        # button styles
        load_style = dict(button_color="#69add1", description_width="initial")
        action_style = dict(button_color="#ae3cf0")

        self.run_model_button = Button(
            description="Run Model",
            style=action_style,
            icon="fa-bolt",
        )
        self.run_model_button.on_click(self.run_model_button_clicked)

        self.extract_shorelines_button = Button(
            description="Extract Shorelines", style=action_style
        )
        self.extract_shorelines_button.on_click(self.extract_shorelines_button_clicked)

        self.use_select_images_button = Button(
            description="Select Images",
            style=load_style,
            icon="fa-file-image-o",
        )
        self.use_select_images_button.on_click(self.use_select_images_button_clicked)

        self.select_model_session_button = Button(
            description="Open model outputs",
            style=load_style,
        )
        self.select_model_session_button.on_click(self.select_session_button_clicked)


    def _create_HTML_widgets(self):
        """create HTML widgets that display the instructions.
        widgets created: instr_create_ro, instr_save_roi, instr_load_btns
         instr_download_roi
        """
        self.line_widget = HTML(
            value="____________________________________________________"
        )

        self.instr_select_images = HTML(
            value="<b>1. Select Images Button</b> \
                <br> - Select an ROI directory containing downloaded imagery.<br>\
                    - The model will be applied to the imagery and the outputs will be saved in the sessions directory under the session name entered.<br>\
            - <span style=\"background-color:yellow;color: black;\">WARNING :</span> You will not be able to see the files within the folder you select.<br>\
            ",
            layout=Layout(margin="0px 0px 0px 20px"),
        )

        self.instr_run_model = HTML(
            value="<b>2. Run Model Button</b> \
                <br> - Make sure to click Select Images Button.<br>\
                    - The model will be applied to the imagery and the outputs will be saved in the sessions directory under the session name entered.<br>\
            ",
            layout=Layout(margin="0px 0px 0px 20px"),
        )

    def handle_model_implementation(self, change):
        self.model_dict["implementation"] = change["new"]

    def handle_model_type(self, change):
        # 2 class model has not been selected disable otsu threhold
        if "2class" not in change["new"]:
            if self.otsu_radio.value == "Enabled":
                self.model_dict["otsu"] = False
                self.otsu_radio.value = "Disabled"
            self.otsu_radio.disabled = True
        # 2 class model was selected enable otsu threhold radio button
        if "2class" in change["new"]:
            self.otsu_radio.disabled = False

        logger.info(f"change: {change}")
        self.model_dict["model_type"] = change["new"]

    def handle_otsu(self, change):
        if change["new"] == "Enabled":
            self.model_dict["otsu"] = True
        if change["new"] == "Disabled":
            self.model_dict["otsu"] = False

    def handle_tta(self, change):
        if change["new"] == "Enabled":
            self.model_dict["tta"] = True
        if change["new"] == "Disabled":
            self.model_dict["tta"] = False

    def handle_model_input_change(self, change):
        if change["new"] == "RGB":
            self.model_dropdown.options = self.RGB_models
        if change["new"] == "MNDWI":
            self.model_dropdown.options = self.MNDWI_models
        if change["new"] == "NDWI":
            self.model_dropdown.options = self.NDWI_models
        if change["new"] == "RGB+MNDWI+NDWI":
            self.model_dropdown.options = self.five_band_models

    @run_model_view.capture(clear_output=True)
    def run_model_button_clicked(self, button):
        # user must have selected imagery first
        if self.model_dict["sample_direc"] is None:
            self.launch_error_box(
                "Cannot Run Model",
                "You must click 'Select Images' first",
            )
            return
        # user must have selected imagery first
        session_name = self.get_session_name()
        if session_name == "":
            self.launch_error_box(
                "Cannot Run Model",
                "Must enter a session name first",
            )
            return
        print("Running the model. Please wait.")
        zoo_model_instance =  self.get_model_instance()
        img_type = self.model_input_dropdown.value

        zoo_model_instance.run_model(
            img_type,
            self.model_dict["implementation"],
            session_name,
            self.model_dict["sample_direc"],
            model_name=self.model_dict["model_type"],
            use_GPU="0",
            use_otsu=self.model_dict["otsu"],
            use_tta=self.model_dict["tta"],
        )

    @run_model_view.capture(clear_output=True)
    def extract_shorelines_button_clicked(self, button):
        # user must have selected imagery first
        session_name = self.get_session_name()
        if session_name == "":
            self.launch_error_box(
                "Cannot Extract Shorelines",
                "Must enter a session name first",
            )
            return
        # must select a directory of model outputs
        if self.session_directory == "":
            self.launch_error_box(
                "Cannot Extract Shorelines",
                "Must click select model session first",
            )
            return  
        print("Extracting shorelines. Please wait.")
        shoreline_settings=self.settings_dashboard.get_settings()
        # get session directory location
        session_directory = self.session_directory
        zoo_model_instance =  self.get_model_instance()
        # load in shoreline settings, session directory with model outputs, and a new session name to store extracted shorelines
        zoo_model_instance.extract_shorelines(shoreline_settings,session_directory,session_name)



    @model_view.capture(clear_output=True)
    def load_callback(self, filechooser: FileChooser) -> None:
        if filechooser.selected:
            self.model_dict["sample_direc"] = os.path.abspath(filechooser.selected)

    @model_view.capture(clear_output=True)
    def selected_session_callback(self, filechooser: FileChooser) -> None:
        if filechooser.selected:
            self.session_directory = os.path.abspath(filechooser.selected)

    @model_view.capture(clear_output=True)
    def use_select_images_button_clicked(self, button):
        # Prompt the user to select a directory of images
        file_chooser = common.create_dir_chooser(
            self.load_callback, title="Select directory of images"
        )
        # clear row and close all widgets in self.file_row before adding new file_chooser
        common.clear_row(self.file_row)
        # add instance of file_chooser to self.file_row
        self.file_row.children = [file_chooser]

    @model_view.capture(clear_output=True)
    def select_session_button_clicked(self, button):
        # Prompt the user to select a directory of images
        file_chooser = common.create_dir_chooser(
            self.selected_session_callback, title="Select directory of model outputs",starting_directory='sessions'
        )
        # clear row and close all widgets in self.file_row before adding new file_chooser
        common.clear_row(self.file_row)
        # add instance of file_chooser to self.file_row
        self.file_row.children = [file_chooser]

    def launch_error_box(self, title: str = None, msg: str = None):
        # Show user error message
        warning_box = common.create_warning_box(title=title, msg=msg)
        # clear row and close all widgets in self.file_row before adding new warning_box
        common.clear_row(self.warning_row)
        # add instance of warning_box to self.warning_row
        self.warning_row.children = [warning_box]
