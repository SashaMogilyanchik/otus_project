import base64
import tempfile
from pathlib import Path


def capture_screenshot(driver) -> bytes:
    errors = []

    try:
        return driver.get_screenshot_as_png()
    except Exception as exc:
        errors.append(f"get_screenshot_as_png: {exc}")

    try:
        data = driver.execute_cdp_cmd(
            "Page.captureScreenshot",
            {"format": "png", "fromSurface": True},
        )["data"]
        return base64.b64decode(data)
    except Exception as exc:
        errors.append(f"cdp Page.captureScreenshot: {exc}")

    path = Path(tempfile.mkstemp(suffix=".png")[1])
    try:
        if driver.save_screenshot(str(path)):
            return path.read_bytes()
        errors.append("save_screenshot: returned False")
    except Exception as exc:
        errors.append(f"save_screenshot: {exc}")
    finally:
        path.unlink(missing_ok=True)

    raise RuntimeError("; ".join(errors))
