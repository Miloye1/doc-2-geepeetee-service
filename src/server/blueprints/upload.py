from flask import Blueprint, request

from ..service.upload_service import upload_files

bp = Blueprint("upload", __name__)


@bp.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        upload_files(request.files)

    return []
