import selenium_loader, pathlib, yaml


if __name__ == '__main__':
    config_file = pathlib.Path("./examples/download_file.yml")
    with open(config_file.absolute(), "r") as stream:
        config = yaml.load(stream, Loader=yaml.loader.SafeLoader)
        browser = selenium_loader.Browser(config)
        browser.run()
