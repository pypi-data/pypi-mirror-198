import inspect
from pathlib import Path
from ververser.make_global_game_window import make_global_game_window


def host_this_folder() -> None:
    # Determine the path of the file in which we invoked this function
    call_site_frame_info = inspect.stack()[ 1 ]
    call_site_frame = call_site_frame_info[ 0 ]
    call_site_module = inspect.getmodule( call_site_frame )
    call_site_module_path = call_site_module.__file__
    call_site_folder_path = Path( call_site_module_path ).parent

    # Run the game, using the invocation folder as entrypoint
    game = make_global_game_window( call_site_folder_path )
    game.run()