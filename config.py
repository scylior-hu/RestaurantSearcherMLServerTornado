project_name = "rsearchernlp"

plugins = [
    "oz.core",
    project_name,
]

app_options = dict(
    port = 80,
    debug = True,
    static_path = "static",
    template_path = "templates",
    xsrf_cookies = False,
    gzip = False
)
