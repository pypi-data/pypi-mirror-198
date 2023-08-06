# built in
import importlib

# site
from voluxcli import demos
from volux import VoluxDemo
import click

RED = "\033[31m"
YELLOW = "\033[33m"
BLACK = "\033[30m"
WHITE_BACK = "\033[47m"
ANSI_RESET = "\033[0m"

PACKAGE_ALLOWLIST = ["voluxaudio", "voluxexamplemodule", "voluxlight"]


def collect_demos():
    demos_collected = []
    for attrib in dir(demos):
        demo_ = getattr(demos, attrib)
        if type(demo_) is type:
            if issubclass(demo_, VoluxDemo) is True:
                demos_collected.append(
                    {
                        "id": demo_().id,
                        "description": demo_.description,
                        "demo": demo_,
                    }
                )

    return demos_collected


def demo_requirements_satisfied(demo):
    """Check whether a demo's requirements are satisfied."""
    missing_requirements = []
    for req in demo.DEV__requirements:
        try:
            importlib.import_module(req["distribution_name"])

            # FIXME: temp for debugging
            # print("---- IMPORTED: " + req + " ----")
            # if "voluxexamplemodule" in sys.modules:
            #     print("yes!")
            # for module in sys.modules:
            #     if "volux" in module:
            #         print("!!!!" + module)
            # print(dir(sys.modules["voluxexamplemodule"]))
            # print(sys.modules["voluxexamplemodule"])

        except Exception as e:
            # raise e
            missing_requirements.append(req)

    if len(missing_requirements) > 0:
        click.echo("Error: Failed to import the following demo requirements!")
        for missing_req in missing_requirements:
            click.echo(
                "  - "
                + missing_req["distribution_name"]
                + (
                    " *"
                    if missing_req["distribution_name"] in PACKAGE_ALLOWLIST
                    else ""
                )
            )
        missing_but_allowlisted = [
            req
            for req in missing_requirements
            if req["distribution_name"] in PACKAGE_ALLOWLIST
        ]
        if len(missing_but_allowlisted) > 0:
            click.echo(
                "\n"
                + YELLOW
                + "Tip: You can install all missing requirements with an asterisk"
                + " using this command:\n"
                + BLACK
                + WHITE_BACK
                + "$ pip install "
                + " ".join(
                    [
                        f'"{req["distribution_name"]}{req["version_requirement"]}"'
                        for req in missing_but_allowlisted
                    ]
                )
                + ANSI_RESET
            )
    else:
        return True
