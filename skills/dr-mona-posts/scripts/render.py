#!/usr/bin/env python3
"""
Render Dr. Mona slide HTML to PNG with headless Chrome, at 2x device scale.

    python3 render.py slide-01.html                 -> output/slide-01.png  (2160x2160)
    python3 render.py post-folder/*.html            -> a whole carousel
    python3 render.py cover.html --height 1920      -> reel cover (2160x3840)
    python3 render.py slide-01.html --width 1080 --height 1350   -> portrait
    python3 render.py old-slide.html --legacy-crop  -> for files with body{padding:40px}
    python3 render.py slide-01.html --scale 1       -> exact 1080px, no 2x

Standard library only. Finds Chrome (or Edge/Chromium) on macOS, Windows and Linux.

The shipped templates keep their preview padding behind a `@media (min-width:1200px)`
guard, so a window sized exactly to the canvas screenshots the canvas exactly - no crop
step, no Pillow. Hand-built older files with an unconditional `body{padding:40px}` need
--legacy-crop, which inflates the window and crops back; that path needs Pillow.
"""
import argparse
import glob
import os
import shutil
import subprocess
import sys

CANDIDATES = [
    # macOS
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    # Windows
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    # Linux
    "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/microsoft-edge",
]
ON_PATH = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
           "chrome", "msedge"]


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for p in CANDIDATES:
        if p and os.path.exists(p):
            return p
    for name in ON_PATH:
        found = shutil.which(name)
        if found:
            return found
    sys.exit(
        "Could not find Chrome, Chromium or Edge.\n"
        "Install Google Chrome, or point the CHROME environment variable at the binary:\n"
        "  macOS   export CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'\n"
        "  Windows set CHROME=C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\n"
        "  Linux   export CHROME=/usr/bin/google-chrome"
    )


def shoot(chrome, html, png, win_w, win_h, scale, budget, timeout, profile=None):
    if os.path.exists(png):
        os.remove(png)
    cmd = [
        chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--allow-file-access-from-files",
        f"--force-device-scale-factor={scale}",
        f"--window-size={win_w},{win_h}",
        f"--virtual-time-budget={budget}",
        "--default-background-color=00000000",
        f"--screenshot={png}",
        os.path.abspath(html),
    ]
    # No --user-data-dir by default: a throwaway profile makes Chrome run first-run
    # setup and then sit there for minutes after the screenshot has landed. Pass
    # --profile only if a Chrome you have open blocks the default profile.
    if profile:
        cmd[5:5] = [f"--user-data-dir={profile}", "--no-first-run",
                    "--no-default-browser-check", "--disable-default-apps",
                    "--disable-extensions", "--disable-background-networking",
                    "--disable-component-update", "--disable-sync"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        err = res.stderr or res.stdout
    except subprocess.TimeoutExpired:
        # Chrome sometimes writes the PNG and then refuses to exit. If the file landed,
        # that is a good render; only a missing file is a failure.
        err = (f"chrome did not exit within {timeout}s — if this happens every time, "
               f"raise --timeout or drop --profile")
    if not os.path.exists(png):
        sys.stderr.write(err or "")
        sys.exit(f"render failed: {html}")


def crop(png, left, top, w, h):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("--legacy-crop needs Pillow:  python3 -m pip install pillow\n"
                 "Or convert the file to the shipped template's media-query preview "
                 "padding and drop --legacy-crop.")
    with Image.open(png) as im:
        im.crop((left, top, left + w, top + h)).save(png)


def render_one(chrome, html, args):
    out_dir = os.path.join(os.path.dirname(os.path.abspath(html)), "output")
    os.makedirs(out_dir, exist_ok=True)
    png = os.path.join(out_dir, os.path.splitext(os.path.basename(html))[0] + ".png")

    if args.legacy_crop:
        pad = args.pad
        shoot(chrome, html, png, args.width + pad * 2, args.height + pad * 2,
              args.scale, args.budget, args.timeout, args.profile)
        crop(png, pad * args.scale, pad * args.scale,
             args.width * args.scale, args.height * args.scale)
    else:
        shoot(chrome, html, png, args.width, args.height, args.scale, args.budget,
              args.timeout, args.profile)

    size = os.path.getsize(png)
    print(f"  ok  {os.path.relpath(png)}  "
          f"{args.width * args.scale} x {args.height * args.scale}  ({size // 1024} KB)")
    return png


def main():
    ap = argparse.ArgumentParser(
        description="Render Dr. Mona slide HTML to PNG at 2x.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("files", nargs="+", help="slide HTML files (globs allowed)")
    ap.add_argument("--width", type=int, default=1080, help="canvas width (default 1080)")
    ap.add_argument("--height", type=int, default=1080,
                    help="canvas height: 1080 square, 1350 portrait, 1920 reel cover")
    ap.add_argument("--scale", type=int, default=2, help="device scale factor (default 2)")
    ap.add_argument("--budget", type=int, default=10000,
                    help="virtual time budget in ms — Google Fonts need it (default 10000)")
    ap.add_argument("--profile", default=None, metavar="DIR",
                    help="run Chrome against this user-data-dir instead of the default "
                         "profile — only needed if an open Chrome blocks the render")
    ap.add_argument("--timeout", type=int, default=90,
                    help="seconds to wait for Chrome to exit (default 90)")
    ap.add_argument("--legacy-crop", action="store_true",
                    help="inflate the window and crop back, for files with unconditional "
                         "body padding (needs Pillow)")
    ap.add_argument("--pad", type=int, default=40,
                    help="the body padding to inflate by, with --legacy-crop (default 40)")
    args = ap.parse_args()

    paths = []
    for pattern in args.files:
        hits = sorted(glob.glob(pattern))
        paths.extend(hits if hits else [pattern])
    missing = [p for p in paths if not os.path.exists(p)]
    if missing:
        sys.exit("not found: " + ", ".join(missing))

    chrome = find_chrome()
    print(f"chrome: {chrome}")
    print(f"rendering {len(paths)} file(s) at {args.scale}x "
          f"-> {args.width * args.scale} x {args.height * args.scale}")
    for p in paths:
        render_one(chrome, p, args)
    print("done. Now open the PNGs and look at them before reporting anything finished.")


if __name__ == "__main__":
    main()
