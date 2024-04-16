from werkzeug.datastructures import FileStorage, ImmutableMultiDict


def upload_files(files: ImmutableMultiDict[str, FileStorage]):
    _files = files.to_dict().items()

    for name, file in _files:
        filename = file.filename
        print(name)
        print(filename)

        file.save(f"/tmp/{filename}")

        print("saved")
