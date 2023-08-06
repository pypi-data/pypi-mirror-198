from tkinter import messagebox as mb

WINDOW_TITLE = 'SIMBA ERROR'

class SimbaError(Exception):
    def __init__(self, msg: str, show_window: bool):
        self.msg = msg
        if show_window:
            mb.showerror(title=WINDOW_TITLE, message=msg)

    def __str__(self):
        return self.msg


class NoSpecifiedOutputError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class ROICoordinatesNotFoundError(SimbaError):
    def __init__(self, expected_file_path: str, show_window: bool = False):
        msg = f'No ROI coordinates found. Please use the [ROI] tab to define ROIs. Expected at location {expected_file_path}'
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class NoChoosenClassifierError(SimbaError):
    def __init__(self, show_window: bool = False):
        msg = f'Select at least one classifiers'
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class NoChoosenROIError(SimbaError):
    def __init__(self, show_window: bool = False):
        msg = f'Please select at least one ROI.'
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class NoChoosenMeasurementError(SimbaError):
    def __init__(self, show_window: bool = False):
        msg = 'Please select at least one measurement to calculate descriptive statistics for.'
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')


class NoROIDataError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(msg)


class MixedMosaicError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(msg)

class AnimalNumberError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class InvalidFilepathError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')


class NoFilesFoundError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class NotDirectoryError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class DirectoryExistError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class FileExistError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')


class FrameRangeError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class AdvancedLabellingError(SimbaError):
    def __init__(self, frame: str, lbl_lst: list, unlabel_lst: list, show_window: bool = False):
        self.msg = 'SIMBA ERROR: In advanced labelling of multiple behaviors, any annotated frame cannot have some ' \
                   'behaviors annotated as present/absent, while other behaviors are un-labelled. All behaviors need ' \
                   'labels for a frame with one or more labels. In frame {}, behaviors {} are labelled, while behaviors ' \
                   '{} are un-labelled.'.format(str(frame), lbl_lst, unlabel_lst)
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class InvalidHyperparametersFileError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class InvalidVideoFileError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class InvalidFileTypeError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class CountError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')

class DuplicationError(SimbaError):
    def __init__(self, msg: str, show_window: bool = False):
        super().__init__(msg=msg, show_window=show_window)
        print(f'SIMBA ERROR: {msg}')



#####

class ThirdPartyAnnotationEventCountError(SimbaError):
    def __init__(self, video_name: str, clf_name: str, start_event_cnt: int, stop_event_cnt: int, show_window: bool = False):
        msg = f'SIMBA THIRD-PARTY ANNOTATION ERROR: The annotations for behavior {clf_name} in video {video_name} contains {str(start_event_cnt)} start events and {str(stop_event_cnt)} stop events. SimBA requires the number of stop and start event counts to be equal'
        super().__init__(msg=msg, show_window=show_window)
        print(msg)

class ThirdPartyAnnotationOverlapError(SimbaError):
    def __init__(self, video_name: str, clf_name: str, show_window: bool = False):
        msg = f'SIMBA THIRD-PARTY ANNOTATION ERROR: The annotations for behavior {clf_name} in video {video_name} contains behavior start events that are initiated PRIOR to the PRECEDING behavior event ending. SimBA requires a specific behavior event to end before another behavior event can start.'
        super().__init__(msg=msg, show_window=show_window)
        print(msg)

class ColumnNotFoundError(SimbaError):
    def __init__(self, column_name: str, file_name: str, show_window: bool = False):
        msg = f'SIMBA ERROR: Field name {column_name} could not be found in file {file_name}'
        super().__init__(msg=msg, show_window=show_window)
        print(msg)

class AnnotationFileNotFoundError(SimbaError):
    def __init__(self, video_name: str, show_window: bool = False):
        msg = f'SIMBA THIRD-PARTY ANNOTATION ERROR: NO ANNOTATION DATA FOR VIDEO {video_name} FOUND'
        super().__init__(msg=msg, show_window=show_window)
        print(msg)





class ThirdPartyAnnotationsOutsidePoseEstimationDataError(SimbaError):
    def __init__(self,
                 video_name: str,
                 clf_name: str,
                 frm_cnt: int,
                 first_error_frm: int,
                 ambiguous_cnt: int,
                 show_window: bool = False):

       msg = (f'SIMBA BORIS WARNING: SimBA found BORIS annotations for behavior {clf_name} in video '
              f'{video_name} that are annotated to occur at times which is not present in the '
              f'video data you imported into SIMBA. The video you imported to SimBA has {str(frm_cnt)} frames. '
              f'However, in BORIS, you have annotated {clf_name} to happen at frame number {str(first_error_frm)}. '
              f'These ambiguous annotations occur in {str(ambiguous_cnt)} different frames for video {video_name} that SimBA will **remove** by default. '
              f'Please make sure you imported the same video as you annotated in BORIS into SimBA and the video is registered with the correct frame rate.')
       super().__init__(msg=msg, show_window=show_window)
       print(msg)




