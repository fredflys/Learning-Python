from backend.core.request_handler import BaseRequestHandler
import json

class UploadImageHandler(BaseRequestHandler):
    def post(self, *args, **kwargs):
        file_metas = self.request.files["image"]
        # print(file_metas)
        for meta in file_metas:
            file_name = meta['filename']
            file_path = os.path.join('statics', 'upload', generate_md5(file_name))
            with open(file_path, 'wb') as up:
                up.write(meta['body'])

        ret = {'status': True, 'path': file_path}
        self.write(json.dumps(ret))