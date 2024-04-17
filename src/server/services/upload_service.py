from hashlib import md5
from datetime import datetime

from werkzeug.datastructures import FileStorage, ImmutableMultiDict

from geepeetee.keydb import keydb


def upload_files(files: ImmutableMultiDict[str, FileStorage]):
    _files = files.to_dict().items()

    for name, file in _files:
        filename = file.filename

        file.save(f"/tmp/{filename}")

        with open(f"/tmp/{filename}", "rb") as f:
            mdhash = md5(f.read()).hexdigest()

        print(mdhash)

        if keydb.hgetall(mdhash):
            print("file already indexed")
        else:
            keydb.hset(
                mdhash,
                mapping={
                    "filename": name,
                    "created_at": str(datetime.now()),
                },
            )

            print("saved")
